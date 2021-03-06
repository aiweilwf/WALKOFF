# coding: utf-8

"""
    WALKOFF

    An active cyber defense development framework enabling orchestration capabilities to be written once and deployed across WALKOFF-enabled orchestration tools. https://nsacyber.github.io/WALKOFF/  # noqa: E501

    The version of the OpenAPI document: 0.9.1
    Contact: walkoff@nsa.gov
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Error(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'detail': 'str',
        'instance': 'str',
        'status': 'str',
        'title': 'str',
        'type': 'str'
    }

    attribute_map = {
        'detail': 'detail',
        'instance': 'instance',
        'status': 'status',
        'title': 'title',
        'type': 'type'
    }

    def __init__(self, detail=None, instance=None, status=None, title=None, type='about:blank'):  # noqa: E501
        """Error - a model defined in OpenAPI"""  # noqa: E501

        self._detail = None
        self._instance = None
        self._status = None
        self._title = None
        self._type = None
        self.discriminator = None

        self.detail = detail
        if instance is not None:
            self.instance = instance
        self.status = status
        self.title = title
        self.type = type

    @property
    def detail(self):
        """Gets the detail of this Error.  # noqa: E501

        A human-readable explanation specific to this occurrence of the problem  # noqa: E501

        :return: The detail of this Error.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this Error.

        A human-readable explanation specific to this occurrence of the problem  # noqa: E501

        :param detail: The detail of this Error.  # noqa: E501
        :type: str
        """
        if detail is None:
            raise ValueError("Invalid value for `detail`, must not be `None`")  # noqa: E501

        self._detail = detail

    @property
    def instance(self):
        """Gets the instance of this Error.  # noqa: E501

        A URI reference that identifies the specific occurrence of the problem. It may or may not yield further information if dereferenced.   # noqa: E501

        :return: The instance of this Error.  # noqa: E501
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this Error.

        A URI reference that identifies the specific occurrence of the problem. It may or may not yield further information if dereferenced.   # noqa: E501

        :param instance: The instance of this Error.  # noqa: E501
        :type: str
        """

        self._instance = instance

    @property
    def status(self):
        """Gets the status of this Error.  # noqa: E501

        The HTTP status code generated for this occurrence of the problem  # noqa: E501

        :return: The status of this Error.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Error.

        The HTTP status code generated for this occurrence of the problem  # noqa: E501

        :param status: The status of this Error.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def title(self):
        """Gets the title of this Error.  # noqa: E501

        A short, human-readable summary of the problem type.  # noqa: E501

        :return: The title of this Error.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Error.

        A short, human-readable summary of the problem type.  # noqa: E501

        :param title: The title of this Error.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def type(self):
        """Gets the type of this Error.  # noqa: E501

        A URI reference that identifies the problem type. When dereferenced it should provide human-readable documentation for the problem type.   # noqa: E501

        :return: The type of this Error.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Error.

        A URI reference that identifies the problem type. When dereferenced it should provide human-readable documentation for the problem type.   # noqa: E501

        :param type: The type of this Error.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
