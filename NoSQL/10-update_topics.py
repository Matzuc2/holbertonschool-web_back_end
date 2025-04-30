#!/usr/bin/env python3
"""
Module for MongoDB operations using PyMongo - update topics functionality
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name

    Args:
        mongo_collection: The pymongo collection object
        name: The school name to update
        topics: List of topics to set for the school

    Returns:
        None
    """
    query_filter = {'name': name}
    update_operation = {'$set': {'topics': topics}}
    mongo_collection.update_many(query_filter, update_operation)


if __name__ == "__main__":
    """Main entry point, executed only when run directly"""
    pass
