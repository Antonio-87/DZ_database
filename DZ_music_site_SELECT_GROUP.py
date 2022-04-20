import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://sqlpy51:sql51@localhost:5432/music_site')
connection = engine.connect()

# количество исполнителей в каждом жанре;
print(connection.execute(
"""
SELECT g.name, COUNT(p.id) pq FROM genres g
JOIN genres_performers gp ON g.id = gp.genre_id
JOIN performers p ON gp.performer_id = p.id
GROUP BY g.name
ORDER BY pq DESC;
""").fetchall())

# количество треков, вошедших в альбомы 2019-2020 годов;
print(connection.execute(
"""
SELECT COUNT(*), a.release_year FROM albums a
JOIN tracks t ON a.id = t.album_id
WHERE (a.release_year >= 2019) and (a.release_year <= 2020)
GROUP BY a.release_year;
""").fetchall())

# средняя продолжительность треков по каждому альбому;
print(connection.execute(
"""
SELECT a.name, ROUND(AVG(t.duration), 2) td FROM albums a
JOIN tracks t ON a.id = t.album_id
GROUP BY a.name
ORDER BY td;
""").fetchall())

# все исполнители, которые не выпустили альбомы в 2020 году;
print(connection.execute(
"""
SELECT p.name_alias FROM performers p
JOIN performers_albums pa ON p.id = pa.performer_id
JOIN albums a ON pa.album_id = a.id
WHERE a.release_year NOT IN (
    SELECT release_year  FROM albums
    WHERE release_year = 2020
    )
GROUP BY p.name_alias;
""").fetchall())

# названия сборников, в которых присутствует конкретный исполнитель (Nirvana);
print(connection.execute(
"""
SELECT DISTINCT c.name FROM collections c
JOIN tracks_collections tc ON c.id = tc.collection_id
JOIN tracks t ON tc.track_id = t.id
JOIN albums a ON t.album_id = a.id
JOIN performers_albums pa ON a.id = pa.album_id
JOIN performers p ON pa.performer_id = p.id
WHERE p.name_alias ILIKE '%%nirvana%%';
""").fetchall())

# название альбомов, в которых присутствуют исполнители более 1 жанра;
print(connection.execute(
"""
SELECT a.name FROM albums a
JOIN performers_albums pa ON a.id = pa.album_id
JOIN performers p ON pa.performer_id = p.id
JOIN genres_performers gp ON p.id = gp.performer_id
JOIN genres g ON gp.genre_id = g.id
GROUP BY a.name
HAVING COUNT(g.name) > 1;
""").fetchall())

# наименование треков, которые не входят в сборники;
print(connection.execute(
"""
SELECT t.name FROM tracks t
LEFT JOIN tracks_collections tc ON t.id = tc.track_id
WHERE tc.track_id is null;
""").fetchall())

# исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
print(connection.execute(
"""
SELECT p.name_alias, t.duration FROM tracks t
JOIN albums a ON t.album_id = a.id
JOIN performers_albums pa ON a.id = pa.album_id
JOIN performers p ON pa.performer_id = p.id
GROUP BY p.name_alias, t.duration
HAVING t.duration = (SELECT MIN(duration) FROM tracks)
ORDER BY p.name_alias;
""").fetchall())

# название альбомов, содержащих наименьшее количество треков.
print(connection.execute(
"""
SELECT a.name FROM albums a
JOIN tracks t ON a.id = t.album_id
WHERE t.album_id = (
    SELECT album_id FROM tracks
    GROUP BY album_id
    HAVING COUNT(id) = (
        SELECT COUNT(id) FROM tracks
        GROUP BY album_id
        ORDER BY COUNT
        LIMIT 1
        )
    )
ORDER BY a.name;
""").fetchall())
