# Getting started
This section will guide you through the installation and setup of the development environment.

## Installation
The first step is to install the `wsadmin-type-hints` package.

- Using `pip` (global install):
```
pip install wsadmin-type-hints
```

- Using `poetry`:
```
poetry add wsadmin-type-hints --group dev 
```

- Using `pipenv`:
```
pipenv install --dev wsadmin-type-hints
```

- *For other dependency managers (such as [pdm](https://github.com/pdm-project/pdm) or [hatch](https://github.com/pypa/hatch)) see the respective documentation...*

!!! note

	If installed inside a virtual environment, you may need to activate it first, to be able to use it.

## Usage
The `wsadmin-type-hints` package is intended to be used to provide **type hints** to the Python interpreter used by IDE language servers (such as Pylance). 
Because of this, the functions _do not contain actual code_ and their body is _always empty_.

The following steps will allow you to make use of modern IDE intellisense for `wsadmin` objects:

1. To differentiate between the development and production environment we can use a `try..except` block:
```python
try:
	(AdminControl, AdminConfig, AdminApp, AdminTask, Help)
except NameError:
	# wsadmin objects are not defined, so this is the development environment.
	from wsadmin_type_hints import *
else:
	print("Production environment, i'm not needed here 😃")
```
	This block could even be left as-is in the code deployed on the production server (maybe leaving out the emoji before uploading 😇), since it won't ever reach the import (and even then the script would simply fail because of the `wsadmin-type-hints` package not being there).

2. Use the `wsadmin` objects like always: 
```python
current_cell = AdminControl.getCell()
print("Current cell: %s" % current_cell)
```