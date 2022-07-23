import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

staging_events_table_create= ("""
CREATE TABLE staging_events(
    event_id INT,
    artist_name TEXT,
    auth TEXT,
    user_first_name TEXT,
    user_gender VARCHAR(1),
    item_in_session INT,
    user_last_name TEXT,
    song_length FLOAT, 
    user_level TEXT,
    location TEXT,
    method TEXT,
    page TEXT,
    registration FLOAT,
    session_id INT,
    song_title TEXT,
    status INT, 
    ts BIGINT,
    user_agent TEXT,
    user_id INT,
    PRIMARY KEY (event_id))
""")

staging_songs_table_create = ("""
CREATE TABLE staging_songs(
    song_id VARCHAR(50) NOT NULL,
    num_songs INT,
    artist_id INT,
    artist_latitude DECIMAL(8,6),
    artist_longitude DECIMAL(9,6),
    artist_location TEXT,
    artist_name TEXT,
    title TEXT,
    duration FLOAT,
    year INT,
    PRIMARY KEY (song_id))
""")

songplay_table_create = ("""
CREATE TABLE songplays(
    songplay_id INT, 
    start_time TIMESTAMP, 
    user_id INT, 
    level TEXT, 
    song_id VARCHAR(50) NOT NULL, 
    artist_id INT, 
    session_id INT, 
    location TEXT, 
    user_agent TEXT,
    PRIMARY KEY (songplay_id))
""")

user_table_create = ("""
CREATE TABLE users(
    user_id INT, 
    first_name TEXT, 
    last_name TEXT, 
    gender VARCHAR(1), 
    level TEXT,
    PRIMARY KEY (user_id))
""")

song_table_create = ("""
CREATE TABLE songs(
    song_id VARCHAR(50) NOT NULL, 
    title TEXT, 
    artist_id INT, 
    year INT, 
    duration FLOAT,
    PRIMARY KEY (song_id))
""")

artist_table_create = ("""
CREATE TABLE artists(
    artist_id INT, 
    name TEXT, 
    location TEXT, 
    latitude DECIMAL(8,6),
    longitude DECIMAL(9,6),
    PRIMARY KEY (artist_id))
""")

time_table_create = ("""
CREATE TABLE time(
    start_time TIMESTAMP, 
    hour INT, 
    day INT, 
    week INT, 
    month INT, 
    year INT, 
    weekday INT,
    PRIMARY KEY (start_time))
""")

# STAGING TABLES

staging_events_copy = ("""COPY staging_events from '{}'
                          IAM_ROLE {}
                          JSON {};

                        """).format(config.get('S3','LOG_DATA'), 
                                    config.get('IAM_ROLE', 'ARN'),
                                    config.get('S3','LOG_JSONPATH'))
staging_songs_copy = ("""COPY staging_songs from '{}'
                            IAM_ROLE '{}'
                            JSON 'auto';
                            """).format(config.get('S3','SONG_DATA'), 
                                        config.get('IAM_ROLE', 'ARN'))

# FINAL TABLES

songplay_table_insert = ("""
INSERT INTO songplays(start_time, user_id, level, song_id, artist_id,    session_id, location, user_agent)
SELECT 
TIMESTAMP 'epoch' + e.ts/1000 * INTERVAL '1 second' as start_time,
e.user_id,
e.user_level as level,
s.song_id,
s.artist_id,
e.session_id,
e.location,
e.ser_agent,
FROM staging_events e, 
JOIN stage_song s ON 
WHERE e.song = s.title AND
e.artist_name = s.artist_name
""")

user_table_insert = ("""
INSERT INTO users(user_id, first_name, last_name, gender, level)
SELECT DISTINCT
user_id,
user_first_name as first_name,
user_last_name as last_name,
user_gender as gender,
user_level as level
FROM staging_events
WHERE page = 'NextSong'
""")

song_table_insert = ("""
INSERT INTO songs(song_id, title, artist_id, year, duration)
SELECT DISTINCT
song_id,
title,
artist_id,
year,
duration
FROM staging_songs
""")

artist_table_insert = ("""
INSERT INTO artists(artist_id, name, location, latitude, longitude)
SELECT DISTINCT
artist_id,
artist_name as name,
artist_location as location,
artist_latitude as latitude, 
artist_longitude as longitude
FROM staging_songs 
""")

time_table_insert = ("""
INSERT INTO time(start_time, hour, day, week, month, year, weekday)
SELECT start_time, 
EXTRACT(hour from start_time) AS hour,
EXTRACT(day from start_time) AS day,
EXTRACT(week from start_time) AS week,
EXTRACT(month from start_time) AS month,
EXTRACT(year from start_time) AS year, 
EXTRACT(weekday from start_time) AS weekday 
FROM songplays
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
