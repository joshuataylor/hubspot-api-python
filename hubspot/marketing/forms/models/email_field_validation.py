# coding: utf-8

"""
    FormsExternalService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.marketing.forms.configuration import Configuration


class EmailFieldValidation(object):
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
        'blocked_email_domains': 'list[str]',
        'use_default_block_list': 'bool'
    }

    attribute_map = {
        'blocked_email_domains': 'blockedEmailDomains',
        'use_default_block_list': 'useDefaultBlockList'
    }

    def __init__(self, blocked_email_domains=None, use_default_block_list=None, local_vars_configuration=None):  # noqa: E501
        """EmailFieldValidation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._blocked_email_domains = None
        self._use_default_block_list = None
        self.discriminator = None

        self.blocked_email_domains = blocked_email_domains
        self.use_default_block_list = use_default_block_list

    @property
    def blocked_email_domains(self):
        """Gets the blocked_email_domains of this EmailFieldValidation.  # noqa: E501

        A list of email domains to block.  # noqa: E501

        :return: The blocked_email_domains of this EmailFieldValidation.  # noqa: E501
        :rtype: list[str]
        """
        return self._blocked_email_domains

    @blocked_email_domains.setter
    def blocked_email_domains(self, blocked_email_domains):
        """Sets the blocked_email_domains of this EmailFieldValidation.

        A list of email domains to block.  # noqa: E501

        :param blocked_email_domains: The blocked_email_domains of this EmailFieldValidation.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and blocked_email_domains is None:  # noqa: E501
            raise ValueError("Invalid value for `blocked_email_domains`, must not be `None`")  # noqa: E501

        self._blocked_email_domains = blocked_email_domains

    @property
    def use_default_block_list(self):
        """Gets the use_default_block_list of this EmailFieldValidation.  # noqa: E501

        Whether to block the free email providers.  # noqa: E501

        :return: The use_default_block_list of this EmailFieldValidation.  # noqa: E501
        :rtype: bool
        """
        return self._use_default_block_list

    @use_default_block_list.setter
    def use_default_block_list(self, use_default_block_list):
        """Sets the use_default_block_list of this EmailFieldValidation.

        Whether to block the free email providers.  # noqa: E501

        :param use_default_block_list: The use_default_block_list of this EmailFieldValidation.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and use_default_block_list is None:  # noqa: E501
            raise ValueError("Invalid value for `use_default_block_list`, must not be `None`")  # noqa: E501

        self._use_default_block_list = use_default_block_list

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
        if not isinstance(other, EmailFieldValidation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailFieldValidation):
            return True

        return self.to_dict() != other.to_dict()
