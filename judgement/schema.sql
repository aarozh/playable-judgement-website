PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS lobby;
DROP TABLE IF EXISTS players;

CREATE TABLE lobby(
  lobby_id INTEGER,
  deck_id VARCHAR(20) NOT NULL,
  deck_type VARCHAR(10) NOT NULL,
  cards VARCHAR(10) NOT NULL,
  modeup VARCHAR(10) NOT NULL,
  round_start INTEGER NOT NULL,
  cur_round INTEGER NOT NULL,
  player_count INTEGER NOT NULL,
  dealer INTEGER NOT NULL,
  PRIMARY KEY (lobby_id)
);

CREATE TABLE players(
  lobby_id INTEGER NOT NULL,
  player_id INTEGER PRIMARY KEY AUTOINCREMENT,
  pile_name VARCHAR(20) NOT NULL,
  total_points INTEGER NOT NULL,
  round_guess INTEGER NOT NULL,
  round_points INTEGER NOT NULL,
  FOREIGN KEY (lobby_id) REFERENCES lobby(lobby_id) ON DELETE CASCADE
);