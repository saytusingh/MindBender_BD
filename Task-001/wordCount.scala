import scala.io.Source

object WordCount extends App {
	val filename =  "/home/fieldemployee/Desktop/Shakespeare.txt"


	def WordCount = 
		Source.fromFile(filename).getLines()
			.filter(_.nonEmpty)
			.flatMap(_.split("""\W+""")).toSeq
			.groupBy(_.toLowerCase())
			.mapValues(_.size).toSeq
			.sortWith { case ((_, v0), (_,v1)) => v0 > v1 }

	WordCount.foreach {
		case ((word, count)) => println(f"$word%-8s $count%6d")
	}
}