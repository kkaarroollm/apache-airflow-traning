# extract transform load
import pendulum
from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG, task

with DAG(
    dag_id="etl_data_processing",
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    schedule="@daily",
    catchup=False,
    tags={"example"},
) as dag:
    hello = BashOperator(task_id="say_hello", bash_command="echo 'Hello from Airflow!'")

    @task
    def python_task():
        print("This is a Python task in the ETL DAG.")

    hello >> python_task()
