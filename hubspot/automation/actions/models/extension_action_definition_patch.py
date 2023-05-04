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


class ExtensionActionDefinitionPatch(object):
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
        "action_url": "str",
        "published": "bool",
        "input_fields": "list[InputFieldDefinition]",
        "object_request_options": "ObjectRequestOptions",
        "input_field_dependencies": "list[ExtensionActionDefinitionPatchInputFieldDependenciesInner]",
        "labels": "dict[str, ActionLabels]",
        "object_types": "list[str]",
    }

    attribute_map = {
        "action_url": "actionUrl",
        "published": "published",
        "input_fields": "inputFields",
        "object_request_options": "objectRequestOptions",
        "input_field_dependencies": "inputFieldDependencies",
        "labels": "labels",
        "object_types": "objectTypes",
    }

    def __init__(
        self, action_url=None, published=None, input_fields=None, object_request_options=None, input_field_dependencies=None, labels=None, object_types=None, local_vars_configuration=None
    ):  # noqa: E501
        """ExtensionActionDefinitionPatch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._action_url = None
        self._published = None
        self._input_fields = None
        self._object_request_options = None
        self._input_field_dependencies = None
        self._labels = None
        self._object_types = None
        self.discriminator = None

        if action_url is not None:
            self.action_url = action_url
        if published is not None:
            self.published = published
        if input_fields is not None:
            self.input_fields = input_fields
        if object_request_options is not None:
            self.object_request_options = object_request_options
        if input_field_dependencies is not None:
            self.input_field_dependencies = input_field_dependencies
        if labels is not None:
            self.labels = labels
        if object_types is not None:
            self.object_types = object_types

    @property
    def action_url(self):
        """Gets the action_url of this ExtensionActionDefinitionPatch.  # noqa: E501

        The URL that will accept an HTTPS request each time workflows executes the custom action.  # noqa: E501

        :return: The action_url of this ExtensionActionDefinitionPatch.  # noqa: E501
        :rtype: str
        """
        return self._action_url

    @action_url.setter
    def action_url(self, action_url):
        """Sets the action_url of this ExtensionActionDefinitionPatch.

        The URL that will accept an HTTPS request each time workflows executes the custom action.  # noqa: E501

        :param action_url: The action_url of this ExtensionActionDefinitionPatch.  # noqa: E501
        :type action_url: str
        """

        self._action_url = action_url

    @property
    def published(self):
        """Gets the published of this ExtensionActionDefinitionPatch.  # noqa: E501

        Whether this custom action is published to customers.  # noqa: E501

        :return: The published of this ExtensionActionDefinitionPatch.  # noqa: E501
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """Sets the published of this ExtensionActionDefinitionPatch.

        Whether this custom action is published to customers.  # noqa: E501

        :param published: The published of this ExtensionActionDefinitionPatch.  # noqa: E501
        :type published: bool
        """

        self._published = published

    @property
    def input_fields(self):
        """Gets the input_fields of this ExtensionActionDefinitionPatch.  # noqa: E501

        The list of input fields to display in this custom action.  # noqa: E501

        :return: The input_fields of this ExtensionActionDefinitionPatch.  # noqa: E501
        :rtype: list[InputFieldDefinition]
        """
        return self._input_fields

    @input_fields.setter
    def input_fields(self, input_fields):
        """Sets the input_fields of this ExtensionActionDefinitionPatch.

        The list of input fields to display in this custom action.  # noqa: E501

        :param input_fields: The input_fields of this ExtensionActionDefinitionPatch.  # noqa: E501
        :type input_fields: list[InputFieldDefinition]
        """

        self._input_fields = input_fields

    @property
    def object_request_options(self):
        """Gets the object_request_options of this ExtensionActionDefinitionPatch.  # noqa: E501


        :return: The object_request_options of this ExtensionActionDefinitionPatch.  # noqa: E501
        :rtype: ObjectRequestOptions
        """
        return self._object_request_options

    @object_request_options.setter
    def object_request_options(self, object_request_options):
        """Sets the object_request_options of this ExtensionActionDefinitionPatch.


        :param object_request_options: The object_request_options of this ExtensionActionDefinitionPatch.  # noqa: E501
        :type object_request_options: ObjectRequestOptions
        """

        self._object_request_options = object_request_options

    @property
    def input_field_dependencies(self):
        """Gets the input_field_dependencies of this ExtensionActionDefinitionPatch.  # noqa: E501

        A list of dependencies between the input fields. These configure when the input fields should be visible.  # noqa: E501

        :return: The input_field_dependencies of this ExtensionActionDefinitionPatch.  # noqa: E501
        :rtype: list[ExtensionActionDefinitionPatchInputFieldDependenciesInner]
        """
        return self._input_field_dependencies

    @input_field_dependencies.setter
    def input_field_dependencies(self, input_field_dependencies):
        """Sets the input_field_dependencies of this ExtensionActionDefinitionPatch.

        A list of dependencies between the input fields. These configure when the input fields should be visible.  # noqa: E501

        :param input_field_dependencies: The input_field_dependencies of this ExtensionActionDefinitionPatch.  # noqa: E501
        :type input_field_dependencies: list[ExtensionActionDefinitionPatchInputFieldDependenciesInner]
        """

        self._input_field_dependencies = input_field_dependencies

    @property
    def labels(self):
        """Gets the labels of this ExtensionActionDefinitionPatch.  # noqa: E501

        The user-facing labels for the custom action.  # noqa: E501

        :return: The labels of this ExtensionActionDefinitionPatch.  # noqa: E501
        :rtype: dict[str, ActionLabels]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ExtensionActionDefinitionPatch.

        The user-facing labels for the custom action.  # noqa: E501

        :param labels: The labels of this ExtensionActionDefinitionPatch.  # noqa: E501
        :type labels: dict[str, ActionLabels]
        """

        self._labels = labels

    @property
    def object_types(self):
        """Gets the object_types of this ExtensionActionDefinitionPatch.  # noqa: E501

        The object types that this custom action supports.  # noqa: E501

        :return: The object_types of this ExtensionActionDefinitionPatch.  # noqa: E501
        :rtype: list[str]
        """
        return self._object_types

    @object_types.setter
    def object_types(self, object_types):
        """Sets the object_types of this ExtensionActionDefinitionPatch.

        The object types that this custom action supports.  # noqa: E501

        :param object_types: The object_types of this ExtensionActionDefinitionPatch.  # noqa: E501
        :type object_types: list[str]
        """

        self._object_types = object_types

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
        if not isinstance(other, ExtensionActionDefinitionPatch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExtensionActionDefinitionPatch):
            return True

        return self.to_dict() != other.to_dict()
