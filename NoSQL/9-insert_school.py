import pymongo

def insert_school(mongo_collection, **kwargs):
    cursor = mongo_collection.find({})
    my_dict = kwargs
    x = mongo_collection.insert_one(my_dict)
    return x.inserted_id

