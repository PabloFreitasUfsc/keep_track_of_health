# https://www.w3schools.com/python/python_mongodb_getstarted.asp

import pymongo

# from pymongo import collection

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

db_collection = mydb["mydatabase"]

# mylist = [
#     {"name": "Amy", "address": "Apple st 652"},
#     {"name": "Hannah", "address": "Mountain 21"},
#     {"name": "Michael", "address": "Valley 345"},
#     {"name": "Sandy", "address": "Ocean blvd 2"},
#     {"name": "Betty", "address": "Green Grass 1"},
#     {"name": "Richard", "address": "Sky st 331"},
#     {"name": "Susan", "address": "One way 98"},
#     {"name": "Vicky", "address": "Yellow Garden 2"},
#     {"name": "Ben", "address": "Park Lane 38"},
#     {"name": "William", "address": "Central st 954"},
#     {"name": "Chuck", "address": "Main Road 989"},
#     {"name": "Viola", "address": "Sideway 1633"},
# ]


# post = {"_id": "1", "name": "tim", "score": [0, 1]}

# collection.insert_one(post)
# collection.insert_many(mylist)
# dblist = myclient.list_database_names()
# if "mydatabase" in dblist:
#     print("The database exists.")

for x in db_collection.find({}, {"_id": 0}):
    print(x)
