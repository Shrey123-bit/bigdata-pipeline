# PySpark job pseudocode for DevOps Big Data assignment

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ExampleBigDataJob").getOrCreate()

df = spark.read.csv("data/input.csv", header=True)
df.show()

spark.stop()
