import re
import requests
from bs4 import BeautifulSoup # type: ignore

from typing import List, Union
from collections.abc import Callable

from .types import DocumentationModule, DocumentationVersion, WasVersion


DOCUMENTATION_API_BASE_URL = "https://www.ibm.com/docs/api/v1"


def get_updated_modules() -> List[DocumentationVersion]:
	"""Returns a list of modules taken from the documentation (https://www.ibm.com/docs/en/was-nd)

	Returns:
		List[DocumentationVersion]: List of modules/methods available grouped by WAS version.
	"""
	api_information = []
	available_versions = get_available_was_versions()

	for was_version in available_versions:
		api_url = f"{DOCUMENTATION_API_BASE_URL}/toc/{was_version['newHref']}?lang=en"
		response = requests.get(api_url)
		
		topics = response.json()

		wsadmin_commands_topic = list(search_json(
			topics, 
			lambda s: s.get("topicId") == "sasew-scripting-command-line-reference-material-using-wsadmin-scripting"
		))

		if len(wsadmin_commands_topic) != 1:
			print(f"ERROR - {len(wsadmin_commands_topic)} did not match expected command topic number (1)")
			continue

		current_version_json: DocumentationVersion = {
			"name": was_version["label"],
			"version": was_version["version"] if was_version["version"] else "No version found",
			"modules": []
		}

		for topic in wsadmin_commands_topic[0].get("topics", []):
			label = topic.get("label")
			topic_href = topic.get("href")

			command_regex = re.search(r"Commands for the (.*?) object using wsadmin scripting", label)

			if not command_regex:
				continue

			command = command_regex.group(1)


			api_reference_url = f"{DOCUMENTATION_API_BASE_URL}/content/{topic_href}?parsebody=true&lang=en"

			response = requests.get(api_reference_url)
			soup = BeautifulSoup(response.text, 'html.parser')
			
			methods = soup.select("article > div.body > section > h2")
			last_update = soup.select_one("#lastModifiedDate").text.strip().removeprefix("Last Updated: ")
			module_description = '\n\n'.join(list(map(lambda el: el.text.strip(), soup.select("article > div.body > p"))))
			
			current_module_info: DocumentationModule = {
				"name": command,
				"description": module_description,
				"documentation": {
					"url": f"https://www.ibm.com/docs/en/{was_version['newHref']}?topic={topic_href}",
					"lastUpdate": last_update
				},
				"methods": []
			}


			for title in methods:
				method_description = title.find_next_sibling("p")
				method_name = re.sub(r"^([-A-Za-z_0-9]+)\s*.*", r"\1", title.text.strip())

				deprecated = "deprecated" in title.text.strip().lower()

				current_module_info["methods"].append({
					"name": method_name,
					"description": method_description.text.strip(),
					"parent": command,
					"fullName": f"{command}.{method_name}",
					"deprecated": deprecated,
					"documentation": {
						"url": f"https://www.ibm.com/docs/en/{was_version['newHref']}?topic={topic_href}#{title.get('id')}",
						"lastUpdate": last_update
					}
				})
		
			current_version_json["modules"].append(current_module_info)
		api_information.append(current_version_json)

	return api_information


def get_available_was_versions() -> List[WasVersion]:
	response = requests.get(f"{DOCUMENTATION_API_BASE_URL}/otherversion/was-nd?existingTopicsOnly=false&lang=en")
	json = response.json()

	return json["otherVersions"]


def search_json(json_object: Union[list, dict], validator_func: Callable[[dict], bool]):
	"""Searches and returns an object inside a JSON-like object.

	Args:
		json_object (dict|list): The object to search on.
		validator_func (Callable[[dict], bool]): A function returning a boolean value.

	Yields:
		Iterator[str]: The found element, if any.
	"""
	if isinstance(json_object, dict):
		if validator_func(json_object):
			yield json_object

		for key in json_object.keys():
			yield from search_json(json_object[key], validator_func)

	elif isinstance(json_object, list):
		for item in json_object:
			yield from search_json(item, validator_func)

