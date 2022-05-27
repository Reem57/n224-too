from flask import Flask, render_template,Blueprint,request
import sqlite3
import json
from flask_login import current_user, login_required
import requests
questions = Blueprint("questions",__name__)
# Table has keys ID, SUBJECT, SUBCAT, QUESTION,NOTES,USERNAME
# conn = sqlite3.connect("model/data.db")
# conn.execute("ALTER TABLE QUESTIONS RENAME COLUMN COLNew TO USERNAME")
# conn.commit()
# print("renamed")
# # cursor = conn.execute("SELECT * from QUESTIONS")
# # for row in cursor:
# #     print(row)
# conn.close()
@questions.route("/questions/",methods=["GET","POST"])
@login_required
def question():
    response = requests.get("http://127.0.0.1:5000/getQuestions/")
    if request.form:
        id = request.form.get("formID")
        if id=="add":
            conn = sqlite3.connect("model/data.db")
            subject = request.form.get("subject")
            question = request.form.get("question")
            note = request.form.get("note")
            subcat = request.form.get("subcat")
            user  = current_user.name
            print(user)
            if len(note) ==0 and len(subcat) == 0:
                conn.execute(f"INSERT INTO QUESTIONS (SUBJECT,QUESTION,USERNAME) VALUES ('{subject}','{question}','{user}')")
                conn.commit()
            elif len(note) == 0:
                conn.execute(f"INSERT INTO QUESTIONS (SUBJECT,SUBCAT.QUESTION,USERNAME) VALUES ('{subject}','{subcat}','{question}','{user}')")
                conn.commit()
            elif len(subcat) == 0:
                conn.execute(f"INSERT INTO QUESTIONS (SUBJECT,QUESTION,NOTES,USERNAME) VALUES ('{subject}','{question}','{note}','{user}')")
                conn.commit()
            else:
                conn.execute(f"INSERT INTO QUESTIONS (SUBJECT,SUBCAT,QUESTION,NOTES,USERNAME) VALUES ('{subject}','{subcat}','{question}','{note}','{user}')")
                conn.commit()
            conn.close()
        if id=="search":
            term = request.form.get("term")
            print(term)
            response = requests.get(f'http://127.0.0.1:5000/getQuestions?term={term}')
        if id=="delete":
            conn = sqlite3.connect("model/data.db")
            id = request.form.get("questionid")
            conn.execute(f"DELETE FROM QUESTIONS WHERE id={id}")
            conn.commit()
    return render_template("questions.html",questions=response.json())
@questions.route("/question/<int:questionID>")
@login_required
def questionPage(questionID):
    response = requests.get(f'http://127.0.0.1:5000/getQuestions?id={questionID}')
    response2 = requests.get(f'http://127.0.0.1:5000/getAnswers?id={questionID}')
    response = response.json()
    response2 = response2.json()
    return render_template("questionPage.html", question = response[list(response.keys())[0]],answers = response2)
@questions.route("/getQuestions/")
def getQuestions():
    term = request.args.get("term")
    id = request.args.get("id")
    conn = sqlite3.connect("model/data.db")
    data = {}
    if id:
        cursor1 = conn.execute(f"SELECT * FROM QUESTIONS WHERE id={id}")
        for row in cursor1:
            data[row[0]] = list(row[1:])
    elif term:
        cursor1 = conn.execute(f"SELECT * FROM QUESTIONS WHERE SUBJECT LIKE '%{term}%'")
        cursor2 = conn.execute(f"SELECT * FROM QUESTIONS WHERE SUBCAT LIKE '%{term}%'")
        cursor3 = conn.execute(f"SELECT * FROM QUESTIONS WHERE QUESTION LIKE '%{term}%'")
        cursor4 = conn.execute(f"SELECT * FROM QUESTIONS WHERE NOTES LIKE '%{term}%'")
        cursor5 = conn.execute(f"SELECT * FROM QUESTIONS WHERE USERNAME LIKE '%{term}%'")
        for row in cursor1:
            data[row[0]] = list(row[1:])
        for row in cursor2:
            data[row[0]] = list(row[1:])
        for row in cursor3:
            data[row[0]] = list(row[1:])
        for row in cursor4:
            data[row[0]] = list(row[1:])
        for row in cursor5:
            data[row[0]] = list(row[1:])
    else:
        cursor = conn.execute("SELECT * FROM QUESTIONS")
        for row in cursor:
            data[row[0]] = list(row[1:])
    return json.dumps(data)

conn = sqlite3.connect("model/data.db")
cursor = conn.execute("SELECT * from QUESTIONS")
for row in cursor:
    print(row)
conn.close()