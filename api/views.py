from .controllers import get_books, post_books, delete_books
from flask import Blueprint, request, jsonify
import json

bp = Blueprint("views_library-cataliog", __name__)


@bp.route("/books", methods=["GET"])
def get():
    args = dict(request.args)
    data = get_books(args)
    return jsonify(data)


@bp.route("/books", methods=["POST"])
def post():
    body = dict(request.json)
    data = post_books(body)
    return json.dumps(data, default=str)


@bp.route("/books", methods=["DELETE"])
def delete():
    args = dict(request.args)
    data = delete_books(args)
    return json.dumps(data, default=str)
