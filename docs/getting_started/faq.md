# FAQ

## Package

### Does this package let me interact with Websphere Application Server?
**No**, this package only provides autocompletion and intellisense functionality, as well as an online manual complete with examples.

### Do I need the same Python version of the `wsadmin`?
**No**, to work this package needs **Python >3.7**. However, the syntax of your scripts should match the Pyhon version run by the `wsadmin` Jython interpreter.


## Jython
### Can I use keyword arguments in `wsadmin` methods?
**No**, you can't.

Passing a keyword argument to a `wsadmin` method (for example [`AdminConfig.help()`][wsadmin_type_hints.AdminConfig.help]) will throw a `TypeError`:
```pycon
>>> AdminConfig.help(method_name="help")
WASX7015E: Exception running command: "AdminConfig.help(method_name="help")"; exception information:
com.ibm.bsf.BSFException: exception from Jython:
Traceback (innermost last):
  File "<input>", line 1, in ?
TypeError: help(): takes no keyword arguments
```

You can however write **custom functions** or methods that accept both **positional and keyword arguments**:
```pycon
>>> def test(arg="default"):
>>>         print str(arg).capitalize() + " argument"
>>>
>>> test()
Default argument
>>>
>>> test("positional")
Positional argument
>>>
>>> test(arg="keyword")
Keyword argument
>>>
```