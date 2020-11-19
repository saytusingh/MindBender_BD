from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession 
import json 

if __name__ == "__main__":

    sc = SparkContext(appName="tweets")
	ssc = StreamingContext(sc, 10)

    kafkaStream = KafkaUtils.createStream(ssc, 'localhost:2181', 'tweets', {'twitter':1})
    
    parsed = kafkaStream.map(lambda v: json.loads(v[1]))

    user_counts = parsed.map(lambda tweet: (tweet['user']["screen_name"], 1)).reduceByKey(lambda x,y: x + y)

    user_counts.pprint()

    ssc.start()
    ssc.awaitTermination()
