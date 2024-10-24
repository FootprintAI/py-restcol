# RestColServiceCreateDocumentBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** |  | [optional] 
**data** | **bytearray** |  | [optional] 
**dataformat** | [**ApiDataFormat**](ApiDataFormat.md) |  | [optional] [default to ApiDataFormat.UNKNOWN]

## Example

```python
from openapi_client.models.rest_col_service_create_document_body import RestColServiceCreateDocumentBody

# TODO update the JSON string below
json = "{}"
# create an instance of RestColServiceCreateDocumentBody from a JSON string
rest_col_service_create_document_body_instance = RestColServiceCreateDocumentBody.from_json(json)
# print the JSON string representation of the object
print(RestColServiceCreateDocumentBody.to_json())

# convert the object into a dict
rest_col_service_create_document_body_dict = rest_col_service_create_document_body_instance.to_dict()
# create an instance of RestColServiceCreateDocumentBody from a dict
rest_col_service_create_document_body_from_dict = RestColServiceCreateDocumentBody.from_dict(rest_col_service_create_document_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


