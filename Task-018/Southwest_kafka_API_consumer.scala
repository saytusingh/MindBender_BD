import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.streaming._
import org.apache.spark.sql.types._
import org.apache.spark.sql.SparkSession


case class SWA(cardId:string, departureTime:int, durationMinutes:int, numberofStops:int, startingFromAmount:int)


object southwest {
	def main(args: Array[String]): Unit = {

		val spark = SparkSession
		.builder.appName("Southwest").getOrCreate()


	val schema = StructType(List(
			StructField("CARDID", StringType, true),
			StructField("DEPARTURETIME", IntType, true),
			StructField("DURATIONMINUTES", IntType, true),
			StructField("NUMBEROFSTOPS", IntType, true),
			StructField("STARTINGFROMAMOUNT", IntType, true)
		))


		import spark.implicits._
		val rdd = spark
			 .readStream
			 .format("kafka")
			 .option("kafka.bootstrap.servers", "localhost:9099,localhost:9098,localhost:9097")
			 .option("subscribe", "transdata")
             .load()
             .select($"value" cast "string" as "json")
             .select(from_json($"json", schema) as "data")
             .select("data.*")

    val expandedData = rdd


    	val query = expandedData
    	.writeStream
    	.outputMode("update")
    	.format("console")
    	.start()



    query.awaitTermination()
}
}
            

