# dataframe from file

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Spark").getOrCreate()

df = spark.read.\
    format("csv").\
    option("header", "True").\
    option("inferschema", "True").\
    option("path", "hdfs:///user/maria_dev/spark/insurance.csv").\
    load()


df.printSchema()

output = df.select(df.age, df.sex, df.children, df.expenses)\
    .where(df.age<25)\
    .orderBy(df.age)\
    .cache()

output.write\
    .format("json")\
    .mode("overwrite")\
    .option("path", "hdfs:///user/maria_dev/spark/job-output1")\
    .partitionBy("age")\
    .save()

spark.stop()