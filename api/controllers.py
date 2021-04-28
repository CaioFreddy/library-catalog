from .models import Book, Author

from .mongo import connect_mongo


def get_books(args):
    mongo = connect_mongo()
    collection = mongo["books"]
    items = collection.find(args)
    return [Book(**item).dict() for item in items if items]


def post_books(body):
    data = Book(**body).dict()
    mongo = connect_mongo()
    collection = mongo["books"]
    res = collection.update(data, data, upsert=True)
    return res


def delete_books(args):
    mongo = connect_mongo()
    collection = mongo["books"]
    res = collection.delete_many(args)
    return 'Sucess'
