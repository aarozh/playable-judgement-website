"""
Judgement get and post route for lobby page.

URLs include:
/lobby/
"""

import flask
import flask_socketio
import judgement
from .helper import lobby_exists

@judgement.app.route("/lobby/<lobby_id>", methods=["POST", "GET"])
def lobby_page(lobby_id):
    """Lobby page post and get request route handling."""

    # if not lobby_exists(lobby_id) or flask.session["name"] is None:
    #     return flask.redirect(flask.url_for("main_page"))

    return flask.render_template('lobbypage.html', lobby_id=lobby_id)

# @flask.socketio.on("connect")
# def connect(auth):
#     lobby_id = flask.session.get("lobby_id")
#     name = flask.session.get("name")
#     if not lobby_id or not name:
#         return
#     if not lobby_exists(lobby_id):
#         flask_socketio.leave_room(lobby_id)
#         return
    
#     flask_socketio.join_room(lobby_id)
#     flask_socketio.send({"name": name, "message": "joined"}, to=lobby_id)
#     # TODO add player to database

# @flask.socketio.on("disconnect")
# def disconnect():
#     lobby_id = flask.session.get("lobby_id")
#     name = flask.session.get("name")
#     flask_socketio.leave_room(lobby_id)
#     if lobby_exists(lobby_id):
#         # TODO remove player from lobby
#         # TODO if there are no more players in the lobby, delete the lobby
#         return
#     return
