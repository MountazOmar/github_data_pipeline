from pyspark.sql import functions as F

def add_integration_date(df):
    return df.withColumn('integration_date', F.now())

def add_integration_hour(df):
    return df.withColumn('integration_hour', F.hour(F.now()))
