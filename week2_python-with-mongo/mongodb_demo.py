from pprint import pprint
import pymongo
from pymongo import MongoClient

"""
All of the below are selections from:
https://github.com/warestack/cc/blob/master/Class-2/Lab2.3-MongoDB-tutorial-with-Python.md
"""

server = "mongodb+srv://student:1234@cluster.qz1mk.mongodb.net/?retryWrites=true&w=majority&appName=cluster"

conn = MongoClient(server)



if __name__ == '__main__':
    # using the connection to the database we can retrieve the collection cluster
    col_films = conn.MiniFilms.films

    # You do not need to create the data object in mongo
    #   The next two assignments and .insert_one() can be run and the object is created in mongoDB including the data
    col_users = conn.MiniFilms.users
    # user1 = {
    #     "user_name": "Tom Jones",
    #     "user_age": 44,
    #     "user_location": "London"
    # }
    # col_users.insert_one(user1)

    # Insert multiple users
    """    user2 = {
        "user_name": "Jane Williams",
        "user_age": 50,
        "user_location": "London"
    }

    user3 = {
        "user_name": "Kate Johnson",
        "user_age": 35,
        "user_location": "Brighton"
    }

    col_users.insert_many([user2, user3])"""
    # Bring bag everything but user_name = true, and user_location=true
    # pprint(col_users.find_one({}, {'user_name': 1, 'user_location': 1}))

    results = col_users.find().sort('user_age', -1) # sort by field desc
    for record in results:
        print(record)
    pprint(col_users.find().sort('user_age', -1).limit(1)[0]) # oldest user

    """
    Aggregations using $ as a pipeline of aggregations
    """

    agg_result = col_users.aggregate(
        [{
            "$group":
                {"_id": "$user_location",
                 "num_instances": {"$sum": 1}
                 }}
        ])

    for record in agg_result:
        print(record)

    print()

    pipeline = [
        {
            "$match": {
                "user_location": "London"
            }
        },
        {
            "$sort": {
                "user_age": pymongo.ASCENDING
            }
        },
    ]
    results = col_users.aggregate(pipeline)

    for record in results:
        print(record)


