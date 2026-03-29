import requests
from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from requests.models import Response
from models import Book
from extensions import db

book_insert_param = reqparse.RequestParser()
book_insert_param.add_argument('title', type=str, help='Title of book is required.', required=True)
book_insert_param.add_argument('isbn', type=int, help='Title of book is required.', required=True)
book_insert_param.add_argument('description', type=str, help='Title of book is required.', required=True)
book_insert_param.add_argument('release_year', type=int, help='Title of book is required.', required=True)
book_insert_param.add_argument('author', type=str, help='Title of book is required.', required=True)
book_insert_param.add_argument('author_id', type=int, help='Title of book is required.', required=True)
book_insert_param.add_argument('themes', type=str, help='Title of book is required.', required=True)
book_insert_param.add_argument('status', type=str, help='Title of book is required.', required=True)

book_update_param = reqparse.RequestParser()
book_update_param.add_argument('title', type=str, help='Title of book is required.')
book_update_param.add_argument('isbn', type=int, help='Title of book is required.')
book_update_param.add_argument('description', type=str, help='Title of book is required.')
book_update_param.add_argument('release_year', type=int, help='Title of book is required')
book_update_param.add_argument('author', type=str, help='Title of book is required.')
book_update_param.add_argument('author_id', type=int, help='Title of book is required.')
book_update_param.add_argument('themes', type=str, help='Title of book is required.')
book_update_param.add_argument('status', type=str, help='Title of book is required.')

book_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'isbn': fields.String,
    'description': fields.String,
    'release_year': fields.Integer,
    'author': fields.String,
    'author_id': fields.Integer,
    'themes': fields.String,
    'status': fields.String,
}

def check_record(book_id:int) -> Response | bool:
    result = Book.query.filter_by(id=book_id).first()
    return result if result else False

class BookAction(Resource):
    @marshal_with(book_fields) 
    def get(self, book_id) -> Response:
        result = check_record(book_id)
        if not result:
            abort(404, message='Could not find book with given ID.')
        return result

    @marshal_with(book_fields)
    def put(self, book_id) -> str:
        if check_record(book_id):
            abort(409, message='Book with given ID already exists.')

        args = book_insert_param.parse_args()

        book = Book(
            id=book_id,
            title=args['title'],
            isbn=args['isbn'],
            description=args['description'],
            release_year=args['release_year'],
            author=args['author'],
            author_id=args['author_id'],
            themes=args['themes'],
            status=args['status'],
        )

        db.session.add(book)
        db.session.commit()
        return 'Book record successfully inserted.'

    @marshal_with(book_fields)
    def patch(self, book_id) -> dict[str, str]:
        args = book_update_param.parse_args()
        result = check_record(book_id)

        if not result:
            abort(404, message='Book record not within database, cannot update.')

        db.session.commit()
        return {'message': 'Book record successfully updated.'}

    def delete(self, book_id:int) -> str:
        if not check_record(book_id):
            abort(404, message='Book record not within database, cannot delete.')

        db.session.query(Book).filter(Book.id==book_id).delete()
        db.session.commit()
        return f'Book record successfully deleted.\n Code; {204}'