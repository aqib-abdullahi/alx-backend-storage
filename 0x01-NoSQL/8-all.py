#!/usr/bin/env python3
"""mongodb script using pymongo
"""


def list_all(mongo_collection):
    """lists all documents in mongo_colection
    """
    return mongo_collection.find()
