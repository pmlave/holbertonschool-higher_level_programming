-- List all cities in the database by id and state
SELECT cities.id, cities.name, states.name FROM states
INNER JOIN cities ON cities.state_id=states.id ORDER BY cities.id ASC;
