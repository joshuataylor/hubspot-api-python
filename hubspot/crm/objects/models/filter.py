# coding: utf-8

"""
    CRM Objects

    CRM objects such as companies, contacts, deals, line items, products, tickets, and quotes are standard objects in HubSpot’s CRM. These core building blocks support custom properties, store critical information, and play a central role in the HubSpot application.  ## Supported Object Types  This API provides access to collections of CRM objects, which return a map of property names to values. Each object type has its own set of default properties, which can be found by exploring the [CRM Object Properties API](https://developers.hubspot.com/docs/methods/crm-properties/crm-properties-overview).  |Object Type |Properties returned by default | |--|--| | `companies` | `name`, `domain` | | `contacts` | `firstname`, `lastname`, `email` | | `deals` | `dealname`, `amount`, `closedate`, `pipeline`, `dealstage` | | `products` | `name`, `description`, `price` | | `tickets` | `content`, `hs_pipeline`, `hs_pipeline_stage`, `hs_ticket_category`, `hs_ticket_priority`, `subject` |  Find a list of all properties for an object type using the [CRM Object Properties](https://developers.hubspot.com/docs/methods/crm-properties/get-properties) API. e.g. `GET https://api.hubapi.com/properties/v2/companies/properties`. Change the properties returned in the response using the `properties` array in the request body.  # noqa: E501

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

from hubspot.crm.objects.configuration import Configuration


class Filter(object):
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
    openapi_types = {"value": "str", "high_value": "str", "values": "list[str]", "property_name": "str", "operator": "str"}

    attribute_map = {"value": "value", "high_value": "highValue", "values": "values", "property_name": "propertyName", "operator": "operator"}

    def __init__(self, value=None, high_value=None, values=None, property_name=None, operator=None, local_vars_configuration=None):  # noqa: E501
        """Filter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._value = None
        self._high_value = None
        self._values = None
        self._property_name = None
        self._operator = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if high_value is not None:
            self.high_value = high_value
        if values is not None:
            self.values = values
        self.property_name = property_name
        self.operator = operator

    @property
    def value(self):
        """Gets the value of this Filter.  # noqa: E501


        :return: The value of this Filter.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Filter.


        :param value: The value of this Filter.  # noqa: E501
        :type value: str
        """

        self._value = value

    @property
    def high_value(self):
        """Gets the high_value of this Filter.  # noqa: E501


        :return: The high_value of this Filter.  # noqa: E501
        :rtype: str
        """
        return self._high_value

    @high_value.setter
    def high_value(self, high_value):
        """Sets the high_value of this Filter.


        :param high_value: The high_value of this Filter.  # noqa: E501
        :type high_value: str
        """

        self._high_value = high_value

    @property
    def values(self):
        """Gets the values of this Filter.  # noqa: E501


        :return: The values of this Filter.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this Filter.


        :param values: The values of this Filter.  # noqa: E501
        :type values: list[str]
        """

        self._values = values

    @property
    def property_name(self):
        """Gets the property_name of this Filter.  # noqa: E501


        :return: The property_name of this Filter.  # noqa: E501
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this Filter.


        :param property_name: The property_name of this Filter.  # noqa: E501
        :type property_name: str
        """
        if self.local_vars_configuration.client_side_validation and property_name is None:  # noqa: E501
            raise ValueError("Invalid value for `property_name`, must not be `None`")  # noqa: E501

        self._property_name = property_name

    @property
    def operator(self):
        """Gets the operator of this Filter.  # noqa: E501

        null  # noqa: E501

        :return: The operator of this Filter.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this Filter.

        null  # noqa: E501

        :param operator: The operator of this Filter.  # noqa: E501
        :type operator: str
        """
        if self.local_vars_configuration.client_side_validation and operator is None:  # noqa: E501
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501
        allowed_values = ["EQ", "NEQ", "LT", "LTE", "GT", "GTE", "BETWEEN", "IN", "NOT_IN", "HAS_PROPERTY", "NOT_HAS_PROPERTY", "CONTAINS_TOKEN", "NOT_CONTAINS_TOKEN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and operator not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `operator` ({0}), must be one of {1}".format(operator, allowed_values))  # noqa: E501

        self._operator = operator

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
        if not isinstance(other, Filter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Filter):
            return True

        return self.to_dict() != other.to_dict()
