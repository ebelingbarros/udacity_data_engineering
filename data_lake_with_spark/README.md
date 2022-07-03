# 4th Project: Data Lake with Spark

## Project outline

Sparkify's user base and song database has been growing considerably and now they are considering moving their data warehouse to a data lake. As of now, their raw data is stored in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

In order to store their data in a data lake, Sparkify is planning to build an ETL pipeline designed to extract data from S3, process it using Spark (which is deployed on a cluster using AWS), and then load back data into S3 in the form of dimensional tables. Using a data lake will permit the startup's analytics team to optimize the process of finding insights in the songs tjhe users are listening to. 

## Data 

The data used in this project is Stored in Amazon S3, in two directories:

**Song data**: s3://udacity-dend/song_data<br>
**Log data**: s3://udacity-dend/log_data

See below an example of what a single **song** file, TRAABJL12903CDCF1A.json, looks like.

```{
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
}
```

By its turn, this is the format of a typical **log file**, 2018-11-12-events.json:

<p align="center">
  <img width="100%" height="100%" src="https://github.com/ebelingbarros/udacity_data_engineering/blob/main/data_lake_with_spark/images/log-data.png"> 
</p> 

## Schema 

In this project, data is modelled in a star Schema, in order to facilitate querying and analysis:  

# Here Schema

## Project Files

The project contains the following files:

1. etl.py reads data from S3, processes that data using Spark, and writes them back to S3
2. dl.cfg contains ther AWS credentials

## Use Instructions

In order to run the project, it is necessary to first, insert AWS credentials into the dl.cfg file

``` 
[AWS]  
key = 
secret =
```

After this, in order to run the ETL process, run the ETL script:

``` 
python etl.py
``` 

In the event of sucess, you will see a preview of the output data.







