# import "packages" from flask
from flask import render_template
from __init__ import app
from cruddy.app_crud import app_crud
from cruddy.app_crud_api import app_crud_api
from cruddy.app_notes import app_notes
from userNotes import userNotes
from questions import questions
from answers import answers
from my_calendar import my_cal


app.register_blueprint(userNotes)
app.register_blueprint(questions)
app.register_blueprint(answers)
app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)
app.register_blueprint(app_notes)
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

@app.route('/flashcards/')
def flashcards():
    return render_template("flashcards.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
