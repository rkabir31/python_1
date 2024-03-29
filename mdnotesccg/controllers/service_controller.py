# -*- coding: utf-8 -*-

"""
mdnotesccg

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from mdnotesccg.api_helper import APIHelper
from mdnotesccg.configuration import Server
from mdnotesccg.controllers.base_controller import BaseController
from mdnotesccg.http.auth.o_auth_2 import OAuth2
from mdnotesccg.models.service_status import ServiceStatus


class ServiceController(BaseController):

    """A Controller to access Endpoints in the mdnotesccg API."""

    def __init__(self, config, call_back=None):
        super(ServiceController, self).__init__(config, call_back)

    def get_status(self):
        """Does a GET request to /status.

        TODO: type endpoint description here.

        Returns:
            ServiceStatus: Response from the API.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/status'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.check_auth(self.config)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, ServiceStatus.from_dictionary)

        return decoded
