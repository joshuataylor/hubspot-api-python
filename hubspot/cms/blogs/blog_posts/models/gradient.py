# coding: utf-8

"""
    Blog Post endpoints

    Use these endpoints for interacting with Blog Posts, Blog Authors, and Blog Tags  # noqa: E501

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

from hubspot.cms.blogs.blog_posts.configuration import Configuration


class Gradient(object):
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
    openapi_types = {"side_or_corner": "SideOrCorner", "angle": "Angle", "colors": "list[ColorStop]"}

    attribute_map = {"side_or_corner": "sideOrCorner", "angle": "angle", "colors": "colors"}

    def __init__(self, side_or_corner=None, angle=None, colors=None, local_vars_configuration=None):  # noqa: E501
        """Gradient - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._side_or_corner = None
        self._angle = None
        self._colors = None
        self.discriminator = None

        self.side_or_corner = side_or_corner
        self.angle = angle
        self.colors = colors

    @property
    def side_or_corner(self):
        """Gets the side_or_corner of this Gradient.  # noqa: E501


        :return: The side_or_corner of this Gradient.  # noqa: E501
        :rtype: SideOrCorner
        """
        return self._side_or_corner

    @side_or_corner.setter
    def side_or_corner(self, side_or_corner):
        """Sets the side_or_corner of this Gradient.


        :param side_or_corner: The side_or_corner of this Gradient.  # noqa: E501
        :type side_or_corner: SideOrCorner
        """
        if self.local_vars_configuration.client_side_validation and side_or_corner is None:  # noqa: E501
            raise ValueError("Invalid value for `side_or_corner`, must not be `None`")  # noqa: E501

        self._side_or_corner = side_or_corner

    @property
    def angle(self):
        """Gets the angle of this Gradient.  # noqa: E501


        :return: The angle of this Gradient.  # noqa: E501
        :rtype: Angle
        """
        return self._angle

    @angle.setter
    def angle(self, angle):
        """Sets the angle of this Gradient.


        :param angle: The angle of this Gradient.  # noqa: E501
        :type angle: Angle
        """
        if self.local_vars_configuration.client_side_validation and angle is None:  # noqa: E501
            raise ValueError("Invalid value for `angle`, must not be `None`")  # noqa: E501

        self._angle = angle

    @property
    def colors(self):
        """Gets the colors of this Gradient.  # noqa: E501


        :return: The colors of this Gradient.  # noqa: E501
        :rtype: list[ColorStop]
        """
        return self._colors

    @colors.setter
    def colors(self, colors):
        """Sets the colors of this Gradient.


        :param colors: The colors of this Gradient.  # noqa: E501
        :type colors: list[ColorStop]
        """
        if self.local_vars_configuration.client_side_validation and colors is None:  # noqa: E501
            raise ValueError("Invalid value for `colors`, must not be `None`")  # noqa: E501

        self._colors = colors

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
        if not isinstance(other, Gradient):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Gradient):
            return True

        return self.to_dict() != other.to_dict()
