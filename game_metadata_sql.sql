UPDATE games
SET genre = lower(genre),
	theme = lower(theme),
	play_mode = lower(play_mode),
	developer = lower(developer);

UPDATE games
SET genre = replace(genre, '|',','),
	theme = replace(theme, '|',','),
	play_mode = replace(play_mode, '|',','),
	developer = replace(developer, '|',',');

