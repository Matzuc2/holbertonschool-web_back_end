#!/usr/bin/env python3
"""Unit tests for GithubOrgClient. blablabla"""

from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """class for testing githuborgclient class"""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get):
        """testing mock on get_json, with memoized"""
        mock_get.return_value = Mock()
        client = GithubOrgClient(org_name)
        # here, it became a callable obj
        mocked_org = client.org
        mock_get.assert_called_once_with(client.ORG_URL.format(org=org_name))
        self.assertEqual(mocked_org, mock_get.return_value)

    def test_public_repos_url(self):
        """test to mock a property directly from a class"""
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_repo:
            mock_public_repo.return_value = {
                "repos_url": "https://api.github.com/orgs/aaa"
            }
            client = GithubOrgClient("aaa")
            public_repo = client._public_repos_url
            self.assertEqual(mock_public_repo.return_value, public_repo)

    @patch("client.get_json")
    def test_public_repos(self, mock_get):
        """testing combined test at once from above"""
        mock_get.return_value = {"hello": "world"}
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_repo:
            mock_public_repo.return_value = {
                "repos_url": "https://api.github.com/orgs/aaa"
            }
            client = GithubOrgClient("aaa")
            mocked_org = client.org
            public_repo = client._public_repos_url
            self.assertEqual(mock_public_repo.return_value, public_repo)
            self.assertEqual(mock_get.return_value, mocked_org)
            mock_get.assert_called_once()
            mock_public_repo.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "my_license"}}, "other_licence", False)
    ])
    def test_has_license(self, repository, licence_key, expected):
        """test to see if licence key function is greatly brought out"""
        client = GithubOrgClient("aaa")
        boolean = client.has_license(repository, licence_key)
        self.assertEqual(boolean, expected)

from fixtures import TEST_PAYLOAD
@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch("requests.get")

        def side_effect(url):
            payloads = {
                "https://api.github.com/orgs/google": cls.org_payload,
                "https://api.github.com/orgs/google/repos": cls.repos_payload,
            }
            if url not in payloads:
                raise ValueError("Unexpected URL: {}".format(url))
            response = Mock()
            response.json.return_value = payloads[url]
            return response

        mock_get = cls.get_patcher.start()
        mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()
