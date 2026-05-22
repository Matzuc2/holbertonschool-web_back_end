#!/usr/bin/env python3
from typing import Union
import redis
import uuid


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn=None) -> str:
        value = self._redis.get(key, None)
        if fn is int:
            converted_value = self.get_int(value)
        elif fn is str:
            converted_value = self.get_str(value)
        else:
            converted_value = None
        return converted_value

    def get_str(self, key: str) -> str:
        return str(self._redis.get(key))

    def get_int(self, key: str) -> str:
        return int(self._redis.get(key))
