"""Judgement database."""

import sqlite3
import flask


def make_dicts(cursor, row):
    """Converts the tuple input type to dictionary to store in the database."""

    return dict((cursor.description[idx][0], value) for idx, value in enumerate(row))


def get_db():
    """Open a new database connection."""

    if 'db' not in flask.g:
        db_filename = flask.current_app.config['DATABASE_FILENAME']
        flask.g.db = sqlite3.connect(str(db_filename))
        flask.g.db.row_factory = make_dicts

        flask.g.db.execute("PRAGMA foreign_keys = ON")

    return flask.g.db

def close_db(e=None):
    """Close the database connection at the end of a request."""

    db = flask.g.pop('db', None)

    if db is not None: 
        # Mybe need db.commit() late depending on implementation
        db.close()

def init_db(app):
    """
    Initalizes the database.
    Creates tables by reading sql/schema.sql.
    Inserts values into table by reading sql/data.sql.
    """
    
    app.teardown_appcontext(close_db)
    db = get_db()

    with flask.current_app.open_resource('sql/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
    with flask.current_app.open_resource('sql/data.sql') as f:
        db.executescript(f.read().decode('utf8'))
