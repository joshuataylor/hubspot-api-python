# coding: utf-8

"""
    CMS Performance API

    Use these endpoints to get a time series view of your website's performance.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.cms.performance.configuration import Configuration


class PerformanceView(object):
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
        "_403": "int",
        "_404": "int",
        "_500": "int",
        "_504": "int",
        "start_timestamp": "int",
        "end_timestamp": "int",
        "start_datetime": "str",
        "end_datetime": "str",
        "total_requests": "int",
        "cache_hits": "int",
        "cache_hit_rate": "float",
        "total_request_time": "int",
        "avg_origin_response_time": "int",
        "response_time_ms": "int",
        "_100_x": "int",
        "_20_x": "int",
        "_30_x": "int",
        "_40_x": "int",
        "_50_x": "int",
        "_50th": "int",
        "_95th": "int",
        "_99th": "int",
    }

    attribute_map = {
        "_403": "403",
        "_404": "404",
        "_500": "500",
        "_504": "504",
        "start_timestamp": "startTimestamp",
        "end_timestamp": "endTimestamp",
        "start_datetime": "startDatetime",
        "end_datetime": "endDatetime",
        "total_requests": "totalRequests",
        "cache_hits": "cacheHits",
        "cache_hit_rate": "cacheHitRate",
        "total_request_time": "totalRequestTime",
        "avg_origin_response_time": "avgOriginResponseTime",
        "response_time_ms": "responseTimeMs",
        "_100_x": "100X",
        "_20_x": "20X",
        "_30_x": "30X",
        "_40_x": "40X",
        "_50_x": "50X",
        "_50th": "50th",
        "_95th": "95th",
        "_99th": "99th",
    }

    def __init__(
        self,
        _403=None,
        _404=None,
        _500=None,
        _504=None,
        start_timestamp=None,
        end_timestamp=None,
        start_datetime=None,
        end_datetime=None,
        total_requests=None,
        cache_hits=None,
        cache_hit_rate=None,
        total_request_time=None,
        avg_origin_response_time=None,
        response_time_ms=None,
        _100_x=None,
        _20_x=None,
        _30_x=None,
        _40_x=None,
        _50_x=None,
        _50th=None,
        _95th=None,
        _99th=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """PerformanceView - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self.__403 = None
        self.__404 = None
        self.__500 = None
        self.__504 = None
        self._start_timestamp = None
        self._end_timestamp = None
        self._start_datetime = None
        self._end_datetime = None
        self._total_requests = None
        self._cache_hits = None
        self._cache_hit_rate = None
        self._total_request_time = None
        self._avg_origin_response_time = None
        self._response_time_ms = None
        self.__100_x = None
        self.__20_x = None
        self.__30_x = None
        self.__40_x = None
        self.__50_x = None
        self.__50th = None
        self.__95th = None
        self.__99th = None
        self.discriminator = None

        self._403 = _403
        self._404 = _404
        self._500 = _500
        self._504 = _504
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.total_requests = total_requests
        self.cache_hits = cache_hits
        self.cache_hit_rate = cache_hit_rate
        self.total_request_time = total_request_time
        self.avg_origin_response_time = avg_origin_response_time
        self.response_time_ms = response_time_ms
        self._100_x = _100_x
        self._20_x = _20_x
        self._30_x = _30_x
        self._40_x = _40_x
        self._50_x = _50_x
        self._50th = _50th
        self._95th = _95th
        self._99th = _99th

    @property
    def _403(self):
        """Gets the _403 of this PerformanceView.  # noqa: E501

        The number of responses that had an http status code of 403.  # noqa: E501

        :return: The _403 of this PerformanceView.  # noqa: E501
        :rtype: int
        """
        return self.__403

    @_403.setter
    def _403(self, _403):
        """Sets the _403 of this PerformanceView.

        The number of responses that had an http status code of 403.  # noqa: E501

        :param _403: The _403 of this PerformanceView.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and _403 is None:  # noqa: E501
            raise ValueError("Invalid value for `_403`, must not be `None`")  # noqa: E501

        self.__403 = _403

    @property
    def _404(self):
        """Gets the _404 of this PerformanceView.  # noqa: E501

        The number of responses that had an http status code of 404.  # noqa: E501

        :return: The _404 of this PerformanceView.  # noqa: E501
        :rtype: int
        """
        return self.__404

    @_404.setter
    def _404(self, _404):
        """Sets the _404 of this PerformanceView.

        The number of responses that had an http status code of 404.  # noqa: E501

        :param _404: The _404 of this PerformanceView.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and _404 is None:  # noqa: E501
            raise ValueError("Invalid value for `_404`, must not be `None`")  # noqa: E501

        self.__404 = _404

    @property
    def _500(self):
        """Gets the _500 of this PerformanceView.  # noqa: E501

        The number of responses that had an http status code of 500.  # noqa: E501

        :return: The _500 of this PerformanceView.  # noqa: E501
        :rtype: int
        """
        return self.__500

    @_500.setter
    def _500(self, _500):
        """Sets the _500 of this PerformanceView.

        The number of responses that had an http status code of 500.  # noqa: E501

        :param _500: The _500 of this PerformanceView.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and _500 is None:  # noqa: E501
            raise ValueError("Invalid value for `_500`, must not be `None`")  # noqa: E501

        self.__500 = _500

    @property
    def _504(self):
        """Gets the _504 of this PerformanceView.  # noqa: E501

        The number of responses that had an http status code of 504.  # noqa: E501

        :return: The _504 of this PerformanceView.  # noqa: E501
        :rtype: int
        """
        return self.__504

    @_504.setter
    def _504(self, _504):
        """Sets the _504 of this PerformanceView.

        The number of responses that had an http status code of 504.  # noqa: E501

        :param _504: The _504 of this PerformanceView.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and _504 is None:  # noqa: E501
            raise ValueError("Invalid value for `_504`, must not be `None`")  # noqa: E501

        self.__504 = _504

    @property
    def start_timestamp(self):
        """Gets the start_timestamp of this PerformanceView.  # noqa: E501

        The timestamp in milliseconds of the start of this interval.  # noqa: E501

        :return: The start_timestamp of this PerformanceView.  # noqa: E501
        :rtype: int
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        """Sets the start_timestamp of this PerformanceView.

        The timestamp in milliseconds of the start of this interval.  # noqa: E501

        :param start_timestamp: The start_timestamp of this PerformanceView.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and start_timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `start_timestamp`, must not be `None`")  # noqa: E501

        self._start_timestamp = start_timestamp

    @property
    def end_timestamp(self):
        """Gets the end_timestamp of this PerformanceView.  # noqa: E501

        The timestamp in milliseconds of the end of this interval.  # noqa: E501

        :return: The end_timestamp of this PerformanceView.  # noqa: E501
        :rtype: int
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        """Sets the end_timestamp of this PerformanceView.

        The timestamp in milliseconds of the end of this interval.  # noqa: E501

        :param end_timestamp: The end_timestamp of this PerformanceView.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and end_timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `end_timestamp`, must not be `None`")  # noqa: E501

        self._end_timestamp = end_timestamp

    @property
    def start_datetime(self):
        """Gets the start_datetime of this PerformanceView.  # noqa: E501


        :return: The start_datetime of this PerformanceView.  # noqa: E501
        :rtype: str
        """
        return self._start_datetime

    @start_datetime.setter
    def start_datetime(self, start_datetime):
        """Sets the start_datetime of this PerformanceView.


        :param start_datetime: The start_datetime of this PerformanceView.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and start_datetime is None:  # noqa: E501
            raise ValueError("Invalid value for `start_datetime`, must not be `None`")  # noqa: E501

        self._start_datetime = start_datetime

    @property
    def end_datetime(self):
        """Gets the end_datetime of this PerformanceView.  # noqa: E501


        :return: The end_datetime of this PerformanceView.  # noqa: E501
        :rtype: str
        """
        return self._end_datetime

    @end_datetime.setter
    def end_datetime(self, end_datetime):
        """Sets the end_datetime of this PerformanceView.


        :param end_datetime: The end_datetime of this PerformanceView.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and end_datetime is None:  # noqa: E501
            raise ValueError("Invalid value for `end_datetime`, must not be `None`")  # noqa: E501

        self._end_datetime = end_datetime

    @property
    def total_requests(self):
        """Gets the total_requests of this PerformanceView.  # noqa: E501

        The total number of requests received in this period.  # noqa: E501

        :return: The total_requests of this PerformanceView.  # noqa: E501
        :rtype: int
        """
        return self._total_requests

    @total_requests.setter
    def total_requests(self, total_requests):
        """Sets the total_requests of this PerformanceView.

        The total number of requests received in this period.  # noqa: E501

        :param total_requests: The total_requests of this PerformanceView.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_requests is None:  # noqa: E501
            raise ValueError("Invalid value for `total_requests`, must not be `None`")  # noqa: E501

        self._total_requests = total_requests

    @property
    def cache_hits(self):
        """Gets the cache_hits of this PerformanceView.  # noqa: E501

        The total number of requests that were served cached responses.  # noqa: E501

        :return: The cache_hits of this PerformanceView.  # noqa: E501
        :rtype: int
        """
        return self._cache_hits

    @cache_hits.setter
    def cache_hits(self, cache_hits):
        """Sets the cache_hits of this PerformanceView.

        The total number of requests that were served cached responses.  # noqa: E501

        :param cache_hits: The cache_hits of this PerformanceView.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and cache_hits is None:  # noqa: E501
            raise ValueError("Invalid value for `cache_hits`, must not be `None`")  # noqa: E501

        self._cache_hits = cache_hits

    @property
    def cache_hit_rate(self):
        """Gets the cache_hit_rate of this PerformanceView.  # noqa: E501

        The percentage of requests that were served cached responses.  # noqa: E501

        :return: The cache_hit_rate of this PerformanceView.  # noqa: E501
        :rtype: float
        """
        return self._cache_hit_rate

    @cache_hit_rate.setter
    def cache_hit_rate(self, cache_hit_rate):
        """Sets the cache_hit_rate of this PerformanceView.

        The percentage of requests that were served cached responses.  # noqa: E501

        :param cache_hit_rate: The cache_hit_rate of this PerformanceView.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and cache_hit_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `cache_hit_rate`, must not be `None`")  # noqa: E501

        self._cache_hit_rate = cache_hit_rate

    @property
    def total_request_time(self):
        """Gets the total_request_time of this PerformanceView.  # noqa: E501


        :return: The total_request_time of this PerformanceView.  # noqa: E501
        :rtype: int
        """
        return self._total_request_time

    @total_request_time.setter
    def total_request_time(self, total_request_time):
        """Sets the total_request_time of this PerformanceView.


        :param total_request_time: The total_request_time of this PerformanceView.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_request_time is None:  # noqa: E501
            raise ValueError("Invalid value for `total_request_time`, must not be `None`")  # noqa: E501

        self._total_request_time = total_request_time

    @property
    def avg_origin_response_time(self):
        """Gets the avg_origin_response_time of this PerformanceView.  # noqa: E501

        The average response time in milliseconds from the origin to the edge.  # noqa: E501

        :return: The avg_origin_response_time of this PerformanceView.  # noqa: E501
        :rtype: int
        """
        return self._avg_origin_response_time

    @avg_origin_response_time.setter
    def avg_origin_response_time(self, avg_origin_response_time):
        """Sets the avg_origin_response_time of this PerformanceView.

        The average response time in milliseconds from the origin to the edge.  # noqa: E501

        :param avg_origin_response_time: The avg_origin_response_time of this PerformanceView.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and avg_origin_response_time is None:  # noqa: E501
            raise ValueError("Invalid value for `avg_origin_response_time`, must not be `None`")  # noqa: E501

        self._avg_origin_response_time = avg_origin_response_time

    @property
    def response_time_ms(self):
        """Gets the response_time_ms of this PerformanceView.  # noqa: E501

        The average response time in milliseconds.  # noqa: E501

        :return: The response_time_ms of this PerformanceView.  # noqa: E501
        :rtype: int
        """
        return self._response_time_ms

    @response_time_ms.setter
    def response_time_ms(self, response_time_ms):
        """Sets the response_time_ms of this PerformanceView.

        The average response time in milliseconds.  # noqa: E501

        :param response_time_ms: The response_time_ms of this PerformanceView.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and response_time_ms is None:  # noqa: E501
            raise ValueError("Invalid value for `response_time_ms`, must not be `None`")  # noqa: E501

        self._response_time_ms = response_time_ms

    @property
    def _100_x(self):
        """Gets the _100_x of this PerformanceView.  # noqa: E501

        The number of responses that had an http status code between 1000-1999.  # noqa: E501

        :return: The _100_x of this PerformanceView.  # noqa: E501
        :rtype: int
        """
        return self.__100_x

    @_100_x.setter
    def _100_x(self, _100_x):
        """Sets the _100_x of this PerformanceView.

        The number of responses that had an http status code between 1000-1999.  # noqa: E501

        :param _100_x: The _100_x of this PerformanceView.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and _100_x is None:  # noqa: E501
            raise ValueError("Invalid value for `_100_x`, must not be `None`")  # noqa: E501

        self.__100_x = _100_x

    @property
    def _20_x(self):
        """Gets the _20_x of this PerformanceView.  # noqa: E501

        The number of responses that had an http status code between 200-299.  # noqa: E501

        :return: The _20_x of this PerformanceView.  # noqa: E501
        :rtype: int
        """
        return self.__20_x

    @_20_x.setter
    def _20_x(self, _20_x):
        """Sets the _20_x of this PerformanceView.

        The number of responses that had an http status code between 200-299.  # noqa: E501

        :param _20_x: The _20_x of this PerformanceView.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and _20_x is None:  # noqa: E501
            raise ValueError("Invalid value for `_20_x`, must not be `None`")  # noqa: E501

        self.__20_x = _20_x

    @property
    def _30_x(self):
        """Gets the _30_x of this PerformanceView.  # noqa: E501

        The number of responses that had an http status code between 300-399.  # noqa: E501

        :return: The _30_x of this PerformanceView.  # noqa: E501
        :rtype: int
        """
        return self.__30_x

    @_30_x.setter
    def _30_x(self, _30_x):
        """Sets the _30_x of this PerformanceView.

        The number of responses that had an http status code between 300-399.  # noqa: E501

        :param _30_x: The _30_x of this PerformanceView.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and _30_x is None:  # noqa: E501
            raise ValueError("Invalid value for `_30_x`, must not be `None`")  # noqa: E501

        self.__30_x = _30_x

    @property
    def _40_x(self):
        """Gets the _40_x of this PerformanceView.  # noqa: E501

        The number of responses that had an http status code between 400-499.  # noqa: E501

        :return: The _40_x of this PerformanceView.  # noqa: E501
        :rtype: int
        """
        return self.__40_x

    @_40_x.setter
    def _40_x(self, _40_x):
        """Sets the _40_x of this PerformanceView.

        The number of responses that had an http status code between 400-499.  # noqa: E501

        :param _40_x: The _40_x of this PerformanceView.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and _40_x is None:  # noqa: E501
            raise ValueError("Invalid value for `_40_x`, must not be `None`")  # noqa: E501

        self.__40_x = _40_x

    @property
    def _50_x(self):
        """Gets the _50_x of this PerformanceView.  # noqa: E501

        The number of responses that had an http status code between 500-599.  # noqa: E501

        :return: The _50_x of this PerformanceView.  # noqa: E501
        :rtype: int
        """
        return self.__50_x

    @_50_x.setter
    def _50_x(self, _50_x):
        """Sets the _50_x of this PerformanceView.

        The number of responses that had an http status code between 500-599.  # noqa: E501

        :param _50_x: The _50_x of this PerformanceView.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and _50_x is None:  # noqa: E501
            raise ValueError("Invalid value for `_50_x`, must not be `None`")  # noqa: E501

        self.__50_x = _50_x

    @property
    def _50th(self):
        """Gets the _50th of this PerformanceView.  # noqa: E501

        The 50th percentile response time.  # noqa: E501

        :return: The _50th of this PerformanceView.  # noqa: E501
        :rtype: int
        """
        return self.__50th

    @_50th.setter
    def _50th(self, _50th):
        """Sets the _50th of this PerformanceView.

        The 50th percentile response time.  # noqa: E501

        :param _50th: The _50th of this PerformanceView.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and _50th is None:  # noqa: E501
            raise ValueError("Invalid value for `_50th`, must not be `None`")  # noqa: E501

        self.__50th = _50th

    @property
    def _95th(self):
        """Gets the _95th of this PerformanceView.  # noqa: E501

        The 95th percentile response time.  # noqa: E501

        :return: The _95th of this PerformanceView.  # noqa: E501
        :rtype: int
        """
        return self.__95th

    @_95th.setter
    def _95th(self, _95th):
        """Sets the _95th of this PerformanceView.

        The 95th percentile response time.  # noqa: E501

        :param _95th: The _95th of this PerformanceView.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and _95th is None:  # noqa: E501
            raise ValueError("Invalid value for `_95th`, must not be `None`")  # noqa: E501

        self.__95th = _95th

    @property
    def _99th(self):
        """Gets the _99th of this PerformanceView.  # noqa: E501

        The 99th percentile response time.  # noqa: E501

        :return: The _99th of this PerformanceView.  # noqa: E501
        :rtype: int
        """
        return self.__99th

    @_99th.setter
    def _99th(self, _99th):
        """Sets the _99th of this PerformanceView.

        The 99th percentile response time.  # noqa: E501

        :param _99th: The _99th of this PerformanceView.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and _99th is None:  # noqa: E501
            raise ValueError("Invalid value for `_99th`, must not be `None`")  # noqa: E501

        self.__99th = _99th

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item, value.items()))
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
        if not isinstance(other, PerformanceView):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PerformanceView):
            return True

        return self.to_dict() != other.to_dict()
