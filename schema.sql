drop table if exists users, posts;
create table 'users' {
	'user_id' bigint unsigned not null autoincrement,
	'user_username' varchar(20),
	'user_password' varchar(40),
	primary key ('user_id')
