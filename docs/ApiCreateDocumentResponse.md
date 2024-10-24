# ApiCreateDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**ApiDataMetadata**](ApiDataMetadata.md) |  | [optional] 

## Example

```python
from openapi_client.models.api_create_document_response import ApiCreateDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCreateDocumentResponse from a JSON string
api_create_document_response_instance = ApiCreateDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(ApiCreateDocumentResponse.to_json())

# convert the object into a dict
api_create_document_response_dict = api_create_document_response_instance.to_dict()
# create an instance of ApiCreateDocumentResponse from a dict
api_create_document_response_from_dict = ApiCreateDocumentResponse.from_dict(api_create_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


