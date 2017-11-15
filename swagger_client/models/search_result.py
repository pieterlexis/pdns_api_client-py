# coding: utf-8

"""
    PowerDNS Authoritative HTTP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 0.0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SearchResult(object):
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
        'disabled': 'bool',
        'name': 'str',
        'object_type': 'str',
        'zone_id': 'str',
        'zone': 'str',
        'type': 'str',
        'ttl': 'int'
    }

    attribute_map = {
        'content': 'content',
        'disabled': 'disabled',
        'name': 'name',
        'object_type': 'object_type',
        'zone_id': 'zone_id',
        'zone': 'zone',
        'type': 'type',
        'ttl': 'ttl'
    }

    def __init__(self, content=None, disabled=None, name=None, object_type=None, zone_id=None, zone=None, type=None, ttl=None):
        """
        SearchResult - a model defined in Swagger
        """

        self._content = None
        self._disabled = None
        self._name = None
        self._object_type = None
        self._zone_id = None
        self._zone = None
        self._type = None
        self._ttl = None

        if content is not None:
          self.content = content
        if disabled is not None:
          self.disabled = disabled
        if name is not None:
          self.name = name
        if object_type is not None:
          self.object_type = object_type
        if zone_id is not None:
          self.zone_id = zone_id
        if zone is not None:
          self.zone = zone
        if type is not None:
          self.type = type
        if ttl is not None:
          self.ttl = ttl

    @property
    def content(self):
        """
        Gets the content of this SearchResult.

        :return: The content of this SearchResult.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this SearchResult.

        :param content: The content of this SearchResult.
        :type: str
        """

        self._content = content

    @property
    def disabled(self):
        """
        Gets the disabled of this SearchResult.

        :return: The disabled of this SearchResult.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """
        Sets the disabled of this SearchResult.

        :param disabled: The disabled of this SearchResult.
        :type: bool
        """

        self._disabled = disabled

    @property
    def name(self):
        """
        Gets the name of this SearchResult.

        :return: The name of this SearchResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SearchResult.

        :param name: The name of this SearchResult.
        :type: str
        """

        self._name = name

    @property
    def object_type(self):
        """
        Gets the object_type of this SearchResult.
        set to one of \"record, zone, comment\"

        :return: The object_type of this SearchResult.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this SearchResult.
        set to one of \"record, zone, comment\"

        :param object_type: The object_type of this SearchResult.
        :type: str
        """

        self._object_type = object_type

    @property
    def zone_id(self):
        """
        Gets the zone_id of this SearchResult.

        :return: The zone_id of this SearchResult.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """
        Sets the zone_id of this SearchResult.

        :param zone_id: The zone_id of this SearchResult.
        :type: str
        """

        self._zone_id = zone_id

    @property
    def zone(self):
        """
        Gets the zone of this SearchResult.

        :return: The zone of this SearchResult.
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """
        Sets the zone of this SearchResult.

        :param zone: The zone of this SearchResult.
        :type: str
        """

        self._zone = zone

    @property
    def type(self):
        """
        Gets the type of this SearchResult.

        :return: The type of this SearchResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SearchResult.

        :param type: The type of this SearchResult.
        :type: str
        """

        self._type = type

    @property
    def ttl(self):
        """
        Gets the ttl of this SearchResult.

        :return: The ttl of this SearchResult.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """
        Sets the ttl of this SearchResult.

        :param ttl: The ttl of this SearchResult.
        :type: int
        """

        self._ttl = ttl

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
        if not isinstance(other, SearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other