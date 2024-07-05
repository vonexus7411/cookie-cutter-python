from pyspark.sql import SparkSession

# Create a Spark session
spark = (SparkSession.builder
    .appName("{{ cookiecutter.project_slug }}")
    .getOrCreate()
)

spark

spark.stop()