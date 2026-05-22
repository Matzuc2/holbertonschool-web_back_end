#!/usr/bin/env python3
import redis
import uuid


class Cache():
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        key = str(uuid.uuid1())
        self._redis.set(key, 'Alice')
        return key
