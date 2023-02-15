"""
Use the `AdminTask` object to run administrative commands with the `wsadmin` tool.

Administrative commands are loaded dynamically when you start the `wsadmin` tool. 

The administrative commands that are available for you to use, and what you can do 
with them, depends on the edition of the product that you use.

For more info see the [official documentation](https://www.ibm.com/docs/en/was-nd/8.5.5?topic=scripting-commands-admintask-object-using-wsadmin).
"""
from typing import Any, overload
from wsadmin_type_hints.wsadmin_types import ConfigurationObjectName
    
@overload
def createTCPEndPoint(flag: str) -> Any:
    ...

@overload
def createTCPEndPoint(target_object: ConfigurationObjectName, endpoint_configuration: str | list) -> ConfigurationObjectName:
    ...

def createTCPEndPoint(target_object: ConfigurationObjectName | str, endpoint_configuration: str | list) -> ConfigurationObjectName:
    """Create a new endpoint that you can associate with a TCP inbound channel.

    - If `target_object` is set to a string with value `"-interactive"`, the endpoint will 
        be created in _interactive mode_.

    Args:
        target_object (ConfigurationObjectName | str): Parent instance of the TransportChannelService that contains the TCPInboundChannel. If `target_object` is set to a string with value `"-interactive"`, the endpoint will be created in _interactive mode_.
        endpoint_configuration (str | list): String containing the `-name`, `-host` and `-port` parameters (all **required**) with their values set.

    Returns:
        ConfigurationObjectName: The object name of the endpoint that was created.

    Example:
        ```pycon
        >>> target = 'cells/mybuildCell01/nodes/mybuildCellManager01/servers/dmgr|server.xml#TransportChannelService_1'
        
        # As a string...
        >>> AdminTask.createTCPEndPoint(target, '[-name Sample_End_Pt_Name -host mybuild.location.ibm.com -port 8978]')
        
        # ... or as a list...
        >>> AdminTask.createTCPEndPoint(target, ['-name', 'Sample_End_Pt_Name', '-host', 'mybuild.location.ibm.com', '-port', '8978'])
        ```    
    """
    # AdminTask.createTCPEndPoint(
    #     'cells/mybuildCell01/nodes/mybuildCellManager01/servers/dmgr|server.xml#TransportChannelService_1',
    #     '[-name Sample_End_Pt_Name -host mybuild.location.ibm.com -port 8978]'
    # )

    # AdminTask.createTCPEndPoint(
    #     'cells/mybuildCell01/nodes/mybuildCellManager01/servers/dmgr|server.xml#TransportChannelService_1', 
    #     ['-name', 'Sample_End_Pt_Name', '-host', 'mybuild.location.ibm.com', '-port', '8978']
    # )

    pass

def getTCPEndPoint(): # undocumented
    pass

def help(): # undocumented
    pass

def listTCPEndPoints(): # undocumented
    pass

def listTCPThreadPools(): # undocumented
    pass

def updateAppOnCluster(): # undocumented
    pass
