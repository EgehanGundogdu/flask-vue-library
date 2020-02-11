import json
from bson import json_util
from bson.objectid import ObjectId
from application import app
from flask import jsonify, request, abort
from application import db
from datetime import datetime


@app.route('/api')
@app.route('/api/index')
def index():
    return jsonify({
        "hello": "world"
    })


@app.route('/api/addbook', methods=['POST'])
def add_book():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({
            'status': 400,
            'message': 'name is required'
        })
    data['created'] = datetime.now()
    book_id = db.books.insert_one(data).inserted_id
    return jsonify({
        'status': 201,
        'message': 'Created successfully! Check your db!',
        'object_id': str(book_id)
    })


@app.route('/api/getbook/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def get_book(book_id):
    if request.method == 'PUT':
        data = request.get_json()
        if 'status' not in data:
            return jsonify({'message': 'Bad request', 'status': 400})
        updated = db.books.update_one({
            '_id': ObjectId(book_id)
        }, {
            '$set': {
                'status': data['status']
            }
        })

        return jsonify({
            'message': 'Updated succesfully!',
            'status': 200
        })
    elif request.method == 'DELETE':
        db.books.delete_one({
            '_id': ObjectId(book_id)
        },)
        return jsonify({
            'status': 200,
            'message': 'Deleted succesfully!'
        })

    book = db.books.find_one({
        '_id': ObjectId(book_id)
    })
    book.pop('_id')
    return jsonify(book)
