# -*- coding: utf-8 -*-

"""
mdnotesccg

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from tests.http_response_catcher import HttpResponseCatcher
from mdnotesccg.api_helper import APIHelper
from mdnotesccg.controllers.service_controller import ServiceController


class ServiceControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(ServiceControllerTests, cls).setUpClass()
        cls.response_catcher = HttpResponseCatcher()
        cls.controller = ServiceController(cls.config, cls.response_catcher)

    # Todo: Add description for test test_check_service_status
    def test_check_service_status(self):

        # Perform the API call through the SDK function
        result = self.controller.get_status()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

