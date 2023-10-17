#!/usr/bin/env python3
"""function inserts new document
"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """inserts kwargs in a document in the
    mongo collection
    """
    document = {}
    for key, value in kwargs.items():
        document[key] = value

    insertion = mongo_collection.insert_one(document)
    return insertion.inserted_id
