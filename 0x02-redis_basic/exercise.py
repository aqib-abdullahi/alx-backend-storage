#!/usr/bin/env python3
"""Cache module task0
"""
from typing import Union, Callable
import redis
import uuid


class Cache():
    """cache class
    """
    def __init__(self):
        """initializer
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generates a random key and inputs data in redis
        using the random key
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(key: str, fn: Callable = None):
        """takes a key string argument and an optional callable
        which will be used to convert data back to the desired
        format"""
        data = self._redis.get(key)
        if data and fn is not None:
            fn(data)
            return data
        else:
            return data

    def get_str(self, key: str) -> Union[str, None]:
        """parametrize Cache.get with the correct conversion
        function.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        return self.get(key, fn=lambda d: int(d))
