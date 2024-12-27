def test_create_member(client):
    """
    Test the creation of a library member.
    """
    response = client.post('/members', json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json['message'] == "Member added successfully"
    assert response.json['member']['name'] == "John Doe"

def test_get_members(client):
    """
    Test fetching the list of members.
    """
    client.post('/members', json={"name": "Jane Smith", "email": "jane@example.com"})
    response = client.get('/members')
    assert response.status_code == 200
    assert len(response.json) > 0

def test_update_member(client):
    """
    Test updating a member's details.
    """
    client.post('/members', json={"name": "Alice", "email": "alice@example.com"})
    response = client.put('/members/1', json={"email": "alice_new@example.com"})
    assert response.status_code == 200
    assert response.json['member']['email'] == "alice_new@example.com"

def test_delete_member(client):
    """
    Test deleting a member.
    """
    client.post('/members', json={"name": "Bob", "email": "bob@example.com"})
    response = client.delete('/members/1')
    assert response.status_code == 200
    assert response.json['message'] == "Member deleted successfully"
