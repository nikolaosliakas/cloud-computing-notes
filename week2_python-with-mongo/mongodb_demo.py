from pymongo import MongoClient

server = "mongodb+srv://student:1234@cluster.qz1mk.mongodb.net/?retryWrites=true&w=majority&appName=cluster"

conn = MongoClient(server)

if __name__ == '__main__':
    # using the connection to the database we can retrieve the collection cluster
    col_films = conn.MiniFilms.films
    print(col_films.find_one())