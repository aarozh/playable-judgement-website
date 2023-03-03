"""Judgement package initializer."""

import flask
# import flask_socketio

def create_app():
    app = flask.Flask(__name__)
    app.config.from_object('judgement.config')
    # socketio = flask_socketio.SocketIO(app)
    # socketio.run(app)

    from .main import main
    from .lobby import lobby

    app.register_blueprint(main, url_prefix="/")
    app.register_blueprint(lobby, url_prefix="/")

    from . import db
    with app.app_context():
        db.init_db(app)

    # @socketio.on("connect")
    # def connect(auth):
    #     lobby_id = flask.session.get("lobby_id")
    #     name = flask.session.get("name")
    #     if not lobby_id or not name:
    #         return
    #     if not judgement.views.lobby_exists(lobby_id):
    #         flask_socketio.leave_room(lobby_id)
    #         return
        
    #     flask_socketio.join_room(lobby_id)
    #     flask_socketio.send({"name": name, "message": "joined"}, to=lobby_id)
    #     # TODO add player to database

    # @socketio.on("disconnect")
    # def disconnect():
    #     lobby_id = flask.session.get("lobby_id")
    #     name = flask.session.get("name")
    #     flask_socketio.leave_room(lobby_id)
    #     if judgement.views.lobby_exists(lobby_id):
    #         # TODO remove player from lobby
    #         # TODO if there are no more players in the lobby, delete the lobby
    #         return
        
    #     flask_socketio.send({"name": name, "message": "has left"}, to=lobby_id)
    #     return

    return app
