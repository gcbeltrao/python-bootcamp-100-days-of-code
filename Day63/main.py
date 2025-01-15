from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()

cached_books = []


@app.route('/')
def home():
    with app.app_context():
        if not cached_books:
            new_books = db.session.execute(db.select(Book)).scalars()
        if cached_books:
            new_books = db.session.execute(db.select(Book).where(Book.id > cached_books[-1].id)).scalars()
        for book in new_books:
            cached_books.append(book)
    return render_template("index.html", list=cached_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        book_title = request.form['title']
        book_author = request.form['author']
        book_rating = request.form['rating']
        with app.app_context():
            new_book = Book(title=book_title, author=book_author, rating=book_rating)
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")  


if __name__ == "__main__":
    app.run(debug=True)