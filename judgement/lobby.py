"""
Judgement get and post route for lobby page.

URLs include:
/lobby/
"""

import flask
from .helper import lobby_exists

lobby = flask.Blueprint("lobby", __name__)

@lobby.route("/lobby/<lobby_id>", methods=["POST", "GET"])
def lobby_page(lobby_id):
    """Lobby page post and get request route handling."""

    if not lobby_exists(lobby_id) or flask.session["name"] is None:
        return flask.redirect(flask.url_for("main_page"))
    
    # post request if user filled out main page
    if flask.request.method == "POST":
        name = flask.request.form.get("name")
        code = flask.request.form.get("code").upper()
        join = flask.request.form.get("join", False)
        create = flask.request.form.get("create", False)

        # redirect to lobby page
        return flask.redirect(flask.url_for("game.game_page", lobby_id = lobby_id))

    return flask.render_template('lobbypage.html', lobby_id=lobby_id)
