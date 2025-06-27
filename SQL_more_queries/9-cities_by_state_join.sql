-- list all cities contained in the database hbtn_0d_usa
SELECT id, name FROM cities
WHERE cities_id = (SELECT id, name FROM cities, SELECT name FROM states)
ORDER BY id ASC;
