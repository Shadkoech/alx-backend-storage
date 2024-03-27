#!/usr/bin/env python3
"""
Python module that uses Redis NoSQL for data storage """

import redis
import uuid
from typing import Union


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
