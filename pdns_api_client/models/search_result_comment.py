# coding: utf-8

"""
    PowerDNS Authoritative HTTP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 0.0.13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SearchResultComment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'content': 'str',
        'name': 'str',
        'object_type': 'str',
        'zone_id': 'str',
        'zone': 'str'
    }

    attribute_map = {
        'content': 'content',
        'name': 'name',
        'object_type': 'object_type',
        'zone_id': 'zone_id',
        'zone': 'zone'
    }

    def __init__(self, content=None, name=None, object_type=None, zone_id=None, zone=None):
        """
        SearchResultComment - a model defined in Swagger
        """

        self._content = None
        self._name = None
        self._object_type = None
        self._zone_id = None
        self._zone = None

        if content is not None:
          self.content = content
        if name is not None:
          self.name = name
        if object_type is not None:
          self.object_type = object_type
        if zone_id is not None:
          self.zone_id = zone_id
        if zone is not None:
          self.zone = zone

    @property
    def content(self):
        """
        Gets the content of this SearchResultComment.

        :return: The content of this SearchResultComment.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this SearchResultComment.

        :param content: The content of this SearchResultComment.
        :type: str
        """

        self._content = content

    @property
    def name(self):
        """
        Gets the name of this SearchResultComment.

        :return: The name of this SearchResultComment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SearchResultComment.

        :param name: The name of this SearchResultComment.
        :type: str
        """

        self._name = name

    @property
    def object_type(self):
        """
        Gets the object_type of this SearchResultComment.
        set to \"comment\"

        :return: The object_type of this SearchResultComment.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this SearchResultComment.
        set to \"comment\"

        :param object_type: The object_type of this SearchResultComment.
        :type: str
        """

        self._object_type = object_type

    @property
    def zone_id(self):
        """
        Gets the zone_id of this SearchResultComment.

        :return: The zone_id of this SearchResultComment.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """
        Sets the zone_id of this SearchResultComment.

        :param zone_id: The zone_id of this SearchResultComment.
        :type: str
        """

        self._zone_id = zone_id

    @property
    def zone(self):
        """
        Gets the zone of this SearchResultComment.

        :return: The zone of this SearchResultComment.
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """
        Sets the zone of this SearchResultComment.

        :param zone: The zone of this SearchResultComment.
        :type: str
        """

        self._zone = zone

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SearchResultComment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
