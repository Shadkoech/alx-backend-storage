#!/usr/bin/env python3
"""
Python module returning all students sorted by average score"""


def top_students(mongo_collection):
    """
    Function returning all students sorted by average score
    Parameters:
        mongo_collection: The pymongo collection object.
    Returns:
        list: list of dictionaries rep students sorted by average score.
    """

    topstudent = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return topstudent
