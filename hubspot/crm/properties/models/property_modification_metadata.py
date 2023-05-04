# coding: utf-8

"""
    Properties

    All HubSpot objects store data in default and custom properties. These endpoints provide access to read and modify object properties in HubSpot.  # noqa: E501

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

from hubspot.crm.properties.configuration import Configuration


class PropertyModificationMetadata(object):
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
    openapi_types = {"archivable": "bool", "read_only_definition": "bool", "read_only_options": "bool", "read_only_value": "bool"}

    attribute_map = {"archivable": "archivable", "read_only_definition": "readOnlyDefinition", "read_only_options": "readOnlyOptions", "read_only_value": "readOnlyValue"}

    def __init__(self, archivable=None, read_only_definition=None, read_only_options=None, read_only_value=None, local_vars_configuration=None):  # noqa: E501
        """PropertyModificationMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._archivable = None
        self._read_only_definition = None
        self._read_only_options = None
        self._read_only_value = None
        self.discriminator = None

        self.archivable = archivable
        self.read_only_definition = read_only_definition
        if read_only_options is not None:
            self.read_only_options = read_only_options
        self.read_only_value = read_only_value

    @property
    def archivable(self):
        """Gets the archivable of this PropertyModificationMetadata.  # noqa: E501


        :return: The archivable of this PropertyModificationMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._archivable

    @archivable.setter
    def archivable(self, archivable):
        """Sets the archivable of this PropertyModificationMetadata.


        :param archivable: The archivable of this PropertyModificationMetadata.  # noqa: E501
        :type archivable: bool
        """
        if self.local_vars_configuration.client_side_validation and archivable is None:  # noqa: E501
            raise ValueError("Invalid value for `archivable`, must not be `None`")  # noqa: E501

        self._archivable = archivable

    @property
    def read_only_definition(self):
        """Gets the read_only_definition of this PropertyModificationMetadata.  # noqa: E501


        :return: The read_only_definition of this PropertyModificationMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._read_only_definition

    @read_only_definition.setter
    def read_only_definition(self, read_only_definition):
        """Sets the read_only_definition of this PropertyModificationMetadata.


        :param read_only_definition: The read_only_definition of this PropertyModificationMetadata.  # noqa: E501
        :type read_only_definition: bool
        """
        if self.local_vars_configuration.client_side_validation and read_only_definition is None:  # noqa: E501
            raise ValueError("Invalid value for `read_only_definition`, must not be `None`")  # noqa: E501

        self._read_only_definition = read_only_definition

    @property
    def read_only_options(self):
        """Gets the read_only_options of this PropertyModificationMetadata.  # noqa: E501


        :return: The read_only_options of this PropertyModificationMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._read_only_options

    @read_only_options.setter
    def read_only_options(self, read_only_options):
        """Sets the read_only_options of this PropertyModificationMetadata.


        :param read_only_options: The read_only_options of this PropertyModificationMetadata.  # noqa: E501
        :type read_only_options: bool
        """

        self._read_only_options = read_only_options

    @property
    def read_only_value(self):
        """Gets the read_only_value of this PropertyModificationMetadata.  # noqa: E501


        :return: The read_only_value of this PropertyModificationMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._read_only_value

    @read_only_value.setter
    def read_only_value(self, read_only_value):
        """Sets the read_only_value of this PropertyModificationMetadata.


        :param read_only_value: The read_only_value of this PropertyModificationMetadata.  # noqa: E501
        :type read_only_value: bool
        """
        if self.local_vars_configuration.client_side_validation and read_only_value is None:  # noqa: E501
            raise ValueError("Invalid value for `read_only_value`, must not be `None`")  # noqa: E501

        self._read_only_value = read_only_value

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
        if not isinstance(other, PropertyModificationMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PropertyModificationMetadata):
            return True

        return self.to_dict() != other.to_dict()
