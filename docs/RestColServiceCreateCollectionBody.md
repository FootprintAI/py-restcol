# RestColServiceCreateCollectionBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**collection_type** | [**ApiCollectionType**](ApiCollectionType.md) |  | [optional] [default to ApiCollectionType.NONE]
**schemas** | [**List[ApiSchemaField]**](ApiSchemaField.md) |  | [optional] 

## Example

```python
from openapi_client.models.rest_col_service_create_collection_body import RestColServiceCreateCollectionBody

# TODO update the JSON string below
json = "{}"
# create an instance of RestColServiceCreateCollectionBody from a JSON string
rest_col_service_create_collection_body_instance = RestColServiceCreateCollectionBody.from_json(json)
# print the JSON string representation of the object
print(RestColServiceCreateCollectionBody.to_json())

# convert the object into a dict
rest_col_service_create_collection_body_dict = rest_col_service_create_collection_body_instance.to_dict()
# create an instance of RestColServiceCreateCollectionBody from a dict
rest_col_service_create_collection_body_from_dict = RestColServiceCreateCollectionBody.from_dict(rest_col_service_create_collection_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


