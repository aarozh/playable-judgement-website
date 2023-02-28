"""Judgement database."""

import sqlite3
import flask
import judgement


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value) for idx, value in enumerate(row))


def get_db():
    """Open a new database connection."""

    if 'db' not in flask.g:
        db_filename = judgement.app.config['DATABASE_FILENAME']
        flask.g.db = sqlite3.connect(str(db_filename))
        flask.g.db.row_factory = make_dicts

        flask.g.sqlite_db.execute("PRAGMA foreign_keys = ON")

    return flask.g.db

@judgement.app.teardown_appcontext
def close_db(e=None):
    """Close the database connection at the end of a request."""
    db = flask.g.pop('db', None)

    if db is not None: 
        # Mybe need db.commit() late depending on implementation
        db.close()
