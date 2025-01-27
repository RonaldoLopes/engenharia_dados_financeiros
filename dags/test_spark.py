from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from pyspark.sql import SparkSession

def run_spark_job():
    spark = SparkSession.builder.appName("Airflow Spark Job").master("local[*]").getOrCreate()
    data = [("Alice", 29), ("Bob", 34), ("Cathy", 25)]
    df = spark.createDataFrame(data, ["Name", "Age"])
    df.show()

    spark.stop()

#DAG
default_args = {
    'owner': 'Ronaldo Lopes',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 26),
    'email_on_failure': False,
    'email_on_retry': False,
}

with DAG(
         dag_id='pyspark_local_example',
         default_args=default_args,
         description='Exemplo de execução do PySpark localmente no Airflow',
         schedule_interval=None,
         catchup=False,
        ) as dag:
    spark_task = PythonOperator(
        task_id='run_spark_task',
        python_callable=run_spark_job,
    )

    spark_task
