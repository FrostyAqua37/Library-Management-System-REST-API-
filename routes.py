from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from models import Book
from extensions import db
from main import api, app

book_insert_param = reqparse.RequestParser()

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

class BookAction(Resource):
    @marshal_with(book_fields) 
    def get(self, book_id):
        result = Book.query.filter_by(id=book_id).first()
        if not result:
            abort(404, message='Could not find book with given ID.')
        return result, type(result)

    @marshal_with(book_fields)
    def put(self, book_id):
        args = book_insert_param.parse_args()
        result = Book.query.filter_by(id=book_id).first()
        if result:
            abort(409, message='Book with given ID already exists.')

        book = Book(
            id=book_id,
            title=args['title'],
            isbn=args['isbn'],
            description=args['description'],
            release_year=args['release_year'],
            author=args['author'],
            author_id=args['author_id'],
            themese=args['themes'],
            status=args['status'],
        )

        db.session.add(book)
        db.session.commit()
        return book, 201


api.add_resource(BookAction, '/book/<int:book_id>')

if __name__ == '__main__':
    app.run(debug=True)




