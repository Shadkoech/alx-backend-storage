#!/usr/bin/env python3
"""
Python module that inserts new document in a collection
based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection based on keyword arguments.
    Returns:
        ObjectId: The _id of the newly inserted document."""

    return mongo_collection.insert_one(kwargs).inserted_id
