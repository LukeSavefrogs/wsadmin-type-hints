# Custom properties

## List custom properties...
### ...for a server
```python
# Get the desired server
server = AdminConfig.getid('/Server:myServer/')

# List all properties for that specific server
custom_properties = AdminConfig.list('Property', server).splitlines()
```

### ...for a transaction service
```python
# Get the desired server
server = AdminConfig.getid('/TransactionService:myTS/')

# List all properties for that specific transaction service
custom_properties = AdminConfig.list('Property', server).splitlines()
```


## Operations on a custom property
### Remove a property based on its value
```python
custom_properties = AdminConfig.list('Property', server).splitlines()
for prop in custom_properties:
    if AdminConfig.showAttribute(prop, "value") == "value_not_valid":
        AdminConfig.remove(prop)

# `AdminConfig.reset()` or `AdminConfig.save()`
```

<!-- ### Change a property that has a specific name
```python
custom_properties = AdminConfig.list('Property', server).splitlines()
for prop in custom_properties:
    if AdminConfig.showAttribute(prop, "value") == "value_not_valid":
        AdminConfig.remove(prop)

# `AdminConfig.reset()` or `AdminConfig.save()`
``` -->
