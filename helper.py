from functools import wraps

from flask import redirect, render_template, session

import time
import datetime


def apology(message, code):
    return render_template("apology.html", text = message, code = code)


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def timer(m):
    total_seconds = m * 60
    while total_seconds > 0:
        time_left = datetime.timedelta(seconds = total_seconds)
        print(time_left, end = "/r")
        time.sleep(1)
        total_seconds -= 1
    print("time's up")
