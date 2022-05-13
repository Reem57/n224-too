# import "packages" from flask
import requests
from __init__ import app
from flask import Flask, request, Blueprint, render_template
from cruddy.app_crud import app_crud
from cruddy.app_crud_api import app_crud_api
from userNotes import userNotes

app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)
app.register_blueprint(userNotes)
# connects default URL to render index.html

@app.route('/')
def index():
    return render_template("index.html")


# @app.route('/simple_calc/')
# def stub():
#     return render_template("simple_calc.html")

@app.route('/register/')
def register():
    return render_template("login_page/register.html")


@app.route('/login/')
def login():
    return render_template("login_page/login.html")

 
# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
