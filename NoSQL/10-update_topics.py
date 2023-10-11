#!/usr/bin/env python3
"""function that changes all topics of a school document"""


def update_topics(mongo_collection, name, topics):
    """changes document based on the name"""
    return mongo_collection.update_many({"name": name},
                                        {"$set":{"topics": topics}})
