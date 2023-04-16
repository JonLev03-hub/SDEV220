from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String)
    publisher = db.Column(db.String)

with app.app_context():
    db.create_all()

    def __repr__(self):
        return f"{self.book_name}, by {self.author}"


@app.route('/')
def index():
    return 'Welcome to the book api thing.'


@app.route('/books')
def get_books():
    books = Book.query.all()
    book_list = []
    for book in books:
        book_list.append({
            "id": book.id,
            "book_name": book.book_name,
            "author": book.author,
            "publisher": book.publisher
        })
    return book_list

@app.route("/books/<int:id>",methods = ["GET"])
def get_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "Book has not been found"}
    return {
            "id": book.id,
            "book_name": book.book_name,
            "author": book.author,
            "publisher": book.publisher
        }
    
@app.route('/books/add', methods = ["POST"])
def create_book():
    book = Book(
        id = request.json["id"],
        book_name = request.json["book_name"],
        author = request.json["author"],
        publisher = request.json["publisher"],
    )
    db.session.add(book)
    db.session.commit()
    return "Book was created successfully"

@app.route('/books/remove/<int:id>', methods = ["DELETE"])
def remove_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "Book has not been found"}
    db.session.delete(book)
    db.session.commit()
    return "Book was removed successfully"

@app.route('/books/update/<int:id>', methods = ["PUT"])
def update_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "Book has not been found"}
    book.book_name = request.json.get("book_name", book.book_name)
    book.author = request.json.get("author", book.author)
    book.publisher = request.json.get("publisher", book.publisher)
    db.session.commit()
    return "Book was updated successfully"