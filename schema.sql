drop table if exists users;
drop table if exists posts;
create table users(user_id bigint unsigned auto-increment, user_username varchar(20) primary key, user_password varchar(40));
select * from users;
create table posts(post_id bigint unsigned auto-increment primary key, user_id varchar(20), post_title varchar(200), post_url varchar(200));
select * from posts;
