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


class Option(object):
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
    openapi_types = {"label": "str", "value": "str", "description": "str", "display_order": "int", "hidden": "bool"}

    attribute_map = {"label": "label", "value": "value", "description": "description", "display_order": "displayOrder", "hidden": "hidden"}

    def __init__(self, label=None, value=None, description=None, display_order=None, hidden=None, local_vars_configuration=None):  # noqa: E501
        """Option - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._label = None
        self._value = None
        self._description = None
        self._display_order = None
        self._hidden = None
        self.discriminator = None

        self.label = label
        self.value = value
        if description is not None:
            self.description = description
        if display_order is not None:
            self.display_order = display_order
        self.hidden = hidden

    @property
    def label(self):
        """Gets the label of this Option.  # noqa: E501

        A human-readable option label that will be shown in HubSpot.  # noqa: E501

        :return: The label of this Option.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Option.

        A human-readable option label that will be shown in HubSpot.  # noqa: E501

        :param label: The label of this Option.  # noqa: E501
        :type label: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def value(self):
        """Gets the value of this Option.  # noqa: E501

        The internal value of the option, which must be used when setting the property value through the API.  # noqa: E501

        :return: The value of this Option.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Option.

        The internal value of the option, which must be used when setting the property value through the API.  # noqa: E501

        :param value: The value of this Option.  # noqa: E501
        :type value: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def description(self):
        """Gets the description of this Option.  # noqa: E501

        A description of the option.  # noqa: E501

        :return: The description of this Option.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Option.

        A description of the option.  # noqa: E501

        :param description: The description of this Option.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def display_order(self):
        """Gets the display_order of this Option.  # noqa: E501

        Options are displayed in order starting with the lowest positive integer value. Values of -1 will cause the option to be displayed after any positive values.  # noqa: E501

        :return: The display_order of this Option.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this Option.

        Options are displayed in order starting with the lowest positive integer value. Values of -1 will cause the option to be displayed after any positive values.  # noqa: E501

        :param display_order: The display_order of this Option.  # noqa: E501
        :type display_order: int
        """

        self._display_order = display_order

    @property
    def hidden(self):
        """Gets the hidden of this Option.  # noqa: E501

        Hidden options will not be displayed in HubSpot.  # noqa: E501

        :return: The hidden of this Option.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this Option.

        Hidden options will not be displayed in HubSpot.  # noqa: E501

        :param hidden: The hidden of this Option.  # noqa: E501
        :type hidden: bool
        """
        if self.local_vars_configuration.client_side_validation and hidden is None:  # noqa: E501
            raise ValueError("Invalid value for `hidden`, must not be `None`")  # noqa: E501

        self._hidden = hidden

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
        if not isinstance(other, Option):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Option):
            return True

        return self.to_dict() != other.to_dict()
