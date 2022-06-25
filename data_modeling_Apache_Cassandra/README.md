# 2nd Project: Data Modeling with Apache Cassandra

### Project outline
This Udacity Data Engineering nanodegree project creates an Apache Cassandra database sparkifyks for a music app, Sparkify. The purpose of the NoSQL database is to answer queries on song play data. The data model includes a table for each of the following queries:

The purpose of this project is to create an Apache Cassandra database for a ficticious startup called Sparkify to query on song play data. The raw data is in a directory of CSV files, and we will build a ETL pipeline to transform the raw data into the Apache Cassandra database.

### Data

There is one dataset called event_data which is in a directory of CSV files partitioned by date. The filepaths are given as event_data/<yyyy>-<mm>-<dd>-events.csv where <yyyy> indicates the year, <mm> indicates the month and <dd> indicates the year. The fields of of event_data are:

artist (string)
auth (string)
firstName (string)
gender (char)
itemInSession (int)
lastName (string)
length (float)
level (string)
location (string)
method (string)
page (string)
registration (float)
sessionId (int)
song (string)
status (int)
ts (float)
userId (int)

### ETL Pipeline
Start with the raw csv data files as described in Dataset
For each row of the csv data, insert the data in the appropriate column as described in Schema
Perform the Select query as described in Queries
  
  
 ### Queries

  
  The data are stored as a collection of csv files partitioned by date. The ETL pipeline and data modeling are written in a single jupyter notebook, Project_1B_Project_Template.ipynb.

ETL copies data from the date-partitioned csv files to a single csv file event_datafile_new.csv which is used to populate the denormalized Cassandra tables optimised for the 3 queries above. The 3 tables in the model are named after the song play query they are created to solve:

songinfo_by_session_by_item includes artist, song title and song length information for a given sessionId and itemInSessionId.

songinfo_by_user_by_session includes artist, song and user for a given userId and sessionId.

userinfo_by_song includes user names for a given song.

The example queries are returned as pandas dataframes to facilitate further data manipulation.
  
Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4

Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182

Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'  
  
For NoSQL databases, we design the schema based on the queries we know we want to perform. For this project, we have three queries:

Find artist, song title and song length that was heard during sessionId=338, and itemInSession=4.
SELECT artist, song, length from table_1 WHERE sessionId=338 AND itemInSession=4
Find name of artist, song (sorted by itemInSession) and user (first and last name) for userid=10, sessionId=182.
SELECT artist, song, firstName, lastName FROM table_2 WHERE userId=10 and sessionId=182
Find every user name (first and last) who listened to the song 'All Hands Against His Own'.
SELECT firstName, lastName WHERE song='All Hands Againgst His Own'
  
  
  





