# 2nd Project: Data Modeling with Apache Cassandra

## Project outline
In this second Udacity Data Engineering nanodegree project an Apache Cassandra database is created for Sparkify, a fictitious startups that offers a music app. Through an ETL pipeline that uses NoSQL, tables are created and are used to answer business questions. 

## Data

The raw data used for creating the tables and answering the business questions is stored in a directory of CSV files. The data is partitionated by dates. These are the features from the data and the respective data types:

**artist** *string*,<br>
**auth** *string*,<br>
**firstName** *string*,<br>
**gender** *char*,<br>
**itemInSession** *int*,<br>
**lastName** *string*,<br>
**length** *float*,<br>
**level** *string*,<br>
**location** *string*,<br>
**method** *string*,<br>
**page** *string*,<br>
**registration** *float*,<br>
**sessionId** *int*,<br>
**song** *string*,<br>
**status** *int*,<br>
**ts** *float*,<br>
**user**Id *int*,<br>

## ETL Pipeline

As mentioned above, the data is stored in a data folder within csv files which are partitioned by date. The ETL pipeline and data modeling exercise are performed in a one Jupyter notebook called Project_1B_Project_Template.ipynb. In the ETL pipeline, data from several csv files is compiled into a single csv file called event_datafile_new.csv. This file is used used to create denormalized tables in schemas specifically created for the 3 queries below.

## Queries
 
#### 1. Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4
*"SELECT artist, song, length FROM artist_song WHERE sessionId = 338 and itemInSession = 4"*

#### 2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182
*"SELECT artist, song, firstName, lastName FROM artist_song_user WHERE userId = 10 and sessionid = 182 order by itemInSession DESC"*

#### 3. Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'
*"SELECT song, firstName, lastName FROM user WHERE song = 'All Hands Against His Own'"*
  





