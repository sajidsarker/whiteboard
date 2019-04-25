DROP TABLE IF EXISTS users;

DROP TABLE IF EXISTS posts;

CREATE TABLE users(
		user_id SERIAL,
		user_username VARCHAR(20) PRIMARY KEY,
		user_password VARCHAR(40),
		user_datetime TIMESTAMP
	     );

SELECT * FROM users;

CREATE TABLE posts(
		post_id SERIAL PRIMARY KEY,
		user_id UNSIGNED BIGINT,
		user_username VARCHAR(20),
		post_title MEDIUMTEXT,
		post_url MEDIUMTEXT,
		post_body LONGTEXT,
		post_datetime TIMESTAMP
	     );

SELECT * FROM posts;
