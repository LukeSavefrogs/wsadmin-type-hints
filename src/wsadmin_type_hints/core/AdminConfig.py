"""
Use the `AdminConfig` object to invoke configuration commands and to create or 
change elements of the WebSphere® Application Server configuration, for example, 
creating a data source.

TODO: Check renamed symbols get resolved in the documentation.

For more info see the [official documentation](https://www.ibm.com/docs/en/was-nd/8.5.5?topic=scripting-commands-adminconfig-object-using-wsadmin).
"""
from typing import (
    Any as _Any,
    List as _List,
    Literal as _Literal,
    Optional as _Optional,
    Union as _Union,
    overload as _overload,
)

from wsadmin_type_hints.typing_objects.object_name import (
    ConfigurationContainmentPath as _ConfigurationContainmentPath,
    ConfigurationObjectName as _ConfigurationObjectName,
    RunningObjectName as _RunningObjectName,
)
from wsadmin_type_hints.typing_objects.wsadmin_types import (
    MultilineList as _MultilineList,
    MultilineTableWithHeader as _MultilineTableWithHeader,
    MultilineTableWithoutHeader as _MultilineTableWithoutHeader,
    OpaqueDigestObject as _OpaqueDigestObject,
)
from wsadmin_type_hints.typing_objects.object_types import ObjectType as _ObjectType


def attributes(object_type: _ObjectType, /) -> _MultilineTableWithoutHeader[str]:
    """Displays all the possible **attributes** contained by an object of type `object_type`.

    The _attribute types_ are also displayed:

    - When the attribute represents a **reference to another object**,
        the type of the attribute has a suffix of `@`.
    - When the attribute represents a **collection of objects**,
        the type has a suffix of `*`.
    - If the type represents a **base type**,
        possible subtypes are listed after the base type in parenthesis.
    - If the type is an **enumeration**,
        it is listed as `ENUM`, followed by the possible values in parentheses.

    Args:
        object_type (_ObjectType): name of the object type. Use [`AdminConfig.types()`][wsadmin_type_hints.AdminConfig.types] to get a list of available types.

    Returns:
        attributes_table (_MultilineTableWithoutHeader[str]): Multiline table with the attributes of the given type.
            The first "word" in each line is the **attribute name**, and the rest is the **attribute** value **type**.

    Example:
        ```pycon
        >>> print(AdminConfig.attributes("Server"))
        adjustPort Boolean
        changeGroupAfterStartup String
        changeUserAfterStartup String
        clusterName String
        [...]
        customServices CustomService*
        [...]
        processDefinition ProcessDef(JavaProcessDef, NamedJavaProcessDef, NamedProcessDef)
        processDefinitions ProcessDef(JavaProcessDef, NamedJavaProcessDef, NamedProcessDef)*
        ```
    """
    ...


# TODO: Check return type
def checkin(document_uri: str, filename: str, digest: _OpaqueDigestObject, /) -> _Any:
    """Checks a document into the configuration repository.

    Args:
        document_uri (str): The document URI, relative to the root of the configuration repository.
            This document MUST exist in the repository.
        filename (str): The valid local filename where the contents of the document are located.
        digest (_OpaqueDigestObject): The opaque object returned by a prior call to the `AdminConfig.extract()` command.

    Question: More testing needed
        The **return type** needs to be checked.

    !!! abstract "See also"
        - [`AdminConfig.extract()`][wsadmin_type_hints.AdminConfig.extract]
    """
    ...


def convertToCluster(
    server_id: _ConfigurationObjectName, cluster_name: str, /
) -> _ConfigurationObjectName:
    """Converts the server `server_id` so that it is the first member of the
        new server cluster `cluster_name`.

    Creates a new `ServerCluster` object with the name specified by `cluster_name`,
        and makes the server specified by `server_id` the first member of this cluster.

    Applications loaded on this server are now configured on the new cluster.

    Args:
        server_id (_ConfigurationObjectName): The ID of the server to use as the first member of the cluster.
        cluster_name (str): The name of the new cluster.

    Returns:
        cluster_id(_ConfigurationObjectName): The configuration ID of the newly created Cluster.

    Example:
        ```pycon
        >>> server = AdminConfig.getid('/Server:myServer/')
        >>> new_cluster = AdminConfig.convertToCluster(server, 'myCluster')
        >>> print(new_cluster)
        myCluster(cells/myCell/clusters/myCluster|cluster.xml#ClusterMember_2)
        ```
    """
    ...


# --------------------------------------------------------------------------
@_overload
def create(
    type: _ObjectType,
    parent: _ConfigurationObjectName,
    attributes: _Union[str, _List[_List[str]]],
    /,
) -> _ConfigurationObjectName:
    """Create a new configuration object.

    Create a configuration object of the type named by
        `type`, the parent named by `parent`, using the attributes supplied by
        `attributes`.

    Args:
        type (_ObjectType): The type of the configuration object that will be created.
        parent (_ConfigurationObjectName): The configuration ID of the parent object.
        attributes (_Union[str, _List[_List[str]]]): A list of attributes to add to the new configuration object. Can be either in the string format or in the list format (see `attributes` for more information).

    Returns:
        new_object(_ConfigurationObjectName): The newly created configuration object.
    """
    ...


@_overload
def create(
    type: _ObjectType,
    parent: _ConfigurationObjectName,
    attributes: _Union[str, _List[_List[str]]],
    parent_attribute_name: str = "",
    /,
) -> _ConfigurationObjectName:
    """Create a new configuration object.

    Create a configuration object of the type named by
        `type`, the parent named by `parent`, using the attributes supplied
        by `attributes` and the attribute name in the parent given by
        `parent_attribute_name`.

    Args:
        type (_ObjectType): The type of the configuration object that will be created.
        parent (_ConfigurationObjectName): The configuration ID of the parent object.
        attributes (_Union[str, _List[_List[str]]]): A list of attributes to add to the new configuration object. Can be either in the string format or in the list format (see `attributes` for more information).
        parent_attribute_name (str, optional): _description_. Defaults to "".

    Returns:
        new_object(_ConfigurationObjectName): The newly created configuration object.
    """
    ...


def create(type: _ObjectType, parent: _ConfigurationObjectName, attributes: _Union[str, _List[_List[str]]], parent_attribute_name: str = "", /) -> _ConfigurationObjectName:  # type: ignore[misc]
    """Create a new configuration object.

    Create a configuration object of the type named by
        `type`, the parent named by `parent`, using the attributes supplied
        by `attributes` and, optionally, the attribute name in the parent given by
        `parent_attribute_name`.

    Args:
        type (_ObjectType): The type of the configuration object that will be created.
        parent (_ConfigurationObjectName): The configuration ID of the parent object.
        attributes (_Union[str, _List[_List[str]]]): A list of attributes to add to the new configuration object. Can be either in the string format or in the list format (see `attributes` for more information).
        parent_attribute_name (str, optional): _description_. Defaults to "".

    Returns:
        new_object(_ConfigurationObjectName): The newly created configuration object.

    Example:

        - Using Jython string attributes:
        ```pycon
        >>> jdbc1 = AdminConfig.getid('/JDBCProvider:jdbc1/')
        >>> print AdminConfig.create('DataSource', jdbc1, '[[name ds1]]')
        ```

        - Using Jython with list attributes:
        ```pycon
        >>> jdbc1 = AdminConfig.getid('/JDBCProvider:jdbc1/')
        >>> print AdminConfig.create('DataSource', jdbc1, [['name', 'ds1']])
        ```

    Question: More testing needed
        The documentation is not clear on how to use the `create` method.

        For example, on the offline server documentation, the **additional `parent_attribute_name`** is cited, while
        in the online server documentation this is **not present**.

        The examples should be tested.


    !!! abstract "See also"
        - [`AdminConfig.modify()`][wsadmin_type_hints.AdminConfig.modify]
        - [`AdminConfig.remove()`][wsadmin_type_hints.AdminConfig.remove]
    """
    ...


# --------------------------------------------------------------------------


def createClusterMember(*args: _Any) -> _Any:  # undocumented
    ...


def createDocument(document_uri: str, filename: str, /) -> _Any:
    """Creates a document in the configuration repository.

    Args:
        document_uri (str): The document to be created in the repository.
        filename (str): A valid local filename where the contents of the document are located.

    Example:
        ```pycon
        >>> AdminConfig.createDocument('cells/myCell/myfile.xml', '/mydir/myfile')
        ```

    Question: More testing needed
        The **return type** needs to be checked.

    !!! abstract "See also"
        - [`AdminConfig.deleteDocument()`][wsadmin_type_hints.AdminConfig.deleteDocument]
        - [`AdminConfig.existsDocument()`][wsadmin_type_hints.AdminConfig.existsDocument]
    """
    ...


def createUsingTemplate(type: _ObjectType, parent: _ConfigurationObjectName, attributes: _Union[str, _List[_List[str]]], template: _ConfigurationObjectName) -> _ConfigurationObjectName:
    """ Creates a new configuration object of the given type
    using the specified template as the basis.
    
    The specified attributes override settings in the template.

    The template parameter is a configuration ID of an existing object.
    This object can be either a template object, returned by using the
    `AdminConfig.listTemplates()` method, or any other existing object
    of the correct type.

    Args:
        type (_ObjectType): The type of the configuration object that will be created.
        parent (_ConfigurationObjectName): The configuration ID of the parent object.
        attributes (str | _List[_List[str]]): A list of attributes to add to the new configuration object. 
            Can be either in the string format or in the list format (see `attributes` for more information).
        template (_ConfigurationObjectName): The configuration ID of the template object.

    Returns:
        new_object(_ConfigurationObjectName): The newly created configuration object.

    Example:
        ```pycon
        >>> provider = AdminConfig.getid('/JDBCProvider:myProvider/')
        >>> template = AdminConfig.listTemplates('DataSource', '"Oracle JDBC Driver DataSource').splitlines()[0]
        >>> print(AdminConfig.createUsingTemplate('DataSource', provider, '[[name ds1]]', template))
        ds1(cells/myCell|resources.xml#DataSource_1699530172743)
        ```
    
    !!! abstract "See also"
        - [`AdminConfig.listTemplates()`][wsadmin_type_hints.AdminConfig.listTemplates]
        - [`AdminConfig.create()`][wsadmin_type_hints.AdminConfig.create]
        - [`AdminConfig.modify()`][wsadmin_type_hints.AdminConfig.modify]
        - [`AdminConfig.remove()`][wsadmin_type_hints.AdminConfig.remove]
    """


def defaults(object_type: _ObjectType, /) -> _MultilineTableWithHeader[str]:
    """Displays all the possible attributes contained by an object of type `object_type`, along with
        the type and default value of each attribute, if the attribute has a default value.

    Args:
        object_type (_ObjectType): The type of the object

    Returns:
        defaults (_MultilineTableWithHeader[str]): Tab-separated table with all the attribute defaults.
            The table consists of the following columns:

            1. `Attribute`: Attribute name
            2. `Type`: Attribute type
            3. `Default`: Default value


    Example:
        ```pycon
        >>> print AdminConfig.defaults("Server")
        Attribute                       Type                            Default
        name                            String
        clusterName                     String
        modelId                         String
        shortName                       String
        uniqueId                        String
        developmentMode                 boolean                         false
        parallelStartEnabled            boolean                         true
        [...]
        ```
    """
    ...


def deleteDocument(document_uri: str, /) -> _Any:
    """Deletes a document from the configuration repository.

    Args:
        document_uri (str): The document to be deleted from the repository.

    Example:
        ```pycon
        >>> AdminConfig.deleteDocument('cells/mycell/myfile.xml')
        ```

    Question: More testing needed
        The **return type** needs to be checked.

    !!! abstract "See also"
        - [`AdminConfig.createDocument()`][wsadmin_type_hints.AdminConfig.createDocument]
        - [`AdminConfig.existsDocument()`][wsadmin_type_hints.AdminConfig.existsDocument]
    """
    ...


def existsDocument(document_uri: str, /) -> bool:
    """Tests to see if a document exists in the configuration repository.

    Args:
        document_uri (str): The document to be tested in the repository.

    Returns:
        exists(bool): Returns `1` if the document exists; `0` otherwise.

    Example:
        ```pycon
        >>> exists = AdminConfig.existsDocument('cells/mycell/myfile.xml')
        >>> print(exists)
        1
        >>> if exists:
        ...     print("Document exists")
        ... else:
        ...     print("Document does not exist")
        ...
        Document exists
        ```

    !!! abstract "See also"
        - [`AdminConfig.createDocument()`][wsadmin_type_hints.AdminConfig.createDocument]
        - [`AdminConfig.deleteDocument()`][wsadmin_type_hints.AdminConfig.deleteDocument]
    """
    ...


def extract(document_uri: str, filename: str, /) -> _OpaqueDigestObject:
    """Extracts a configuration repository file that is described by the document URI and places it in the file named by filename.
    This method only applies to deployment manager configurations.

    Args:
        document_uri (str): The document URI, relative to the root of the configuration repository. This MUST exist in the repository.
        filename (str): The name of the source file to check. If it exists already, it will be overwritten.

    Returns:
        _OpaqueDigestObject: An opaque "digest" object which should be used to check the file back in using the checkin command.

    !!! abstract "See also"
        - [`AdminConfig.checkin()`][wsadmin_type_hints.AdminConfig.checkin]
    """
    ...


def getCrossDocumentValidationEnabled() -> str:
    """Returns a message giving the current cross-document enablement setting.

    Returns:
        message(str): The current cross-document enablement setting.

    Example:
        ```pycon
        >>> print(AdminConfig.getCrossDocumentValidationEnabled())
        WASX7188I: Cross-document validation enablement set to true
        ```

    !!! abstract "See also"
        - [`AdminConfig.setCrossDocumentValidationEnabled()`][wsadmin_type_hints.AdminConfig.setCrossDocumentValidationEnabled]
    """
    ...


def getid(
    containment_path: _ConfigurationContainmentPath, /
) -> _ConfigurationObjectName:
    """Returns the unique configuration ID for an object described by the
        given containment path.

    Args:
        containment_path (_ConfigurationContainmentPath): The containment path of the requested object

    Returns:
        configuration_id (_ConfigurationObjectName): The configuration ID for the object

    Example:
        ```pycon
        >>> print(AdminConfig.getid("/Node:myNode/Server:myServer/"))
        myServer(cells/myCell/nodes/myNode/servers/myServer|server.xml#Server_1)
        ```
    """
    ...


def getObjectName(
    configuration_id: _ConfigurationObjectName, /
) -> _Union[_RunningObjectName, _Literal[""]]:
    """Returns a string version of the ObjectName for the MBean that corresponds to this configuration ID.

    If there is no such running MBean this returns an empty string.

    Args:
        configuration_id (_ConfigurationObjectName): The configuration ID of the object

    Returns:
        mbean_object_name (_RunningObjectName | _Literal[""]): ObjectName of the MBean corresponding to the specified configuration ID.

    Example:
        ```pycon
        # Search the configuration ID of the object
        >>> server = AdminConfig.getid("/Node:myNode/Server:myServer/")
        >>> print(server)
        myServer(cells/myCell/nodes/myNode/servers/myServer|server.xml#Server_1)

        # Retrieve the running object from the configuration ID (not running if empty string)
        >>> server_instance = AdminConfig.getObjectName(server)
        >>> print(server_instance)
        WebSphere:name=myServer,process=myServer,platform=proxy,node=myNode,j2eeType=J2EEServer,version=9.0.5.14,type=Server,mbeanIdentifier=cells/myCell/nodes/myNode/servers/myServer/server.xml#Server_1,cell=myCell,spec=1.0,processType=ManagedProcess
        ```
    """
    ...


def getObjectType(configuration_id: _ConfigurationObjectName, /) -> _ObjectType:
    """Displays the configuration object type indentified by `configuration_id`.

    Args:
        configuration_id (_ConfigurationObjectName): The configuration object which type is being requested.

    Returns:
        object_type (_ObjectType): The object type indentified by `configuration_id`.

    Example:
        ```pycon
        >>> configuration_id = AdminConfig.getid("/Cell:myCell/")
        >>> print(AdminConfig.getObjectType(configuration_id))
        Cell
        ```
    """
    ...


def getSaveMode() -> _Literal["overwriteOnConflict", "rollbackOnConflict"]:
    """Returns the mode that will be used when the [`AdminConfig.save()`][wsadmin_type_hints.AdminConfig.save] method will be invoked.

    Returns:
        save_mode (_Literal["overwriteOnConflict", "rollbackOnConflict"]): The mode used when `save` is invoked.
            Possible values are:

            - `"overwriteOnConflict"` to save changes even if they conflict
                with other configuration changes;
            - `"rollbackOnConflict"` to cause a save operation to fail if
            changes conflict with other configuration changes;
            this value is the default.

    Example:
        ```pycon
        >>> print(AdminConfig.getSaveMode())
        rollbackOnConflict
        ```

    !!! abstract "See also"
        - [`AdminConfig.setSaveMode()`][wsadmin_type_hints.AdminConfig.setSaveMode]
        - [`AdminConfig.save()`][wsadmin_type_hints.AdminConfig.save]
        - [`AdminConfig.reset()`][wsadmin_type_hints.AdminConfig.reset]
    """
    ...


def getValidationLevel() -> str:
    """Returns a message giving the current validation level.

    Returns:
        message(str): The current validation level.

    Example:
        ```pycon
        >>> print(AdminConfig.getValidationLevel())
        WASX7189I: Validation level set to HIGHEST
        ```

    !!! abstract "See also"
        - [`AdminConfig.setValidationLevel()`][wsadmin_type_hints.AdminConfig.setValidationLevel]
    """
    ...


def getValidationSeverityResult(
    severity: _Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], /
) -> int:
    """Returns the number of validation messages with the given
        severity from the most recent validation.

    Args:
        severity (int): The severity level for which to return the number of validation messages.
            Specify an integer value **between 0 and 9**.

    Returns:
        messages_count(int): A string that indicates the number of validation messages of the given severity.

    Example:
        ```pycon
        >>> print(AdminConfig.getValidationSeverityResult(1))
        16
        ```
    """
    ...


def hasChanges() -> bool:
    """Check if there are unsaved configuration changes.

    Returns:
        has_changes (bool): Truthy (actual value is `1`) if unsaved configuration changes exist, falsy (`0`) otherwise.

    Example:
        ```pycon
        >>> print(AdminConfig.hasChanges())
        0
        ```
    """
    ...


# --------------------------------------------------------------------------
@_overload
def help() -> str:
    """Displays general help for the `AdminConfig` module.

    Returns:
        help (str): A general help.
    """
    ...


@_overload
def help(method_name: str, /) -> str:
    """Displays help for the `AdminConfig` method specified by `method_name`.

    Args:
        method_name (str): The name of the method whose description needs to be retrieved.

    Returns:
        help (str): A more specific help regarding the method `method_name`.
    """
    ...


def help(method_name: str = "", /) -> str:  # type: ignore[misc]
    """Displays help for the `AdminConfig` module and its methods.

    Args:
        method_name (str, optional): The name of the method whose description needs to be retrieved.

    Returns:
        message (str): The help message regarding the method `method_name` (if provided), otherwise the description of the `AdminConfig` module and its methods.

    Example:
        - To get an **overview** of the module and its methods:
        ```pycon
        >>> print(AdminConfig.help())
        WASX7053I: The AdminConfig object communicates with the
        Config Service in a WebSphere server to manipulate configuration data
        for a WebSphere installation.  AdminConfig has commands to list, create,
        remove, display, and modify configuration data, as well as commands to
        display information about configuration data types.
        [...]
        ```

        - For a more detailed description of a **single method**:
        ```pycon
        >>> print(AdminConfig.help("attributes"))
        WASX7061I: Method: attributes

        Arguments: type

        Description: Displays all the possible attributes contained by an
        object of type "type."  The attribute types are also displayed; when
        the attribute represents a reference to another object, the type of
        [...]
        ```
    """
    ...


# --------------------------------------------------------------------------


def installResourceAdapter(*args: _Any) -> _Any:  # undocumented
    ...


# --------------------------------------------------------------------------
@_overload
def list(object_type: _ObjectType, /) -> _MultilineList[_ConfigurationObjectName]:
    """Lists all the configuration objects of the type named by `object_type`.

    Args:
        object_type (_ObjectType): The name of the object type.

    Returns:
        objects(_MultilineList[_ConfigurationObjectName]): Multiline list of objects of the given type.
    """
    ...


@_overload
def list(
    object_type: _ObjectType, scope: _ConfigurationObjectName, /
) -> _MultilineList[_ConfigurationObjectName]:
    """Lists all the configuration objects of the type named by `object_type` in the scope of `scope`.

    Args:
        object_type (_ObjectType): The name of the object type.
        scope (_ConfigurationObjectName): The scope of the search.

    Returns:
        objects(_MultilineList[_ConfigurationObjectName]): Multiline list of objects of the given type found under the scope of `scope`.
    """
    ...


@_overload
def list(
    object_type: _ObjectType, pattern: str, /
) -> _MultilineList[_ConfigurationObjectName]:
    """Lists all the configuration objects of the type named by `object_type` and matching
    wildcard characters or Java regular expressions.

    Args:
        object_type (_ObjectType): The name of the object type.
        pattern (str): The pattern (wildcard characters or Java regular expressions) that needs to be matched.

    Returns:
        objects(_MultilineList[_ConfigurationObjectName]): Multiline list of objects of the given type matching the pattern `pattern`
    """
    ...


def list(object_type: _ObjectType, scope_or_pattern: _Optional[_Union[_ConfigurationObjectName, str]] = "", /) -> _MultilineList[_ConfigurationObjectName]:  # type: ignore[misc]
    """Lists all the configuration objects of the type named by `object_type`.

    Args:
        object_type (_ObjectType): The name of the object type.
        scope_or_pattern (_Union[_ConfigurationObjectName, str], optional): This parameter causes a different behaviour depending on its type:

            - `_ConfigurationObjectName`: Limit the search within the scope of the configuration object named by `scope`.
            - `str`: Search all the configuration objects matching wildcard characters or Java regular expressions.

    Returns:
        objects(_MultilineList[_ConfigurationObjectName]): Multiline list of objects of a given type, possibly scoped by a parent.

    Example:
        If the `scope_or_pattern` parameter is omitted, then will be returned a list of all servers defined:
        ```pycon
        >>> print(AdminConfig.list("Server"))
        ```

        You can narrow the search using the `scope_or_pattern` parameter:

        - Limit the search to only the servers under the **scope** of the node `node`:
            ```pycon
            >>> node = AdminConfig.list("Node").splitlines()[0]
            >>> print(AdminConfig.list("Server", node))
            ```
        - Search the servers matching a specific **wildcard** pattern:
            ```pycon
            >>> print(AdminConfig.list("Server", "server1*"))
            ```
        - Search the servers matching a specific **regular expression** pattern:
            ```pycon
            >>> print(AdminConfig.list("Server", "server1.*"))
            ```
    """
    ...


# --------------------------------------------------------------------------


@_overload
def listTemplates(type: _ObjectType, /) -> _MultilineList[_ConfigurationObjectName]:
    """Returns a list of all the templates available for the given type.

    These templates may be used in invocations of [`AdminConfig.createUsingTemplate`][wsadmin_type_hints.AdminConfig.createUsingTemplate].

    Args:
        type (_ObjectType): The name of the target object type.

    Returns:
        _MultilineList[_ConfigurationObjectName]: Multiline string with the requested templates configuration IDs.

    Example:
        ```pycon
        >>> print(AdminConfig.listTemplates("Server"))
        apache13(templates/servertypes/APACHE_SERVER/servers/apache13|server.xml#Server_1)
        apache20(templates/servertypes/APACHE_SERVER/servers/apache20|server.xml#Server_1)
        apache22(templates/servertypes/APACHE_SERVER/servers/apache22|server.xml#Server_1)
        customHTTP(templates/servertypes/CUSTOMHTTP_SERVER/servers/customHTTP|server.xml#Server_1177012689063)
        default(templates/servertypes/APPLICATION_SERVER/servers/default|server.xml#Server_1)
        default(templates/servertypes/GENERIC_SERVER/servers/default|server.xml#Genericserver_1)
        defaultXD(templates/servertypes/APPLICATION_SERVER/servers/defaultXD|server.xml#Server_1)
        [...]
        ```
    """
    ...


@_overload
def listTemplates(
    type: _ObjectType, pattern: str, /
) -> _MultilineList[_ConfigurationObjectName]:
    """Returns a list of the templates available for the given type that match the provided `pattern`.

    These templates may be used in invocations of [`AdminConfig.createUsingTemplate`][wsadmin_type_hints.AdminConfig.createUsingTemplate].

    Args:
        type (_ObjectType): The name of the target object type.
        pattern (str): A query (wildcard characters or Java regular expressions) to filter the results.

    Returns:
        _MultilineList[_ConfigurationObjectName]: Multiline string with the requested templates configuration IDs.

    Example:
        ```pycon
        >>> print(AdminConfig.listTemplates("Server", "php"))
        phpserver(templates/servertypes/PHP_SERVER/servers/APACHE13_PHP4|server.xml#Server_1)
        phpserver(templates/servertypes/PHP_SERVER/servers/APACHE13_PHP5|server.xml#Server_1)
        phpserver(templates/servertypes/PHP_SERVER/servers/APACHE20_PHP4|server.xml#Server_1)
        phpserver(templates/servertypes/PHP_SERVER/servers/APACHE20_PHP5|server.xml#Server_1)
        phpserver(templates/servertypes/PHP_SERVER/servers/APACHE22_PHP4|server.xml#Server_1)
        phpserver(templates/servertypes/PHP_SERVER/servers/APACHE22_PHP5|server.xml#Server_1)
        ```
    """
    ...


def listTemplates(type: _ObjectType, pattern: str = "", /) -> _MultilineList[_ConfigurationObjectName]:  # type: ignore[misc]
    """Returns a list of the templates available for the given type that match the provided `pattern`.

    These templates may be used in invocations of [`AdminConfig.createUsingTemplate`][wsadmin_type_hints.AdminConfig.createUsingTemplate].

    Args:
        type (_ObjectType): The name of the target object type.
        pattern (str): A query (wildcard characters or Java regular expressions) to filter the results.

    Returns:
        configuration_ids (_MultilineList[_ConfigurationObjectName]): Multiline string with the requested templates configuration IDs.

    Example:
        ```pycon
        >>> print(AdminConfig.listTemplates("Server", "php"))
        phpserver(templates/servertypes/PHP_SERVER/servers/APACHE13_PHP4|server.xml#Server_1)
        phpserver(templates/servertypes/PHP_SERVER/servers/APACHE13_PHP5|server.xml#Server_1)
        phpserver(templates/servertypes/PHP_SERVER/servers/APACHE20_PHP4|server.xml#Server_1)
        phpserver(templates/servertypes/PHP_SERVER/servers/APACHE20_PHP5|server.xml#Server_1)
        phpserver(templates/servertypes/PHP_SERVER/servers/APACHE22_PHP4|server.xml#Server_1)
        phpserver(templates/servertypes/PHP_SERVER/servers/APACHE22_PHP5|server.xml#Server_1)
        ```

    !!! abstract "See also"
        - [`AdminConfig.createUsingTemplate()`][wsadmin_type_hints.AdminConfig.createUsingTemplate]
    """
    ...


# --------------------------------------------------------------------------


def modify(
    configuration_id: _ConfigurationObjectName,
    attributes: _Union[str, _List[_List[str]]],
    /,
) -> _Literal[""]:
    """Change only the attributes specified by `attributes`
        for the configuration object named by `configuration_id`.

    Args:
        configuration_id (_ConfigurationObjectName): The configuration ID of the object whose `attribute`s need to be changed.
        attributes (str | _List[_List[str]]): The attributes to modify, along with their new value.

    Returns:
        empty (_Literal['']): An empty string.

    Example:
        In this example we'll take for granted that every code block is preceded by the following commands:
        ```pycon
        >>> datasource = AdminConfig.list("DataSource", "*LUCAXA*").splitlines()[0]
        >>> print(datasource)
        DUMMYDB24LUCAXA(cells/myCell/clusters/myCluster|resources.xml#DataSource_1678720288191)
        >>> print(AdminConfig.showAttribute(datasource, "description"))
        Datasource Test
        ```

        This is how you can modify an existing configuration object:

        - Using **lists**:
        ```pycon
        >>> AdminConfig.modify(datasource, [["description", "This is the new description!"]])
        ''
        >>> print(AdminConfig.showAttribute(datasource, "description"))
        This is the new description!
        ```

        - Using a **string**:
            ```pycon
            >>> AdminConfig.modify(datasource, '[[description "This is the new(er) description!"]]')
            ''
            >>> print(AdminConfig.showAttribute(datasource, "description"))
            This is the new(er) description!
            ```
            Notice how it _**may seem** like a list_ enclosed in quotes BUT with some differences:

            1. The **comma** (`,`) between the key and the value **must be omitted**;
            1. Both keys and values do not need to be surrounded in **quotes**, except when they **contain spaces or special characters**.

    !!! abstract "See also"
        - [`AdminConfig.create()`][wsadmin_type_hints.AdminConfig.create]
        - [`AdminConfig.remove()`][wsadmin_type_hints.AdminConfig.remove]
        - [`AdminConfig.resetAttributes()`][wsadmin_type_hints.AdminConfig.resetAttributes]
        - [`AdminConfig.show()`][wsadmin_type_hints.AdminConfig.show]
        - [`AdminConfig.showall()`][wsadmin_type_hints.AdminConfig.showall]
        - [`AdminConfig.showAttribute()`][wsadmin_type_hints.AdminConfig.showAttribute]
    """
    ...


def parents(type: _ObjectType, /) -> _MultilineList[_ObjectType]:
    """Displays the object types that can contain `type`.

    Args:
        type (_ObjectType): The object type you want to find parents of.

    Returns:
        parents (_MultilineList[_ObjectType]): The parent object types.

    Example:
        ```pycon
        >>> print(AdminConfig.parents("Server"))
        DynamicCluster
        Node
        ServerCluster
        ```
    """
    ...


def queryChanges() -> _MultilineList[str]:
    """Returns a list of unsaved configuration files.

    Returns:
        changed_files (str): Multiline list of unsaved configuration files.

    Example:
        - If some unsaved changes are **found**:
        ```pycon
        >>> print(AdminConfig.queryChanges())
        WASX7146I: The following configuration files contain unsaved changes:
        cells/mycell/nodes/mynode/servers/server1|resources.xml
        ```

        - In case unsaved changes are **not found**:
        ```pycon
        >>> print(AdminConfig.queryChanges())
        WASX7241I: There are no unsaved changes in this workspace.
        ```

    !!! Warning
        **Do NOT** use this method as a way to **check** if there are changes that need to be saved!
        If that is your goal, see if you can use the [**`AdminConfig.hasChanges()`**][wsadmin_type_hints.AdminConfig.hasChanges] method instead.

        Use the `AdminConfig.queryChanges()` method ONLY to **show** which files have been changed but not saved.
    """
    ...


def remove(*args: _Any) -> _Any:  # undocumented
    ...


def required(object_type: _ObjectType, /) -> _MultilineTableWithHeader[str]:
    """Displays a table with the required attributes contained by an object of type `object_type`.

    Args:
        object_type (_ObjectType): The object type as returned by the [`AdminConfig.types()`][wsadmin_type_hints.AdminConfig.types] method.

    Returns:
        required_schema (_MultilineTableWithHeader[str]): A table with the required attributes contained by the object.
            The first row contains the header.

    Example:
        This is an example of how to use the `required()` method:
        ```pycon
        >>> print(AdminConfig.required("Server"))
        Attribute                       Type
        name                            String
        ```

    Warning:
        When the type has **no required attributes**, the returned table will NOT be an empty string.
        Instead, it will contain only the message _`WASX7361I`_:
        ```pycon
        >>> print(AdminConfig.required("JavaVirtualMachine"))
        WASX7361I: No required attribute found for type "JavaVirtualMachine".
        ```

    !!! abstract "See also"
        - For a list of all the available object types, see [`AdminConfig.types()`][wsadmin_type_hints.AdminConfig.types]
        - For a list of all the attributes available for the requested object type, see [`AdminConfig.attributes()`][wsadmin_type_hints.AdminConfig.attributes]
        - For a list of all the default values for the attributes of the requested object type, see [`AdminConfig.defaults()`][wsadmin_type_hints.AdminConfig.defaults]
    """
    ...


def reset() -> _Literal[""]:
    """Discard unsaved configuration changes.

    Returns:
        empty (_Literal['']): An empty string is always returned

    !!! abstract "See also"
        - For the opposite operation, see [`AdminConfig.save()`][wsadmin_type_hints.AdminConfig.save]
    """
    ...


def resetAttributes(*args: _Any) -> _Any:  # undocumented
    ...


def save() -> _Literal[""]:
    """Commits unsaved changes to the configuration repository.

    Returns:
        empty (_Literal['']): An empty string is always returned

    !!! abstract "See also"
        - For the opposite operation, see [`AdminConfig.reset()`][wsadmin_type_hints.AdminConfig.reset]
    """
    ...


def setCrossDocumentValidationEnabled(flag: _Literal["true", "false"], /) -> str:
    """Enables or disables the cross-document validation.

    Args:
        flag (_Literal["true", "false"]): Pass `true` to enable the cross-document validation, or `false` to disable it.

    Returns:
        message (str): The same message returned by [`AdminConfig.getCrossDocumentValidationEnabled()`][wsadmin_type_hints.AdminConfig.getCrossDocumentValidationEnabled].

    Example:
        ```pycon
        >>> print(AdminConfig.getCrossDocumentValidationEnabled())
        WASX7188I: Cross-document validation enablement set to true

        >>> print(AdminConfig.setCrossDocumentValidationEnabled("false"))
        WASX7188I: Cross-document validation enablement set to false

        >>> print(AdminConfig.getCrossDocumentValidationEnabled())
        WASX7188I: Cross-document validation enablement set to false
        ```

    !!! abstract "See also"
        - [`AdminConfig.getCrossDocumentValidationEnabled()`][wsadmin_type_hints.AdminConfig.getCrossDocumentValidationEnabled]
    """
    ...


def setSaveMode(
    save_mode: _Literal["overwriteOnConflict", "rollbackOnConflict"], /
) -> _Literal[""]:
    """Changes the mode that will be used when the [`AdminConfig.save()`][wsadmin_type_hints.AdminConfig.save] method will be invoked.

    Args:
        save_mode (_Literal["overwriteOnConflict", "rollbackOnConflict"]): The save mode for the configuration repository

    Example:
        ```pycon
        >>> print(AdminConfig.getSaveMode())
        rollbackOnConflict
        >>> AdminConfig.setSaveMode("overwriteOnConflict")
        >>> print(AdminConfig.getSaveMode())
        overwriteOnConflict
        ```

    !!! abstract "See also"
        - [`AdminConfig.getSaveMode()`][wsadmin_type_hints.AdminConfig.getSaveMode]
        - [`AdminConfig.save()`][wsadmin_type_hints.AdminConfig.save]
        - [`AdminConfig.reset()`][wsadmin_type_hints.AdminConfig.reset]
    """
    ...


def setValidationLevel(
    level: _Literal["none", "low", "medium", "high", "highest"], /
) -> str:
    """Sets the validation used when files are extracted from the repository.

    Args:
        level (_Literal["none", "low", "medium", "high", "highest"]): The validation level to use.

    Returns:
        message(str): A message indicating the current validation level.

    Example:
        ```pycon
        >>> print(AdminConfig.getValidationLevel())
        WASX7188I: Validation level set to "none"

        >>> print(AdminConfig.setValidationLevel("high"))
        WASX7188I: Validation level set to "high"

        >>> print(AdminConfig.getValidationLevel())
        WASX7188I: Validation level set to "high"
        ```

    !!! abstract "See also"
        - [`AdminConfig.getValidationLevel()`][wsadmin_type_hints.AdminConfig.getValidationLevel]
    """
    ...


def show(
    configuration_id: _ConfigurationObjectName,
    attributes: _Optional[_List[str]] = None,
    /,
) -> str:
    """Displays all the attributes for the configuration object named by `configuration_id`.

    If the `attributes` parameter is not specified, all the attributes for the configuration
    object are displayed, otherwise only the attributes specified in the `attributes` parameter.

    Args:
        configuration_id (_ConfigurationObjectName): The configuration ID for the configuration object to display.
        attributes (_Optional[_List[str]]): A list of attributes to display. If not specified, all the attributes are displayed.

    Returns:
        attributes (str): The list of attributes for the configuration object.

    Example:
        ```pycon
        >>> variable_id = AdminConfig.list("VariableSubstitutionEntry").splitlines()[0]
        >>> print(AdminConfig.show(variable_id))
        [description []]
        [symbolicName DB2_JCC_DRIVER_PATH]
        [value /opt/XLWAS/drivers/DB2V11/4.23.1044]
        ```

    !!! abstract "See also"
        - [`AdminConfig.showall()`][wsadmin_type_hints.AdminConfig.showall]
        - [`AdminConfig.attributes()`][wsadmin_type_hints.AdminConfig.attributes]
        - [`AdminConfig.showAttribute()`][wsadmin_type_hints.AdminConfig.showAttribute]
    """
    ...


def showall(
    configuration_id: _ConfigurationObjectName,
    attributes: _Optional[_List[str]] = None,
    /,
) -> str:
    """Recursively displays all the attributes for the configuration object named by `configuration_id`.

    If the `attributes` parameter is not specified, all the attributes for the configuration
    object are displayed, otherwise only the attributes specified in the `attributes` parameter.

    Args:
        configuration_id (_ConfigurationObjectName): The configuration ID for the configuration object to display.
        attributes (_Optional[_List[str]]): A list of attributes to display. If not specified, all the attributes are displayed.

    Returns:
        attributes (str): The list of attributes for the configuration object.

    Example:
        In the following examples you can see the difference between the `AdminConfig.show()`
        and `AdminConfig.showall()` methods:

        - When the `AdminConfig.showall()` method encounters a reference to another configuration object,
        it _recursively_ descends into the referenced configuration object and displays its attributes,
        continuing until all children and grand-children are "expanded".
        - On the other hand, the `AdminConfig.show()` method always returns the _string representation_ of the
        configuration object ID.

        ```pycon
        >>> server_id = AdminConfig.getid("/Node:myNode/Server:myServer/")

        >>> print AdminConfig.show(server_id, ["errorStreamRedirect"])
        [errorStreamRedirect (cells/myCell/nodes/myNode/servers/myServer|server.xml#StreamRedirect_1599578915053)]

        >>> print AdminConfig.showall(server_id, ["errorStreamRedirect"])
        [errorStreamRedirect [[baseHour 1]
        [fileName /WebSphere_LOG/was/myCell/myNode/myCluster/APPSERVER/myServer-SystemErr.log]
        [formatWrites false]
        [maxNumberOfBackupFiles 5]
        [messageFormatKind BASIC]
        [rolloverPeriod 24]
        [rolloverSize 100]
        [rolloverType BOTH]
        [suppressStackTrace false]
        [suppressWrites false]]]
        ```

    !!! abstract "See also"
        - [`AdminConfig.show()`][wsadmin_type_hints.AdminConfig.show]
        - [`AdminConfig.attributes()`][wsadmin_type_hints.AdminConfig.attributes]
        - [`AdminConfig.showAttribute()`][wsadmin_type_hints.AdminConfig.showAttribute]
    """
    ...


def showAttribute(
    configuration_id: _ConfigurationObjectName, attribute: str, /
) -> _Any:
    """Shows the value of the single attribute specified for the configuration object named by `configuration_id`.

    The output of this command is different from the output of [`AdminConfig.show()`][wsadmin_type_hints.AdminConfig.show] when a single
    attribute is specified: the `AdminConfig.showAttribute` command does not display a
    list containing the attribute name and value; rather, the **attribute value alone** is displayed.

    Args:
        configuration_id (_ConfigurationObjectName): The configuration ID for the parent object of the `attribute`.
        attribute (str): The name of the attribute value to retrieve.

    Returns:
        attribute_value (_Any): The value of the single attribute specified.

    !!! Tip
        For a complete list of attributes available for the configuration object use the [`AdminConfig.attributes()`][wsadmin_type_hints.AdminConfig.attributes]
        method passing the object type as a parameter.

        For example, if you don't remember the name of an attribute for the `Server` object type, you can `print(AdminConfig.attributes("Server"))`.

    Example:
        ```pycon
        >>> server = AdminConfig.getid("/Node:myNode/Server:myServer/")
        >>> server_name, server_cluster = AdminConfig.showAttribute(server, "name"), AdminConfig.showAttribute(server, "clusterName")
        >>> print("Server '%s' is part of cluster '%s'" % (server_name, server_cluster))
        Server 'myServer' is part of cluster 'myCluster'
        ```
    """
    ...


# --------------------------------------------------------------------------
@_overload
def types() -> _MultilineList[_ObjectType]:
    """Displays all the possible top-level configuration object types.

    Returns:
        types(_MultilineList[_ObjectType]): All the top-level configuration object types.
    """
    ...


@_overload
def types(pattern: str, /) -> _MultilineList[_ObjectType]:
    """Displays all the possible top-level configuration object types matching
    with the `pattern`, which can be a wildcard or a regular expression.

    Args:
        pattern (str): A wildcard or a regular expression matching the type to search.

    Returns:
        types(_MultilineList[_ObjectType]): A multiline list of all the possible top-level configuration object types
            matching the provided `pattern`.
    """
    ...


def types(pattern: _Optional[str] = "", /) -> _MultilineList[_ObjectType]:  # type: ignore[misc]
    """Displays all the possible top-level configuration object types, restricting the
    search to the types matching the `pattern` parameter, if specified.

    Args:
        pattern (_Optional[str], optional): A wildcard or a regular expression matching the type to search.

    Returns:
        types(_MultilineList[_ObjectType]): A multiline list of all the possible top-level configuration object types
            matching the provided `pattern` (if specified).

    Example:
        - Print **all** the available types:
            ```pycon
            >>> print(AdminConfig.types())
            AccessPointGroup
            Action
            ActivationSpec
            ActivationSpecTemplateProps
            ActiveAffinityType
            [...]
            ```
        - Print **only** the types matching the regex `No.*`:
            ```pycon
            >>> print(AdminConfig.types("No.*"))
            NoOpPolicy
            Node
            NodeAgent
            NodeGroup
            NodeGroupMember
            ```
    """
    ...


# --------------------------------------------------------------------------


def uninstallResourceAdapter(*args: _Any) -> _Any:  # undocumented
    ...


def unsetAttributes(*args: _Any) -> _Any:  # undocumented
    ...


# --------------------------------------------------------------------------
@_overload
def validate() -> str:
    r"""Requests **configuration validation** results based on the
    files in your workspace, the value of the cross-document validation
    enabled flag, and the validation level setting.

    Returns:
        validation_result (str): The result of the validation request.

    Example:
        ```pycon
        >>> print(AdminConfig.validate())
        WASX7193I: Validation results are logged in c:\WebSphere5\AppServer\logs\wsadmin.valout: Total number of messages: 16
        WASX7194I: Number of messages of severity 1: 16
        ```
    """
    ...


@_overload
def validate(configuration_id: _ConfigurationObjectName, /) -> str:
    r"""Requests **configuration validation** results based on the
    files in your workspace, the value of the cross-document validation
    enabled flag, and the validation level setting.

    The **scope** of this request is the object named by `configuration_id`.

    Args:
        configuration_id (_ConfigurationObjectName, optional): The scope of the request.

    Returns:
        validation_result (str): The result of the validation request.

    Example:
        ```pycon
        >>> server = AdminConfig.getid("/Node:myNode/Server:myServer/")
        >>> print(AdminConfig.validate(server))
        WASX7193I: Validation results are logged in c:\WebSphere5\AppServer\logs\wsadmin.valout_2: Total number of messages: 0
        ```
    """
    ...


def validate(configuration_id: _ConfigurationObjectName = "", /) -> str:  # type: ignore[misc]
    r"""Requests **configuration validation** results based on the
    files in your workspace, the value of the cross-document validation
    enabled flag, and the validation level setting.

    If provided, the **scope** of this request will be the object named by `configuration_id`.

    Args:
        configuration_id (_ConfigurationObjectName, optional): The scope of the request.

    Returns:
        validation_result (str): The result of the validation request.
            The number of messages is always stored in the first line and can be matched using the following regex:
            ```
            Total number of messages: ([0-9]+)
            ```

    !!! Warning
        When the configuration has **no errors**, the returned string will NOT be empty.
        Instead, it will contain only the first line (_`WASX7193I`_):
        ```pycon
        >>> server = AdminConfig.getid("/Node:myNode/Server:myServer/")
        >>> print(AdminConfig.validate(server))
        WASX7193I: Validation results are logged in c:\WebSphere5\AppServer\logs\wsadmin.valout_2: Total number of messages: 0
        ```

    Example:
        - Validate configuration globally:
        ```pycon
        >>> print(AdminConfig.validate())
        WASX7193I: Validation results are logged in c:\WebSphere5\AppServer\logs\wsadmin.valout: Total number of messages: 16
        WASX7194I: Number of messages of severity 1: 16
        ```

        - Validate configuration only for a specific configuration object:
        ```pycon
        >>> server = AdminConfig.getid("/Node:myNode/Server:myServer/")
        >>> print(AdminConfig.validate(server))
        WASX7193I: Validation results are logged in c:\WebSphere5\AppServer\logs\wsadmin.valout_2: Total number of messages: 0
        ```
    """
    ...


# --------------------------------------------------------------------------
