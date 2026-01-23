#!/usr/bin/python3
"""LIFO caching module that implements a Last-In-First-Out cache system."""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache implements a LIFO (Last-In-First-Out) caching system.

    This class inherits from BaseCaching and provides a cache implementation
    that evicts the most recently added item when the cache reaches its
    maximum size.
    """

    def __init__(self):
        """Initialize the LIFOCache instance by calling parent constructor."""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache using LIFO eviction policy.

        Args:
            key: The key under which to store the item.
            item: The item to store in the cache.

        If either key or item is None, this method does nothing.
        If the cache exceeds MAX_ITEMS, the last item added is removed.
        """
        if key and item:
                self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data)[-2]
            self.cache_data.pop(last_key)
            print(f"DISCARD: {last_key}")
    def get(self, key):
        """Retrieve an item from the cache by key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key, or None if the key doesn't
            exist or is None.
        """
        if key and self.cache_data.get(key):
            return self.cache_data.get(key)
        else:
            return None
