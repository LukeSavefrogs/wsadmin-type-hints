# Tips and Tricks

The following section lists a series of tips and tricks I found useful in my experience.

This includes:

- Solutions to language problems
- Tips for using the `wsadmin`

## `NameError` with Boolean values
Being Python 2.7 the earliest Python version i was used to work on, i was shocked to find that simple scripts running on **Python 2.1** failed with `NameError: True` and `NameError: False`.

Upon investigation I found that:

- `> 3.0`: `True` and `False` are **reserved keywords** (and so cannot be defined) and in Python;
- `>= 2.3`: `True` and `False` are defined simply as **constants**, so they could even be assigned arbitrary values;
- `< 2.3`: `True` and `False` are **NOT defined** at all, hence the `NameError` exception.

!!! Info 
    **More informations** on this subject and other interesting considerations can be found in [**this article**](https://giedrius.blog/2018/01/04/what-is-actually-true-and-false-in-python/).

### Solutions
Since boolean values were introduced in **Python 2.3** (with [PEP 285](https://peps.python.org/pep-0285/){: target=_blank}), if the `wsadmin` is running an older Jython version, you won't be able to use `True` or `False` (nor the `bool(...)` function) in your scripts. 

To overcome this problem you have **2 options**:

1. [Provide a polyfill for `True` and `False`](#1-define-truefalse)
1. [Use `0` (falsy) and `1` (truthy)](#2-use-01)


Let's explore these options in detail...
#### 1. Define `True`/`False`
To use `True` and `False` in the scripts **add the following line** at the top of your code, then you'll be able to write your scripts as usual:
```python
exec("try: (True, False)\nexcept NameError: exec('True = 1==1; False = 1==0')")
```

!!! Info
    The code is wrapped in an `exec(...)` function for two primary reasons:

    1. To provide a **oneliner** fix, easier to _copy-paste_, thus _reducing errors_;
    1. To **elude linters and static type checkers** like `pylint` or `mypy` which consider this an error _(while it is only a false positive, since we're dealing with old legacy Python versions)_.
    1. The inner `exec` call serves the sole purpose of safe guarding in case the script is being executed (while testing) on Python 3.x (the `SyntaxError` raised when trying to assign a keyword cannot be catched).

!!! quote "Source"
    This **workaround** is inspired by [this SO answer](https://stackoverflow.com/q/31042827/8965861){: target=_blank}.

!!! Example
    The following example shows how the `False` value gets correctly evaluated in a condition:
    ```pycon
    >>> exec("try: (True, False)\nexcept NameError: exec('True = 1==1; False = 1==0')")
    >>> exists = True
    
    >>> if exists:
    ...     print("File exists.")
    ... else:
    ...     print("File does not exists.")
    File exists.
    ```

#### 2. Use `0`/`1`
Python interprets **`0`** and **`1`** respectively as **falsy** and **truthy values**.
This means that we can use `0` instead of `False` and `1` instead of `True`.

!!! Example
    We can rewrite the previous example like this:
    ```pycon
    >>> exists = 1
    
    >>> if exists:
    ...     print("File exists.")
    ... else:
    ...     print("File does not exists.")
    File exists.
    ```

## The `__future__` module
Just like Python, Jython also provides the `__future__` module.

This built-in module was **added in Python 2.1** and allows the developer to **force** the Python (and so, Jython) interpreters into using **newer features** of the language.

!!! Warning
    The list of features the module exposes **depends on the version of Jython** your DMGR is running, so always make sure that the feature you're trying to import is actually present in the `__future__` module. 

    A full list of features available, with all their descriptions and version prerequisites can be found [here](https://docs.python.org/3/library/__future__.html).

1. To **discover** the features **available** in _your Jython environment_ use the following commands:
```pycon
>>> import __future__
>>> print([feature for feature in dir(__future__) if not feature.startswith("_")])
['nested_scopes']
```

1. Then, if you intend to use them, just **`import`** them like a regular module:
```pycon
>>> from __future__ import nested_scopes
```

    !!! Info 
        In this case I'm using the _`nested_scopes`_ feature, which **backports** [**PEP 227**](https://peps.python.org/pep-0227/) (introduced in _Python 2.2_) down to _Python 2.1_.