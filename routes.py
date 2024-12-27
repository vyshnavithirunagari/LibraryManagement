from flask import Flask, request, jsonify
from models import books, members, Book, Member
from utils import paginate, verify_token

app = Flask(__name__)


@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    book = Book(book_id=len(books) + 1, title=data['title'], author=data['author'])
    books.append(book.__dict__)
    return jsonify({"message": "Book added successfully", "book": book.__dict__}), 201


@app.route('/books', methods=['GET'])
def get_books():
    query = request.args.get('q')
    page = int(request.args.get('page', 1))
    if query:
        filtered_books = [b for b in books if query.lower() in b['title'].lower() or query.lower() in b['author'].lower()]
    else:
        filtered_books = books
    return jsonify(paginate(filtered_books, page, 5)), 200


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    for book in books:
        if book['book_id'] == book_id:
            book.update(data)
            return jsonify({"message": "Book updated successfully", "book": book}), 200
    return jsonify({"error": "Book not found"}), 404


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['book_id'] != book_id]
    return jsonify({"message": "Book deleted successfully"}), 200


