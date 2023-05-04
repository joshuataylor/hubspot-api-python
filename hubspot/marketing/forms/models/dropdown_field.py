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


class DropdownField(object):
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
        "field_type": "str",
        "object_type_id": "str",
        "name": "str",
        "label": "str",
        "description": "str",
        "required": "bool",
        "hidden": "bool",
        "dependent_fields": "list[DependentField]",
        "default_values": "list[str]",
        "options": "list[EnumeratedFieldOption]",
        "placeholder": "str",
    }

    attribute_map = {
        "field_type": "fieldType",
        "object_type_id": "objectTypeId",
        "name": "name",
        "label": "label",
        "description": "description",
        "required": "required",
        "hidden": "hidden",
        "dependent_fields": "dependentFields",
        "default_values": "defaultValues",
        "options": "options",
        "placeholder": "placeholder",
    }

    def __init__(
        self,
        field_type="dropdown",
        object_type_id=None,
        name=None,
        label=None,
        description=None,
        required=None,
        hidden=None,
        dependent_fields=None,
        default_values=None,
        options=None,
        placeholder=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """DropdownField - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._field_type = None
        self._object_type_id = None
        self._name = None
        self._label = None
        self._description = None
        self._required = None
        self._hidden = None
        self._dependent_fields = None
        self._default_values = None
        self._options = None
        self._placeholder = None
        self.discriminator = None

        self.field_type = field_type
        if object_type_id is not None:
            self.object_type_id = object_type_id
        if name is not None:
            self.name = name
        if label is not None:
            self.label = label
        if description is not None:
            self.description = description
        if required is not None:
            self.required = required
        if hidden is not None:
            self.hidden = hidden
        if dependent_fields is not None:
            self.dependent_fields = dependent_fields
        if default_values is not None:
            self.default_values = default_values
        if options is not None:
            self.options = options
        if placeholder is not None:
            self.placeholder = placeholder

    @property
    def field_type(self):
        """Gets the field_type of this DropdownField.  # noqa: E501

        Determines how the field will be displayed and validated.  # noqa: E501

        :return: The field_type of this DropdownField.  # noqa: E501
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this DropdownField.

        Determines how the field will be displayed and validated.  # noqa: E501

        :param field_type: The field_type of this DropdownField.  # noqa: E501
        :type field_type: str
        """
        if self.local_vars_configuration.client_side_validation and field_type is None:  # noqa: E501
            raise ValueError("Invalid value for `field_type`, must not be `None`")  # noqa: E501
        allowed_values = ["dropdown"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and field_type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `field_type` ({0}), must be one of {1}".format(field_type, allowed_values))  # noqa: E501

        self._field_type = field_type

    @property
    def object_type_id(self):
        """Gets the object_type_id of this DropdownField.  # noqa: E501

        A unique ID for this field's CRM object type. For example a CONTACT field will have the object type ID 0-1.  # noqa: E501

        :return: The object_type_id of this DropdownField.  # noqa: E501
        :rtype: str
        """
        return self._object_type_id

    @object_type_id.setter
    def object_type_id(self, object_type_id):
        """Sets the object_type_id of this DropdownField.

        A unique ID for this field's CRM object type. For example a CONTACT field will have the object type ID 0-1.  # noqa: E501

        :param object_type_id: The object_type_id of this DropdownField.  # noqa: E501
        :type object_type_id: str
        """

        self._object_type_id = object_type_id

    @property
    def name(self):
        """Gets the name of this DropdownField.  # noqa: E501

        The identifier of the field. In combination with the object type ID, it must be unique.  # noqa: E501

        :return: The name of this DropdownField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DropdownField.

        The identifier of the field. In combination with the object type ID, it must be unique.  # noqa: E501

        :param name: The name of this DropdownField.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def label(self):
        """Gets the label of this DropdownField.  # noqa: E501

        The main label for the form field.  # noqa: E501

        :return: The label of this DropdownField.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this DropdownField.

        The main label for the form field.  # noqa: E501

        :param label: The label of this DropdownField.  # noqa: E501
        :type label: str
        """

        self._label = label

    @property
    def description(self):
        """Gets the description of this DropdownField.  # noqa: E501

        Additional text helping the customer to complete the field.  # noqa: E501

        :return: The description of this DropdownField.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DropdownField.

        Additional text helping the customer to complete the field.  # noqa: E501

        :param description: The description of this DropdownField.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def required(self):
        """Gets the required of this DropdownField.  # noqa: E501

        Whether a value for this field is required when submitting the form.  # noqa: E501

        :return: The required of this DropdownField.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this DropdownField.

        Whether a value for this field is required when submitting the form.  # noqa: E501

        :param required: The required of this DropdownField.  # noqa: E501
        :type required: bool
        """

        self._required = required

    @property
    def hidden(self):
        """Gets the hidden of this DropdownField.  # noqa: E501

        Whether a field should be hidden or not. Hidden fields won't appear on the form, but can be used to pass a value to a property without requiring the customer to fill it in.  # noqa: E501

        :return: The hidden of this DropdownField.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this DropdownField.

        Whether a field should be hidden or not. Hidden fields won't appear on the form, but can be used to pass a value to a property without requiring the customer to fill it in.  # noqa: E501

        :param hidden: The hidden of this DropdownField.  # noqa: E501
        :type hidden: bool
        """

        self._hidden = hidden

    @property
    def dependent_fields(self):
        """Gets the dependent_fields of this DropdownField.  # noqa: E501

        A list of other fields to make visible based on the value filled in for this field.  # noqa: E501

        :return: The dependent_fields of this DropdownField.  # noqa: E501
        :rtype: list[DependentField]
        """
        return self._dependent_fields

    @dependent_fields.setter
    def dependent_fields(self, dependent_fields):
        """Sets the dependent_fields of this DropdownField.

        A list of other fields to make visible based on the value filled in for this field.  # noqa: E501

        :param dependent_fields: The dependent_fields of this DropdownField.  # noqa: E501
        :type dependent_fields: list[DependentField]
        """

        self._dependent_fields = dependent_fields

    @property
    def default_values(self):
        """Gets the default_values of this DropdownField.  # noqa: E501

        The values selected by default. Those values will be submitted unless the customer modifies them.  # noqa: E501

        :return: The default_values of this DropdownField.  # noqa: E501
        :rtype: list[str]
        """
        return self._default_values

    @default_values.setter
    def default_values(self, default_values):
        """Sets the default_values of this DropdownField.

        The values selected by default. Those values will be submitted unless the customer modifies them.  # noqa: E501

        :param default_values: The default_values of this DropdownField.  # noqa: E501
        :type default_values: list[str]
        """

        self._default_values = default_values

    @property
    def options(self):
        """Gets the options of this DropdownField.  # noqa: E501

        The list of available choices for this field.  # noqa: E501

        :return: The options of this DropdownField.  # noqa: E501
        :rtype: list[EnumeratedFieldOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this DropdownField.

        The list of available choices for this field.  # noqa: E501

        :param options: The options of this DropdownField.  # noqa: E501
        :type options: list[EnumeratedFieldOption]
        """

        self._options = options

    @property
    def placeholder(self):
        """Gets the placeholder of this DropdownField.  # noqa: E501

        The prompt text showing when the field isn't filled in.  # noqa: E501

        :return: The placeholder of this DropdownField.  # noqa: E501
        :rtype: str
        """
        return self._placeholder

    @placeholder.setter
    def placeholder(self, placeholder):
        """Sets the placeholder of this DropdownField.

        The prompt text showing when the field isn't filled in.  # noqa: E501

        :param placeholder: The placeholder of this DropdownField.  # noqa: E501
        :type placeholder: str
        """

        self._placeholder = placeholder

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
        if not isinstance(other, DropdownField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DropdownField):
            return True

        return self.to_dict() != other.to_dict()
