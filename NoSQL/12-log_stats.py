#!/usr/bin/env python3
"""
Module for providing statistics about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    count = logs_collection.estimated_document_count()
    get_meth = logs_collection.count_documents({"method": "GET"})
    post_meth = logs_collection.count_documents({"method": "POST"})
    put_meth = logs_collection.count_documents({"method": "PUT"})
    patch_meth = logs_collection.count_documents({"method": "PATCH"})
    del_meth = logs_collection.count_documents({"method": "DELETE"})
    status_path_get = logs_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f'{count} logs')
    print("Methods:")
    print('\tmethod GET: {}'.format(get_meth))
    print('\tmethod POST: {}'.format(post_meth))
    print('\tmethod PUT: {}'.format(put_meth))
    print('\tmethod PATCH: {}'.format(patch_meth))
    print('\tmethod DELETE: {}'.format(del_meth))
    print('{} status check'.format(status_path_get))
