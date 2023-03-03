"""Judgement package initializer."""

import flask
import flask_socketio

def create_app():
    app = flask.Flask(__name__)
    app.config.from_object('judgement.config')
    socketio = flask_socketio.SocketIO(app)

    from .main import main
    from .lobby import lobby

    app.register_blueprint(main, url_prefix="/")
    app.register_blueprint(lobby, url_prefix="/")

    from . import db
    with app.app_context():
        db.init_db(app)

    from .helper import lobby_exists

    @socketio.on("connect")
    def connect(auth):
        lobby_id = flask.session.get("lobby_id")
        name = flask.session.get("name")
        if not lobby_id or not name:
            return
        if not lobby_exists(lobby_id):
            flask_socketio.leave_room(lobby_id)
            return
        
        flask_socketio.join_room(lobby_id)
        flask_socketio.send({"name": name, "message": "joined"}, to=lobby_id)

        connection = db.get_db()
        connection.execute(
            "UPDATE lobby "
            "SET player_count = player_count + 1 "
            "WHERE lobby_id = (?)",
            [lobby_id]
        )

    @socketio.on("disconnect")
    def disconnect():
        lobby_id = flask.session.get("lobby_id")
        name = flask.session.get("name")
        flask_socketio.leave_room(lobby_id)
        if lobby_exists(lobby_id):
            connection = db.get_db()
            connection.execute(
                "UPDATE lobby "
                "SET player_count = player_count - 1 "
                "WHERE lobby_id = (?)",
                [lobby_id]
            )
            player_count = connection.execute(
                "SELECT * "
                "FROM lobby "
                "WHERE lobby_id = (?) "
                "AND player_count = 0",
                [lobby_id]
            )
            if player_count.fetchone() is not None:
                connection.execute(
                    "DELETE FROM lobby "
                    "WHERE lobby_id = (?)",
                    [lobby_id]
                )
        
        flask_socketio.send({"name": name, "message": "has left"}, to=lobby_id)
        return

    return app, socketio
