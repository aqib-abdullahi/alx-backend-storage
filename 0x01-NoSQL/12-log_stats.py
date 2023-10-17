#!/usr/bin/env python3
"""Nginx log stats
"""
from pymongo import MongoClient


def count_logs_with_method(mongo_collection, method):
    """counts logs with methods
    """
    return mongo_collection.count_documents({"method": method})

def count_logs_with_status_check(mongo_collection):
    """counts logs with status check
    """
    return mongo_collection.count_documents({"method": "GET", "path": "/status"})

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    total_logs = logs_collection.count_documents({})
    get_count = count_logs_with_method(logs_collection, "GET")
    post_count = count_logs_with_method(logs_collection, "POST")
    put_count = count_logs_with_method(logs_collection, "PUT")
    patch_count = count_logs_with_method(logs_collection, "PATCH")
    delete_count = count_logs_with_method(logs_collection, "DELETE")
    status_check_count = count_logs_with_status_check(logs_collection)

    print(f"{total_logs} logs")
    print("Methods:")
    print(f"\tmethod GET: {get_count}")
    print(f"\tmethod POST: {post_count}")
    print(f"\tmethod PUT: {put_count}")
    print(f"\tmethod PATCH: {patch_count}")
    print(f"\tmethod DELETE: {delete_count}")
    print(f"{status_check_count} status check")
