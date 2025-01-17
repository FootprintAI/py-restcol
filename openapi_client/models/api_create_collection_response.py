# coding: utf-8

"""
    RestCol API Documentations

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.api_collection_metadata import ApiCollectionMetadata
from openapi_client.models.api_collection_type import ApiCollectionType
from openapi_client.models.api_schema_field import ApiSchemaField
from typing import Optional, Set
from typing_extensions import Self

class ApiCreateCollectionResponse(BaseModel):
    """
    ApiCreateCollectionResponse
    """ # noqa: E501
    metadata: Optional[ApiCollectionMetadata] = Field(default=None, alias="Metadata")
    description: Optional[StrictStr] = None
    collection_type: Optional[ApiCollectionType] = Field(default=ApiCollectionType.NONE, alias="collectionType")
    schemas: Optional[List[ApiSchemaField]] = None
    __properties: ClassVar[List[str]] = ["Metadata", "description", "collectionType", "schemas"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ApiCreateCollectionResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['Metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in schemas (list)
        _items = []
        if self.schemas:
            for _item_schemas in self.schemas:
                if _item_schemas:
                    _items.append(_item_schemas.to_dict())
            _dict['schemas'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiCreateCollectionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Metadata": ApiCollectionMetadata.from_dict(obj["Metadata"]) if obj.get("Metadata") is not None else None,
            "description": obj.get("description"),
            "collectionType": obj.get("collectionType") if obj.get("collectionType") is not None else ApiCollectionType.NONE,
            "schemas": [ApiSchemaField.from_dict(_item) for _item in obj["schemas"]] if obj.get("schemas") is not None else None
        })
        return _obj


