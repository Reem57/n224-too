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


# @app.route('/stub/')
# def stub():
#     return render_template("stub.html")

@app.route('/simple_calc/')
def simple_calc():
    return render_template("simple_calc.html")

 
# runs the application on the development server
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0",port=8080)