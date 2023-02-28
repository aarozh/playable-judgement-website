"""Judgement package initializer."""

import flask
import flask_socketio

app = flask.Flask(__name__)

app.config.from_object('judgement.config')

app.config.from_envvar('JUDGEMENT_SETTINGS', silent = True)

socketio = flask_socketio.SocketIO(app)

if __name__ == "__main__": #__main__ should be change maybe?
    socketio.run(app)

import judgement.db
import judgement.views
