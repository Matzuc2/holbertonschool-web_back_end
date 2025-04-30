#!/usr/bin/env python3
"""
Module for providing statistics about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Access the nginx collection in the logs database
    logs_collection = client.logs.nginx

    # Count total number of log documents
    count = logs_collection.count_documents({})  # Using count_documents instead of estimated_document_count

    # Count documents for each HTTP method
    get_meth = logs_collection.count_documents({"method": "GET"})
    post_meth = logs_collection.count_documents({"method": "POST"})
    put_meth = logs_collection.count_documents({"method": "PUT"})
    patch_meth = logs_collection.count_documents({"method": "PATCH"})
    del_meth = logs_collection.count_documents({"method": "DELETE"})

    # Count documents that are GET requests to /status path
    status_path_get = logs_collection.count_documents(
        {"method": "GET", "path": "/status"})

    # Print statistics exactly as shown in the example
    print(f"{count} logs")
    print("Methods:")
    print(f"\tmethod GET: {get_meth}")
    print(f"\tmethod POST: {post_meth}")
    print(f"\tmethod PUT: {put_meth}")
    print(f"\tmethod PATCH: {patch_meth}")
    print(f"\tmethod DELETE: {del_meth}")
    print(f"{status_path_get} status check")
