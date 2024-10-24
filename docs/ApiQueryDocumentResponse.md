# ApiQueryDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**docs** | [**List[ApiGetDocumentResponse]**](ApiGetDocumentResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.api_query_document_response import ApiQueryDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiQueryDocumentResponse from a JSON string
api_query_document_response_instance = ApiQueryDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(ApiQueryDocumentResponse.to_json())

# convert the object into a dict
api_query_document_response_dict = api_query_document_response_instance.to_dict()
# create an instance of ApiQueryDocumentResponse from a dict
api_query_document_response_from_dict = ApiQueryDocumentResponse.from_dict(api_query_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


