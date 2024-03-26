#!/usr/bin/env python3
"""
Python module that changes all topics of a school
document based on the name"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.
    Parameters:
        mongo_collection: The pymongo collection object.
        name (str): The name of the school to update.
        topics (list of str): The list of topics approached in the school.
    Returns:
        int: The number of documents updated."""

    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )

    return result.modified_count
