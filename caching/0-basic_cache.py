#!/usr/bin/python3
"""Basic caching module that implements a simple cache system without 
any limit."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache implements a basic caching system without any size limit.

    This class inherits from BaseCaching and provides a simple cache
    implementation that stores key-value pairs without any eviction policy.
    """

    def __init__(self):
        """Initialize the BasicCache instance by calling the parent constructor."""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache.

        Args:
            key: The key under which to store the item.
            item: The item to store in the cache.

        If either key or item is None, this method does nothing.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache by key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key, or None if the key
            doesn't exist
            or is None.
        """
        if self.cache_data.get(key) and key:
            value = self.cache_data.get(key)
            return value
        else:
            return None
