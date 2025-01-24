from flask import Flask
import random

app = Flask(__name__)

correct_number = random.randint(0, 9)

@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>"

@app.route('/<int:number>')
def right_number(number):
    if number == correct_number:
        return "<h1 style=color: green'>You found me!</h1> \
            <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif number < correct_number:
        return "<h1 style=color: red'>Too low, try again!</h1> \
            <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h1 style=color: purple'>Too high, try again! </h1> \
            <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    
if __name__ == '__main__':
    app.run(debug=True)