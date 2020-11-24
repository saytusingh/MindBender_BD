from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession 
import json

def Process(rdd):
	if not rdd.isEmpty():
		global ss 
		df = ss.createDataFrame(rdd, schema=['MinPrice','Direct','OutboundLeg'])
		df.show()
		df.write.saveAsTable(name="default.flights", format="hive", mode="append")


sc = SparkContext("local[*]", "FlightData")
ssc = StreamingContext(sc, 5)

ss = SparkSession.builder.appName("FlightData").config("spark.sql.warehouse.dir","/user/hive/warehouse").config("hive.metastore.uris","thrift://localhost:9083").enableHiveSupport().getOrCreate()

kafkaStream = KafkaUtils.createStream(ssc, 'localhost:2181', 'Flights', {'flights':1})
    
parsed = kafkaStream.map(lambda v: json.loads(v[1]))

#user_counts = parsed.map(lambda tweet: (tweet['user']["screen_name"], 1)).reduceByKey(lambda x,y: x + y)

#user_counts.pprint()


longest_duration = parsed.flatMap(lambda v: v.get("Quotes"))
#longest_duration.pprint()

table = longest_duration.map(lambda v: (v.get("MinPrice"),v.get("Direct"), v.get("OutboundLeg")))

longest_duration.pprint()

table.foreachRDD(Process)

ssc.start()
ssc.awaitTermination()
