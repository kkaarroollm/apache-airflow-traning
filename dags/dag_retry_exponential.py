import pendulum
from airflow.sdk import dag, task


@dag(
    dag_id="dag_retry_exponential",
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    schedule="@daily",
    catchup=False,
    tags={"demo", "retry"},
)
def retry_basic_dag():
    @task(
        retries=4,
        retry_delay=pendulum.duration(seconds=10),
        retry_exponential_backoff=True,
        max_retry_delay=pendulum.duration(minutes=5),
    )
    def fail_one():
        raise ValueError("This is designed to fail once.")

    fail_one()


retry_basic_dag()
