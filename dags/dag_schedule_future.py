import pendulum
from airflow.sdk import dag, task, get_current_context


# even with CYNGIEL won't execute until 2026
@dag(
    dag_id="dag_schedule_future",
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    schedule="@daily",
    catchup=False,
    tags={"demo", "retry"},
)
def task_future():
    @task
    def print_future_date():
        print("Current execution date is:", get_current_context()["ds"])

    print_future_date()


task_future()
