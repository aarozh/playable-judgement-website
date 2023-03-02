PRAGMA foreign_keys = ON;

INSERT INTO lobby (
	lobby_id,
    deck_id,
    deck_type,
    cards,
    modeup,
    round_start,
    cur_round,
    player_count,
    dealer
)
VALUES 
	(
        'ABCDEF',
        'a',
		'awdeorio', 
		'Andrew DeOrio',
		'awdeorio@umich.edu',
		1,
        1,
        1,
        1
    );