-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT tvs.title
FROM tv_shows AS tvs
WHERE id NOT IN (SELECT tvsg.show_id FROM tv_show_genres AS tvsg JOIN
tv_genres AS tvg ON tvg.id = tvsg.genre_id WHERE tvg.name = 'Comedy')
GROUP BY title ORDER BY title;
