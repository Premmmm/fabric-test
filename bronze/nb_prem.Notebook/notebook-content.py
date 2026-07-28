# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "a7024160-7145-4303-b4e1-c3de9450282e",
# META       "default_lakehouse_name": "lh_prem",
# META       "default_lakehouse_workspace_id": "33acc747-26fb-47a4-b231-451d71282085",
# META       "known_lakehouses": [
# META         {
# META           "id": "a7024160-7145-4303-b4e1-c3de9450282e"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

import json

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

context =- notebookutils.runtime.context
spark.conf.set(
    "spark.databricks.delta.commitInfo.userMetadata",
    json.dumps({
      "prcs_name": "test_process",
      "business_unit": "test_business_unit",
      "script_name": context("currentNotebookName"),
      "db_name": "test_db",
      "workflow_name": "tst_pipeline",
      "job_id": "asdfasfasfsafasdfsadfsa12312"
    })
)

# spark.conf.set(
#    "spark.databricks.delta.commitInfo.userMetadata",
#    metadata
# )

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Initialize Spark Session
spark = SparkSession.builder.appName("SampleData").getOrCreate()

# Method A: Basic list with column names
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
columns = ["Name", "Age"]
df1 = spark.createDataFrame(data, schema=columns)

# Method B: Detailed schema using StructType
schema = StructType([
    StructField("Name", StringType(), True),
    StructField("Age", IntegerType(), True)
])
df2 = spark.createDataFrame(data, schema=schema)

df1.show()


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df1.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("dbo.sample_data")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC DESCRIBE HISTORY dbo.sample_data;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

print('prem')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
