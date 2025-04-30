#!/usr/bin/env python3
"""
Module for MongoDB operations using PyMongo - search functionality
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic
    
    Args:
        mongo_collection: The pymongo collection object
        topic: Topic to search for
        
    Returns:
        List of schools that have the specified topic
    """
    cursor = mongo_collection.find({"topics": topic})
    return list(cursor)


if __name__ == "__main__":
    """Main entry point, executed only when run directly"""
    pass