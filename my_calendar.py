from flask import Flask, render_template, Blueprint

my_cal = Blueprint('my_cal', __name__)


events = [
    {
        'todo' : 'Cyberborn Book Drive Begins',
        'date' : '2022-05-23',
    },
    {
        'todo' : 'Cyberborn Book Drive Ends',
        'date' : '2022-06-03',
    },
]


@my_cal.route("/my_calendar/",methods=["GET","POST"])
def my_calendar():
    print("go to calendar")
    return render_template('my_calendar/calendar.html', events = events)