-- This script 
SELECT
    ts.title,
    tsg.genre_id
FROM
    tv_shows ts
JOIN
    tv_show_genres tsg ON ts.id = tsg.show_id
ORDER BY
    ts.title ASC,
    tsg.genre_id ASC;
