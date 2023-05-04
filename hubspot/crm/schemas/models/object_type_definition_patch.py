# coding: utf-8

"""
    Schemas

    The CRM uses schemas to define how custom objects should store and represent information in the HubSpot CRM. Schemas define details about an object's type, properties, and associations. The schema can be uniquely identified by its **object type ID**.  # noqa: E501

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

from hubspot.crm.schemas.configuration import Configuration


class ObjectTypeDefinitionPatch(object):
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
        "labels": "ObjectTypeDefinitionLabels",
        "required_properties": "list[str]",
        "searchable_properties": "list[str]",
        "primary_display_property": "str",
        "secondary_display_properties": "list[str]",
        "restorable": "bool",
    }

    attribute_map = {
        "labels": "labels",
        "required_properties": "requiredProperties",
        "searchable_properties": "searchableProperties",
        "primary_display_property": "primaryDisplayProperty",
        "secondary_display_properties": "secondaryDisplayProperties",
        "restorable": "restorable",
    }

    def __init__(
        self, labels=None, required_properties=None, searchable_properties=None, primary_display_property=None, secondary_display_properties=None, restorable=None, local_vars_configuration=None
    ):  # noqa: E501
        """ObjectTypeDefinitionPatch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._labels = None
        self._required_properties = None
        self._searchable_properties = None
        self._primary_display_property = None
        self._secondary_display_properties = None
        self._restorable = None
        self.discriminator = None

        if labels is not None:
            self.labels = labels
        if required_properties is not None:
            self.required_properties = required_properties
        if searchable_properties is not None:
            self.searchable_properties = searchable_properties
        if primary_display_property is not None:
            self.primary_display_property = primary_display_property
        if secondary_display_properties is not None:
            self.secondary_display_properties = secondary_display_properties
        if restorable is not None:
            self.restorable = restorable

    @property
    def labels(self):
        """Gets the labels of this ObjectTypeDefinitionPatch.  # noqa: E501


        :return: The labels of this ObjectTypeDefinitionPatch.  # noqa: E501
        :rtype: ObjectTypeDefinitionLabels
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ObjectTypeDefinitionPatch.


        :param labels: The labels of this ObjectTypeDefinitionPatch.  # noqa: E501
        :type labels: ObjectTypeDefinitionLabels
        """

        self._labels = labels

    @property
    def required_properties(self):
        """Gets the required_properties of this ObjectTypeDefinitionPatch.  # noqa: E501

        The names of properties that should be **required** when creating an object of this type.  # noqa: E501

        :return: The required_properties of this ObjectTypeDefinitionPatch.  # noqa: E501
        :rtype: list[str]
        """
        return self._required_properties

    @required_properties.setter
    def required_properties(self, required_properties):
        """Sets the required_properties of this ObjectTypeDefinitionPatch.

        The names of properties that should be **required** when creating an object of this type.  # noqa: E501

        :param required_properties: The required_properties of this ObjectTypeDefinitionPatch.  # noqa: E501
        :type required_properties: list[str]
        """

        self._required_properties = required_properties

    @property
    def searchable_properties(self):
        """Gets the searchable_properties of this ObjectTypeDefinitionPatch.  # noqa: E501

        Names of properties that will be indexed for this object type in by HubSpot's product search.  # noqa: E501

        :return: The searchable_properties of this ObjectTypeDefinitionPatch.  # noqa: E501
        :rtype: list[str]
        """
        return self._searchable_properties

    @searchable_properties.setter
    def searchable_properties(self, searchable_properties):
        """Sets the searchable_properties of this ObjectTypeDefinitionPatch.

        Names of properties that will be indexed for this object type in by HubSpot's product search.  # noqa: E501

        :param searchable_properties: The searchable_properties of this ObjectTypeDefinitionPatch.  # noqa: E501
        :type searchable_properties: list[str]
        """

        self._searchable_properties = searchable_properties

    @property
    def primary_display_property(self):
        """Gets the primary_display_property of this ObjectTypeDefinitionPatch.  # noqa: E501

        The name of the primary property for this object. This will be displayed as primary on the HubSpot record page for this object type.  # noqa: E501

        :return: The primary_display_property of this ObjectTypeDefinitionPatch.  # noqa: E501
        :rtype: str
        """
        return self._primary_display_property

    @primary_display_property.setter
    def primary_display_property(self, primary_display_property):
        """Sets the primary_display_property of this ObjectTypeDefinitionPatch.

        The name of the primary property for this object. This will be displayed as primary on the HubSpot record page for this object type.  # noqa: E501

        :param primary_display_property: The primary_display_property of this ObjectTypeDefinitionPatch.  # noqa: E501
        :type primary_display_property: str
        """

        self._primary_display_property = primary_display_property

    @property
    def secondary_display_properties(self):
        """Gets the secondary_display_properties of this ObjectTypeDefinitionPatch.  # noqa: E501

        The names of secondary properties for this object. These will be displayed as secondary on the HubSpot record page for this object type.  # noqa: E501

        :return: The secondary_display_properties of this ObjectTypeDefinitionPatch.  # noqa: E501
        :rtype: list[str]
        """
        return self._secondary_display_properties

    @secondary_display_properties.setter
    def secondary_display_properties(self, secondary_display_properties):
        """Sets the secondary_display_properties of this ObjectTypeDefinitionPatch.

        The names of secondary properties for this object. These will be displayed as secondary on the HubSpot record page for this object type.  # noqa: E501

        :param secondary_display_properties: The secondary_display_properties of this ObjectTypeDefinitionPatch.  # noqa: E501
        :type secondary_display_properties: list[str]
        """

        self._secondary_display_properties = secondary_display_properties

    @property
    def restorable(self):
        """Gets the restorable of this ObjectTypeDefinitionPatch.  # noqa: E501


        :return: The restorable of this ObjectTypeDefinitionPatch.  # noqa: E501
        :rtype: bool
        """
        return self._restorable

    @restorable.setter
    def restorable(self, restorable):
        """Sets the restorable of this ObjectTypeDefinitionPatch.


        :param restorable: The restorable of this ObjectTypeDefinitionPatch.  # noqa: E501
        :type restorable: bool
        """

        self._restorable = restorable

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
        if not isinstance(other, ObjectTypeDefinitionPatch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ObjectTypeDefinitionPatch):
            return True

        return self.to_dict() != other.to_dict()
