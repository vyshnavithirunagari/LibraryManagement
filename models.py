from typing import List, Dict

books: List[Dict] = []
members: List[Dict] = []

class Book:
    def __init__(self, book_id: int, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author

class Member:
    def __init__(self, member_id: int, name: str, email: str):
        self.member_id = member_id
        self.name = name
        self.email = email
