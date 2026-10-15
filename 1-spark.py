# creating dataframe
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("LearningDataframes").getOrCreate()

studentsData = (("Muhammad Ali", "Data Science", 3.8), 
              ("Sarah Ansari", "Software Engineering", 3.9),
              ("Khalid Mehmood", "Electrical Engineering", 3.7),)


columns = ["student_name", "discipline", "cgpa"]

df = spark.createDataFrame(data=studentsData, schema=columns)

df.printSchema()

df.show()

spark.stop()

