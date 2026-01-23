#!/usr/bin/python3
from base_caching import BaseCaching
class BasicCache(BaseCaching):
    def __init__(self):
        super().__init__()
    def put(self, key, item):
        if key and item :
            self.cache_data[key] = item
    def get(self, key):
        if self.cache_data.get(key) and key:
            value = self.cache_data.get(key)
            return value
        else:
            return None
