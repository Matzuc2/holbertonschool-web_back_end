#!/usr/bin/env python3
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
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

    def test_public_repos_url(self):
        """test to mock a property directly from a class"""
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repo:
            mock_public_repo.return_value = {"repos_url": "https://api.github.com/orgs/aaa"}
            client = GithubOrgClient("aaa")
            public_repo = client._public_repos_url
            self.assertEqual(mock_public_repo.return_value, public_repo)

    @patch('client.get_json')
    def test_public_repos(self, mock_get):
        """testing combined test at once from above"""
        mock_get.return_value = {"hello": "world"}
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repo:
            mock_public_repo.return_value = {"repos_url": 'https://api.github.com/orgs/aaa'}
            client = GithubOrgClient("aaa")
            mocked_org = client.org
            public_repo = client._public_repos_url
            self.assertEqual(mock_public_repo.return_value, public_repo )
            self.assertEqual(mock_get.return_value, mocked_org)
            mock_get.assert_called_once()
            mock_public_repo.assert_called_once()

        
