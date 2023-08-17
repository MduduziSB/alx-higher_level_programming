-- This script lists all genres in the database
-- hbtn_0d_tvshows_rate by their rating
SELECT tg.name, SUM(tr.rate) AS rating
FROM tv_genres tg
LEFT JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
LEFT JOIN tv_show_ratings tr ON tsg.show_id = tr.show_id
GROUP BY tg.id, tg.name
ORDER BY rating DESC;
