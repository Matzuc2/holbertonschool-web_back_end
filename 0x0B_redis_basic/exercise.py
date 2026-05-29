#!/usr/bin/env python3
from functools import wraps
from typing import Union, Optional, Callable, Any
import redis
import uuid


def call_history(method: Callable) -> Callable:
    key = method.__qualname__
    key_output_list = key + ":outputs"
    key_input_list = key + ":inputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(key_input_list, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(key_output_list, output)
        return output
    return wrapper


def replay(method: Callable) -> None:
    redis_client = method.__self__._redis
    method_name = method.__qualname__
    inputs_key = f"{method_name}:inputs"
    outputs_key = f"{method_name}:outputs"

    inputs = redis_client.lrange(inputs_key, 0, -1)
    outputs = redis_client.lrange(outputs_key, 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")
    for input_args, output in zip(inputs, outputs):
        print(f"{method_name}(*{input_args.decode()}) -> {output.decode()}")


def count_calls(method: Callable) -> Callable:
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        return self.get(key).decode()

    def get_int(self, key: str) -> Optional[int]:
        return self.get(key).decode()
