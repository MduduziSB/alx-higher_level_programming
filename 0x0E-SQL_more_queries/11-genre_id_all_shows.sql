--- This script lists all shows contained
-- In the database hbtn_0d_tvshows
SELECT
  ts.title,
  IFNULL(GROUP_CONCAT(tsg.genre_id ORDER BY tsg.genre_id ASC), 'NULL') AS genre_ids
FROM
  tv_shows ts
LEFT JOIN
  tv_show_genres tsg ON ts.id = tsg.show_id
GROUP BY
  ts.id, ts.title
ORDER BY
  ts.title ASC, genre_ids;
