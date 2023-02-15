from wsadmin_type_hints import *

assert AdminControl.__doc__ != ""


try:
	(AdminControl, AdminConfig, AdminApp, AdminTask, Help)
except NameError:
	from wsadmin_type_hints import *
else:
	print("AdminControl is already defined, i'm not needed here 😃")