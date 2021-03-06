import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, date_format


config = configparser.ConfigParser()
config.read('dl.cfg')

os.environ['AWS_ACCESS_KEY_ID']=config['AWS']['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY']=config['AWS']['AWS_SECRET_ACCESS_KEY']


def create_spark_session():
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark


def process_song_data(spark, input_data, output_data):
    # get filepath to song data file
    song_data=input_data+'/song_data/A/A/A/*.json'
    #song_data = os.path.join(input_data, 'song_data/A/A/*/*.json') 
    
    # read song data file
    df = spark.read.json(song_data)

    # extract columns to create songs table
    songs_table = df.select("song_id", 
                            "title", 
                            "artist_id", 
                            "year","duration").dropDuplicates()
    
    # write songs table to parquet files partitioned by year and artist
    songs_table.write.parquet(output_data+'songs/'+'songs.parquet').partitionBy("year","artist_id")
                                                                                             
    # extract columns to create artists table
    artists_table = df.select(col('artist_id'),
                              col('artist_name'),
                              col('artist_location'),
                              col('artist_latitude'),
     col('artist_longitude')).drop_duplicates()
                                                                          
                                                                    
    # write artists table to parquet files
    artists_table.write.mode('overwrite').parquet(os.path.join(output_data, 'artists/artists.parquet'))


def process_log_data(spark, input_data, output_data):
    # get filepath to log data file
    log_data = log_data = input_data + 'log-data/*.json'

    # read log data file
    df = spark.read.json(log_data)
    
    # filter by actions for song plays
    df = df.filter("page == 'NextSong'")

    # extract columns for users table    
    users_table = df.select("user_id", "first_name", "last_name", "gender", "level").dropDuplicates()
                                          
    # write users table to parquet files
    users_table.write.mode('overwrite').parquet(os.path.join(output_data, 'users/users.parquet'))

    # create timestamp column from original timestamp column
    get_timestamp = udf(lambda x: datetime.fromtimestamp(x / 1000), TimestampType())
    df = df.withColumn('timestamp', get_timestamp(col('ts')))
                                        
    # create datetime column from original timestamp column
    get_datetime = udf(lambda x: int(datetime.datetime.fromtimestamp(x / 1000.0)))     
    
    # extract columns to create time table
    time_table = df.select(col("timestamp").alias("start_time"),
                           hour(col("datetime")).alias("hour"),
                           dayofmonth(col("datetime")).alias("day"),
                           weekofyear(col("datetime")).alias("week"),
                           month(col("datetime")).alias("month"),
                           year(col("datetime")).alias("year"),
                           dayofweek(col("datetime")).alias("weekday")).orderBy(asc("hour")).dropDuplicates()
                            
    
    # write time table to parquet files partitioned by year and month
    time_table.write.mode('overwrite').partitionBy("year","month").parquet(os.path.join(output_data, 'time/time.parquet'))


    # read in song data to use for songplays table
    song_df = spark.read.json(input_data + 'song_data/A/A/A/*.json')
                                                                      

    # extract columns from joined song and log datasets to create songplays table 
    songplays_table = df.join(song_data, (song_data.title == df.song)).select(col("timestamp").alias("start_time"),
                                col("userId").alias("user_id"),
                                col("level"),
                                col("song_id"),
                                col("artist_id"),
                                col("sessionId").alias("session_id"),
                                col("location"),col("userAgent").alias("user_agent")).dropDuplicates().orderBy(asc("user_id"))

    # write songplays table to parquet files partitioned by year and month
    songplays_table.mode('overwrite').partitionBy("year","month").parquet(os.path.join(output_data, 'songplays/songplays.parquet'))


def main():
    spark = create_spark_session()
    input_data = "s3a://udacity-dend/"
    output_data = "s3a://sparkify-data-lake/"
    
    process_song_data(spark, input_data, output_data)    
    process_log_data(spark, input_data, output_data)


if __name__ == "__main__":
    main()
