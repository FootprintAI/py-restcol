# openapi_client.SwaggerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rest_col_service_get_swagger_doc**](SwaggerApi.md#rest_col_service_get_swagger_doc) | **GET** /v1/projects/{projectId}/apidoc | Return API Doc in Swagger
[**rest_col_service_get_swagger_doc2**](SwaggerApi.md#rest_col_service_get_swagger_doc2) | **GET** /v1/projects/{projectId}/collections/{collectionId}/apidoc | Return API Doc in Swagger


# **rest_col_service_get_swagger_doc**
> ApiHttpBody rest_col_service_get_swagger_doc(project_id, collection_id=collection_id)

Return API Doc in Swagger

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_http_body import ApiHttpBody
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
    api_instance = openapi_client.SwaggerApi(api_client)
    project_id = 'project_id_example' # str | 
    collection_id = 'collection_id_example' # str |  (optional)

    try:
        # Return API Doc in Swagger
        api_response = api_instance.rest_col_service_get_swagger_doc(project_id, collection_id=collection_id)
        print("The response of SwaggerApi->rest_col_service_get_swagger_doc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwaggerApi->rest_col_service_get_swagger_doc: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **collection_id** | **str**|  | [optional] 

### Return type

[**ApiHttpBody**](ApiHttpBody.md)

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

# **rest_col_service_get_swagger_doc2**
> ApiHttpBody rest_col_service_get_swagger_doc2(project_id, collection_id)

Return API Doc in Swagger

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.api_http_body import ApiHttpBody
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
    api_instance = openapi_client.SwaggerApi(api_client)
    project_id = 'project_id_example' # str | 
    collection_id = 'collection_id_example' # str | 

    try:
        # Return API Doc in Swagger
        api_response = api_instance.rest_col_service_get_swagger_doc2(project_id, collection_id)
        print("The response of SwaggerApi->rest_col_service_get_swagger_doc2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SwaggerApi->rest_col_service_get_swagger_doc2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **collection_id** | **str**|  | 

### Return type

[**ApiHttpBody**](ApiHttpBody.md)

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
