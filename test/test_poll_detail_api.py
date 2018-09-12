# coding: utf-8

"""
    LOCKSS Poller Service REST API

    API of the LOCKSS Poller REST Service  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: lockss-support@lockss.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import lockss_poller
from lockss_poller.api.poll_detail_api import PollDetailApi  # noqa: E501
from lockss_poller.rest import ApiException


class TestPollDetailApi(unittest.TestCase):
    """PollDetailApi unit test stubs"""

    def setUp(self):
        self.api = lockss_poller.api.poll_detail_api.PollDetailApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_poll_peer_vote_urls(self):
        """Test case for get_poll_peer_vote_urls

        Poll Peer Data  # noqa: E501
        """
        pass

    def test_get_repair_queue_data(self):
        """Test case for get_repair_queue_data

        Poll Repairs  # noqa: E501
        """
        pass

    def test_get_tally_urls(self):
        """Test case for get_tally_urls

        Page Tally  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()