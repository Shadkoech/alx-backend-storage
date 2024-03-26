#!/usr/bin/env python3
"""
Python module that returns the list of school
having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """
    function listing schools having a specific topic.
    Parameters:
        mongo_collection: The pymongo collection object.
        topic (str): The topic searched.
    Returns:
        list: list dictionaries rep school docs containing specified topic.
    """

    school_list = mongo_collection.find({"topics": topic})
    return school_list
