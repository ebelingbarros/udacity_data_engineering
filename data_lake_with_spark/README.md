# 4th Project: Data Lake with Spark

## Project outline

Sparkify's user base and song database has been growing considerably and now they are considering moving their data warehouse to a data lake. As of now, their raw data is stored in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

In order to store their data in a data lake, Sparkify is planning to build an ETL pipeline designed to extract data from S3, process it using Spark (which is deployed on a cluster using AWS), and then load back data into S3 in the form of dimensional tables. Using a data lake will permit the startup's analytics team to optimize the process of finding insights in the songs tjhe users are listening to. 

## Data 

The data used in this project is Stored in Amazon S3, in two directories:

Song data: s3://udacity-dend/song_data
Log data: s3://udacity-dend/log_data

See below an example of what a single **song** file, TRAABJL12903CDCF1A.json, looks like.

`{
    "num_songs": 1, 
    "artist_id": "ARJIE2Y1187B994AB7", 
    "artist_latitude": null, 
    "artist_longitude": null, 
    "artist_location": "", 
    "artist_name": "Line Renaud", 
    "song_id": "SOUPIRU12A6D4FA1E1", 
    "title": "Der Kleine Dompfaff", 
    "duration": 152.92036, 
    "year": 0    
}`

By its turn, this is the format of a typical **log file**, 2018-11-12-events.json:






# Schema 

Data Modeling with Star Schema
Star Schema for Song Play Analysis!


Data Lake to store extracted dimentional tables
"s3a://udacity-de-sparkify-data-lake/artists"
"s3a://udacity-de-sparkify-data-lake/songs"
"s3a://udacity-de-sparkify-data-lake/time"
"s3a://udacity-de-sparkify-data-lake/users"
"s3a://udacity-de-sparkify-data-lake/songplays"


# Project Files
In addition to the data files, the project workspace includes 5 files:

1. dl.cfg Contains the Secret Key for ASW access
2. create_bucket.py Create bucket in AWS S3 to store the extracted dimentional tables.
3. etl.py Loading song data and log data from S3 to Spark, transforms data into a set of dimensional tables, then save the table back to S3
4. etl.ipynb Used to design ETL pipelines
5. README.md Provides project info

## Use Instructions

Configuration
Set up a config file dl.cfg that uses the following schema. Put in the information for your IAM-Role that can read and write S3 buckets.

[S3]
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
ETL pipeline
Simply run the ETL script.

python etl.py
If the ETL pipeline was successful, a preview of the output data will be displayed.

Configuration
Remember to set key and secret in ./aws/dl.cfg before run etl.py

[AWS]
key =
secret =





Build ETL Pipeline
etl.py will process the entire datasets.



Instruction
Set key and secrect in dwh.cfg file


Run create_bucket.py
python create_bucket.py


Use following command to start ETL process
python etl.py

