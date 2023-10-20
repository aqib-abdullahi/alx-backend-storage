#!/usr/bin/env python3
"""Getting and cching a page
"""
import redis
import requests
from typing import Callable
import functools


redis = redis.Redis()
def caching(method: Callable) -> Callabe:
    """Caches data output
    """
    @functools.wraps(method)
    def wrapper(url: str) -> str:
        """caches the output
        """
        redis.incr(f'count:{url}')
        result = redis.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis.set(f'count:{url}', 0)
        redis.setex(f'result:{url}', 10, result)
        return result
    return wrapper


@caching
def get_page(url: str) -> str:
    """returns a page's contents using the
    URL
    """
    content = requests.get(url).text
    return content


