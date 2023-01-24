import pyspark.sql.functions as f
from pyspark.sql.functions import udf
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StringType,
    StructField,
    StructType,
    MapType
)

events_schema = StructType([
    StructField('event_type', StringType(), True),
    StructField('id', StringType(), True),
    StructField('person_id', StringType(), True),
    StructField('category', StringType(), True),
    StructField('approved_content', StringType(), True),
])

events = [{
    'event_type': 'click',
    'id': '223',
    'person_id': 201031940,
    'category': 'Chronicles',
    'approved_content': 1
}]
spark = SparkSession.builder.appName("Python").getOrCreate()
df = spark.createDataFrame(events, schema=events_schema)
df.show()