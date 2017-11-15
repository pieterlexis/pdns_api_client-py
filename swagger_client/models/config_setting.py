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


class ConfigSetting(object):
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
        'name': 'str',
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, name=None, type=None, value=None):
        """
        ConfigSetting - a model defined in Swagger
        """

        self._name = None
        self._type = None
        self._value = None

        if name is not None:
          self.name = name
        if type is not None:
          self.type = type
        if value is not None:
          self.value = value

    @property
    def name(self):
        """
        Gets the name of this ConfigSetting.
        set to \"ConfigSetting\"

        :return: The name of this ConfigSetting.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConfigSetting.
        set to \"ConfigSetting\"

        :param name: The name of this ConfigSetting.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this ConfigSetting.
        The name of this setting (e.g. ‘webserver-port’)

        :return: The type of this ConfigSetting.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ConfigSetting.
        The name of this setting (e.g. ‘webserver-port’)

        :param type: The type of this ConfigSetting.
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """
        Gets the value of this ConfigSetting.
        The value of setting name

        :return: The value of this ConfigSetting.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ConfigSetting.
        The value of setting name

        :param value: The value of this ConfigSetting.
        :type: str
        """

        self._value = value

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
        if not isinstance(other, ConfigSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other