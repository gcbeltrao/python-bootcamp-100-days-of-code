from flask import Flask, render_template
import requests
import datetime as dt

BLOG_URL = "https://api.npoint.io/2f1c23beb632d5f36d7d"
current_year = dt.datetime.now().year

response = requests.get(BLOG_URL)
posts = response.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=posts, year=current_year)

@app.route('/posts/post<int:number>')
def get_post(number):
    for post in posts:
        if post["id"] == number:
            correct_post = post
    return render_template("post.html", year=current_year, post=correct_post)

if __name__ == "__main__":
    app.run(debug=True)
