#!/usr/bin/env python3
"""
Writing string to Redis
"""


import uuid
import redis
from typing import Union, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ increment every call
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    list_key_in = f"{method.__qualname__}:inputs"
    list_key_out = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        self._redis.rpush(list_key_in, str(args))
        output = method(self, *args, **kwds)
        self._redis.rpush(list_key_out, str(output))
        return output
    return wrapper


def replay(method: Callable) -> None:
    """ display history of calls
    """
    pass


class Cache:
    """store instance of redis
    """
    def __init__(self):
        """initialization
        """
        # store instance of redis client
        self._redis = redis.Redis()
        # flush the instance with 'flushdb'
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store the input
        """
        # generate key
        key = str(uuid.uuid4())
        # store
        self._redis.set(key, data)
        # return key
        return key

    def get(self, key: str,
            fn: Callable[..., Any] = None) -> Union[str, bytes, int, float]:
        """read from redis
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self):
        """parametrize get
        """
        pass

    def get_int(self):
        """parametrize get
        """
        pass
