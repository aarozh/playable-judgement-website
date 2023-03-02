"""
Judgement helper file.

Functions include:
lobby_exists: returns if a lobby_id parameter already exists
"""

def lobby_exists(connection, code):
    """Check to make sure that a lobby code exists in the database."""

    existing_code = connection.execute(
        "SELECT lobby_id "
        "FROM lobby "
        "WHERE lobby_id = (?)",
        [code]
    )
    if existing_code.fetchone() is not None:
        return True
    return False