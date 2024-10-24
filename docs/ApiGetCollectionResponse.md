# ApiGetCollectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**ApiCollectionMetadata**](ApiCollectionMetadata.md) |  | [optional] 
**description** | **str** |  | [optional] 
**collection_type** | [**ApiCollectionType**](ApiCollectionType.md) |  | [optional] [default to ApiCollectionType.NONE]
**schemas** | [**List[ApiSchemaField]**](ApiSchemaField.md) |  | [optional] 

## Example

```python
from openapi_client.models.api_get_collection_response import ApiGetCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiGetCollectionResponse from a JSON string
api_get_collection_response_instance = ApiGetCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(ApiGetCollectionResponse.to_json())

# convert the object into a dict
api_get_collection_response_dict = api_get_collection_response_instance.to_dict()
# create an instance of ApiGetCollectionResponse from a dict
api_get_collection_response_from_dict = ApiGetCollectionResponse.from_dict(api_get_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


