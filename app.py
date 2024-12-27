from flask import Flask, request, jsonify, render_template

books = []
members = []

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/books', methods=['GET', 'POST'])
def manage_books():
    if request.method == 'POST':
        data = request.json
        new_book = {
            "book_id": len(books) + 1,
            "title": data['title'],
            "author": data['author']
        }
        books.append(new_book)
        return jsonify({"message": "Book added successfully", "book": new_book}), 201

    query = request.args.get('q', '').lower()
    filtered_books = [b for b in books if query in b['title'].lower() or query in b['author'].lower()] if query else books
    return jsonify(filtered_books), 200

@app.route('/books/<int:book_id>', methods=['PUT', 'DELETE'])
def update_or_delete_book(book_id):
    global books

    if request.method == 'PUT':
        data = request.json
        for book in books:
            if book['book_id'] == book_id:
                book.update(data)
                return jsonify({"message": "Book updated successfully", "book": book}), 200
        return jsonify({"error": "Book not found"}), 404

    if request.method == 'DELETE':
        books = [b for b in books if b['book_id'] != book_id]
        return jsonify({"message": "Book deleted successfully"}), 200

@app.route('/members', methods=['GET', 'POST'])
def manage_members():
    if request.method == 'POST':
        data = request.json
        new_member = {
            "member_id": len(members) + 1,
            "name": data['name'],
            "email": data['email']
        }
        members.append(new_member)
        return jsonify({"message": "Member added successfully", "member": new_member}), 201

    return jsonify(members), 200

@app.route('/members/<int:member_id>', methods=['PUT', 'DELETE'])
def update_or_delete_member(member_id):
    global members

    if request.method == 'PUT':
        data = request.json
        for member in members:
            if member['member_id'] == member_id:
                member.update(data)
                return jsonify({"message": "Member updated successfully", "member": member}), 200
        return jsonify({"error": "Member not found"}), 404

    if request.method == 'DELETE':
        members = [m for m in members if m['member_id'] != member_id]
        return jsonify({"message": "Member deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
