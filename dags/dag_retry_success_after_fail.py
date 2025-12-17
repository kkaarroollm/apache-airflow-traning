import pendulum
from airflow.sdk import dag, task, get_current_context


@dag(
    dag_id="dag_retry_success_after_fail",
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
    def fail_once():
        ctx = get_current_context()
        ti = ctx["ti"]
        if ti.try_number < 2:
            raise ValueError("This is designed to fail once.")
        print("Task succeeded on retry number", ti.try_number)

    fail_once()


retry_basic_dag()
