# coding: utf-8

"""
    CRM cards

    Allows an app to extend the CRM UI by surfacing custom cards in the sidebar of record pages. These cards are defined up-front as part of app configuration, then populated by external data fetch requests when the record page is accessed by a user.  # noqa: E501

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

from hubspot.crm.extensions.cards.configuration import Configuration


class CardDisplayProperty(object):
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
    openapi_types = {"name": "str", "label": "str", "data_type": "str", "options": "list[DisplayOption]"}

    attribute_map = {"name": "name", "label": "label", "data_type": "dataType", "options": "options"}

    def __init__(self, name=None, label=None, data_type=None, options=None, local_vars_configuration=None):  # noqa: E501
        """CardDisplayProperty - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._label = None
        self._data_type = None
        self._options = None
        self.discriminator = None

        self.name = name
        self.label = label
        self.data_type = data_type
        self.options = options

    @property
    def name(self):
        """Gets the name of this CardDisplayProperty.  # noqa: E501

        An internal identifier for this property. This value must be unique TODO.  # noqa: E501

        :return: The name of this CardDisplayProperty.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CardDisplayProperty.

        An internal identifier for this property. This value must be unique TODO.  # noqa: E501

        :param name: The name of this CardDisplayProperty.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def label(self):
        """Gets the label of this CardDisplayProperty.  # noqa: E501

        The label for this property as you'd like it displayed to users.  # noqa: E501

        :return: The label of this CardDisplayProperty.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CardDisplayProperty.

        The label for this property as you'd like it displayed to users.  # noqa: E501

        :param label: The label of this CardDisplayProperty.  # noqa: E501
        :type label: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def data_type(self):
        """Gets the data_type of this CardDisplayProperty.  # noqa: E501

        Type of data represented by this property.  # noqa: E501

        :return: The data_type of this CardDisplayProperty.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this CardDisplayProperty.

        Type of data represented by this property.  # noqa: E501

        :param data_type: The data_type of this CardDisplayProperty.  # noqa: E501
        :type data_type: str
        """
        if self.local_vars_configuration.client_side_validation and data_type is None:  # noqa: E501
            raise ValueError("Invalid value for `data_type`, must not be `None`")  # noqa: E501
        allowed_values = ["BOOLEAN", "CURRENCY", "DATE", "DATETIME", "EMAIL", "LINK", "NUMERIC", "STRING", "STATUS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and data_type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `data_type` ({0}), must be one of {1}".format(data_type, allowed_values))  # noqa: E501

        self._data_type = data_type

    @property
    def options(self):
        """Gets the options of this CardDisplayProperty.  # noqa: E501

        An array of available options that can be displayed. Only used in when `dataType` is `STATUS`.  # noqa: E501

        :return: The options of this CardDisplayProperty.  # noqa: E501
        :rtype: list[DisplayOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this CardDisplayProperty.

        An array of available options that can be displayed. Only used in when `dataType` is `STATUS`.  # noqa: E501

        :param options: The options of this CardDisplayProperty.  # noqa: E501
        :type options: list[DisplayOption]
        """
        if self.local_vars_configuration.client_side_validation and options is None:  # noqa: E501
            raise ValueError("Invalid value for `options`, must not be `None`")  # noqa: E501

        self._options = options

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
        if not isinstance(other, CardDisplayProperty):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CardDisplayProperty):
            return True

        return self.to_dict() != other.to_dict()
