
from pyspark import SparkContext, SparkConf

# Set up Spark configuration
conf = (
    SparkConf()
    .setAppName("spark-worker")
    .setMaster("spark://spark-master:7077")
    .set("spark.executor.memory", "1g")
)

# Create Spark Context
sc = SparkContext.getOrCreate(conf=conf)

# Do data processing here
# ...

# Stop Spark Context
sc.stop()
