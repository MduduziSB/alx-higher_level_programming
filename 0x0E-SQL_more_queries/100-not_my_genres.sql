-- This script list all genres not linked to the show Dexter
SELECT g.name
FROM tv_genres g
WHERE g.id NOT IN (
    SELECT s.genre_id
    FROM tv_show_genres s
    JOIN tv_shows t ON s.show_id = t.id
    WHERE t.title = 'Dexter'
)
ORDER BY g.name ASC;
