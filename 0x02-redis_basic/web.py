#!/usr/bin/env python3
"""Getting and cching a page
"""
import redis
import requests
from typing import Callable
import functools


redis = redis.Redis()


def caching(method: Callable) -> Callable:
    """Caches data output
    """
    @functools.wraps(method)
    def wrapper(url) -> str:
        """caches the output
        """
        count_key = f'count:{url}'
        result_key = f'result:{url}'
        count = redis.incr(count_key)

        if count_key == 1:
            redis.set(count_key, 0)
            redis.expire(count_key, 10)
        else:
            redis.expire(count_key, 10)
        result = redis.get(result_key)
        if result:
            return result.decode('utf-8')
        result = method(url)
#        redis.set(f'count:{url}', 0)
        redis.setex(result_key, 10, result)
        return result
    return wrapper


@caching
def get_page(url: str) -> str:
    """returns a page's contents using the
    URL
    """
    content = requests.get(url).text
    return content
