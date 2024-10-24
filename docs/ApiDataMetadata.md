# ApiDataMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | [optional] 
**collection_id** | **str** |  | [optional] 
**schema_id** | **str** |  | [optional] 
**document_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 
**dataformat** | [**ApiDataFormat**](ApiDataFormat.md) |  | [optional] [default to ApiDataFormat.UNKNOWN]

## Example

```python
from openapi_client.models.api_data_metadata import ApiDataMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDataMetadata from a JSON string
api_data_metadata_instance = ApiDataMetadata.from_json(json)
# print the JSON string representation of the object
print(ApiDataMetadata.to_json())

# convert the object into a dict
api_data_metadata_dict = api_data_metadata_instance.to_dict()
# create an instance of ApiDataMetadata from a dict
api_data_metadata_from_dict = ApiDataMetadata.from_dict(api_data_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


