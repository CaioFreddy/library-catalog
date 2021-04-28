from pymongo import MongoClient

def connect_mongo():
    mongo = MongoClient('localhost', 27017)
    banco = mongo['library-catalog']
    return banco
