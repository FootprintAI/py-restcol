# ApiSchemaField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**datatype** | [**ApiSchemaFieldDataType**](ApiSchemaFieldDataType.md) |  | [optional] [default to ApiSchemaFieldDataType.NONE]
**example** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.api_schema_field import ApiSchemaField

# TODO update the JSON string below
json = "{}"
# create an instance of ApiSchemaField from a JSON string
api_schema_field_instance = ApiSchemaField.from_json(json)
# print the JSON string representation of the object
print(ApiSchemaField.to_json())

# convert the object into a dict
api_schema_field_dict = api_schema_field_instance.to_dict()
# create an instance of ApiSchemaField from a dict
api_schema_field_from_dict = ApiSchemaField.from_dict(api_schema_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


