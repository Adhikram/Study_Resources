from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col

# Create a SparkSession
spark = SparkSession.builder \
    .appName("WordCount") \
    .getOrCreate()

# Read the text file
text_df = spark.read.text("path_to_your_text_file.txt")

# Split the lines into words
words_df = text_df.select(explode(split(col("value"), " ")).alias("word"))

# Count the occurrences of each word
word_counts = words_df.groupBy("word").count()

# Show the word counts
word_counts.show()

# Stop the SparkSession
spark.stop()
# In summary:

# Total Jobs: One job is triggered during the creation of SparkSession.

# Total Stages: At least three stages are created: one for reading the text file, 
# one for splitting lines into words, and one for the word count operation.

# Total Tasks: The exact number of tasks depends on the number of partitions 
# in the data and the size of the DataFrames after each transformation. Spark dynamically determines the number of tasks.