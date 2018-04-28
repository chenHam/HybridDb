import pandas as pd
from pyspark.shell import spark
from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.ml.clustering import KMeans
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("FinalProjectDataBases").master("local[*]").getOrCreate()


cf = spark.read.csv('queryesForPivot.csv', header=True)
tokenizer = Tokenizer(inputCol="query", outputCol="words")
wordsData = tokenizer.transform(cf)
hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=20)
featurizedData = hashingTF.transform(wordsData)
idf = IDF(inputCol="rawFeatures", outputCol="features")
idfModel = idf.fit(featurizedData)
rescaledData = idfModel.transform(featurizedData)
rescaledData.select("query","StartTime","RunTime", "features")

numOfClusters=5
kmeans = KMeans(k=numOfClusters, seed=1)
model = kmeans.fit(rescaledData.select('features'))

transformed = model.transform(rescaledData)
# transformed.show()

transformed.createOrReplaceTempView("df")
timesDf = spark.sql("SELECT StartTime,cast(RunTime as int),prediction FROM df")
sumDf= spark.sql("SELECT StartTime,prediction,count(prediction) FROM df group by StartTime,prediction")


# PIVOT
pivotDf1 = sumDf.groupby('StartTime') \
    .pivot('prediction') \
    .max('count(prediction)')
pivotDf1 = pivotDf1.fillna(0)
pivotDf1.createOrReplaceTempView('pivotDf')
pivotDf1.show()
# PIVOT
pivotDf = timesDf.groupby('StartTime') \
    .pivot('prediction') \
    .sum('RunTime')
pivotDf = pivotDf.fillna(0)
pivotDf.createOrReplaceTempView('pivotDf')
pivotDf.show()



