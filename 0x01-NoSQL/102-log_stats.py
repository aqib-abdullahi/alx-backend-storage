#!/usr/bin/env python3
"""advanced task 102
"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """top 10 ip address occurences
    """
    total_logs = mongo_collection.count_documents({})

    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in http_methods:
        count = mongo_collection.count_documents({"method": method})
        method_counts[method] = count

    status_check = mongo_collection.count_documents({"path": "/status"})

    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = list(mongo_collection.aggregate(pipeline))

    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check} status check")
    print("IPs:")
    for ip_info in top_ips:
        print(f"\t{ip_info['_id']}: {ip_info['count']}")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    log_stats(logs_collection)
