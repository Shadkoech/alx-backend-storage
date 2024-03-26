#!/usr/bin/env python3
"""
Python module that lists all documents in a collection"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection."""

    return [doc for doc in mongo_collection.find()]
