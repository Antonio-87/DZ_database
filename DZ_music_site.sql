create table if not exists genres(
	id serial primary key,
	name varchar(40) not null
);

create table if not exists performers(
	id serial primary key,
	name varchar(40) not null,
	alias varchar(40),
	genre_id integer references genres(id)
);

create table if not exists albums(
	id serial primary key,
	name varchar(40) not null,
	release_year int check(release_year > 0),
	performer_id integer references performers(id)
);

create table if not exists tracks(
	id serial primary key,
	name varchar(40) not null,
	duration time not null,
	album_id integer references albums(id)
);
