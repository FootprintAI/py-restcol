# openapi_client.CollectionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_col_service_create_collection**](CollectionApi.md#rest_col_service_create_collection) | **POST** /v1/projects/{projectId}/collections | Add collection endpoint, a collection is a set of documents with scheme-free.
[**rest_col_service_delete_collection**](CollectionApi.md#rest_col_service_delete_collection) | **DELETE** /v1/projects/{projectId}/collections/{collectionId} | 
[**rest_col_service_get_collection**](CollectionApi.md#rest_col_service_get_collection) | **GET** /v1/projects/{projectId}/collections/{collectionId} | 
[**rest_col_service_list_collections**](CollectionApi.md#rest_col_service_list_collections) | **GET** /v1/projects/{projectId}/collections | list collections endpoint


# **rest_col_service_create_collection**
> ApiCreateCollectionResponse rest_col_service_create_collection(project_id, body)

Add collection endpoint, a collection is a set of documents with scheme-free.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_create_collection_response import ApiCreateCollectionResponse
from openapi_client.models.rest_col_service_create_collection_body import RestColServiceCreateCollectionBody
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
    api_instance = openapi_client.CollectionApi(api_client)
    project_id = 'project_id_example' # str | 
    body = openapi_client.RestColServiceCreateCollectionBody() # RestColServiceCreateCollectionBody | 

    try:
        # Add collection endpoint, a collection is a set of documents with scheme-free.
        api_response = api_instance.rest_col_service_create_collection(project_id, body)
        print("The response of CollectionApi->rest_col_service_create_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->rest_col_service_create_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **body** | [**RestColServiceCreateCollectionBody**](RestColServiceCreateCollectionBody.md)|  | 

### Return type

[**ApiCreateCollectionResponse**](ApiCreateCollectionResponse.md)

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

# **rest_col_service_delete_collection**
> object rest_col_service_delete_collection(project_id, collection_id)



remove an individual collection and its associated doc

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
    api_instance = openapi_client.CollectionApi(api_client)
    project_id = 'project_id_example' # str | 
    collection_id = 'collection_id_example' # str | 

    try:
        api_response = api_instance.rest_col_service_delete_collection(project_id, collection_id)
        print("The response of CollectionApi->rest_col_service_delete_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->rest_col_service_delete_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **collection_id** | **str**|  | 

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

# **rest_col_service_get_collection**
> ApiGetCollectionResponse rest_col_service_get_collection(project_id, collection_id)



retrieve an individual collection information and document keys assocaited with it

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_get_collection_response import ApiGetCollectionResponse
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
    api_instance = openapi_client.CollectionApi(api_client)
    project_id = 'project_id_example' # str | 
    collection_id = 'collection_id_example' # str | 

    try:
        api_response = api_instance.rest_col_service_get_collection(project_id, collection_id)
        print("The response of CollectionApi->rest_col_service_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->rest_col_service_get_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **collection_id** | **str**|  | 

### Return type

[**ApiGetCollectionResponse**](ApiGetCollectionResponse.md)

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

# **rest_col_service_list_collections**
> object rest_col_service_list_collections(project_id)

list collections endpoint

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
    api_instance = openapi_client.CollectionApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # list collections endpoint
        api_response = api_instance.rest_col_service_list_collections(project_id)
        print("The response of CollectionApi->rest_col_service_list_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->rest_col_service_list_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

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

