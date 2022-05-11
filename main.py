# import "packages" from flask
from flask import Flask, render_template
import requests
from userNotes import userNotes

# create a Flask instance
app = Flask(__name__)

app.register_blueprint(userNotes)
# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")

#test


@app.route('/stub/')
def stub():
    return render_template("stub.html")

# @app.route('/simple_calc/')
# def stub():
#     return render_template("simple_calc.html")

 
# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
