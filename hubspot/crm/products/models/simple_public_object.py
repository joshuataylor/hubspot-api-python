# coding: utf-8

"""
    Products

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

from hubspot.crm.products.configuration import Configuration


class SimplePublicObject(object):
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
        "id": "str",
        "properties": "dict[str, str]",
        "properties_with_history": "dict[str, list[ValueWithTimestamp]]",
        "created_at": "datetime",
        "updated_at": "datetime",
        "archived": "bool",
        "archived_at": "datetime",
    }

    attribute_map = {
        "id": "id",
        "properties": "properties",
        "properties_with_history": "propertiesWithHistory",
        "created_at": "createdAt",
        "updated_at": "updatedAt",
        "archived": "archived",
        "archived_at": "archivedAt",
    }

    def __init__(self, id=None, properties=None, properties_with_history=None, created_at=None, updated_at=None, archived=None, archived_at=None, local_vars_configuration=None):  # noqa: E501
        """SimplePublicObject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._properties = None
        self._properties_with_history = None
        self._created_at = None
        self._updated_at = None
        self._archived = None
        self._archived_at = None
        self.discriminator = None

        self.id = id
        self.properties = properties
        if properties_with_history is not None:
            self.properties_with_history = properties_with_history
        self.created_at = created_at
        self.updated_at = updated_at
        if archived is not None:
            self.archived = archived
        if archived_at is not None:
            self.archived_at = archived_at

    @property
    def id(self):
        """Gets the id of this SimplePublicObject.  # noqa: E501


        :return: The id of this SimplePublicObject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimplePublicObject.


        :param id: The id of this SimplePublicObject.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def properties(self):
        """Gets the properties of this SimplePublicObject.  # noqa: E501


        :return: The properties of this SimplePublicObject.  # noqa: E501
        :rtype: dict[str, str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this SimplePublicObject.


        :param properties: The properties of this SimplePublicObject.  # noqa: E501
        :type properties: dict[str, str]
        """
        if self.local_vars_configuration.client_side_validation and properties is None:  # noqa: E501
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def properties_with_history(self):
        """Gets the properties_with_history of this SimplePublicObject.  # noqa: E501


        :return: The properties_with_history of this SimplePublicObject.  # noqa: E501
        :rtype: dict[str, list[ValueWithTimestamp]]
        """
        return self._properties_with_history

    @properties_with_history.setter
    def properties_with_history(self, properties_with_history):
        """Sets the properties_with_history of this SimplePublicObject.


        :param properties_with_history: The properties_with_history of this SimplePublicObject.  # noqa: E501
        :type properties_with_history: dict[str, list[ValueWithTimestamp]]
        """

        self._properties_with_history = properties_with_history

    @property
    def created_at(self):
        """Gets the created_at of this SimplePublicObject.  # noqa: E501


        :return: The created_at of this SimplePublicObject.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SimplePublicObject.


        :param created_at: The created_at of this SimplePublicObject.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SimplePublicObject.  # noqa: E501


        :return: The updated_at of this SimplePublicObject.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SimplePublicObject.


        :param updated_at: The updated_at of this SimplePublicObject.  # noqa: E501
        :type updated_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def archived(self):
        """Gets the archived of this SimplePublicObject.  # noqa: E501


        :return: The archived of this SimplePublicObject.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this SimplePublicObject.


        :param archived: The archived of this SimplePublicObject.  # noqa: E501
        :type archived: bool
        """

        self._archived = archived

    @property
    def archived_at(self):
        """Gets the archived_at of this SimplePublicObject.  # noqa: E501


        :return: The archived_at of this SimplePublicObject.  # noqa: E501
        :rtype: datetime
        """
        return self._archived_at

    @archived_at.setter
    def archived_at(self, archived_at):
        """Sets the archived_at of this SimplePublicObject.


        :param archived_at: The archived_at of this SimplePublicObject.  # noqa: E501
        :type archived_at: datetime
        """

        self._archived_at = archived_at

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
        if not isinstance(other, SimplePublicObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimplePublicObject):
            return True

        return self.to_dict() != other.to_dict()
