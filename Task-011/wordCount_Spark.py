import sys
 
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
 
if __name__ == "__main__":
	
	# create Spark context with necessary configuration
	sc = SparkContext("local[*]","PySpark Word Count Exmaple")
	ssc = StreamingContext(sc, 3)

	ss = SparkSession.builder \
	.enableHiveSupport() \
	.getOrCreate()

	
	# read data from text file and split each line into words; read file into RDD
	words = sc.textFile("/home/fieldemployee/Shakespeare.txt").flatMap(lambda line: line.split(" "))
	
	# count the occurrence of each word
	wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)
	
	# save the counts to output
	wordCounts.saveAsTextFile("/home/fieldemployee/output/")

	ssc.start()
	ssc.awaitTermination()
