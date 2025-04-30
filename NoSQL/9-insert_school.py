#!/usr/bin/env python3
"""
Module for MongoDB operations using PyMongo - insert functionality
"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a MongoDB collection based on kwargs

    Args:
        mongo_collection: The pymongo collection object
        **kwargs: Key/value pairs representing the document to insert

    Returns:
        The new document's _id
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id


if __name__ == "__main__":
    """Main entry point, executed only when run directly"""
    pass
