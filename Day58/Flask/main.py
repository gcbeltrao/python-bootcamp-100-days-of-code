from flask import Flask, render_template
import datetime as dt

app = Flask(__name__)

current_year = dt.datetime.now().year

@app.route('/')
def home_route():
    return render_template("index.html", year=current_year)

if __name__ == '__main__':
    app.run(debug=True)