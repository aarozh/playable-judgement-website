"""
Judgement helper file.

Functions include:
lobby_exists: returns if a lobby_id parameter already exists
"""

from . import db

def lobby_exists(code):
    """Check to make sure that a lobby code exists in the database."""

    connection = db.get_db()
    existing_code = connection.execute(
        "SELECT lobby_id "
        "FROM lobby "
        "WHERE lobby_id = (?)",
        [code]
    )
    if existing_code.fetchone() is not None:
        return True
    return False