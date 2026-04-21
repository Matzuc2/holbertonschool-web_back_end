#!/usr/bin/env python3
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock
class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get):
        """testing mock on get_json, with memoized"""
        mock_get.return_value = Mock()
        client = GithubOrgClient(org_name)
        mocked_org = client.org #here, it became a callable obj
        mock_get.assert_called_once_with(client.ORG_URL.format(org=org_name))
        self.assertEqual(mocked_org, mock_get.return_value)


        
