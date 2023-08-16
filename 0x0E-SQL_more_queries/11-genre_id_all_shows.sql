--- This script lists all shows contained
-- In the database hbtn_0d_tvshows
SELECT
  ts.title,
  tsg.genre_id
FROM
  tv_shows ts
LEFT JOIN
  tv_show_genres tsg ON ts.id = tsg.show_id
ORDER BY
  ts.title ASC,
  tsg.genre_id ASC;
