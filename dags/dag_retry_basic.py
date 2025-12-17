import pendulum
from airflow.sdk import dag, task


@dag(
    dag_id="dag_retry_basic",
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    schedule="@daily",
    catchup=False,
    tags={"demo", "retry"},
)
def retry_basic_dag():
    @task(
        retries=1,
        retry_delay=pendulum.duration(minutes=1),
    )
    def fail_one():
        raise ValueError("This is designed to fail once.")

    @task
    def fail_two():
        raise ValueError("This is designed to fail twice.")

    fail_one()
    fail_two()


retry_basic_dag()
