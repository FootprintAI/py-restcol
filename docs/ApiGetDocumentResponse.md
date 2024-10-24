# ApiGetDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**ApiDataMetadata**](ApiDataMetadata.md) |  | [optional] 
**data** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.api_get_document_response import ApiGetDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiGetDocumentResponse from a JSON string
api_get_document_response_instance = ApiGetDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(ApiGetDocumentResponse.to_json())

# convert the object into a dict
api_get_document_response_dict = api_get_document_response_instance.to_dict()
# create an instance of ApiGetDocumentResponse from a dict
api_get_document_response_from_dict = ApiGetDocumentResponse.from_dict(api_get_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


