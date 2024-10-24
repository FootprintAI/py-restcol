# coding: utf-8

"""
    RestCol API Documentations

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.api_data_metadata import ApiDataMetadata

class TestApiDataMetadata(unittest.TestCase):
    """ApiDataMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiDataMetadata:
        """Test ApiDataMetadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiDataMetadata`
        """
        model = ApiDataMetadata()
        if include_optional:
            return ApiDataMetadata(
                project_id = '',
                collection_id = '',
                schema_id = '',
                document_id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                dataformat = 'DATA_FORMAT_UNKNOWN'
            )
        else:
            return ApiDataMetadata(
        )
        """

    def testApiDataMetadata(self):
        """Test ApiDataMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()