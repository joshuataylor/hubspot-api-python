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


class FormDefinitionBase(object):
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
        "form_type": "str",
        "id": "str",
        "name": "str",
        "created_at": "datetime",
        "updated_at": "datetime",
        "archived": "bool",
        "archived_at": "datetime",
        "field_groups": "list[FieldGroup]",
        "configuration": "HubSpotFormConfiguration",
        "display_options": "FormDisplayOptions",
        "legal_consent_options": "object",
    }

    attribute_map = {
        "form_type": "formType",
        "id": "id",
        "name": "name",
        "created_at": "createdAt",
        "updated_at": "updatedAt",
        "archived": "archived",
        "archived_at": "archivedAt",
        "field_groups": "fieldGroups",
        "configuration": "configuration",
        "display_options": "displayOptions",
        "legal_consent_options": "legalConsentOptions",
    }

    def __init__(
        self,
        form_type="hubspot",
        id=None,
        name=None,
        created_at=None,
        updated_at=None,
        archived=None,
        archived_at=None,
        field_groups=None,
        configuration=None,
        display_options=None,
        legal_consent_options=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """FormDefinitionBase - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._form_type = None
        self._id = None
        self._name = None
        self._created_at = None
        self._updated_at = None
        self._archived = None
        self._archived_at = None
        self._field_groups = None
        self._configuration = None
        self._display_options = None
        self._legal_consent_options = None
        self.discriminator = None

        self.form_type = form_type
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
        self.archived = archived
        if archived_at is not None:
            self.archived_at = archived_at
        self.field_groups = field_groups
        self.configuration = configuration
        self.display_options = display_options
        self.legal_consent_options = legal_consent_options

    @property
    def form_type(self):
        """Gets the form_type of this FormDefinitionBase.  # noqa: E501


        :return: The form_type of this FormDefinitionBase.  # noqa: E501
        :rtype: str
        """
        return self._form_type

    @form_type.setter
    def form_type(self, form_type):
        """Sets the form_type of this FormDefinitionBase.


        :param form_type: The form_type of this FormDefinitionBase.  # noqa: E501
        :type form_type: str
        """
        if self.local_vars_configuration.client_side_validation and form_type is None:  # noqa: E501
            raise ValueError("Invalid value for `form_type`, must not be `None`")  # noqa: E501
        allowed_values = ["hubspot"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and form_type not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `form_type` ({0}), must be one of {1}".format(form_type, allowed_values))  # noqa: E501

        self._form_type = form_type

    @property
    def id(self):
        """Gets the id of this FormDefinitionBase.  # noqa: E501


        :return: The id of this FormDefinitionBase.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FormDefinitionBase.


        :param id: The id of this FormDefinitionBase.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this FormDefinitionBase.  # noqa: E501


        :return: The name of this FormDefinitionBase.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FormDefinitionBase.


        :param name: The name of this FormDefinitionBase.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this FormDefinitionBase.  # noqa: E501


        :return: The created_at of this FormDefinitionBase.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FormDefinitionBase.


        :param created_at: The created_at of this FormDefinitionBase.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this FormDefinitionBase.  # noqa: E501


        :return: The updated_at of this FormDefinitionBase.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this FormDefinitionBase.


        :param updated_at: The updated_at of this FormDefinitionBase.  # noqa: E501
        :type updated_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def archived(self):
        """Gets the archived of this FormDefinitionBase.  # noqa: E501


        :return: The archived of this FormDefinitionBase.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this FormDefinitionBase.


        :param archived: The archived of this FormDefinitionBase.  # noqa: E501
        :type archived: bool
        """
        if self.local_vars_configuration.client_side_validation and archived is None:  # noqa: E501
            raise ValueError("Invalid value for `archived`, must not be `None`")  # noqa: E501

        self._archived = archived

    @property
    def archived_at(self):
        """Gets the archived_at of this FormDefinitionBase.  # noqa: E501


        :return: The archived_at of this FormDefinitionBase.  # noqa: E501
        :rtype: datetime
        """
        return self._archived_at

    @archived_at.setter
    def archived_at(self, archived_at):
        """Sets the archived_at of this FormDefinitionBase.


        :param archived_at: The archived_at of this FormDefinitionBase.  # noqa: E501
        :type archived_at: datetime
        """

        self._archived_at = archived_at

    @property
    def field_groups(self):
        """Gets the field_groups of this FormDefinitionBase.  # noqa: E501


        :return: The field_groups of this FormDefinitionBase.  # noqa: E501
        :rtype: list[FieldGroup]
        """
        return self._field_groups

    @field_groups.setter
    def field_groups(self, field_groups):
        """Sets the field_groups of this FormDefinitionBase.


        :param field_groups: The field_groups of this FormDefinitionBase.  # noqa: E501
        :type field_groups: list[FieldGroup]
        """
        if self.local_vars_configuration.client_side_validation and field_groups is None:  # noqa: E501
            raise ValueError("Invalid value for `field_groups`, must not be `None`")  # noqa: E501

        self._field_groups = field_groups

    @property
    def configuration(self):
        """Gets the configuration of this FormDefinitionBase.  # noqa: E501


        :return: The configuration of this FormDefinitionBase.  # noqa: E501
        :rtype: HubSpotFormConfiguration
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this FormDefinitionBase.


        :param configuration: The configuration of this FormDefinitionBase.  # noqa: E501
        :type configuration: HubSpotFormConfiguration
        """
        if self.local_vars_configuration.client_side_validation and configuration is None:  # noqa: E501
            raise ValueError("Invalid value for `configuration`, must not be `None`")  # noqa: E501

        self._configuration = configuration

    @property
    def display_options(self):
        """Gets the display_options of this FormDefinitionBase.  # noqa: E501


        :return: The display_options of this FormDefinitionBase.  # noqa: E501
        :rtype: FormDisplayOptions
        """
        return self._display_options

    @display_options.setter
    def display_options(self, display_options):
        """Sets the display_options of this FormDefinitionBase.


        :param display_options: The display_options of this FormDefinitionBase.  # noqa: E501
        :type display_options: FormDisplayOptions
        """
        if self.local_vars_configuration.client_side_validation and display_options is None:  # noqa: E501
            raise ValueError("Invalid value for `display_options`, must not be `None`")  # noqa: E501

        self._display_options = display_options

    @property
    def legal_consent_options(self):
        """Gets the legal_consent_options of this FormDefinitionBase.  # noqa: E501


        :return: The legal_consent_options of this FormDefinitionBase.  # noqa: E501
        :rtype: object
        """
        return self._legal_consent_options

    @legal_consent_options.setter
    def legal_consent_options(self, legal_consent_options):
        """Sets the legal_consent_options of this FormDefinitionBase.


        :param legal_consent_options: The legal_consent_options of this FormDefinitionBase.  # noqa: E501
        :type legal_consent_options: object
        """
        if self.local_vars_configuration.client_side_validation and legal_consent_options is None:  # noqa: E501
            raise ValueError("Invalid value for `legal_consent_options`, must not be `None`")  # noqa: E501

        self._legal_consent_options = legal_consent_options

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
        if not isinstance(other, FormDefinitionBase):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FormDefinitionBase):
            return True

        return self.to_dict() != other.to_dict()
