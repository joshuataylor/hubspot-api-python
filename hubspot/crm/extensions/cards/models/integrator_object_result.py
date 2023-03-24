# coding: utf-8

"""
    CRM cards

    Allows an app to extend the CRM UI by surfacing custom cards in the sidebar of record pages. These cards are defined up-front as part of app configuration, then populated by external data fetch requests when the record page is accessed by a user.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.extensions.cards.configuration import Configuration


class IntegratorObjectResult(object):
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
        'title': 'str',
        'link_url': 'str',
        'tokens': 'list[ObjectToken]',
        'actions': 'list[OneOfActionHookActionBodyIFrameActionBody]'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'link_url': 'linkUrl',
        'tokens': 'tokens',
        'actions': 'actions'
    }

    def __init__(self, id=None, title=None, link_url=None, tokens=None, actions=None, local_vars_configuration=None):  # noqa: E501
        """IntegratorObjectResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._title = None
        self._link_url = None
        self._tokens = None
        self._actions = None
        self.discriminator = None

        self.id = id
        self.title = title
        if link_url is not None:
            self.link_url = link_url
        self.tokens = tokens
        self.actions = actions

    @property
    def id(self):
        """Gets the id of this IntegratorObjectResult.  # noqa: E501


        :return: The id of this IntegratorObjectResult.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IntegratorObjectResult.


        :param id: The id of this IntegratorObjectResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def title(self):
        """Gets the title of this IntegratorObjectResult.  # noqa: E501


        :return: The title of this IntegratorObjectResult.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this IntegratorObjectResult.


        :param title: The title of this IntegratorObjectResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def link_url(self):
        """Gets the link_url of this IntegratorObjectResult.  # noqa: E501


        :return: The link_url of this IntegratorObjectResult.  # noqa: E501
        :rtype: str
        """
        return self._link_url

    @link_url.setter
    def link_url(self, link_url):
        """Sets the link_url of this IntegratorObjectResult.


        :param link_url: The link_url of this IntegratorObjectResult.  # noqa: E501
        :type: str
        """

        self._link_url = link_url

    @property
    def tokens(self):
        """Gets the tokens of this IntegratorObjectResult.  # noqa: E501


        :return: The tokens of this IntegratorObjectResult.  # noqa: E501
        :rtype: list[ObjectToken]
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        """Sets the tokens of this IntegratorObjectResult.


        :param tokens: The tokens of this IntegratorObjectResult.  # noqa: E501
        :type: list[ObjectToken]
        """
        if self.local_vars_configuration.client_side_validation and tokens is None:  # noqa: E501
            raise ValueError("Invalid value for `tokens`, must not be `None`")  # noqa: E501

        self._tokens = tokens

    @property
    def actions(self):
        """Gets the actions of this IntegratorObjectResult.  # noqa: E501


        :return: The actions of this IntegratorObjectResult.  # noqa: E501
        :rtype: list[OneOfActionHookActionBodyIFrameActionBody]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this IntegratorObjectResult.


        :param actions: The actions of this IntegratorObjectResult.  # noqa: E501
        :type: list[OneOfActionHookActionBodyIFrameActionBody]
        """
        if self.local_vars_configuration.client_side_validation and actions is None:  # noqa: E501
            raise ValueError("Invalid value for `actions`, must not be `None`")  # noqa: E501

        self._actions = actions

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
        if not isinstance(other, IntegratorObjectResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IntegratorObjectResult):
            return True

        return self.to_dict() != other.to_dict()
