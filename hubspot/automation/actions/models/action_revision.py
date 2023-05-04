# coding: utf-8

"""
    Custom Workflow Actions

    Create custom workflow actions  # noqa: E501

    The version of the OpenAPI document: v4
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.automation.actions.configuration import Configuration


class ActionRevision(object):
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
    openapi_types = {"definition": "ExtensionActionDefinition", "created_at": "datetime", "id": "str", "revision_id": "str"}

    attribute_map = {"definition": "definition", "created_at": "createdAt", "id": "id", "revision_id": "revisionId"}

    def __init__(self, definition=None, created_at=None, id=None, revision_id=None, local_vars_configuration=None):  # noqa: E501
        """ActionRevision - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._definition = None
        self._created_at = None
        self._id = None
        self._revision_id = None
        self.discriminator = None

        self.definition = definition
        self.created_at = created_at
        self.id = id
        self.revision_id = revision_id

    @property
    def definition(self):
        """Gets the definition of this ActionRevision.  # noqa: E501


        :return: The definition of this ActionRevision.  # noqa: E501
        :rtype: ExtensionActionDefinition
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        """Sets the definition of this ActionRevision.


        :param definition: The definition of this ActionRevision.  # noqa: E501
        :type definition: ExtensionActionDefinition
        """
        if self.local_vars_configuration.client_side_validation and definition is None:  # noqa: E501
            raise ValueError("Invalid value for `definition`, must not be `None`")  # noqa: E501

        self._definition = definition

    @property
    def created_at(self):
        """Gets the created_at of this ActionRevision.  # noqa: E501

        The date the revision was created.  # noqa: E501

        :return: The created_at of this ActionRevision.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ActionRevision.

        The date the revision was created.  # noqa: E501

        :param created_at: The created_at of this ActionRevision.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this ActionRevision.  # noqa: E501


        :return: The id of this ActionRevision.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ActionRevision.


        :param id: The id of this ActionRevision.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def revision_id(self):
        """Gets the revision_id of this ActionRevision.  # noqa: E501

        The version number of the custom action.  # noqa: E501

        :return: The revision_id of this ActionRevision.  # noqa: E501
        :rtype: str
        """
        return self._revision_id

    @revision_id.setter
    def revision_id(self, revision_id):
        """Sets the revision_id of this ActionRevision.

        The version number of the custom action.  # noqa: E501

        :param revision_id: The revision_id of this ActionRevision.  # noqa: E501
        :type revision_id: str
        """
        if self.local_vars_configuration.client_side_validation and revision_id is None:  # noqa: E501
            raise ValueError("Invalid value for `revision_id`, must not be `None`")  # noqa: E501

        self._revision_id = revision_id

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
        if not isinstance(other, ActionRevision):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActionRevision):
            return True

        return self.to_dict() != other.to_dict()
