# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class TapiOduOduPoolPac(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, client_capacity=None, max_client_size=None, max_client_instances=None):  # noqa: E501
        """TapiOduOduPoolPac - a model defined in OpenAPI

        :param client_capacity: The client_capacity of this TapiOduOduPoolPac.  # noqa: E501
        :type client_capacity: int
        :param max_client_size: The max_client_size of this TapiOduOduPoolPac.  # noqa: E501
        :type max_client_size: int
        :param max_client_instances: The max_client_instances of this TapiOduOduPoolPac.  # noqa: E501
        :type max_client_instances: int
        """
        self.openapi_types = {
            'client_capacity': int,
            'max_client_size': int,
            'max_client_instances': int
        }

        self.attribute_map = {
            'client_capacity': 'client-capacity',
            'max_client_size': 'max-client-size',
            'max_client_instances': 'max-client-instances'
        }

        self._client_capacity = client_capacity
        self._max_client_size = max_client_size
        self._max_client_instances = max_client_instances

    @classmethod
    def from_dict(cls, dikt) -> 'TapiOduOduPoolPac':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The tapi.odu.OduPoolPac of this TapiOduOduPoolPac.  # noqa: E501
        :rtype: TapiOduOduPoolPac
        """
        return util.deserialize_model(dikt, cls)

    @property
    def client_capacity(self):
        """Gets the client_capacity of this TapiOduOduPoolPac.

        none  # noqa: E501

        :return: The client_capacity of this TapiOduOduPoolPac.
        :rtype: int
        """
        return self._client_capacity

    @client_capacity.setter
    def client_capacity(self, client_capacity):
        """Sets the client_capacity of this TapiOduOduPoolPac.

        none  # noqa: E501

        :param client_capacity: The client_capacity of this TapiOduOduPoolPac.
        :type client_capacity: int
        """

        self._client_capacity = client_capacity

    @property
    def max_client_size(self):
        """Gets the max_client_size of this TapiOduOduPoolPac.

        none  # noqa: E501

        :return: The max_client_size of this TapiOduOduPoolPac.
        :rtype: int
        """
        return self._max_client_size

    @max_client_size.setter
    def max_client_size(self, max_client_size):
        """Sets the max_client_size of this TapiOduOduPoolPac.

        none  # noqa: E501

        :param max_client_size: The max_client_size of this TapiOduOduPoolPac.
        :type max_client_size: int
        """

        self._max_client_size = max_client_size

    @property
    def max_client_instances(self):
        """Gets the max_client_instances of this TapiOduOduPoolPac.

        none  # noqa: E501

        :return: The max_client_instances of this TapiOduOduPoolPac.
        :rtype: int
        """
        return self._max_client_instances

    @max_client_instances.setter
    def max_client_instances(self, max_client_instances):
        """Sets the max_client_instances of this TapiOduOduPoolPac.

        none  # noqa: E501

        :param max_client_instances: The max_client_instances of this TapiOduOduPoolPac.
        :type max_client_instances: int
        """

        self._max_client_instances = max_client_instances
