# openapi_client.DocumentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_col_service_create_document**](DocumentApi.md#rest_col_service_create_document) | **POST** /v1/projects/{projectId}/newdoc | 
[**rest_col_service_create_document2**](DocumentApi.md#rest_col_service_create_document2) | **POST** /v1/projects/{projectId}/collections/{collectionId}:newdoc | 
[**rest_col_service_delete_document**](DocumentApi.md#rest_col_service_delete_document) | **DELETE** /v1/projects/{projectId}/collections/{collectionId}/docs/{documentId} | DeleteDocument endpoint is a generic endpoint for deleting a specific data
[**rest_col_service_get_document**](DocumentApi.md#rest_col_service_get_document) | **GET** /v1/projects/{projectId}/collections/{collectionId}/docs/{documentId} | GetDocument endpoint is a generic endpoint for retrieving data across multiple collections
[**rest_col_service_query_document**](DocumentApi.md#rest_col_service_query_document) | **GET** /v1/projects/{projectId}/collections/{collectionId}/docs | 
[**rest_col_service_query_documents_stream**](DocumentApi.md#rest_col_service_query_documents_stream) | **GET** /v1/projects/{projectId}/collections/{collectionId}/docs:stream | 


# **rest_col_service_create_document**
> ApiCreateDocumentResponse rest_col_service_create_document(project_id, body)



create a document to the collection

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_create_document_response import ApiCreateDocumentResponse
from openapi_client.models.rest_col_service_create_document_body import RestColServiceCreateDocumentBody
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentApi(api_client)
    project_id = 'project_id_example' # str | 
    body = openapi_client.RestColServiceCreateDocumentBody() # RestColServiceCreateDocumentBody | 

    try:
        api_response = api_instance.rest_col_service_create_document(project_id, body)
        print("The response of DocumentApi->rest_col_service_create_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->rest_col_service_create_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **body** | [**RestColServiceCreateDocumentBody**](RestColServiceCreateDocumentBody.md)|  | 

### Return type

[**ApiCreateDocumentResponse**](ApiCreateDocumentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_col_service_create_document2**
> ApiCreateDocumentResponse rest_col_service_create_document2(project_id, collection_id, body)



create a document to the collection

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_create_document_response import ApiCreateDocumentResponse
from openapi_client.models.rest_col_service_create_document_body import RestColServiceCreateDocumentBody
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentApi(api_client)
    project_id = 'project_id_example' # str | 
    collection_id = 'collection_id_example' # str | 
    body = openapi_client.RestColServiceCreateDocumentBody() # RestColServiceCreateDocumentBody | 

    try:
        api_response = api_instance.rest_col_service_create_document2(project_id, collection_id, body)
        print("The response of DocumentApi->rest_col_service_create_document2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->rest_col_service_create_document2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **collection_id** | **str**|  | 
 **body** | [**RestColServiceCreateDocumentBody**](RestColServiceCreateDocumentBody.md)|  | 

### Return type

[**ApiCreateDocumentResponse**](ApiCreateDocumentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_col_service_delete_document**
> object rest_col_service_delete_document(project_id, collection_id, document_id)

DeleteDocument endpoint is a generic endpoint for deleting a specific data

Remove the specific document from the collection

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentApi(api_client)
    project_id = 'project_id_example' # str | 
    collection_id = 'collection_id_example' # str | 
    document_id = 'document_id_example' # str | 

    try:
        # DeleteDocument endpoint is a generic endpoint for deleting a specific data
        api_response = api_instance.rest_col_service_delete_document(project_id, collection_id, document_id)
        print("The response of DocumentApi->rest_col_service_delete_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->rest_col_service_delete_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **collection_id** | **str**|  | 
 **document_id** | **str**|  | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_col_service_get_document**
> ApiGetDocumentResponse rest_col_service_get_document(project_id, collection_id, document_id, field_selectors=field_selectors)

GetDocument endpoint is a generic endpoint for retrieving data across multiple collections

retrieve a document information from the collection.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_get_document_response import ApiGetDocumentResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentApi(api_client)
    project_id = 'project_id_example' # str | 
    collection_id = 'collection_id_example' # str | 
    document_id = 'document_id_example' # str | 
    field_selectors = ['field_selectors_example'] # List[str] | dot-concatenated fields, ex: fielda.fieldb.fieldc (optional)

    try:
        # GetDocument endpoint is a generic endpoint for retrieving data across multiple collections
        api_response = api_instance.rest_col_service_get_document(project_id, collection_id, document_id, field_selectors=field_selectors)
        print("The response of DocumentApi->rest_col_service_get_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->rest_col_service_get_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **collection_id** | **str**|  | 
 **document_id** | **str**|  | 
 **field_selectors** | [**List[str]**](str.md)| dot-concatenated fields, ex: fielda.fieldb.fieldc | [optional] 

### Return type

[**ApiGetDocumentResponse**](ApiGetDocumentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_col_service_query_document**
> ApiQueryDocumentResponse rest_col_service_query_document(project_id, collection_id, since_ts=since_ts, ended_at=ended_at, field_selectors=field_selectors, limit_count=limit_count)



run query against a collection, return documents matched the query

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_query_document_response import ApiQueryDocumentResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentApi(api_client)
    project_id = 'project_id_example' # str | 
    collection_id = 'collection_id_example' # str | 
    since_ts = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    ended_at = '2013-10-20T19:20:30+01:00' # datetime | endedAt specifies when is the ended timeframe of the query (optional)
    field_selectors = ['field_selectors_example'] # List[str] | dot-concatenated fields, ex: fielda.fieldb.fieldc (optional)
    limit_count = 56 # int |  (optional)

    try:
        api_response = api_instance.rest_col_service_query_document(project_id, collection_id, since_ts=since_ts, ended_at=ended_at, field_selectors=field_selectors, limit_count=limit_count)
        print("The response of DocumentApi->rest_col_service_query_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->rest_col_service_query_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **collection_id** | **str**|  | 
 **since_ts** | **datetime**|  | [optional] 
 **ended_at** | **datetime**| endedAt specifies when is the ended timeframe of the query | [optional] 
 **field_selectors** | [**List[str]**](str.md)| dot-concatenated fields, ex: fielda.fieldb.fieldc | [optional] 
 **limit_count** | **int**|  | [optional] 

### Return type

[**ApiQueryDocumentResponse**](ApiQueryDocumentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rest_col_service_query_documents_stream**
> StreamResultOfApiGetDocumentResponse rest_col_service_query_documents_stream(project_id, collection_id, since_ts=since_ts, ended_at=ended_at, field_selectors=field_selectors, follow_up_mode=follow_up_mode, limit_count=limit_count)



run query against a collection, return documents in streaming which matched the query

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.stream_result_of_api_get_document_response import StreamResultOfApiGetDocumentResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DocumentApi(api_client)
    project_id = 'project_id_example' # str | 
    collection_id = 'collection_id_example' # str | 
    since_ts = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    ended_at = '2013-10-20T19:20:30+01:00' # datetime | endedAt specifies when is the ended timeframe of the query (optional)
    field_selectors = ['field_selectors_example'] # List[str] | dot-concatenated fields, ex: fielda.fieldb.fieldc (optional)
    follow_up_mode = True # bool | if on, the service would keep watch new coming docs (optional)
    limit_count = 56 # int |  (optional)

    try:
        api_response = api_instance.rest_col_service_query_documents_stream(project_id, collection_id, since_ts=since_ts, ended_at=ended_at, field_selectors=field_selectors, follow_up_mode=follow_up_mode, limit_count=limit_count)
        print("The response of DocumentApi->rest_col_service_query_documents_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->rest_col_service_query_documents_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **collection_id** | **str**|  | 
 **since_ts** | **datetime**|  | [optional] 
 **ended_at** | **datetime**| endedAt specifies when is the ended timeframe of the query | [optional] 
 **field_selectors** | [**List[str]**](str.md)| dot-concatenated fields, ex: fielda.fieldb.fieldc | [optional] 
 **follow_up_mode** | **bool**| if on, the service would keep watch new coming docs | [optional] 
 **limit_count** | **int**|  | [optional] 

### Return type

[**StreamResultOfApiGetDocumentResponse**](StreamResultOfApiGetDocumentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response.(streaming responses) |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

