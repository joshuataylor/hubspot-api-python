# coding: utf-8

"""
    Accounting Extension

    These APIs allow you to interact with HubSpot's Accounting Extension. It allows you to: * Specify the URLs that HubSpot will use when making webhook requests to your external accounting system. * Respond to webhook calls made to your external accounting system by HubSpot   # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.extensions.accounting.configuration import Configuration


class InvoiceReadResponse(object):
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
        'external_invoice_number': 'str',
        'total_amount_billed': 'float',
        'balance_due': 'float',
        'currency_code': 'str',
        'due_date': 'date',
        'external_recipient_id': 'str',
        'received_by_recipient_date': 'int',
        'external_create_date_time': 'int',
        'is_voided': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'archived_at': 'datetime',
        'archived': 'bool',
        'external_account_id': 'str',
        'invoice_status': 'str',
        'id': 'str'
    }

    attribute_map = {
        'external_invoice_number': 'externalInvoiceNumber',
        'total_amount_billed': 'totalAmountBilled',
        'balance_due': 'balanceDue',
        'currency_code': 'currencyCode',
        'due_date': 'dueDate',
        'external_recipient_id': 'externalRecipientId',
        'received_by_recipient_date': 'receivedByRecipientDate',
        'external_create_date_time': 'externalCreateDateTime',
        'is_voided': 'isVoided',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'archived_at': 'archivedAt',
        'archived': 'archived',
        'external_account_id': 'externalAccountId',
        'invoice_status': 'invoiceStatus',
        'id': 'id'
    }

    def __init__(self, external_invoice_number=None, total_amount_billed=None, balance_due=None, currency_code=None, due_date=None, external_recipient_id=None, received_by_recipient_date=None, external_create_date_time=None, is_voided=None, created_at=None, updated_at=None, archived_at=None, archived=None, external_account_id=None, invoice_status=None, id=None, local_vars_configuration=None):  # noqa: E501
        """InvoiceReadResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._external_invoice_number = None
        self._total_amount_billed = None
        self._balance_due = None
        self._currency_code = None
        self._due_date = None
        self._external_recipient_id = None
        self._received_by_recipient_date = None
        self._external_create_date_time = None
        self._is_voided = None
        self._created_at = None
        self._updated_at = None
        self._archived_at = None
        self._archived = None
        self._external_account_id = None
        self._invoice_status = None
        self._id = None
        self.discriminator = None

        if external_invoice_number is not None:
            self.external_invoice_number = external_invoice_number
        self.total_amount_billed = total_amount_billed
        self.balance_due = balance_due
        self.currency_code = currency_code
        self.due_date = due_date
        self.external_recipient_id = external_recipient_id
        if received_by_recipient_date is not None:
            self.received_by_recipient_date = received_by_recipient_date
        if external_create_date_time is not None:
            self.external_create_date_time = external_create_date_time
        self.is_voided = is_voided
        self.created_at = created_at
        self.updated_at = updated_at
        if archived_at is not None:
            self.archived_at = archived_at
        self.archived = archived
        self.external_account_id = external_account_id
        self.invoice_status = invoice_status
        self.id = id

    @property
    def external_invoice_number(self):
        """Gets the external_invoice_number of this InvoiceReadResponse.  # noqa: E501

        The invoice number. Note that this is _not_ the ID of the invoice, but the number that the billed customer will see.  # noqa: E501

        :return: The external_invoice_number of this InvoiceReadResponse.  # noqa: E501
        :rtype: str
        """
        return self._external_invoice_number

    @external_invoice_number.setter
    def external_invoice_number(self, external_invoice_number):
        """Sets the external_invoice_number of this InvoiceReadResponse.

        The invoice number. Note that this is _not_ the ID of the invoice, but the number that the billed customer will see.  # noqa: E501

        :param external_invoice_number: The external_invoice_number of this InvoiceReadResponse.  # noqa: E501
        :type: str
        """

        self._external_invoice_number = external_invoice_number

    @property
    def total_amount_billed(self):
        """Gets the total_amount_billed of this InvoiceReadResponse.  # noqa: E501

        The total amount that this invoice is for.  # noqa: E501

        :return: The total_amount_billed of this InvoiceReadResponse.  # noqa: E501
        :rtype: float
        """
        return self._total_amount_billed

    @total_amount_billed.setter
    def total_amount_billed(self, total_amount_billed):
        """Sets the total_amount_billed of this InvoiceReadResponse.

        The total amount that this invoice is for.  # noqa: E501

        :param total_amount_billed: The total_amount_billed of this InvoiceReadResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and total_amount_billed is None:  # noqa: E501
            raise ValueError("Invalid value for `total_amount_billed`, must not be `None`")  # noqa: E501

        self._total_amount_billed = total_amount_billed

    @property
    def balance_due(self):
        """Gets the balance_due of this InvoiceReadResponse.  # noqa: E501

        The remaining balance due for the invoice.  # noqa: E501

        :return: The balance_due of this InvoiceReadResponse.  # noqa: E501
        :rtype: float
        """
        return self._balance_due

    @balance_due.setter
    def balance_due(self, balance_due):
        """Sets the balance_due of this InvoiceReadResponse.

        The remaining balance due for the invoice.  # noqa: E501

        :param balance_due: The balance_due of this InvoiceReadResponse.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and balance_due is None:  # noqa: E501
            raise ValueError("Invalid value for `balance_due`, must not be `None`")  # noqa: E501

        self._balance_due = balance_due

    @property
    def currency_code(self):
        """Gets the currency_code of this InvoiceReadResponse.  # noqa: E501

        The ISO 4217 currency code that represents the currency of the invoice.  # noqa: E501

        :return: The currency_code of this InvoiceReadResponse.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this InvoiceReadResponse.

        The ISO 4217 currency code that represents the currency of the invoice.  # noqa: E501

        :param currency_code: The currency_code of this InvoiceReadResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency_code is None:  # noqa: E501
            raise ValueError("Invalid value for `currency_code`, must not be `None`")  # noqa: E501

        self._currency_code = currency_code

    @property
    def due_date(self):
        """Gets the due_date of this InvoiceReadResponse.  # noqa: E501

        The due date of the invoice  # noqa: E501

        :return: The due_date of this InvoiceReadResponse.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this InvoiceReadResponse.

        The due date of the invoice  # noqa: E501

        :param due_date: The due_date of this InvoiceReadResponse.  # noqa: E501
        :type: date
        """
        if self.local_vars_configuration.client_side_validation and due_date is None:  # noqa: E501
            raise ValueError("Invalid value for `due_date`, must not be `None`")  # noqa: E501

        self._due_date = due_date

    @property
    def external_recipient_id(self):
        """Gets the external_recipient_id of this InvoiceReadResponse.  # noqa: E501

        The id of the customer in the external accounting system that the invoice was sent to.  # noqa: E501

        :return: The external_recipient_id of this InvoiceReadResponse.  # noqa: E501
        :rtype: str
        """
        return self._external_recipient_id

    @external_recipient_id.setter
    def external_recipient_id(self, external_recipient_id):
        """Sets the external_recipient_id of this InvoiceReadResponse.

        The id of the customer in the external accounting system that the invoice was sent to.  # noqa: E501

        :param external_recipient_id: The external_recipient_id of this InvoiceReadResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and external_recipient_id is None:  # noqa: E501
            raise ValueError("Invalid value for `external_recipient_id`, must not be `None`")  # noqa: E501

        self._external_recipient_id = external_recipient_id

    @property
    def received_by_recipient_date(self):
        """Gets the received_by_recipient_date of this InvoiceReadResponse.  # noqa: E501

        The datetime that that invoice was sent to the customer.  # noqa: E501

        :return: The received_by_recipient_date of this InvoiceReadResponse.  # noqa: E501
        :rtype: int
        """
        return self._received_by_recipient_date

    @received_by_recipient_date.setter
    def received_by_recipient_date(self, received_by_recipient_date):
        """Sets the received_by_recipient_date of this InvoiceReadResponse.

        The datetime that that invoice was sent to the customer.  # noqa: E501

        :param received_by_recipient_date: The received_by_recipient_date of this InvoiceReadResponse.  # noqa: E501
        :type: int
        """

        self._received_by_recipient_date = received_by_recipient_date

    @property
    def external_create_date_time(self):
        """Gets the external_create_date_time of this InvoiceReadResponse.  # noqa: E501

        The datetime that the invoice was created in the external accounting system.  # noqa: E501

        :return: The external_create_date_time of this InvoiceReadResponse.  # noqa: E501
        :rtype: int
        """
        return self._external_create_date_time

    @external_create_date_time.setter
    def external_create_date_time(self, external_create_date_time):
        """Sets the external_create_date_time of this InvoiceReadResponse.

        The datetime that the invoice was created in the external accounting system.  # noqa: E501

        :param external_create_date_time: The external_create_date_time of this InvoiceReadResponse.  # noqa: E501
        :type: int
        """

        self._external_create_date_time = external_create_date_time

    @property
    def is_voided(self):
        """Gets the is_voided of this InvoiceReadResponse.  # noqa: E501

        Indicated is the invoice has been voided or not.  # noqa: E501

        :return: The is_voided of this InvoiceReadResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_voided

    @is_voided.setter
    def is_voided(self, is_voided):
        """Sets the is_voided of this InvoiceReadResponse.

        Indicated is the invoice has been voided or not.  # noqa: E501

        :param is_voided: The is_voided of this InvoiceReadResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and is_voided is None:  # noqa: E501
            raise ValueError("Invalid value for `is_voided`, must not be `None`")  # noqa: E501

        self._is_voided = is_voided

    @property
    def created_at(self):
        """Gets the created_at of this InvoiceReadResponse.  # noqa: E501

        The datetime that the invoice was created in HubSpot.  # noqa: E501

        :return: The created_at of this InvoiceReadResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InvoiceReadResponse.

        The datetime that the invoice was created in HubSpot.  # noqa: E501

        :param created_at: The created_at of this InvoiceReadResponse.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this InvoiceReadResponse.  # noqa: E501

        The datetime that the invoice was last updated in HubSpot.  # noqa: E501

        :return: The updated_at of this InvoiceReadResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this InvoiceReadResponse.

        The datetime that the invoice was last updated in HubSpot.  # noqa: E501

        :param updated_at: The updated_at of this InvoiceReadResponse.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def archived_at(self):
        """Gets the archived_at of this InvoiceReadResponse.  # noqa: E501


        :return: The archived_at of this InvoiceReadResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._archived_at

    @archived_at.setter
    def archived_at(self, archived_at):
        """Sets the archived_at of this InvoiceReadResponse.


        :param archived_at: The archived_at of this InvoiceReadResponse.  # noqa: E501
        :type: datetime
        """

        self._archived_at = archived_at

    @property
    def archived(self):
        """Gets the archived of this InvoiceReadResponse.  # noqa: E501


        :return: The archived of this InvoiceReadResponse.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this InvoiceReadResponse.


        :param archived: The archived of this InvoiceReadResponse.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and archived is None:  # noqa: E501
            raise ValueError("Invalid value for `archived`, must not be `None`")  # noqa: E501

        self._archived = archived

    @property
    def external_account_id(self):
        """Gets the external_account_id of this InvoiceReadResponse.  # noqa: E501

        The id of the account in the external accounting system that this invoice is related to.  # noqa: E501

        :return: The external_account_id of this InvoiceReadResponse.  # noqa: E501
        :rtype: str
        """
        return self._external_account_id

    @external_account_id.setter
    def external_account_id(self, external_account_id):
        """Sets the external_account_id of this InvoiceReadResponse.

        The id of the account in the external accounting system that this invoice is related to.  # noqa: E501

        :param external_account_id: The external_account_id of this InvoiceReadResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and external_account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `external_account_id`, must not be `None`")  # noqa: E501

        self._external_account_id = external_account_id

    @property
    def invoice_status(self):
        """Gets the invoice_status of this InvoiceReadResponse.  # noqa: E501

        The status of the invoice  # noqa: E501

        :return: The invoice_status of this InvoiceReadResponse.  # noqa: E501
        :rtype: str
        """
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, invoice_status):
        """Sets the invoice_status of this InvoiceReadResponse.

        The status of the invoice  # noqa: E501

        :param invoice_status: The invoice_status of this InvoiceReadResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and invoice_status is None:  # noqa: E501
            raise ValueError("Invalid value for `invoice_status`, must not be `None`")  # noqa: E501
        allowed_values = ["CREATED", "SENT", "PAID", "CLOSED", "OVERDUE", "VOIDED", "NONE", "UNPAID"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and invoice_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `invoice_status` ({0}), must be one of {1}"  # noqa: E501
                .format(invoice_status, allowed_values)
            )

        self._invoice_status = invoice_status

    @property
    def id(self):
        """Gets the id of this InvoiceReadResponse.  # noqa: E501

        The id of this invoice in the external accounting system.  # noqa: E501

        :return: The id of this InvoiceReadResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InvoiceReadResponse.

        The id of this invoice in the external accounting system.  # noqa: E501

        :param id: The id of this InvoiceReadResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if not isinstance(other, InvoiceReadResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvoiceReadResponse):
            return True

        return self.to_dict() != other.to_dict()
