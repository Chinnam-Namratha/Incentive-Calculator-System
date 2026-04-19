import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from src.main.utility.logging_config import *
def spark_session():
    spark = SparkSession.builder.master("local[*]") \
        .appName("namratha_spark2") \
        .config("spark.driver.extraClassPath",
               "C://my_sql_jar//mysql-connector-j-9.3.0.jar") \
        .getOrCreate()
    logger.info("Spark session created: %s", spark)
    return spark

spark = spark_session()  # Call your function

df = spark.read.format('jdbc'
                       ).option("url", "jdbc:mysql://localhost:3306/deproject"
                                ).option("user", "root"
                                         ).option("password", "Namratha@02"
                                                  ).option('dbtable', 'product'
                                                           ).option('driver',
                                                                    'com.mysql.cj.jdbc.Driver'
                                                                    ).load()
df.show()




