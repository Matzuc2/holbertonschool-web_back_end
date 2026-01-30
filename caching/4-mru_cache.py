#!/usr/bin/python3
"""MRU caching module that implements a Most Recently Used cache system."""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache implements an MRU (Most Recently Used) caching system.

    This class inherits from BaseCaching and provides a cache implementation
    that evicts the most recently used item when the cache reaches its
    maximum size.
    """

    def __init__(self):
        """Initialize the MRUCache instance by calling parent constructor."""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache using MRU eviction policy.

        Args:
            key: The key under which to store the item.
            item: The item to store in the cache.

        If either key or item is None, this method does nothing.
        If the cache exceeds MAX_ITEMS, the most recently used item is removed.
        """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            a = list(self.cache_data)[-2]
            self.cache_data.pop(a)
            print(f"DISCARD: {a}")

    def get(self, key):
        """Retrieve an item from the cache by key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key, or None if the key doesn't
            exist or is None.
        """
        if key and self.cache_data.get(key):
            item = self.cache_data.get(key)
            self.cache_data.pop(key)
            self.cache_data[key] = item
            return self.cache_data.get(key)
        else:
            return None
