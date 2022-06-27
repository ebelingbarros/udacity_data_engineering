# 1st Project: Data Modeling with Postgres

## Project outline

The goal of this project is to create a database for Sparkify, a fictional music streaming app. The company's analytics teams requires an efficient and reliable infrastructure to query analyze its data collected on user activity and the songs database. Thedata is currently stored in JSON files in a directory. In this context, this project creates and implements a database schema and an ETL pipeline where the data is uploaded in a PostgreSQL database. 

## Data

The JSONs with song data contains the following information:

**artist_id**<br>
**artist_latitude**<br>
**artist_location**<br>
**artist_longitude**<br>
**artist_name**<br>
**duration**<br>
**num_songs**<br>
**song_id**<br>
**title**<br>
**year**<br>

The JSONs with log data contains the following information:

**artist**<br>
**auth**<br>
**firstName**<br>
**gender**<br>
**itemInSession**<br>
**lastName**<br>
**length**<br>
**level**<br>
**location**<br>
**method**<br>
**page**<br>
**registration**<br>
**sessionId**<br>
**song**<br>
**status**<br>
**ts**<br>
**userAgent**<br>
**userId**<br>

## Database schema

In order to make SQL querying and aggregations more efficient, the data is converted into a star Schema. In that approach, a central table is created - the fact table, which contains the measures that can be quantified. On each "corner" of the fact table, 4 dimension tables are introduced: songs, artists, users and time. Each one of these tables is connected to the fact table through a primary key which is also present in the fact table.

## Project structure

- data folder: this is where the two types of jsons are stored (*song_data* and *log_data*)
- sql_queries.py: this is where the SQL queries needed to create the tables are stored
- create_tables.py: this file is used to drop and create tables
- test.ipynb: carries out test SQL queries in order to check if new database has been created correctly
- etl.ipynb: Jupyter notebook with the JTL process. It combines the separted JSONs into single files and loads the data into the new tables
- etl.py: Does the same exercise as the file above
