-- Select cities in california sorted by cities.id
SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'california')
ORDER BY id ASC;
