#!/usr/bin/env python3
"""tassk 11 return schools with such topics
"""


def schools_by_topic(mongo_collection, topic):
    """returns list of school that has topic that
    matches topic
    """
    schools = mongo_collection.find(
        {"topics": topic}
    )
    return list(schools)
