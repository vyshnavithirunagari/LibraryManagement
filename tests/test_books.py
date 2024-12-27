def test_create_book(client):
    """
    Test the creation of a book.
    """
    response = client.post('/books', json={"title": "1984", "author": "George Orwell"})
    assert response.status_code == 201
    assert response.json['message'] == "Book added successfully"
    assert response.json['book']['title'] == "1984"

def test_get_books(client):
    """
    Test fetching the list of books.
    """
    client.post('/books', json={"title": "To Kill a Mockingbird", "author": "Harper Lee"})
    response = client.get('/books')
    assert response.status_code == 200
    assert len(response.json) > 0

def test_update_book(client):
    """
    Test updating a book's details.
    """
    client.post('/books', json={"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"})
    response = client.put('/books/1', json={"title": "The Greatest Gatsby"})
    assert response.status_code == 200
    assert response.json['book']['title'] == "The Greatest Gatsby"

def test_delete_book(client):
    """
    Test deleting a book.
    """
    client.post('/books', json={"title": "Moby Dick", "author": "Herman Melville"})
    response = client.delete('/books/1')
    assert response.status_code == 200
    assert response.json['message'] == "Book deleted successfully"
