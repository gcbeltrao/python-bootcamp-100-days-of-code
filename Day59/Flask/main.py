from flask import Flask, render_template
import requests
import datetime as dt

BLOG_URL = "https://api.npoint.io/6e1e6892bf538acc01d4"
current_year = dt.datetime.now().year
full_date = dt.datetime.now().strftime("%B %d, %Y")

response = requests.get(BLOG_URL)
posts = response.json()

app = Flask(__name__)

@app.route('/')
def home_route():
    last_post = next(reversed(posts))
    return render_template("index.html", posts=posts, year=current_year, date=full_date, last_post=last_post)

@app.route('/posts/post<int:number>')
def get_post(number):
    for post in posts:
        if post["id"] == number:
            correct_post = post
    return render_template("post.html", year=current_year, post=correct_post)

if __name__ == "__main__":
    app.run(debug=True)
