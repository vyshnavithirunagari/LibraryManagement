LIBRARY MANAGEMENT SYSTEM

A simple Flask application for managing a library's books and members, featuring a RESTful API and a basic HTML front-end interface. The app uses SQLAlchemy for persistent storage and includes a basic login system.

---

## **Features**

- **Books Management:** Add, update, delete, and search for books by title or author.
- **Members Management:** Add, update, and delete library members.
- **RESTful API:** All operations are accessible via HTTP endpoints.
- **Search Functionality:** Easily search for books by title or author.
- **Automated Tests:** Includes unit tests for both books and members endpoints.
- **SQLAlchemy Integration:** Data is stored in a relational database using SQLAlchemy.
- **Basic Login System:** A login system for members using their username and password.
- **Basic UI:** A simple front-end built with HTML and CSS for interacting with the API.

---

## **Setup and Installation**

### **1. Clone the Repository**
```bash
git clone <repository_url>
cd library_management_system
```

### **2. Install Python and Pip**
Ensure Python 3.7+ is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### **3. Install Dependencies**
This project uses **Flask**, **Flask-SQLAlchemy**, and **pytest** for testing. Install them using pip:

```bash
pip install Flask Flask-SQLAlchemy pytest
```

### **4. Database Setup**
The app uses SQLAlchemy for database interaction. By default, it will use an SQLite database (`library.db`) for simplicity.

1. After installing the dependencies, initialize the database by running the application:
    ```bash
    python app.py
    ```
    The app will automatically create the `library.db` file and necessary tables on the first run.

2. If you wish to use another database (e.g., PostgreSQL or MySQL), update the `SQLALCHEMY_DATABASE_URI` in `app.py` to point to your desired database.

---

### **5. Run the Application**
To run the Flask server:
```bash
python app.py
```

### **6. Access the Application**
Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

### **7. Run the Tests**
If you want to run automated tests, first install `pytest` if you haven’t already:

```bash
pip install pytest
```

Then, run the tests:
```bash
pytest
```

---

## **API Endpoints**

### **Books Endpoints**
1. **GET /books**  
   Fetch all books or search for books by title/author using the `q` query parameter.  
   Example: `/books?q=1984`

2. **POST /books**  
   Add a new book by sending a JSON payload:
   ```json
   {
       "title": "Book Title",
       "author": "Author Name"
   }
   ```

3. **PUT /books/<book_id>**  
   Update book details using its `book_id`.

4. **DELETE /books/<book_id>**  
   Delete a book by its `book_id`.

---

### **Members Endpoints**
1. **GET /members**  
   Fetch all members.

2. **POST /members**  
   Add a new member by sending a JSON payload:
   ```json
   {
       "name": "Member Name",
       "email": "email@example.com"
   }
   ```

3. **PUT /members/<member_id>**  
   Update member details using their `member_id`.

4. **DELETE /members/<member_id>**  
   Delete a member by their `member_id`.

---

## **Design Choices**

1. **SQLAlchemy for Persistence:** 
   The app uses SQLAlchemy for database interaction and persistence. All data (books and members) are stored in an SQLite database (`library.db`), which is created automatically on the first run.

2. **Basic Authentication:**  
   A simple login system is integrated to authenticate members using their username and password. The system stores hashed passwords for added security.

3. **Separation of Concerns:**  
   Routes for API and HTML rendering are distinct to maintain clarity.

4. **Test Coverage:**  
   Automated tests ensure correctness of API functionality.

---

## **Assumptions and Limitations**

- **No Persistent Storage (Without Database):**  
  Before using the database, data was stored in memory. Now, data is persisted using SQLAlchemy in the `library.db`.

- **Basic Authentication:**  
  The login system uses basic username and password authentication. This can be extended with more robust authentication methods like JWT or OAuth if required.

---

## **Future Enhancements**
- Add more robust authentication methods such as JWT or OAuth.
- Implement advanced features such as pagination for large book lists.
- Switch to a more powerful database like PostgreSQL for production use.



