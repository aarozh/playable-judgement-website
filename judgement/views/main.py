"""
Judgement get and post route for main page.

URLs include:
/
"""

import flask
import judgement
import random
import string
from .helper import lobby_exists

def generate_room_code():
    """Generate a unique room code."""

    generated_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

    # check if the generated code already exists
    connection = judgement.db.get_db()
    while lobby_exists(connection, generated_code):
        generated_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    return generated_code

@judgement.app.route("/", methods=["POST", "GET"])
def main_page():
    """Main page post and get request route handling."""

    # clear the current session when routing to main page
    flask.session.clear()

    # post request if user filled out main page
    if flask.request.method == "POST":
        name = flask.request.form.get("name")
        code = flask.request.form.get("code").upper()
        join = flask.request.form.get("join", False)
        create = flask.request.form.get("create", False)

        # if the user does not enter a name, prompt the user for a name
        if not name:
            return flask.render_template('mainpage.html', error_name="Please enter a name.", code = code)
        
        # if the user does not enter a code when joining a private room, prompt the user for a code
        if join != False and not code:
            return flask.render_template('mainpage.html', error_code="Please enter a code.", name = name)

        lobby_id = code
        connection = judgement.db.get_db()

        if create != False:
            # user tries to create a new lobby
            lobby_id = generate_room_code()
            # TODO add this lobby_id to lobby table
        elif not lobby_exists(connection, code):
            # if the code the user enters is not a lobby code in the database, prompt user for a different code
            return flask.render_template('mainpage.html', error_code="Room code does not exist.", name = name)    


        # storing information in session
        # TODO subject to change
        flask.session["lobby_id"] = lobby_id
        flask.session["name"] = name


        # redirect to lobby page
        return flask.redirect(flask.url_for("lobby_page", lobby_id = lobby_id))


    return flask.render_template('mainpage.html')