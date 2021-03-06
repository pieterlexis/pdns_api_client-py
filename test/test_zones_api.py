# coding: utf-8

"""
    PowerDNS Authoritative HTTP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 0.0.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import pdns_api_client
from pdns_api_client.rest import ApiException
from pdns_api_client.apis.zones_api import ZonesApi


class TestZonesApi(unittest.TestCase):
    """ ZonesApi unit test stubs """

    def setUp(self):
        self.api = pdns_api_client.apis.zones_api.ZonesApi()

    def tearDown(self):
        pass

    def test_axfr_export_zone(self):
        """
        Test case for axfr_export_zone

        Returns the zone in AXFR format.
        """
        pass

    def test_axfr_retrieve_zone(self):
        """
        Test case for axfr_retrieve_zone

        Send a DNS NOTIFY to all slaves.
        """
        pass

    def test_check_zone(self):
        """
        Test case for check_zone

        Verify zone contents/configuration.
        """
        pass

    def test_create_zone(self):
        """
        Test case for create_zone

        Creates a new domain, returns the Zone on creation.
        """
        pass

    def test_delete_zone(self):
        """
        Test case for delete_zone

        Deletes this zone, all attached metadata and rrsets.
        """
        pass

    def test_list_zone(self):
        """
        Test case for list_zone

        zone managed by a server
        """
        pass

    def test_list_zones(self):
        """
        Test case for list_zones

        List all Zones in a server
        """
        pass

    def test_notify_zone(self):
        """
        Test case for notify_zone

        Send a DNS NOTIFY to all slaves.
        """
        pass

    def test_patch_zone(self):
        """
        Test case for patch_zone

        Modifies present RRsets and comments. Returns 204 No Content on success.
        """
        pass

    def test_put_zone(self):
        """
        Test case for put_zone

        Modifies basic zone data (metadata).
        """
        pass

    def test_rectify_zone(self):
        """
        Test case for rectify_zone

        Rectify the zone data.
        """
        pass


if __name__ == '__main__':
    unittest.main()
