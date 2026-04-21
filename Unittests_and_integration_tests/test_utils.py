#!/usr/bin/env python3
from utils import access_nested_map, get_json, memoize
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ test the access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test the error is as expected with raise in access_nested_map"""
        with self.assertRaises(KeyError, msg=path):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, expected, mock_get):
        """test with mocked data"""
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = expected
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(expected, result)


class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        """test the memoize decorator"""
        class TestClass:
            def a_method(self):
                """return 42 each time"""
                return 42

            @memoize
            def a_property(self):
                """return the result of the mocked method"""
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = Mock()
            instance_test_one = TestClass()
            one_time = instance_test_one.a_property()
            second_time = instance_test_one.a_property()
            mock_method.assert_called_once()
            self.assertEqual(second_time, one_time)


if __name__ == '__main__':
    unittest.main()
