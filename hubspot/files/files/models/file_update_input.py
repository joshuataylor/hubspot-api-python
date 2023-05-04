# coding: utf-8

"""
    Files

    Upload and manage files.  # noqa: E501

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

from hubspot.files.files.configuration import Configuration


class FileUpdateInput(object):
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
    openapi_types = {"name": "str", "parent_folder_id": "str", "parent_folder_path": "str", "is_usable_in_content": "bool", "access": "str"}

    attribute_map = {"name": "name", "parent_folder_id": "parentFolderId", "parent_folder_path": "parentFolderPath", "is_usable_in_content": "isUsableInContent", "access": "access"}

    def __init__(self, name=None, parent_folder_id=None, parent_folder_path=None, is_usable_in_content=None, access=None, local_vars_configuration=None):  # noqa: E501
        """FileUpdateInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._parent_folder_id = None
        self._parent_folder_path = None
        self._is_usable_in_content = None
        self._access = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if parent_folder_id is not None:
            self.parent_folder_id = parent_folder_id
        if parent_folder_path is not None:
            self.parent_folder_path = parent_folder_path
        if is_usable_in_content is not None:
            self.is_usable_in_content = is_usable_in_content
        if access is not None:
            self.access = access

    @property
    def name(self):
        """Gets the name of this FileUpdateInput.  # noqa: E501

        New name for the file.  # noqa: E501

        :return: The name of this FileUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileUpdateInput.

        New name for the file.  # noqa: E501

        :param name: The name of this FileUpdateInput.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def parent_folder_id(self):
        """Gets the parent_folder_id of this FileUpdateInput.  # noqa: E501

        Folder ID where the file should be moved to.  folderId and folderPath cannot be set at the same time.  # noqa: E501

        :return: The parent_folder_id of this FileUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._parent_folder_id

    @parent_folder_id.setter
    def parent_folder_id(self, parent_folder_id):
        """Sets the parent_folder_id of this FileUpdateInput.

        Folder ID where the file should be moved to.  folderId and folderPath cannot be set at the same time.  # noqa: E501

        :param parent_folder_id: The parent_folder_id of this FileUpdateInput.  # noqa: E501
        :type parent_folder_id: str
        """

        self._parent_folder_id = parent_folder_id

    @property
    def parent_folder_path(self):
        """Gets the parent_folder_path of this FileUpdateInput.  # noqa: E501

        Folder path where the file should be moved to. folderId and folderPath cannot be set at the same time.  # noqa: E501

        :return: The parent_folder_path of this FileUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._parent_folder_path

    @parent_folder_path.setter
    def parent_folder_path(self, parent_folder_path):
        """Sets the parent_folder_path of this FileUpdateInput.

        Folder path where the file should be moved to. folderId and folderPath cannot be set at the same time.  # noqa: E501

        :param parent_folder_path: The parent_folder_path of this FileUpdateInput.  # noqa: E501
        :type parent_folder_path: str
        """

        self._parent_folder_path = parent_folder_path

    @property
    def is_usable_in_content(self):
        """Gets the is_usable_in_content of this FileUpdateInput.  # noqa: E501

        Mark weather the file should be used in new content or not.  # noqa: E501

        :return: The is_usable_in_content of this FileUpdateInput.  # noqa: E501
        :rtype: bool
        """
        return self._is_usable_in_content

    @is_usable_in_content.setter
    def is_usable_in_content(self, is_usable_in_content):
        """Sets the is_usable_in_content of this FileUpdateInput.

        Mark weather the file should be used in new content or not.  # noqa: E501

        :param is_usable_in_content: The is_usable_in_content of this FileUpdateInput.  # noqa: E501
        :type is_usable_in_content: bool
        """

        self._is_usable_in_content = is_usable_in_content

    @property
    def access(self):
        """Gets the access of this FileUpdateInput.  # noqa: E501

        NONE: Do not run any duplicate validation. REJECT: Reject the upload if a duplicate is found. RETURN_EXISTING: If a duplicate file is found, do not upload a new file and return the found duplicate instead.   # noqa: E501

        :return: The access of this FileUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this FileUpdateInput.

        NONE: Do not run any duplicate validation. REJECT: Reject the upload if a duplicate is found. RETURN_EXISTING: If a duplicate file is found, do not upload a new file and return the found duplicate instead.   # noqa: E501

        :param access: The access of this FileUpdateInput.  # noqa: E501
        :type access: str
        """
        allowed_values = ["PUBLIC_INDEXABLE", "PUBLIC_NOT_INDEXABLE", "HIDDEN_INDEXABLE", "HIDDEN_NOT_INDEXABLE", "HIDDEN_PRIVATE", "PRIVATE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and access not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `access` ({0}), must be one of {1}".format(access, allowed_values))  # noqa: E501

        self._access = access

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
        if not isinstance(other, FileUpdateInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileUpdateInput):
            return True

        return self.to_dict() != other.to_dict()
