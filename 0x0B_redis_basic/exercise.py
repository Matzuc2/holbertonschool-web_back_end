#!/usr/bin/env python3
"""Module is documented"""

from functools import wraps
from typing import Union, Optional, Callable, Any
import redis
import uuid


def call_history(method: Callable) -> Callable:
    """Record the inputs and outputs of a method call in Redis.

    The inputs are stored in the Redis list named after the method qualified
    name with the suffix ":inputs", and the outputs are stored in the list
    with the suffix ":outputs".

    Args:
        method: The method to wrap.

    Returns:
        A wrapper function that records call history and returns the result
        of the wrapped method.
    """

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
    """Display the history of calls for a given method.

    This function reads the stored inputs and outputs from Redis and prints
    how many times the method was called, followed by each input/output pair.

    Args:
        method: The method whose call history should be displayed.
    """

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
    """Count how many times a method is called.

    Each call increments a Redis counter stored under the method qualified
    name.

    Args:
        method: The method to wrap.

    Returns:
        A wrapper function that increments the call counter and returns the
        result of the wrapped method.
    """

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """Simple Redis-backed cache implementation."""

    def __init__(self):
        """Initialize the cache and clear the Redis database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis and return the generated key.

        Args:
            data: The value to store.

        Returns:
            The generated Redis key as a string.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """Retrieve a value from Redis and optionally transform it.

        Args:
            key: The Redis key to fetch.
            fn: Optional function used to convert the stored bytes.

        Returns:
            The stored value, or None if the key does not exist.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a Redis value as a UTF-8 string."""
        return self.get(key).decode()

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve a Redis value as an integer."""
        return self.get(key).decode()
