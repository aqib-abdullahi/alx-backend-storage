#!/usr/bin/env python3
"""update_topics moule
"""


def update_topics(mongo_collection, name, topics):
    """updates document with topics
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
