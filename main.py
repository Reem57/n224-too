from flask import Flask, render_template
from __init__ import app
from cruddy.app_crud import app_crud
from cruddy.app_crud_api import app_crud_api

app = Flask(__name__)


app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)
app.register_blueprint(app_notes)



@app.route('/')
def index():
    return render_template("index.html")


# @app.route('/simple_calc/')
# def stub():
#     return render_template("simple_calc.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
