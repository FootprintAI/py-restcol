# openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.0
- Generator version: 7.10.0-SNAPSHOT
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/footprintai/restcol](https://github.com/footprintai/restcol)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    body = openapi_client.RestColServiceCreateCollectionBody() # RestColServiceCreateCollectionBody | 

    try:
        # Add collection endpoint, a collection is a set of documents with scheme-free.
        api_response = api_instance.rest_col_service_create_collection(project_id, body)
        print("The response of CollectionApi->rest_col_service_create_collection:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CollectionApi->rest_col_service_create_collection: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CollectionApi* | [**rest_col_service_create_collection**](docs/CollectionApi.md#rest_col_service_create_collection) | **POST** /v1/projects/{projectId}/collections | Add collection endpoint, a collection is a set of documents with scheme-free.
*CollectionApi* | [**rest_col_service_delete_collection**](docs/CollectionApi.md#rest_col_service_delete_collection) | **DELETE** /v1/projects/{projectId}/collections/{collectionId} | 
*CollectionApi* | [**rest_col_service_get_collection**](docs/CollectionApi.md#rest_col_service_get_collection) | **GET** /v1/projects/{projectId}/collections/{collectionId} | 
*CollectionApi* | [**rest_col_service_list_collections**](docs/CollectionApi.md#rest_col_service_list_collections) | **GET** /v1/projects/{projectId}/collections | list collections endpoint
*DocumentApi* | [**rest_col_service_create_document**](docs/DocumentApi.md#rest_col_service_create_document) | **POST** /v1/projects/{projectId}/newdoc | 
*DocumentApi* | [**rest_col_service_create_document2**](docs/DocumentApi.md#rest_col_service_create_document2) | **POST** /v1/projects/{projectId}/collections/{collectionId}:newdoc | 
*DocumentApi* | [**rest_col_service_delete_document**](docs/DocumentApi.md#rest_col_service_delete_document) | **DELETE** /v1/projects/{projectId}/collections/{collectionId}/docs/{documentId} | DeleteDocument endpoint is a generic endpoint for deleting a specific data
*DocumentApi* | [**rest_col_service_get_document**](docs/DocumentApi.md#rest_col_service_get_document) | **GET** /v1/projects/{projectId}/collections/{collectionId}/docs/{documentId} | GetDocument endpoint is a generic endpoint for retrieving data across multiple collections
*DocumentApi* | [**rest_col_service_query_document**](docs/DocumentApi.md#rest_col_service_query_document) | **GET** /v1/projects/{projectId}/collections/{collectionId}/docs | 
*DocumentApi* | [**rest_col_service_query_documents_stream**](docs/DocumentApi.md#rest_col_service_query_documents_stream) | **GET** /v1/projects/{projectId}/collections/{collectionId}/docs:stream | 
*SwaggerApi* | [**rest_col_service_get_swagger_doc**](docs/SwaggerApi.md#rest_col_service_get_swagger_doc) | **GET** /v1/projects/{projectId}/apidoc | Return API Doc in Swagger
*SwaggerApi* | [**rest_col_service_get_swagger_doc2**](docs/SwaggerApi.md#rest_col_service_get_swagger_doc2) | **GET** /v1/projects/{projectId}/collections/{collectionId}/apidoc | Return API Doc in Swagger


## Documentation For Models

 - [ApiCollectionMetadata](docs/ApiCollectionMetadata.md)
 - [ApiCollectionType](docs/ApiCollectionType.md)
 - [ApiCreateCollectionResponse](docs/ApiCreateCollectionResponse.md)
 - [ApiCreateDocumentResponse](docs/ApiCreateDocumentResponse.md)
 - [ApiDataFormat](docs/ApiDataFormat.md)
 - [ApiDataMetadata](docs/ApiDataMetadata.md)
 - [ApiGetCollectionResponse](docs/ApiGetCollectionResponse.md)
 - [ApiGetDocumentResponse](docs/ApiGetDocumentResponse.md)
 - [ApiHttpBody](docs/ApiHttpBody.md)
 - [ApiQueryDocumentResponse](docs/ApiQueryDocumentResponse.md)
 - [ApiSchemaField](docs/ApiSchemaField.md)
 - [ApiSchemaFieldDataType](docs/ApiSchemaFieldDataType.md)
 - [ProtobufAny](docs/ProtobufAny.md)
 - [ProtobufNullValue](docs/ProtobufNullValue.md)
 - [RestColServiceCreateCollectionBody](docs/RestColServiceCreateCollectionBody.md)
 - [RestColServiceCreateDocumentBody](docs/RestColServiceCreateDocumentBody.md)
 - [RpcStatus](docs/RpcStatus.md)
 - [StreamResultOfApiGetDocumentResponse](docs/StreamResultOfApiGetDocumentResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




