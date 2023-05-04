# coding: utf-8

"""
    CMS Source Code

    Endpoints for interacting with files in the CMS Developer File System. These files include HTML templates, CSS, JS, modules, and other assets which are used to create CMS content.  # noqa: E501

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

from hubspot.cms.source_code.configuration import Configuration


class AssetFileMetadata(object):
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
    openapi_types = {"id": "str", "name": "str", "folder": "bool", "children": "list[str]", "updated_at": "int", "created_at": "int", "archived_at": "int"}

    attribute_map = {"id": "id", "name": "name", "folder": "folder", "children": "children", "updated_at": "updatedAt", "created_at": "createdAt", "archived_at": "archivedAt"}

    def __init__(self, id=None, name=None, folder=None, children=None, updated_at=None, created_at=None, archived_at=None, local_vars_configuration=None):  # noqa: E501
        """AssetFileMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._folder = None
        self._children = None
        self._updated_at = None
        self._created_at = None
        self._archived_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.folder = folder
        if children is not None:
            self.children = children
        self.updated_at = updated_at
        self.created_at = created_at
        if archived_at is not None:
            self.archived_at = archived_at

    @property
    def id(self):
        """Gets the id of this AssetFileMetadata.  # noqa: E501

        The path of the file in the CMS Developer File System.  # noqa: E501

        :return: The id of this AssetFileMetadata.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssetFileMetadata.

        The path of the file in the CMS Developer File System.  # noqa: E501

        :param id: The id of this AssetFileMetadata.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this AssetFileMetadata.  # noqa: E501

        The name of the file.  # noqa: E501

        :return: The name of this AssetFileMetadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetFileMetadata.

        The name of the file.  # noqa: E501

        :param name: The name of this AssetFileMetadata.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def folder(self):
        """Gets the folder of this AssetFileMetadata.  # noqa: E501

        Determines whether or not this path points to a folder.  # noqa: E501

        :return: The folder of this AssetFileMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this AssetFileMetadata.

        Determines whether or not this path points to a folder.  # noqa: E501

        :param folder: The folder of this AssetFileMetadata.  # noqa: E501
        :type folder: bool
        """
        if self.local_vars_configuration.client_side_validation and folder is None:  # noqa: E501
            raise ValueError("Invalid value for `folder`, must not be `None`")  # noqa: E501

        self._folder = folder

    @property
    def children(self):
        """Gets the children of this AssetFileMetadata.  # noqa: E501

        If the object is a folder, contains the filenames of the files within the folder.  # noqa: E501

        :return: The children of this AssetFileMetadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this AssetFileMetadata.

        If the object is a folder, contains the filenames of the files within the folder.  # noqa: E501

        :param children: The children of this AssetFileMetadata.  # noqa: E501
        :type children: list[str]
        """

        self._children = children

    @property
    def updated_at(self):
        """Gets the updated_at of this AssetFileMetadata.  # noqa: E501

        Timestamp of when the object was last updated.  # noqa: E501

        :return: The updated_at of this AssetFileMetadata.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AssetFileMetadata.

        Timestamp of when the object was last updated.  # noqa: E501

        :param updated_at: The updated_at of this AssetFileMetadata.  # noqa: E501
        :type updated_at: int
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this AssetFileMetadata.  # noqa: E501

        Timestamp of when the object was first created.  # noqa: E501

        :return: The created_at of this AssetFileMetadata.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AssetFileMetadata.

        Timestamp of when the object was first created.  # noqa: E501

        :param created_at: The created_at of this AssetFileMetadata.  # noqa: E501
        :type created_at: int
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def archived_at(self):
        """Gets the archived_at of this AssetFileMetadata.  # noqa: E501

        Timestamp of when the object was archived (deleted).  # noqa: E501

        :return: The archived_at of this AssetFileMetadata.  # noqa: E501
        :rtype: int
        """
        return self._archived_at

    @archived_at.setter
    def archived_at(self, archived_at):
        """Sets the archived_at of this AssetFileMetadata.

        Timestamp of when the object was archived (deleted).  # noqa: E501

        :param archived_at: The archived_at of this AssetFileMetadata.  # noqa: E501
        :type archived_at: int
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
        if not isinstance(other, AssetFileMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetFileMetadata):
            return True

        return self.to_dict() != other.to_dict()
