from flask import Flask, render_template,Blueprint,request
import sqlite3
import json
import requests
# Table ANSWERS with ID, QID, AUTHOR, ANSWERTEXT
answers = Blueprint("answers",__name__)

@answers.route("/addanswer/",methods=["GET","POST"])
def addanswer():
    response = requests.get("http://127.0.0.1:5000/getQuestions/")
    if request.form:
        conn = sqlite3.connect("model/data.db")
        qid= int(request.form.get("QID"))
        author = request.form.get("AUTHOR")
        answertext=request.form.get("ANSWERTEXT")
        conn.execute(f"INSERT INTO ANSWERS (QID,AUTHOR,ANSWERTEXT) VALUES ({qid},'{author}','{answertext}')")
        conn.commit()
        conn.close()
    return render_template("questions.html",questions=response.json())

@answers.route("/getAnswers/",methods=["GET","POST"])
def getAnswers():
    id=request.args.get("id")
    print(id)
    if not id:
        return "no"
    conn=sqlite3.connect("model/data.db")
    cursor = conn.execute(f"SELECT * FROM ANSWERS WHERE QID={id}")
    data = {}
    for row in cursor:
        data[row[0]] = list(row[1:])
    return json.dumps(data)


# conn = sqlite3.connect("model/data.db")
# cursor = conn.execute("SELECT * from ANSWERS")
# for row in cursor:
#     print(row)
# conn.close()
