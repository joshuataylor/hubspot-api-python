# coding: utf-8

# flake8: noqa

"""
    CRM Owners

    HubSpot uses **owners** to assign CRM objects to specific people in your organization. The endpoints described here are used to get a list of the owners that are available for an account. To assign an owner to an object, set the hubspot_owner_id property using the appropriate CRM object update or create a request.  If teams are available for your HubSpot tier, these endpoints will also indicate which team(s) an owner can access, as well as which team is the owner's primary team.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from hubspot.crm.owners.api.owners_api import OwnersApi

# import ApiClient
from hubspot.crm.owners.api_client import ApiClient
from hubspot.crm.owners.configuration import Configuration
from hubspot.crm.owners.exceptions import OpenApiException
from hubspot.crm.owners.exceptions import ApiTypeError
from hubspot.crm.owners.exceptions import ApiValueError
from hubspot.crm.owners.exceptions import ApiKeyError
from hubspot.crm.owners.exceptions import ApiAttributeError
from hubspot.crm.owners.exceptions import ApiException

# import models into sdk package
from hubspot.crm.owners.models.collection_response_public_owner_forward_paging import CollectionResponsePublicOwnerForwardPaging
from hubspot.crm.owners.models.error import Error
from hubspot.crm.owners.models.error_detail import ErrorDetail
from hubspot.crm.owners.models.forward_paging import ForwardPaging
from hubspot.crm.owners.models.next_page import NextPage
from hubspot.crm.owners.models.public_owner import PublicOwner
from hubspot.crm.owners.models.public_team import PublicTeam
