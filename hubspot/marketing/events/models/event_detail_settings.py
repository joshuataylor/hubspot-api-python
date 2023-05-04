# coding: utf-8

"""
    Marketing Events Extension

    These APIs allow you to interact with HubSpot's Marketing Events Extension. It allows you to: * Create, Read or update Marketing Event information in HubSpot * Specify whether a HubSpot contact has registered, attended or cancelled a registration to a Marketing Event. * Specify a URL that can be called to get the details of a Marketing Event.   # noqa: E501

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

from hubspot.marketing.events.configuration import Configuration


class EventDetailSettings(object):
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
    openapi_types = {"app_id": "int", "event_details_url": "str"}

    attribute_map = {"app_id": "appId", "event_details_url": "eventDetailsUrl"}

    def __init__(self, app_id=None, event_details_url=None, local_vars_configuration=None):  # noqa: E501
        """EventDetailSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._app_id = None
        self._event_details_url = None
        self.discriminator = None

        self.app_id = app_id
        self.event_details_url = event_details_url

    @property
    def app_id(self):
        """Gets the app_id of this EventDetailSettings.  # noqa: E501

        The id of the application the settings are for  # noqa: E501

        :return: The app_id of this EventDetailSettings.  # noqa: E501
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this EventDetailSettings.

        The id of the application the settings are for  # noqa: E501

        :param app_id: The app_id of this EventDetailSettings.  # noqa: E501
        :type app_id: int
        """
        if self.local_vars_configuration.client_side_validation and app_id is None:  # noqa: E501
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def event_details_url(self):
        """Gets the event_details_url of this EventDetailSettings.  # noqa: E501

        The url that will be used to fetch marketing event details by id  # noqa: E501

        :return: The event_details_url of this EventDetailSettings.  # noqa: E501
        :rtype: str
        """
        return self._event_details_url

    @event_details_url.setter
    def event_details_url(self, event_details_url):
        """Sets the event_details_url of this EventDetailSettings.

        The url that will be used to fetch marketing event details by id  # noqa: E501

        :param event_details_url: The event_details_url of this EventDetailSettings.  # noqa: E501
        :type event_details_url: str
        """
        if self.local_vars_configuration.client_side_validation and event_details_url is None:  # noqa: E501
            raise ValueError("Invalid value for `event_details_url`, must not be `None`")  # noqa: E501

        self._event_details_url = event_details_url

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
        if not isinstance(other, EventDetailSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EventDetailSettings):
            return True

        return self.to_dict() != other.to_dict()
