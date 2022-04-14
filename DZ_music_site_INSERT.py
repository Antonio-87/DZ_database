import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://sqlpy51:sql51@localhost:5432/music_site')
connection = engine.connect()

connection.execute(
"""
INSERT INTO genres(name)
VALUES
('Alternative'),
('Indie'),
('Rock'),
('Classic'),
('Metal');
""")

connection.execute(
"""
INSERT INTO performers(name_alias)
VALUES
('Nirvana'),
('Skillet'),
('Muse'),
('Billie Eilish'),
('Queen'),
('2CELLOS'),
('Rammstine'),
('Linkin Park');
""")

connection.execute(
"""
INSERT INTO genres_performers(genre_id, performer_id)
VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 4),
(3, 5),
(4, 6),
(5, 7),
(5, 8);
""")

connection.execute(
"""
INSERT INTO albums(name, release_year)
VALUES
('Smells Like Teen Spirit', 2021),
('Dominion', 2022),
('Simulation Theory', 2018),
('Happier Than Ever', 2021),
('Live Around The World', 2020),
('Dedicated', 2022),
('Remixes', 2020),
('One Step Closer', 2021);
""")

connection.execute(
"""
INSERT INTO performers_albums(performer_id, album_id)
VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8);
""")

connection.execute(
"""
INSERT INTO tracks(name, duration, album_id)
VALUES
('Smells Like Teen Spirit', 301, 1),
('In Bloom', 255, 1),
('Surviving The Game', 238, 2),
('Standing in the Storm', 257, 2),
('Algorithm', 245, 3),
('The Dark Side', 227, 3),
('Getting Older', 244, 4),
('I Did not Change My Number', 158, 4),
('Tear It Up', 184, 5),
('Now I am Here', 306, 5),
('Wherever I Go', 201, 6),
('bad guy', 154, 6),
('Du riechst so gut', 285, 7),
('Rammstein In The House ', 384, 7),
('One Step Closer', 141, 8);
""")

connection.execute(
"""
INSERT INTO collections(name, release_year)
VALUES
('Freedom 1', 2018),
('Freedom 2', 2020),
('Freedom 3', 2021),
('Freedom 4', 2022),
('Sammer 1', 2020),
('Spring 1', 2018),
('Spring 2', 2020),
('Spring 3', 2021);
""")

connection.execute(
"""
INSERT INTO tracks_collections(track_id, collection_id)
VALUES
(1, 3),
(1, 8),
(2, 3),
(2, 8),
(3, 4),
(4, 4),
(5, 1),
(5, 6),
(6, 1),
(6, 6),
(7, 3),
(8, 3),
(9, 2),
(9, 5),
(10, 2),
(10, 5),
(11, 4),
(12, 4),
(13, 2),
(13, 7),
(14, 2),
(14, 7),
(15, 8);
""")
