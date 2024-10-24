# StreamResultOfApiGetDocumentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ApiGetDocumentResponse**](ApiGetDocumentResponse.md) |  | [optional] 
**error** | [**RpcStatus**](RpcStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.stream_result_of_api_get_document_response import StreamResultOfApiGetDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StreamResultOfApiGetDocumentResponse from a JSON string
stream_result_of_api_get_document_response_instance = StreamResultOfApiGetDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(StreamResultOfApiGetDocumentResponse.to_json())

# convert the object into a dict
stream_result_of_api_get_document_response_dict = stream_result_of_api_get_document_response_instance.to_dict()
# create an instance of StreamResultOfApiGetDocumentResponse from a dict
stream_result_of_api_get_document_response_from_dict = StreamResultOfApiGetDocumentResponse.from_dict(stream_result_of_api_get_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


