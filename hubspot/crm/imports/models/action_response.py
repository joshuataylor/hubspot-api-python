# coding: utf-8

"""
    CRM Imports

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.crm.imports.configuration import Configuration


class ActionResponse(object):
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
    openapi_types = {"status": "str", "requested_at": "datetime", "started_at": "datetime", "completed_at": "datetime", "links": "dict[str, str]"}

    attribute_map = {"status": "status", "requested_at": "requestedAt", "started_at": "startedAt", "completed_at": "completedAt", "links": "links"}

    def __init__(self, status=None, requested_at=None, started_at=None, completed_at=None, links=None, local_vars_configuration=None):  # noqa: E501
        """ActionResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._requested_at = None
        self._started_at = None
        self._completed_at = None
        self._links = None
        self.discriminator = None

        self.status = status
        if requested_at is not None:
            self.requested_at = requested_at
        self.started_at = started_at
        self.completed_at = completed_at
        if links is not None:
            self.links = links

    @property
    def status(self):
        """Gets the status of this ActionResponse.  # noqa: E501


        :return: The status of this ActionResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ActionResponse.


        :param status: The status of this ActionResponse.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["PENDING", "PROCESSING", "CANCELED", "COMPLETE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `status` ({0}), must be one of {1}".format(status, allowed_values))  # noqa: E501

        self._status = status

    @property
    def requested_at(self):
        """Gets the requested_at of this ActionResponse.  # noqa: E501


        :return: The requested_at of this ActionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._requested_at

    @requested_at.setter
    def requested_at(self, requested_at):
        """Sets the requested_at of this ActionResponse.


        :param requested_at: The requested_at of this ActionResponse.  # noqa: E501
        :type requested_at: datetime
        """

        self._requested_at = requested_at

    @property
    def started_at(self):
        """Gets the started_at of this ActionResponse.  # noqa: E501


        :return: The started_at of this ActionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this ActionResponse.


        :param started_at: The started_at of this ActionResponse.  # noqa: E501
        :type started_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and started_at is None:  # noqa: E501
            raise ValueError("Invalid value for `started_at`, must not be `None`")  # noqa: E501

        self._started_at = started_at

    @property
    def completed_at(self):
        """Gets the completed_at of this ActionResponse.  # noqa: E501


        :return: The completed_at of this ActionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        """Sets the completed_at of this ActionResponse.


        :param completed_at: The completed_at of this ActionResponse.  # noqa: E501
        :type completed_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and completed_at is None:  # noqa: E501
            raise ValueError("Invalid value for `completed_at`, must not be `None`")  # noqa: E501

        self._completed_at = completed_at

    @property
    def links(self):
        """Gets the links of this ActionResponse.  # noqa: E501


        :return: The links of this ActionResponse.  # noqa: E501
        :rtype: dict[str, str]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ActionResponse.


        :param links: The links of this ActionResponse.  # noqa: E501
        :type links: dict[str, str]
        """

        self._links = links

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], convert(item[1])), value.items()))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ActionResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActionResponse):
            return True

        return self.to_dict() != other.to_dict()
