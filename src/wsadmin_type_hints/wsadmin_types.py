"""
Module used internally by `wsadmin-type-hints` to define appropriate return types for some `wsadmin` methods.

Warning:
    These are NOT real classes, so they can't be used as-is.

    The **actual return type** is the one they inherit from (_for example `RunningObjectName` inherits from `str`, 
        so the actual return type will be `str`_).

    This structure is needed to make the code more **pythonic** and **readable**.
    It also makes it clear just by glancing to the method signature **which** value must be passed,
        instead of remembering which `wsadmin` object method returns the correct Object name.
"""
class _OpaqueDigestObject(object):
    """
    Opaque "digest" object returned by a call to the `AdminConfig.extract()` method.
    
    Question: More testing needed
        I **didn't test this command** in my test environment but i will need to, in order to better understand it.
    """
    pass


class ConfigurationObjectName(str):
    """Object name representing an entry in the configuration.

    Example:
        ``` 
        "Db2JdbcDriver(cells/testcell/nodes/testnode|resources.xml#JDBCProvider_1)"
        ```
    """
    pass

class ContainmentPath(str):
    """Represents the path of a resource in the configuration.

    The containment path must be a path that contains the correct hierarchical order. 
    For example, if you specify /Server:server1/Node:node/ as the containment path, 
        you do not receive a valid configuration ID because Node is a parent of Server and comes before Server in the hierarchy.

    Example:
        ``` 
        "/Cell:testcell/Node:testNode/JDBCProvider:Db2JdbcDriver/"
        ```
    """
    pass

class RunningObjectName(str):
    """This `ObjectName` uniquely identifies running objects and is in the 
        form `[domainName]:property=value[,property=value]*`.
    
    The `RunningObjectName` class consists of the following elements:

    - The domain name `"WebSphere"`.
    - Several key properties, for example:
        - `type` indicates the type of object that is accessible through the MBean, for example, ApplicationServer, and EJBContainer.
        - `name` represents the display name of the particular object, for example, MyServer.
        - `node` represents the name of the node on which the object runs.
        - `process` represents the name of the server process in which the object runs.
        - `mbeanIdentifier` correlates the MBean instance with corresponding configuration data.
    
    You can use the asterisk (*) at the end as a wildcard character, so that you do not have to specify the entire set of key properties.

    For more info see the [official documentation](https://www.ibm.com/docs/en/was-nd/8.5.5?topic=administration-objectname-attribute-attributelist-classes-using-wsadmin-scripting).

    Example:
        ```
        "WebSphere:name="My Server",type=ApplicationServer,node=n1,*"
        ```
    """
    pass