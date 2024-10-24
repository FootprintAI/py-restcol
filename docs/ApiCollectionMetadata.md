# ApiCollectionMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | [optional] 
**collection_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.api_collection_metadata import ApiCollectionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCollectionMetadata from a JSON string
api_collection_metadata_instance = ApiCollectionMetadata.from_json(json)
# print the JSON string representation of the object
print(ApiCollectionMetadata.to_json())

# convert the object into a dict
api_collection_metadata_dict = api_collection_metadata_instance.to_dict()
# create an instance of ApiCollectionMetadata from a dict
api_collection_metadata_from_dict = ApiCollectionMetadata.from_dict(api_collection_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


