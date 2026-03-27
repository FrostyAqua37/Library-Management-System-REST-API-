from flask import Flask
from flask_restful import Api, Resource, reqparse, fields
from models import Book, Author, User, Records
from extensions import db
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)