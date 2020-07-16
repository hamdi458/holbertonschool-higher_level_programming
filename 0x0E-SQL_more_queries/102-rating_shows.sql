-- script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT tvs.title, SUM(tvsr.rate) AS rating
FROM tv_shows AS tvs JOIN tv_show_ratings AS tvsr ON tvsr.show_id = tvs.id
GROUP BY tvs.title ORDER BY rating DESC;
