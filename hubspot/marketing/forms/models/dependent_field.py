# coding: utf-8

"""
    FormsExternalService

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

from hubspot.marketing.forms.configuration import Configuration


class DependentField(object):
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
    openapi_types = {"dependent_condition": "DependentFieldFilter", "dependent_field": "DependentFieldDependentField"}

    attribute_map = {"dependent_condition": "dependentCondition", "dependent_field": "dependentField"}

    def __init__(self, dependent_condition=None, dependent_field=None, local_vars_configuration=None):  # noqa: E501
        """DependentField - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._dependent_condition = None
        self._dependent_field = None
        self.discriminator = None

        if dependent_condition is not None:
            self.dependent_condition = dependent_condition
        self.dependent_field = dependent_field

    @property
    def dependent_condition(self):
        """Gets the dependent_condition of this DependentField.  # noqa: E501


        :return: The dependent_condition of this DependentField.  # noqa: E501
        :rtype: DependentFieldFilter
        """
        return self._dependent_condition

    @dependent_condition.setter
    def dependent_condition(self, dependent_condition):
        """Sets the dependent_condition of this DependentField.


        :param dependent_condition: The dependent_condition of this DependentField.  # noqa: E501
        :type dependent_condition: DependentFieldFilter
        """

        self._dependent_condition = dependent_condition

    @property
    def dependent_field(self):
        """Gets the dependent_field of this DependentField.  # noqa: E501


        :return: The dependent_field of this DependentField.  # noqa: E501
        :rtype: DependentFieldDependentField
        """
        return self._dependent_field

    @dependent_field.setter
    def dependent_field(self, dependent_field):
        """Sets the dependent_field of this DependentField.


        :param dependent_field: The dependent_field of this DependentField.  # noqa: E501
        :type dependent_field: DependentFieldDependentField
        """
        if self.local_vars_configuration.client_side_validation and dependent_field is None:  # noqa: E501
            raise ValueError("Invalid value for `dependent_field`, must not be `None`")  # noqa: E501

        self._dependent_field = dependent_field

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
        if not isinstance(other, DependentField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DependentField):
            return True

        return self.to_dict() != other.to_dict()
