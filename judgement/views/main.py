"""
Judgement get and post route for main page.

URLs include:
/
"""

import flask
import judgement
from flask import Flask
from flask import render_template
import random
import string

def code_exists(code):
    connection = judgement.model.get_db()
    existing_code = connection.execute(
        "SELECT lobby_id"
        "FROM lobby"
        "WHERE lobby_id = ?",
        (code)
    )
    if existing_code.fetchone() is not None:
        return True
    return False

def generate_room_code():
    # check if this code is already created
    generated_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    while code_exists(generated_code):
        generated_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    return generated_code

@judgement.app.route("/", methods=["POST", "GET"])
def main_page():
    flask.session.clear()
    if flask.request.method == "POST":
        name = flask.request.form.get("name")
        code = flask.request.form.get("code")
        join = flask.request.form.get("join", False)
        create = flask.request.form.get("create", False)

        if not name:
            return render_template('mainpage.html', error_name="Please enter a name.", code = code)
        
        if join != False and not code:
            return render_template('mainpage.html', error_code="Please enter a code.", name = name)

        room = code
        if create != False:
            room = generate_room_code()
        elif not code_exists(code):
            return render_template('mainpage.html', error_code="Room code does not exist.", name = name)    

        flask.session["room"] = room
        flask.session["name"] = name
        return flask.redirect(flask.url_for("lobby"))


    return render_template('mainpage.html')