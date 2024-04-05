from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, regexp_replace, col

# Create a SparkSession
spark = SparkSession.builder \
    .appName("WordCount") \
    .getOrCreate()

# Read the text file
text_df = spark.read.text("path_to_your_text_file.txt")

# Replace multiple delimiters (',', ':', and space) with a single space
cleaned_text_df = text_df.withColumn("cleaned_text", regexp_replace(col("value"), "[,:]", " "))

# Split the lines into words
words_df = cleaned_text_df.select(explode(split(col("cleaned_text"), "\s+")).alias("word"))

# Count the occurrences of each word
word_counts = words_df.groupBy("word").count()

# Show the word counts
word_counts.show()

# Stop the SparkSession
spark.stop()
