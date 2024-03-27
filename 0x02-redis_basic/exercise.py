#!/usr/bin/env python3
"""
Python module that uses Redis NoSQL for data storage """

import redis
import uuid
from typing import Union, Callable


class Cache:
    """A class that interact with Redis as cache
    """
    def __init__(self):
        """ Initializes the Cache object by creating a connection to Redis
        and flushing the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data in Redis and returns the key.
        Args:
            data to be stored in the cache(str, bytes, int or float)
        Return:
            str:randomly generated key used to store data in Redis"""

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Retrieves data from Redis using given key and optionally
        applies a conversion function
        Args:
            Key: The key to retrieve data from Redis
            fn: Optional conversion function to apply on retrieved data
        Returns:
            The retrieved data in [str, bytes, int, float]"""

        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Retrieves string from Redis using Key"""
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """"Retrieves integer from Redis using given key"""
        return self.get(key, int)
