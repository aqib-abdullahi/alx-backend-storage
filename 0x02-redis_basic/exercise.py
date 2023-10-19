#!/usr/bin/env python3
"""Cache module task0
"""
from typing import Union
import redis
import uuid


class Cache():
    """cache class
    """
    def __init__(self):
        """initializer
        """
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generates a random key and inputs data in redis
        using the random key
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
