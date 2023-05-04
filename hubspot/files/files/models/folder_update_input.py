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


class FolderUpdateInput(object):
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
    openapi_types = {"id": "str", "name": "str", "parent_folder_id": "int"}

    attribute_map = {"id": "id", "name": "name", "parent_folder_id": "parentFolderId"}

    def __init__(self, id=None, name=None, parent_folder_id=None, local_vars_configuration=None):  # noqa: E501
        """FolderUpdateInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._parent_folder_id = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if parent_folder_id is not None:
            self.parent_folder_id = parent_folder_id

    @property
    def id(self):
        """Gets the id of this FolderUpdateInput.  # noqa: E501

        Id of the folder to change.  # noqa: E501

        :return: The id of this FolderUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FolderUpdateInput.

        Id of the folder to change.  # noqa: E501

        :param id: The id of this FolderUpdateInput.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this FolderUpdateInput.  # noqa: E501

        New name. If specified the folder's name and fullPath will change. All children of the folder will be updated accordingly.  # noqa: E501

        :return: The name of this FolderUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FolderUpdateInput.

        New name. If specified the folder's name and fullPath will change. All children of the folder will be updated accordingly.  # noqa: E501

        :param name: The name of this FolderUpdateInput.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def parent_folder_id(self):
        """Gets the parent_folder_id of this FolderUpdateInput.  # noqa: E501

        New parent folder ID. If changed, the folder and all it's children will be moved into the specified folder. parentFolderId and parentFolderPath cannot be specified at the same time.  # noqa: E501

        :return: The parent_folder_id of this FolderUpdateInput.  # noqa: E501
        :rtype: int
        """
        return self._parent_folder_id

    @parent_folder_id.setter
    def parent_folder_id(self, parent_folder_id):
        """Sets the parent_folder_id of this FolderUpdateInput.

        New parent folder ID. If changed, the folder and all it's children will be moved into the specified folder. parentFolderId and parentFolderPath cannot be specified at the same time.  # noqa: E501

        :param parent_folder_id: The parent_folder_id of this FolderUpdateInput.  # noqa: E501
        :type parent_folder_id: int
        """

        self._parent_folder_id = parent_folder_id

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
        if not isinstance(other, FolderUpdateInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FolderUpdateInput):
            return True

        return self.to_dict() != other.to_dict()
