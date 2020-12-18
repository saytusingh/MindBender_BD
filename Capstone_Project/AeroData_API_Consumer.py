from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql.functions import col
from pyspark.sql import SparkSession, Row
import json 


sc = SparkContext("local[*]", )
ssc = StreamingContext(sc, 6)

ss = SparkSession.builder.appName(sc.appName).master('local[*]').config("spark.sql.warehouse.dir","/user/hive/warehouse").config("hive.metastore.uris","thrift://localhost:9083").enableHiveSupport().getOrCreate()

kafkaStream = KafkaUtils.createStream(ssc, 'localhost:2181', 'aerodata', {'aerodata':1})

parsed = kafkaStream.map(lambda x: json.loads(x[1]))

# parsed1 = parsed.map(lambda x: x.get('airlineName')).pprint()

sch = StructType([StructField('airlineName', StringType(), True), StructField('typeName', StringType(), True), StructField('deliveryDate', IntegerType(), True), StructField('firstFlightDate', IntegerType(), True)])

# parsed.toDF().show()


def Process(rdd):
	if not rdd.isEmpty():
		global ss 
		df = ss.createDataFrame(rdd)
		df2 = df.withColumn('airlineName', col('airlineName'))
		df3 = df2.select(
			df2['ageYears'],
			df2['airlineName'],
			df2['deliveryDate'],
			df2['firstFlightDate'],
			df2['typeName'])
		df3.show()
		df3.printSchema()
		df3.write.saveAsTable(name="default.aircraft_info", format="hive", mode="append")


parsed.foreachRDD(Process)

ssc.start()
ssc.awaitTermination()



#table.foreachRDD(Process)
#sql = ss.sql("select * from default.aerodata")
#sql.show()

#ssc.start()
#ssc.awaitTermination()