-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT ts.title, ge.name
FROM tv_shows ts
LEFT JOIN tv_show_genres s ON ts.id = s.show_id LEFT JOIN tv_genres ge ON s.genre_id = ge.id
ORDER BY ge.name, ts.title;
