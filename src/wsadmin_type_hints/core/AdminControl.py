"""The `AdminControl` object enables the manipulation of MBeans running in a WebSphere server process.

!!! Note
    Many of the `AdminControl` commands support **two different sets of
    signatures**: one that accepts and returns **strings**, and one low-level
    set that works with **JMX** (_Java Management Extensions_) objects like ObjectName and AttributeList.
    
    In most situations, the string signatures are likely to be more useful,
    but JMX-object signature versions are supplied as well.  Each of these
    JMX-object signature commands has "_jmx" appended to the command name.
    Hence there is an "invoke" command, as well as a "invoke_jmx" command.

In addition to operational commands, the AdminControl object supports some utility commands for tracing, 
reconnecting with a server, and converting data types.

For more info see the [official documentation](https://www.ibm.com/docs/en/was-nd/8.5.5?topic=scripting-commands-admincontrol-object-using-wsadmin).
"""

from typing import Any, Union, Literal as _Literal
from wsadmin_type_hints.typing_objects.object_name import (
    RunningObjectName,
    RunningObjectTemplate,
    ConfigurationObjectName as _ConfigurationObjectName,
)
from wsadmin_type_hints.typing_objects.wsadmin_types import MultilineList


def completeObjectName(
    template: Union[RunningObjectName, RunningObjectTemplate], /
) -> RunningObjectName:
    """
    Returns a string version of an **object name** that matches the `template`.
    For example, the template might be `type=Server,*`.

    !!! Warning
        If there are several MBeans that match the template, **only the first match** is returned.

        If what you need is the **full list** of MBeans that match the `template`, then
            use [`AdminControl.queryNames(...)`][wsadmin_type_hints.AdminControl.queryNames].

    Args:
        template (RunningObjectName | RunningObjectTemplate): The object name (already completed or a template) to complete.

    Returns:
        object_name(RunningObjectName): The complete object name of the running MBean.

    Example:
        ```pycon
        >>> print(AdminControl.completeObjectName('node=myNode,type=Server,*'))
            WebSphere:name=myServer,process=myServer,platform=proxy,node=myNode,j2eeType=J2EEServer,version=9.0.5.14,type=Server,mbeanIdentifier=cells/myCell/nodes/myNode/servers/myServer/server.xml#Server_1,cell=myCell,spec=1.0,processType=ManagedProcess
        ```

    Question: More testing needed
        The difference between `object_name` and `template` needs to be checked, since the official documentation does not provide any info on how to use them.
    """


def getAttribute(object_name: RunningObjectName, attribute: str, /) -> str:
    """Returns value of `attribute` for the MBean described by `object_name`.

    Args:
        object_name (RunningObjectName): The object name of the MBean.
        attribute (str): The name of the attribute to retrieve.

    Returns:
        value(str): The attribute value.

    !!! Tip
        For a list of available attributes, use the command [`AdminConfig.attributes(...)`][wsadmin_type_hints.AdminConfig.attributes] with the correct object type.

        For example, if you are trying to request the cluster name of a server but you don't remember the attribute name:
        ```pycon
        >>> server = AdminControl.completeObjectName('type=Server,*')
        >>> print(AdminConfig.attributes("Server"))
        adjustPort Boolean
        changeGroupAfterStartup String
        changeUserAfterStartup String
        clusterName String
        [...]
        >>> print(AdminControl.getAttribute(server, "clusterName"))
        ```

    Example:
        ```python
        objNameString = AdminControl.completeObjectName('WebSphere:type=Server,*')
        process_type  = AdminControl.getAttribute(objNameString, 'processType')

        print(process_type)
        ```
    """


def getAttribute_jmx(object_name, attribute, /):
    """Use the `getAttribute_jmx` command to return the value of the attribute for the name that you provide.

    Args:
        object_name (ObjectName): Specifies the object name of the MBean of interest.
        attribute (str): Specifies the name of the attribute to query.

    Example:
        ```
        import javax.management as mgmt

        objNameString = AdminControl.completeObjectName('WebSphere:=type=Server,*')
        objName       = mgmt.ObjectName(objNameString)
        process_type  = AdminControl.getAttribute_jmx(objName, 'processType')

        print(process_type)
        ```

    Question: Investigation needed
        This is not very clear in the documentation, so it needs more research.
    """


def getAttributes(object_name, attributes, /):
    """Returns a string listing the values of the attributes named in `attributes` for the object named by `object_name`.

    Args:
        object_name (ObjectName): Use the getAttributes command to return the attribute values for the names that you provide.
        attributes (java.lang.String[] or java.lang.Object[]): Specifies the names of the attributes to query.

    Example:

        - Using Jython with string attributes:

        ```python
        objNameString = AdminControl.completeObjectname('WebSphere:type=Server,*)
        attributes    = AdminControl.getAttributes(objNameString, '[cellName nodeName]')

        print(attributes)
        ```

        - Using Jython with object attributes:

        ```python
        objNameString = AdminControl.completeObjectname('WebSphere:type=Server,*)
        attributes    = AdminControl.getAttributes(objNameString, ['cellName', 'nodeName'])

        print(attributes)
        ```
    """


def getAttributes_jmx(*args: Any) -> Any:  # undocumented
    """ """


def getCell() -> str:
    """Returns the **cell name** to which the scripting process is connected.

    Example:
        The following code will show the cell name:
        ```pycon
        >>> print(AdminControl.getCell())
        myCell
        ```

        To get the full configuration ID of the cell, use [`AdminConfig.list("Cell")`][wsadmin_type_hints.AdminConfig.list] instead:
        ```pycon
        >>> print(AdminConfig.list("Cell"))
        myCell(cells/myCell|cell.xml#Cell_1)
        ```

    !!! abstract "See also"
        - [`AdminControl.getHost()`][wsadmin_type_hints.AdminControl.getHost]
        - [`AdminControl.getNode()`][wsadmin_type_hints.AdminControl.getNode]
        - [`AdminControl.getPort()`][wsadmin_type_hints.AdminControl.getPort]
        - [`AdminControl.getType()`][wsadmin_type_hints.AdminControl.getType]
    """


def getConfigId(
    object_name: Union[RunningObjectName, str]
) -> Union[_ConfigurationObjectName, _Literal[""]]:
    """Given the object name of a running MBean, return the **configuration ID** of the object.

    This function communicates with the configuration service to look up
    a configuration ID that can be used by `AdminConfig`.

    If no configuration object exists that corresponds to the supplied `object_name` string,
    `getConfigId` returns an empty string.

    Args:
        object_name (RunningObjectName | str): The object name of the MBean.

    Returns:
        configuration_id(_ConfigurationObjectName | ""): The configuration ID of the object. Empty string if not found.

    Example:
        Using `getConfigId` we can get the configuration ID of a running server:
        ```pycon
        >>> dmgr = AdminControl.getConfigId("name=dmgr,type=Server,*")
        >>> print(dmgr)
        dmgr(cells/myCell/nodes/myNode/servers/dmgr|server.xml#Server_1)
        ```

        This ID can be used as usual, even transforming it again into the object name of the MBean (the reverse operation):
        ```pycon
        >>> print(AdminConfig.getObjectName(dmgr))
        WebSphere:name=dmgr,process=dmgr,platform=proxy,node=myNode,j2eeType=J2EEServer,version=8.5.5.23,
        type=Server,mbeanIdentifier=cells/myCell/nodes/myNode/servers/dmgr/server.xml#Server_1,cell=myCell,
        spec=1.0,processType=DeploymentManager
        ```

    !!! abstract "See also"
        - [`AdminConfig.getObjectName()`][wsadmin_type_hints.AdminConfig.getObjectName]
    """
    ...


def getDefaultDomain(*args: Any) -> Any:  # undocumented
    """ """


def getDomainName(*args: Any) -> Any:  # undocumented
    """ """


def getHost() -> str:
    """Returns the **host** to which the scripting process is connected.

    Example:
        ```pycon
        >>> print(AdminControl.getHost())
        myHost.internal.cloud
        ```

    !!! abstract "See also"
        - [`AdminControl.getCell()`][wsadmin_type_hints.AdminControl.getCell]
        - [`AdminControl.getNode()`][wsadmin_type_hints.AdminControl.getNode]
        - [`AdminControl.getPort()`][wsadmin_type_hints.AdminControl.getPort]
        - [`AdminControl.getType()`][wsadmin_type_hints.AdminControl.getType]
    """


def getMBeanCount(*args: Any) -> Any:  # undocumented
    """ """


def getMBeanInfo_jmx(*args: Any) -> Any:  # undocumented
    """ """


def getNode() -> str:
    """Returns the **name** of the **node** to which the scripting process is connected.

    Example:
        ```pycon
        >>> print(AdminControl.getNode())
        myNode
        ```

    !!! abstract "See also"
        - [`AdminControl.getCell()`][wsadmin_type_hints.AdminControl.getCell]
        - [`AdminControl.getHost()`][wsadmin_type_hints.AdminControl.getHost]
        - [`AdminControl.getPort()`][wsadmin_type_hints.AdminControl.getPort]
        - [`AdminControl.getType()`][wsadmin_type_hints.AdminControl.getType]
    """


def getObjectInstance(*args: Any) -> Any:  # undocumented
    """ """


def getPort() -> str:
    """Returns the port used for scripting connection.

    Example:
        ```pycon
        >>> print(AdminControl.getPort())
        10003
        ```

    !!! abstract "See also"
        - [`AdminControl.getCell()`][wsadmin_type_hints.AdminControl.getCell]
        - [`AdminControl.getHost()`][wsadmin_type_hints.AdminControl.getHost]
        - [`AdminControl.getNode()`][wsadmin_type_hints.AdminControl.getNode]
        - [`AdminControl.getType()`][wsadmin_type_hints.AdminControl.getType]
    """


def getPropertiesForDataSource(*args: Any) -> Any:  # undocumented
    """(Deprecated)"""


def getType(*args: Any) -> Any:  # undocumented
    """Returns the **connection type** used for scripting connection.

    Example:
        ```pycon
        >>> print(AdminControl.getType())
        SOAP
        ```

    !!! abstract "See also"
        - [`AdminControl.getCell()`][wsadmin_type_hints.AdminControl.getCell]
        - [`AdminControl.getHost()`][wsadmin_type_hints.AdminControl.getHost]
        - [`AdminControl.getNode()`][wsadmin_type_hints.AdminControl.getNode]
        - [`AdminControl.getPort()`][wsadmin_type_hints.AdminControl.getPort]
    """


def help(*args: Any) -> Any:  # undocumented
    """ """


def invoke(*args: Any) -> Any:  # undocumented
    """ """


def invoke_jmx(*args: Any) -> Any:  # undocumented
    """ """


def isRegistered(*args: Any) -> Any:  # undocumented
    """ """


def isRegistered_jmx(*args: Any) -> Any:  # undocumented
    """ """


def makeObjectName(*args: Any) -> Any:  # undocumented
    """ """


def queryMBeans(*args: Any) -> Any:  # undocumented
    """ """


def queryNames(
    pattern: Union[RunningObjectTemplate, str]
) -> MultilineList[RunningObjectName]:
    """Returns all the **object names** that match the input object template (_which may include a wild card_).

    Args:
        pattern (RunningObjectTemplate | str): The object template to match (eg. `type=Server,*`).

    Returns:
        object_names(MultilineList[RunningObjectName]): A newline-separated list of object names that match the template.

    Example:
        ```pycon
        >>> print(AdminControl.queryNames('*'))
        WebSphere:cell=MyCell,name=TraceService,mbeanIdentifier=TraceService,type=TraceService,node=MyNode,process=server1
        [...]
        >>> print(AdminControl.queryNames('type=DataSource,*'))
        WebSphere:name=myDataSource,process=XYZ,platform=dynamicproxy,node=myNode,JDBCProvider=[...]
        [...]
        ```

    !!! abstract "See also"
        - [`AdminControl.completeObjectName()`][wsadmin_type_hints.AdminControl.completeObjectName]

        To better understand how object templates work, see [_this explanation_][wsadmin_type_hints.typing_objects.object_name.RunningObjectTemplate].
    """
    ...


def queryNames_jmx(*args: Any) -> Any:  # undocumented
    """ """


def reconnect(*args: Any) -> Any:  # undocumented
    """ """


def setAttribute(*args: Any) -> Any:  # undocumented
    """ """


def setAttribute_jmx(*args: Any) -> Any:  # undocumented
    """ """


def setAttributes(*args: Any) -> Any:  # undocumented
    """ """


def setAttributes_jmx(*args: Any) -> Any:  # undocumented
    """ """


def startServer(*args: Any) -> Any:  # undocumented
    """ """


def stopServer(*args: Any) -> Any:  # undocumented
    """ """


def testConnection(*args: Any) -> Any:  # undocumented
    """ """


def trace(*args: Any) -> Any:  # undocumented
    """ """
