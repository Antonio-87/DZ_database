import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://sqlpy51:sql51@localhost:5432/music_site')
connection = engine.connect()

# название и год выхода альбомов, вышедших в 2018 году;
print(connection.execute(
"""
SELECT name, release_year FROM albums
WHERE release_year = 2018;
""").fetchall())

# название и продолжительность самого длительного трека;
print(connection.execute(
"""
SELECT name, duration FROM tracks
ORDER BY duration DESC
LIMIT 1;
""").fetchall())

# название треков, продолжительность которых не менее 3,5 минуты;
print(connection.execute(
"""
SELECT name FROM tracks
WHERE duration >= 210;
""").fetchall())

# названия сборников, вышедших в период с 2018 по 2020 год включительно;
print(connection.execute(
"""
SELECT name FROM collections
WHERE release_year BETWEEN 2018 AND 2020;
""").fetchall())

# исполнители, чье имя состоит из 1 слова;
print(connection.execute(
"""
SELECT name_alias FROM performers
WHERE name_alias NOT LIKE '%% %%';
""").fetchall())

# название треков, которые содержат слово "мой"/"my".
print(connection.execute(
"""
SELECT name FROM tracks
WHERE name  iLIKE '%%my%%';
""").fetchall())