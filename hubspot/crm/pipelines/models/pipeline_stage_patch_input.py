# coding: utf-8

"""
    CRM Pipelines

    Pipelines represent distinct stages in a workflow, like closing a deal or servicing a support ticket. These endpoints provide access to read and modify pipelines in HubSpot. Pipelines support `deals` and `tickets` object types.  ## Pipeline ID validation  When calling endpoints that take pipelineId as a parameter, that ID must correspond to an existing, un-archived pipeline. Otherwise the request will fail with a `404 Not Found` response.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.pipelines.configuration import Configuration


class PipelineStagePatchInput(object):
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
        'label': 'str',
        'archived': 'bool',
        'display_order': 'int',
        'metadata': 'dict(str, str)'
    }

    attribute_map = {
        'label': 'label',
        'archived': 'archived',
        'display_order': 'displayOrder',
        'metadata': 'metadata'
    }

    def __init__(self, label=None, archived=None, display_order=None, metadata=None, local_vars_configuration=None):  # noqa: E501
        """PipelineStagePatchInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._label = None
        self._archived = None
        self._display_order = None
        self._metadata = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if archived is not None:
            self.archived = archived
        if display_order is not None:
            self.display_order = display_order
        self.metadata = metadata

    @property
    def label(self):
        """Gets the label of this PipelineStagePatchInput.  # noqa: E501

        A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's label must be unique within that pipeline.  # noqa: E501

        :return: The label of this PipelineStagePatchInput.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this PipelineStagePatchInput.

        A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's label must be unique within that pipeline.  # noqa: E501

        :param label: The label of this PipelineStagePatchInput.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def archived(self):
        """Gets the archived of this PipelineStagePatchInput.  # noqa: E501

        Whether the pipeline is archived.  # noqa: E501

        :return: The archived of this PipelineStagePatchInput.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this PipelineStagePatchInput.

        Whether the pipeline is archived.  # noqa: E501

        :param archived: The archived of this PipelineStagePatchInput.  # noqa: E501
        :type: bool
        """

        self._archived = archived

    @property
    def display_order(self):
        """Gets the display_order of this PipelineStagePatchInput.  # noqa: E501

        The order for displaying this pipeline stage. If two pipeline stages have a matching `displayOrder`, they will be sorted alphabetically by label.  # noqa: E501

        :return: The display_order of this PipelineStagePatchInput.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this PipelineStagePatchInput.

        The order for displaying this pipeline stage. If two pipeline stages have a matching `displayOrder`, they will be sorted alphabetically by label.  # noqa: E501

        :param display_order: The display_order of this PipelineStagePatchInput.  # noqa: E501
        :type: int
        """

        self._display_order = display_order

    @property
    def metadata(self):
        """Gets the metadata of this PipelineStagePatchInput.  # noqa: E501

        A JSON object containing properties that are not present on all object pipelines.  For `deals` pipelines, the `probability` field is required (`{ \"probability\": 0.5 }`), and represents the likelihood a deal will close. Possible values are between 0.0 and 1.0 in increments of 0.1.  For `tickets` pipelines, the `ticketState` field is optional (`{ \"ticketState\": \"OPEN\" }`), and represents whether the ticket remains open or has been closed by a member of your Support team. Possible values are `OPEN` or `CLOSED`.  # noqa: E501

        :return: The metadata of this PipelineStagePatchInput.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PipelineStagePatchInput.

        A JSON object containing properties that are not present on all object pipelines.  For `deals` pipelines, the `probability` field is required (`{ \"probability\": 0.5 }`), and represents the likelihood a deal will close. Possible values are between 0.0 and 1.0 in increments of 0.1.  For `tickets` pipelines, the `ticketState` field is optional (`{ \"ticketState\": \"OPEN\" }`), and represents whether the ticket remains open or has been closed by a member of your Support team. Possible values are `OPEN` or `CLOSED`.  # noqa: E501

        :param metadata: The metadata of this PipelineStagePatchInput.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and metadata is None:  # noqa: E501
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

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
        if not isinstance(other, PipelineStagePatchInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PipelineStagePatchInput):
            return True

        return self.to_dict() != other.to_dict()
