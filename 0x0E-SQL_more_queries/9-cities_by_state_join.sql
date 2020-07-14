-- script that lists all cities contained in the database hbtn_0d_usa.
SELECT ct.id, ct.name, st.name
FROM cities ct
JOIN states st
ON ct.state_id = st.id
ORDER BY ct.id;
