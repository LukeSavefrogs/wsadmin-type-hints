from typing import List, Optional, Type, TypedDict, Union

class WasVersion(TypedDict):
	""" Single WAS Documentation version available in the online IBM Documentation. """
	href: str
	label: str
	
	newHref: Optional[str]
	version: Optional[str]
	exists: Optional[bool]

class OtherVersionResponse(TypedDict):
	""" Response of the '/otherversion/was-nd' endpoint of the IBM Documentation API. """
	activeVersion: WasVersion
	otherVersions: List[WasVersion]




class DocumentationInfo(TypedDict):
	url: str
	lastUpdate: str


class DocumentationMethod(TypedDict):
	name: str
	description: str
	parent: str
	fullName: str
	documentation: DocumentationInfo


class DocumentationModule(TypedDict):
	name: str
	description: str
	documentation: DocumentationInfo
	methods: List[DocumentationMethod]

class DocumentationVersion(TypedDict):
	name: str
	version: str
	modules: List[DocumentationModule]