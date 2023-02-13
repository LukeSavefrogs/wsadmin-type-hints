import json
from pathlib import Path
import wsadmin_type_hints

import sys
import os
import importlib

from documentation.core import get_updated_modules

def main():
	api_information = get_updated_modules()

	print(f"Found {len(api_information)} Websphere Application Server versions:")
	
	try:
		for was_version in api_information:
			print(f"\t- [{len(was_version['modules'])} modules] {was_version['name']}")

			for module in was_version['modules']:
				assert module_has_submodule(wsadmin_type_hints, module["name"]), f"Module '{module['name']}' NOT FOUND"

				found_module_methods = eval(f"dir(wsadmin_type_hints.{module['name']})")
				for method in module["methods"]:
					assert method["name"] in found_module_methods, f"Method '{module['name']}.{method['name']}' NOT FOUND"

	except AssertionError as e:
		print(f"\n\t\t{e}\n")	

	json_file_path = Path(__file__).absolute().parent / "methods.json"
	with open(json_file_path, "w") as file:
		json.dump(api_information, file, indent=4)
		

def module_has_submodule(package, module_name):
	""" Check if package has module
	Source: https://stackoverflow.com/a/36115385/8965861
	"""
	name = ".".join([package.__name__, module_name])
	try:
		# None indicates a cached miss; see mark_miss() in Python/import.c.
		return sys.modules[name] is not None
	except KeyError:
		pass

	try:
		package_path = package.__path__   # No __path__, then not a package.
	except AttributeError:
		# Since the remainder of this function assumes that we're dealing with
		# a package (module with a __path__), so if it's not, then bail here.
		return False
	
	for finder in sys.meta_path:
		if finder.find_spec(name, package_path):
			return True

	for entry in package_path:
		try:
			# Try the cached finder.
			finder = sys.path_importer_cache[entry]
			if finder is None:
				# Implicit import machinery should be used.
				try:
					file_, _, _ = importlib.find_spec(module_name, [entry])
					if file_:
						file_.close()
					return True
				except ImportError:
					continue
			# Else see if the finder knows of a loader.
			elif finder.find_spec(name):
				return True
			else:
				continue
		except KeyError:
			# No cached finder, so try and make one.
			for hook in sys.path_hooks:
				try:
					finder = hook(entry)
					# XXX Could cache in sys.path_importer_cache
					if finder.find_spec(name):
						return True
					else:
						# Once a finder is found, stop the search.
						break
				except ImportError:
					# Continue the search for a finder.
					continue
			else:
				# No finder found.
				# Try the implicit import machinery if searching a directory.
				if os.path.isdir(entry):
					try:
						file_, _, _ = importlib.find_spec(module_name, [entry])
						if file_:
							file_.close()
						return True
					except ImportError:
						pass
				# XXX Could insert None or NullImporter
	else:
		# Exhausted the search, so the module cannot be found.
		return False


if __name__ == '__main__':
	main()