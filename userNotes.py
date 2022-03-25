from flask import Flask, render_template,Blueprint,request
import sqlite3
import json
import requests
userNotes = Blueprint("userNotes",__name__)
# table is called NOTES
# columns: subject,unit,ap,note
@userNotes.route('/notes/',methods=["GET","POST"])
def notes():
    if request.form:
        subject = (request.form.get("subject"))
        unit = (request.form.get("unit")) if request.form.get("unit") != '' else None
        ap = (request.form.get("ap")) if request.form.get("ap") != '' else None
        note = (request.form.get("note"))
        conn = sqlite3.connect("model/data.db")
        conn.execute(f"INSERT INTO NOTES (subject,unit,ap,note) VALUES ('{subject}','{unit}','{ap}','{note}')")
        conn.commit()
        conn.close()
        print([subject,unit,ap,note])
    response = requests.get('http://127.0.0.1:5000/getNotes/').json()
    return render_template("notes.html",data =response)

@userNotes.route("/getNotes/")
def getNotes():
    conn = sqlite3.connect("model/data.db")
    cursor = conn.execute("SELECT * FROM NOTES")
    data = {}
    for row in cursor:
        data[row[0]] = list(row[1:])
    return json.dumps(data)