from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:

            load_dotenv()
            MY_EMAIL = os.getenv("MY_EMAIL")
            PASSWORD = os.getenv("PASSWORD")

            subject = "Contact me!"
            body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            msg = f"Subject:{subject}\n\n{body}"

            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=msg.encode("utf-8"))
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
