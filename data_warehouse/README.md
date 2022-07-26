# 3rd Project: Data Warehouse

## Project outline 
This project creates Sparkify's data warehouse, in which the startup's user base and song database are moved into the cloud, on AWS Redshift. For this purpose, an ETL pipeline is built that extracts data from AWS S3, then stages tables on AWS Redshift, and finally performs SQL statements to create tables from the staging tables, which can then be used by the analytics team. The end product is data in a star schema with fact and dimension tables.

## Datasets
The dataset used in this project are obtained from two S3 buckets, and is storedin JSON files. While the first one contains information about songs and artists, teh second one provides log information about the user's behaviour while using the app 

## Schema

From the two initial staging tables (**staging_songs**, which contains information about songs and artists, and **staging_events**, which contains the user's actions while using the app), a star schema is created. It is optimized for querying and performing analyises. The schema contains the following tables:

### Fact Table
**songplays** - records in event data associated with song plays i.e. records with page NextSong

### Dimension Tables
**users** - users in the app<br>
**songs** - songs in music database<br>
**artists** - artists in music database<br>
**time** - timestamps of records in songplays broken down into specific units

# Here Schema

## Project files

**create_table.py** - creates  fact and dimension tables for the star schema in Redshift parting from the staging tables <br>
**etl.py** - loads data from S3 into staging tables on Redshift and then process that data into analytics tables on Redshift <br>
**sql_queries.py** - defines SQL statements, which are then imported into the two filess <br>

## Run instructions 

1. Create IAM role that has read access to S3 <br>
2. Launch the redshift cluster <br>
3. Create tables by running create_tables.py <br>

```
python create_tables.py
```

4. Execute ETL process by running etl.py 

```
python etl.py
```

