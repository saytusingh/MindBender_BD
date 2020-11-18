
import org.apache.spark._
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf

object WordCount{
        def main(args:Array[String]){
                val conf = new SparkConf()
                conf.set("spark.master", "local")
                conf.set("spark.app.name", "App")
                val sc = new SparkContext(conf)
                var map = sc.textFile("/home/fieldemployee/Shakespeare.txt").flatMap(line => line.split(" ")).map(word => (word,1));
                var counts = map.reduceByKey(_ + _);
                counts.saveAsTextFile("/home/fieldemployee/wordCount_Spark_output/");
            
                sc.stop()
    