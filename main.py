# import "packages" from flask
from flask import Flask, render_template
import requests
from userNotes import userNotes
from questions import questions
from answers import answers
from my_calendar import my_cal

# create a Flask instance
app = Flask(__name__)

app.register_blueprint(userNotes)
app.register_blueprint(questions)
app.register_blueprint(answers)
app.register_blueprint(my_cal)
# connects default URL to render index.html


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")


@app.route('/simple_calc/')
def simple_calc():
    return render_template("simple_calc.html")

@app.route('/stoich_calc/')
def stoich_calc():
    return render_template("stoich_calc.html")

@app.route('/graph_calc/')
def graph_calc():
    return render_template("graph_calc.html")

@app.route('/pixel_art/')
def pixel_art():
    return render_template("pixel_art.html")

@app.route('/spell_checker/')
def spell_checker():
    return render_template("spell_checker.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
