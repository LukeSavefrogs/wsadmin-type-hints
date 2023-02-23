# Servers

## List servers

### All servers
This will get you all defined servers in the global scope:
```python
servers = AdminConfig.list("Server").splitlines()
```

### Servers on node
This will get you only the servers running on the desired **node**:
```python
# Get the desired node
node    = AdminConfig.getid('/Node:myNode/')

# Get a list with all the servers for that particular node
servers = AdminConfig.list("Server", node).splitlines()
```

### Servers in cluster
This will get you only the servers from the desired **cluster**:
```python
# Get the desired cluster
cluster = AdminConfig.getid('/ServerCluster:myCluster/')

# Get a list with all the servers for that particular node
servers = AdminConfig.list("Server", cluster).splitlines()
```

## Common operations
### Restart server
```python
# Query the servers that need to be restarted
server = AdminControl.queryNames('WebSphere:*,cell=mycell,node=mynode,name=server1,type=Server,*')

AdminControl.invoke(server, 'restart')
```

### Start server
- Using `AdminControl.invoke`:
```python
# Query the servers that need to be started
server = AdminControl.queryNames('WebSphere:*,cell=mycell,node=mynode,name=server1,type=Server,*')

AdminControl.invoke(server, 'start')
```

- Using `AdminControl.startServer`:
```python
# TBD
```


### Stop server
- Using `AdminControl.invoke`:
```python
# Query the servers that need to be stopped
server = AdminControl.queryNames('WebSphere:*,cell=mycell,node=mynode,name=server1,type=Server,*')

AdminControl.invoke(server, 'stop')
```

- Using `AdminControl.stopServer`:
```python
# TBD
```

### Check server status
If the server is stopped, the `completeObjectName` command will return an empty string (`''`).
```python
server = AdminControl.completeObjectName('cell=mycell,node=mynode,name=server1,type=Server,*')

if server:
    server_status = AdminControl.getAttribute(server, 'state')
else:
    server_status = "STOPPED"

print(server_status)
```


## Utility functions
### Wait until server is stopped/started
```python
import time
def wait_for_state(object_name, target_state, max_wait = 300, interval = 5):
    """Wait until the specified `object_name` has the state `target_state`.

    Args:
        object_name (str): The object name to monitor
        target_state (str): The desired state
        max_wait (int, optional): The maximum time in seconds to wait. Defaults to 300.
        interval (int, optional): The interval in seconds between each check. Defaults to 5.

    Raises:
        Exception: Raises an exception if a timeout occurs
    """    
    current_state = ""
    waited = 0
    while current_state != target_state:
        mbean = AdminControl.completeObjectName(object_name)
        if mbean: 
            current_state = AdminControl.getAttribute(mbean, 'state')

        time.sleep(interval)
        
        waited += interval
        if waited > max_wait:
            raise Exception("Error: Timed out after %d seconds!" % max_wait)
```

??? Example
    Use it like this:
    ```python
    try:
        # [...] Server start operations...
        wait_for_state("WebSphere:*,cell=mycell,node=mynode,name=server1,type=Server,*", "websphere.cluster.running")
        # Now the server is fully started and ready to go!
    except Exception:
        print("Timeout occurred while waiting for the server to start...")
    ```