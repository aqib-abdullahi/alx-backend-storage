#!/usr/bin/env python3
"""Cache module task0
"""
from typing import Union, Callable
import functools
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """counts how many times a Cache method is called
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function
        """
        key = method.__qualname__
        count = self._redis.get(key)
        count = int(count) if count is not None else 0
        self._redis.set(key, count + 1)
        return method(self, *args, **kwargs)

    return wrapper


class Cache():
    """cache class
    """
    def __init__(self):
        """initializer
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generates a random key and inputs data in redis
        using the random key
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """takes a key string argument and an optional callable
        which will be used to convert data back to the desired
        format"""
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """parametrize Cache.get with the correct conversion
        function.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        return self.get(key, fn=lambda d: int(d))
