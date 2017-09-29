BEGIN;

CREATE TABLE mickeys (
	id SERIAL PRIMARY KEY,
	park_id INTEGER REFERENCES parks,
	land_id INTEGER REFERENCES lands,
	attraction_id INTEGER REFERENCES attractions,
	photo_url TEXT,
	description TEXT,
	hint TEXT
);

COMMIT;