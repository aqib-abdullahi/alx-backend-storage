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
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """stores history of inputs and outputs for a particular
    function
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """returns callable
        """
        input_list = f"{method.__qualname__}:inputs"
        output_list = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_list, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_list, str(output))
        return output

    return wrapper


def replay(method: Callable):
    """prints how many times a function has been called
    """
    method_name = method.__qualname__
    inputs = f"{method.__qualname__}:inputs"
    outputs = f"{method.__qualname__}:outputs"
    input_contents = cache._redis.lrange(inputs, 0, -1)
    output_contents = cache._redis.lrange(outputs, 0, -1)
    print(f"{method_name} was called {len(inputs)} times:")

    for input_values, output_values in zip(input_contents, output_contents):
        input_args = eval(input)
        print(f"{method_name}({input_args}) -> {output_data}")


class Cache():
    """cache class
    """
    def __init__(self):
        """initializer
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
