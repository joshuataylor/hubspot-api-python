# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.auth.oauth.configuration import Configuration


class RefreshTokenInfoResponse(object):
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
    openapi_types = {"token": "str", "user": "str", "hub_domain": "str", "scopes": "list[str]", "hub_id": "int", "client_id": "str", "user_id": "int", "token_type": "str"}

    attribute_map = {"token": "token", "user": "user", "hub_domain": "hub_domain", "scopes": "scopes", "hub_id": "hub_id", "client_id": "client_id", "user_id": "user_id", "token_type": "token_type"}

    def __init__(self, token=None, user=None, hub_domain=None, scopes=None, hub_id=None, client_id=None, user_id=None, token_type=None, local_vars_configuration=None):  # noqa: E501
        """RefreshTokenInfoResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._token = None
        self._user = None
        self._hub_domain = None
        self._scopes = None
        self._hub_id = None
        self._client_id = None
        self._user_id = None
        self._token_type = None
        self.discriminator = None

        self.token = token
        if user is not None:
            self.user = user
        if hub_domain is not None:
            self.hub_domain = hub_domain
        self.scopes = scopes
        self.hub_id = hub_id
        self.client_id = client_id
        self.user_id = user_id
        self.token_type = token_type

    @property
    def token(self):
        """Gets the token of this RefreshTokenInfoResponse.  # noqa: E501


        :return: The token of this RefreshTokenInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this RefreshTokenInfoResponse.


        :param token: The token of this RefreshTokenInfoResponse.  # noqa: E501
        :type token: str
        """
        if self.local_vars_configuration.client_side_validation and token is None:  # noqa: E501
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def user(self):
        """Gets the user of this RefreshTokenInfoResponse.  # noqa: E501


        :return: The user of this RefreshTokenInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this RefreshTokenInfoResponse.


        :param user: The user of this RefreshTokenInfoResponse.  # noqa: E501
        :type user: str
        """

        self._user = user

    @property
    def hub_domain(self):
        """Gets the hub_domain of this RefreshTokenInfoResponse.  # noqa: E501


        :return: The hub_domain of this RefreshTokenInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._hub_domain

    @hub_domain.setter
    def hub_domain(self, hub_domain):
        """Sets the hub_domain of this RefreshTokenInfoResponse.


        :param hub_domain: The hub_domain of this RefreshTokenInfoResponse.  # noqa: E501
        :type hub_domain: str
        """

        self._hub_domain = hub_domain

    @property
    def scopes(self):
        """Gets the scopes of this RefreshTokenInfoResponse.  # noqa: E501


        :return: The scopes of this RefreshTokenInfoResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this RefreshTokenInfoResponse.


        :param scopes: The scopes of this RefreshTokenInfoResponse.  # noqa: E501
        :type scopes: list[str]
        """
        if self.local_vars_configuration.client_side_validation and scopes is None:  # noqa: E501
            raise ValueError("Invalid value for `scopes`, must not be `None`")  # noqa: E501

        self._scopes = scopes

    @property
    def hub_id(self):
        """Gets the hub_id of this RefreshTokenInfoResponse.  # noqa: E501


        :return: The hub_id of this RefreshTokenInfoResponse.  # noqa: E501
        :rtype: int
        """
        return self._hub_id

    @hub_id.setter
    def hub_id(self, hub_id):
        """Sets the hub_id of this RefreshTokenInfoResponse.


        :param hub_id: The hub_id of this RefreshTokenInfoResponse.  # noqa: E501
        :type hub_id: int
        """
        if self.local_vars_configuration.client_side_validation and hub_id is None:  # noqa: E501
            raise ValueError("Invalid value for `hub_id`, must not be `None`")  # noqa: E501

        self._hub_id = hub_id

    @property
    def client_id(self):
        """Gets the client_id of this RefreshTokenInfoResponse.  # noqa: E501


        :return: The client_id of this RefreshTokenInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this RefreshTokenInfoResponse.


        :param client_id: The client_id of this RefreshTokenInfoResponse.  # noqa: E501
        :type client_id: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def user_id(self):
        """Gets the user_id of this RefreshTokenInfoResponse.  # noqa: E501


        :return: The user_id of this RefreshTokenInfoResponse.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this RefreshTokenInfoResponse.


        :param user_id: The user_id of this RefreshTokenInfoResponse.  # noqa: E501
        :type user_id: int
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def token_type(self):
        """Gets the token_type of this RefreshTokenInfoResponse.  # noqa: E501


        :return: The token_type of this RefreshTokenInfoResponse.  # noqa: E501
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """Sets the token_type of this RefreshTokenInfoResponse.


        :param token_type: The token_type of this RefreshTokenInfoResponse.  # noqa: E501
        :type token_type: str
        """
        if self.local_vars_configuration.client_side_validation and token_type is None:  # noqa: E501
            raise ValueError("Invalid value for `token_type`, must not be `None`")  # noqa: E501

        self._token_type = token_type

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
        if not isinstance(other, RefreshTokenInfoResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RefreshTokenInfoResponse):
            return True

        return self.to_dict() != other.to_dict()
