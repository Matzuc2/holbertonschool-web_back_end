#!/usr/bin/env python3
"""
Module for MongoDB log stats
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    total_logs = logs_collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in methods:
        method_counts[method] = logs_collection.count_documents(
            {"method": method})
    status_check_count = logs_collection.count_documents({"path": "/status"})
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        if method_counts[method] > 0:
            print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_check_count} status check")
