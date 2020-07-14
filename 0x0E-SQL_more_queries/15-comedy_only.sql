-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT ts.title, ge.name
FROM tv_shows ts
LEFT JOIN tv_show_genres s ON ts.id = s.show_id LEFT JOIN tv_genres ge ON s.genre_id = ge.id
ORDER BY ts.title, ge.name;
