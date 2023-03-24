# coding: utf-8

"""
    Blog Post endpoints

    Use these endpoints for interacting with Blog Posts, Blog Authors, and Blog Tags  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.cms.blogs.authors.configuration import Configuration


class BlogAuthorCloneRequestVNext(object):
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
        'id': 'str',
        'language': 'str',
        'primary_language': 'str',
        'blog_author': 'BlogAuthor'
    }

    attribute_map = {
        'id': 'id',
        'language': 'language',
        'primary_language': 'primaryLanguage',
        'blog_author': 'blogAuthor'
    }

    def __init__(self, id=None, language=None, primary_language=None, blog_author=None, local_vars_configuration=None):  # noqa: E501
        """BlogAuthorCloneRequestVNext - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._language = None
        self._primary_language = None
        self._blog_author = None
        self.discriminator = None

        self.id = id
        if language is not None:
            self.language = language
        if primary_language is not None:
            self.primary_language = primary_language
        self.blog_author = blog_author

    @property
    def id(self):
        """Gets the id of this BlogAuthorCloneRequestVNext.  # noqa: E501

        ID of the object to be cloned.  # noqa: E501

        :return: The id of this BlogAuthorCloneRequestVNext.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BlogAuthorCloneRequestVNext.

        ID of the object to be cloned.  # noqa: E501

        :param id: The id of this BlogAuthorCloneRequestVNext.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def language(self):
        """Gets the language of this BlogAuthorCloneRequestVNext.  # noqa: E501

        Language of newly cloned object.  # noqa: E501

        :return: The language of this BlogAuthorCloneRequestVNext.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this BlogAuthorCloneRequestVNext.

        Language of newly cloned object.  # noqa: E501

        :param language: The language of this BlogAuthorCloneRequestVNext.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def primary_language(self):
        """Gets the primary_language of this BlogAuthorCloneRequestVNext.  # noqa: E501

        Primary language in multi-language group.  # noqa: E501

        :return: The primary_language of this BlogAuthorCloneRequestVNext.  # noqa: E501
        :rtype: str
        """
        return self._primary_language

    @primary_language.setter
    def primary_language(self, primary_language):
        """Sets the primary_language of this BlogAuthorCloneRequestVNext.

        Primary language in multi-language group.  # noqa: E501

        :param primary_language: The primary_language of this BlogAuthorCloneRequestVNext.  # noqa: E501
        :type: str
        """

        self._primary_language = primary_language

    @property
    def blog_author(self):
        """Gets the blog_author of this BlogAuthorCloneRequestVNext.  # noqa: E501


        :return: The blog_author of this BlogAuthorCloneRequestVNext.  # noqa: E501
        :rtype: BlogAuthor
        """
        return self._blog_author

    @blog_author.setter
    def blog_author(self, blog_author):
        """Sets the blog_author of this BlogAuthorCloneRequestVNext.


        :param blog_author: The blog_author of this BlogAuthorCloneRequestVNext.  # noqa: E501
        :type: BlogAuthor
        """
        if self.local_vars_configuration.client_side_validation and blog_author is None:  # noqa: E501
            raise ValueError("Invalid value for `blog_author`, must not be `None`")  # noqa: E501

        self._blog_author = blog_author

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
        if not isinstance(other, BlogAuthorCloneRequestVNext):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BlogAuthorCloneRequestVNext):
            return True

        return self.to_dict() != other.to_dict()
