from dotenv import load_dotenv
from pprint import pprint
import pymongo
import os
from pymongo import MongoClient



"""
All of the below are selections from:
https://github.com/warestack/cc/blob/master/Class-2/Lab2.3-MongoDB-tutorial-with-Python.md
"""



def get_films(connection: MongoClient):
    hello = connection.MiniFilms.films
    return connection.MiniFilms.films

if __name__ == '__main__':
    load_dotenv()
    server = f"mongodb+srv://{os.getenv('MONGO_USER_ID')}:{os.getenv('MONGO_PWD')}@cluster.qz1mk.mongodb.net/?retryWrites=true&w=majority&appName=cluster"

    conn = MongoClient(server)
    # using the connection to the database we can retrieve the collection cluster
    films = get_films(conn)

    print(films)


