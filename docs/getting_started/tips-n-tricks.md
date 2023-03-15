# Tips and Tricks
## `NameError` with Boolean values
Being Python 2.7 the earliest Python version i was used to work on, i was shocked to find that simple scripts running on **Python 2.1** failed with `NameError: True` and `NameError: False`.

Upon investigation I found that:

- `> 3.0`: `True` and `False` are **reserved keywords** (and so cannot be defined) and in Python;
- `>= 2.3`: `True` and `False` are defined simply as **constants**, so they could even be assigned arbitrary values;
- `< 2.3`: `True` and `False` are **NOT defined** at all, hence the `NameError` exception.

!!! Info 
    **More informations** on this subject and other interesting considerations can be found in [**this article**](https://giedrius.blog/2018/01/04/what-is-actually-true-and-false-in-python/).

### Workaround for Jython `2.2` and lower
To fix this, add the following lines at the top of your code (inspired by [this SO answer](https://stackoverflow.com/q/31042827/8965861){: target=_blank}):
```python
# Define True and False, for very old versions of Python (<2.3)
exec("try: (True, False)\nexcept NameError: True = 1==1; False = 1==0")
```

The code is wrapped in an `exec(...)` function for two primary reasons:

- To provide a **oneliner** fix, easier to copy-paste, thus reducing errors;
- To **elude linters and static type checkers** like `pylint` or `mypy` which consider this an error _(while it is only a false positive, since we're dealing with old legacy Python versions)_.

## The `__future__` module
Just like Python, Jython also provides the `__future__` module.

This built-in module was **added in Python 2.1** and allows the developer to **force** the Python (and so, Jython) interpreters into using **newer features** of the language.

!!! Warning
    The list of features the module exposes **depends on the version of Jython** your DMGR is running, so always make sure that the feature you're trying to import is actually present in the `__future__` module. 

    A full list of features available, with all their descriptions and version prerequisites can be found [here](https://docs.python.org/3/library/__future__.html).

1. You can find the features **available** in _your Jython environment_ by running the following commands:
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