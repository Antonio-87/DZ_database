create table if not exists genres(
	id serial primary key,
	name varchar(40) not null
);

create table if not exists performers(
	id serial primary key,
	name_alias varchar(40) not null,
);

create table if not exists genres_performers(
	id serial primary key,
	genre_id integer not null references genres(id),
	performer_id integer not null references performers(id)
);

create table if not exists albums(
	id serial primary key,
	name varchar(40) not null,
	release_year int check(release_year > 0)
);

create table if not exists performers_albums(
	id serial primary key,
	performer_id integer not null references performers(id),
	album_id integer not null references albums(id)
);

create table if not exists tracks(
	id serial primary key,
	name varchar(40) not null,
	duration integer not null,
	album_id integer not null references albums(id)
);

create table if not exists collections(
	id serial primary key,
	name varchar(40) not null,
	release_year int check(release_year > 0)
);

create table if not exists tracks_collections(
	id serial primary key,
	track_id integer not null references tracks(id),
	collection_id integer not null references collections(id)
);