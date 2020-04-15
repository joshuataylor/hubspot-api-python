# coding: utf-8

"""
    CRM Imports

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.imports.configuration import Configuration


class PublicImportResponse(object):
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
        'created_at': 'datetime',
        'metadata': 'PublicImportMetadata',
        'updated_at': 'datetime',
        'state': 'str',
        'import_request_json': 'object',
        'opt_out_import': 'bool',
        'id': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'metadata': 'metadata',
        'updated_at': 'updatedAt',
        'state': 'state',
        'import_request_json': 'importRequestJson',
        'opt_out_import': 'optOutImport',
        'id': 'id'
    }

    def __init__(self, created_at=None, metadata=None, updated_at=None, state=None, import_request_json=None, opt_out_import=None, id=None, local_vars_configuration=None):  # noqa: E501
        """PublicImportResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._metadata = None
        self._updated_at = None
        self._state = None
        self._import_request_json = None
        self._opt_out_import = None
        self._id = None
        self.discriminator = None

        self.created_at = created_at
        self.metadata = metadata
        self.updated_at = updated_at
        self.state = state
        if import_request_json is not None:
            self.import_request_json = import_request_json
        self.opt_out_import = opt_out_import
        self.id = id

    @property
    def created_at(self):
        """Gets the created_at of this PublicImportResponse.  # noqa: E501


        :return: The created_at of this PublicImportResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PublicImportResponse.


        :param created_at: The created_at of this PublicImportResponse.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def metadata(self):
        """Gets the metadata of this PublicImportResponse.  # noqa: E501


        :return: The metadata of this PublicImportResponse.  # noqa: E501
        :rtype: PublicImportMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PublicImportResponse.


        :param metadata: The metadata of this PublicImportResponse.  # noqa: E501
        :type: PublicImportMetadata
        """
        if self.local_vars_configuration.client_side_validation and metadata is None:  # noqa: E501
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def updated_at(self):
        """Gets the updated_at of this PublicImportResponse.  # noqa: E501


        :return: The updated_at of this PublicImportResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PublicImportResponse.


        :param updated_at: The updated_at of this PublicImportResponse.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def state(self):
        """Gets the state of this PublicImportResponse.  # noqa: E501

        The status of the import.  # noqa: E501

        :return: The state of this PublicImportResponse.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PublicImportResponse.

        The status of the import.  # noqa: E501

        :param state: The state of this PublicImportResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["STARTED", "PROCESSING", "DONE", "FAILED", "CANCELED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def import_request_json(self):
        """Gets the import_request_json of this PublicImportResponse.  # noqa: E501


        :return: The import_request_json of this PublicImportResponse.  # noqa: E501
        :rtype: object
        """
        return self._import_request_json

    @import_request_json.setter
    def import_request_json(self, import_request_json):
        """Sets the import_request_json of this PublicImportResponse.


        :param import_request_json: The import_request_json of this PublicImportResponse.  # noqa: E501
        :type: object
        """

        self._import_request_json = import_request_json

    @property
    def opt_out_import(self):
        """Gets the opt_out_import of this PublicImportResponse.  # noqa: E501

        Whether or not the import is a list of people disqualified from receiving emails.  # noqa: E501

        :return: The opt_out_import of this PublicImportResponse.  # noqa: E501
        :rtype: bool
        """
        return self._opt_out_import

    @opt_out_import.setter
    def opt_out_import(self, opt_out_import):
        """Sets the opt_out_import of this PublicImportResponse.

        Whether or not the import is a list of people disqualified from receiving emails.  # noqa: E501

        :param opt_out_import: The opt_out_import of this PublicImportResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and opt_out_import is None:  # noqa: E501
            raise ValueError("Invalid value for `opt_out_import`, must not be `None`")  # noqa: E501

        self._opt_out_import = opt_out_import

    @property
    def id(self):
        """Gets the id of this PublicImportResponse.  # noqa: E501


        :return: The id of this PublicImportResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PublicImportResponse.


        :param id: The id of this PublicImportResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PublicImportResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicImportResponse):
            return True

        return self.to_dict() != other.to_dict()