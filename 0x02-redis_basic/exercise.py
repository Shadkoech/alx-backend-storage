#!/usr/bin/env python3
"""
Python module that uses Redis NoSQL for data storage """

import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """Decorator that counts the number of times a method of the
    Cache class is called"""
    key = method.__qualname__  # Get the qualified name of the method

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ the wrapper functions """
        # Increment the count for the method
        self._redis.incr(key)
        # Call the original method and return its result
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store history of inputs and outputs for particular
    function
    Args:
        method: The function to be decorated"""
    input_list = method.__qualname__ + ":inputs"
    output_list = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args) -> bytes:
        """wrapper function for hist of inputs and outputs"""
        input = str(args)
        self._redis.rpush(input_list, input)
        output = method(self, *args)
        self._redis.rpush(output_list, output)
        return output
    return wrapper


def replay(method: Callable) -> None:
    """function replaying history of a function"""
    # Establish a connection to Redis
    cache = redis.Redis()
    name = method.__qualname__  # Extract qualified function name
    # Retrieve the number of times the function was called
    calls = cache.get(name).decode("utf-8")
    # Print the function name and the number of calls
    print(f"{name} was called {calls} times:")

    # Retrieve the input and output lists from Redis
    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)

    # Iterate through the inputs and outputs and print them
    for i, out in zip(inputs, outputs):
        print("{}(*{}) -> {}"
              .format(name, i.decode('utf-8'), out.decode('utf-8')))


class Cache:
    """A class that interact with Redis as cache
    """
    def __init__(self):
        """ Initializes the Cache object by creating a connection to Redis
        and flushing the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
