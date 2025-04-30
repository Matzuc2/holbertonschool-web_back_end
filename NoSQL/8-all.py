#!/usr/bin/env python3
"""
Module for MongoDB operations using PyMongo
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection
    
    Args:
        mongo_collection: The pymongo collection object
        
    Returns:
        List of all documents in collection, or empty list if no documents
    """
    cursor = mongo_collection.find({})
    result = [document for document in cursor]
    return result


if __name__ == "__main__":
    """Main entry point, executed only when run directly"""
    pass