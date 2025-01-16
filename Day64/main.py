import os

import requests
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Float, Integer, String, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

load_dotenv()
Authorization = os.getenv("Authorization")

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-movies-collection.db"
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(500), nullable=True)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)

    def __repr__(self):
        return f"<Movie {self.title}>"

    def __lt__(self, other):
        return self.rating > other.rating


with app.app_context():
    db.create_all()


class AddForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


class EditForm(FlaskForm):
    rating = StringField(label="Your rating out of 10", validators=[DataRequired()])
    review = StringField(label="Your review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


def quicksort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        quicksort(arr, left, pi - 1)
        quicksort(arr, pi + 1, right)

    for index, movie in enumerate(arr):
        movie.ranking = index + 1


def partition(arr, left, right):
    pivot = arr[right]

    i = left - 1
    for j in range(left, right):
        if arr[j].rating >= pivot.rating:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def search_api(identificator, by_id=False, by_user=False):
    url = f"https://api.themoviedb.org/3/search/movie?query=" + identificator

    headers = {
        "accept": "application/json",
        "Authorization": Authorization,
    }

    if by_id:
        url = "https://api.themoviedb.org/3/movie/" + identificator

    if by_user:
        url = "https://api.themoviedb.org/3/account/21753872/rated/movies"

    movie_search = requests.get(url, headers=headers).json()

    return movie_search


@app.route("/")
def home():
    with app.app_context():
        existing_movies = list(db.session.execute(db.select(Movie)).scalars())

    unique_movie_list = []
    existing_movie_titles = {movie.title for movie in unique_movie_list}

    for movie in existing_movies:
        if movie.title not in existing_movie_titles:
            unique_movie_list.append(movie)
            existing_movie_titles.add(movie.title)

    quicksort(unique_movie_list, 0, len(unique_movie_list) - 1)

    return render_template("index.html", movie_list=unique_movie_list)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    title = request.args.get("title")
    edit_form = EditForm()
    if edit_form.validate_on_submit():
        new_rating = edit_form.rating.data
        new_review = edit_form.review.data
        with app.app_context():
            movie_to_update = db.session.execute(
                db.select(Movie).where(Movie.title == title)
            ).scalar()
            movie_to_update.rating = new_rating
            movie_to_update.review = new_review
            db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=edit_form)


@app.route("/delete")
def delete():
    id = request.args.get("id")
    with app.app_context():
        movie_to_delete = db.session.execute(
            db.select(Movie).where(Movie.id == id)
        ).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        title = add_form.title.data
        return render_template("select.html", movie_search=search_api(title))
    return render_template("add.html", form=add_form)


@app.route("/select", methods=["GET", "POST"])
def select():
    id = request.args.get("id")
    movie_search = search_api(str(id), by_id=True)
    with app.app_context():
        movie = db.session.execute(
            db.select(Movie).where(Movie.title == movie_search["original_title"])
        ).scalar()
        if movie:
            return redirect(url_for("home"))
        new_movie = Movie(
            ranking=None,
            title=movie_search["original_title"],
            rating=0,
            year=movie_search["release_date"][:4],
            description=movie_search["overview"],
            img_url="https://image.tmdb.org/t/p/w500/"
            + movie_search.get("poster_path"),
            review="",
        )
        db.session.add(new_movie)
        db.session.commit()
    return redirect(url_for("edit", title=movie_search["original_title"]))


@app.route("/user")
def user():
    user_movies = search_api(identificator="", by_user=True)
    for movie in user_movies["results"]:
        with app.app_context():
            exist_movie = db.session.execute(
                db.select(Movie).where(Movie.title == movie["original_title"])
            ).scalar()
            if not exist_movie:
                new_movie = Movie(
                    ranking=None,
                    title=movie["original_title"],
                    rating=movie["rating"],
                    year=movie["release_date"][:4],
                    description=movie["overview"],
                    img_url="https://image.tmdb.org/t/p/w500/"
                    + movie.get("poster_path"),
                    review="",
                )
                db.session.add(new_movie)
                db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete_all")
def delete_all():
    with app.app_context():
        db.session.execute(text("DELETE FROM movie"))
        db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
