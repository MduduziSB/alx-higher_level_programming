-- This script lists all shows without the genre Comedy
-- In the database hbtn_0d_tvshows
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
	SELECT tv_shows.id
	FROM tv_shows
	JOIN tv_show_genres tsg ON tv_shows.id = tsg.show_id
	JOIN tv_genres tg ON tg.id = tgs.genre_id
	WHERE tg.name = 'Comedy')
ORDER BY tv_shows.title ASC;
