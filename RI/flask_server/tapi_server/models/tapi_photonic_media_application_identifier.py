# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.tapi_photonic_media_application_identifier_type import TapiPhotonicMediaApplicationIdentifierType  # noqa: F401,E501
from tapi_server import util


class TapiPhotonicMediaApplicationIdentifier(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, application_identifier_type=None, application_code=None):  # noqa: E501
        """TapiPhotonicMediaApplicationIdentifier - a model defined in OpenAPI

        :param application_identifier_type: The application_identifier_type of this TapiPhotonicMediaApplicationIdentifier.  # noqa: E501
        :type application_identifier_type: TapiPhotonicMediaApplicationIdentifierType
        :param application_code: The application_code of this TapiPhotonicMediaApplicationIdentifier.  # noqa: E501
        :type application_code: str
        """
        self.openapi_types = {
            'application_identifier_type': TapiPhotonicMediaApplicationIdentifierType,
            'application_code': str
        }

        self.attribute_map = {
            'application_identifier_type': 'application-identifier-type',
            'application_code': 'application-code'
        }

        self._application_identifier_type = application_identifier_type
        self._application_code = application_code

    @classmethod
    def from_dict(cls, dikt) -> 'TapiPhotonicMediaApplicationIdentifier':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.photonic.media.ApplicationIdentifier of this TapiPhotonicMediaApplicationIdentifier.  # noqa: E501
        :rtype: TapiPhotonicMediaApplicationIdentifier
        """
        return util.deserialize_model(dikt, cls)

    @property
    def application_identifier_type(self):
        """Gets the application_identifier_type of this TapiPhotonicMediaApplicationIdentifier.


        :return: The application_identifier_type of this TapiPhotonicMediaApplicationIdentifier.
        :rtype: TapiPhotonicMediaApplicationIdentifierType
        """
        return self._application_identifier_type

    @application_identifier_type.setter
    def application_identifier_type(self, application_identifier_type):
        """Sets the application_identifier_type of this TapiPhotonicMediaApplicationIdentifier.


        :param application_identifier_type: The application_identifier_type of this TapiPhotonicMediaApplicationIdentifier.
        :type application_identifier_type: TapiPhotonicMediaApplicationIdentifierType
        """

        self._application_identifier_type = application_identifier_type

    @property
    def application_code(self):
        """Gets the application_code of this TapiPhotonicMediaApplicationIdentifier.

        none  # noqa: E501

        :return: The application_code of this TapiPhotonicMediaApplicationIdentifier.
        :rtype: str
        """
        return self._application_code

    @application_code.setter
    def application_code(self, application_code):
        """Sets the application_code of this TapiPhotonicMediaApplicationIdentifier.

        none  # noqa: E501

        :param application_code: The application_code of this TapiPhotonicMediaApplicationIdentifier.
        :type application_code: str
        """

        self._application_code = application_code
