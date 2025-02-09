from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("EcommerceRecommendation").getOrCreate()

# Load dataset
df = spark.read.csv("data/amazon_reviews.csv", header=True, inferSchema=True)

# Select relevant columns
df = df.select("UserId", "ProductId", "Score")

df.show(5)
