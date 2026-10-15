from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

df = spark.read.\
    format("csv").\
    option("header", "True").\
    option("inferschema", "True").\
    option("path", "hdfs:///user/maria_dev/spark/insurance.csv").\
    load()

df.printSchema()

df.createOrReplaceTempView("insurace")

spark.sql("SELECT * FROM insurace WHERE age<=18 ORDER BY age").show()

spark.stop()