from datetime import date

from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor, CKEditorField
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from wtforms import StringField, SubmitField
from wtforms.validators import URL, DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["CKEDITOR_SERVE_LOCAL"] = True
app.config["CKEDITOR_PKG_TYPE"] = "standard"
app.config["CKEDITOR_CONFIG"] = {"versionCheck": False}
Bootstrap5(app)
ckeditor = CKEditor(app)

today = date.today().strftime("%B %d, %Y")


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route("/")
def get_all_posts():
    cached_posts = db.session.execute(db.select(BlogPost)).scalars()
    posts = [post for post in cached_posts]
    return render_template("index.html", all_posts=posts)


@app.route("/<int:post_id>")
def show_post(post_id):
    requested_post = db.session.execute(
        db.select(BlogPost).where(BlogPost.id == post_id)
    ).scalar()
    return render_template("post.html", post=requested_post)


@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    new_post_form = CreatePostForm()
    if new_post_form.validate_on_submit():
        title = new_post_form.title.data
        subtitle = new_post_form.subtitle.data
        author = new_post_form.author.data
        img_url = new_post_form.img_url.data
        body = new_post_form.body.data
        new_post = BlogPost(
            title=title,
            subtitle=subtitle,
            author=author,
            img_url=img_url,
            body=body,
            date=today,
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=new_post_form)


@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.session.execute(
        db.select(BlogPost).where(BlogPost.id == post_id)
    ).scalar()
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body,
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.author = edit_form.author.data
        post.img_url = edit_form.img_url.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_id))
    return render_template("make-post.html", form=edit_form, post_exist=True)


@app.route("/delete<int:post_id>")
def delete_post(post_id):
    post_to_delete = db.session.execute(
        db.select(BlogPost).where(BlogPost.id == post_id)
    ).scalar()
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
