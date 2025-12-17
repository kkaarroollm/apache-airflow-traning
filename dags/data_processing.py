# extract transform load
from typing import Any

import pendulum
from airflow.sdk import dag, task



@dag(
    dag_id="etl_data_processing",
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    schedule="@daily",
    catchup=False,
    tags={"etl", "data_processing"},
)
def etl_data_processing_dag():

    @task.virtualenv(requirements=["polars==1.36.1"], system_site_packages=False)
    def extract_data() -> dict[str, Any]:
        import polars as pl

        return pl.DataFrame({
            "name": ["alice", "bob", "charlie"],
            "age": [25, 30, 35]
        }).to_dicts()[0]

    @task.virtualenv(requirements=["polars==1.36.1"], system_site_packages=False)
    def transform_data(data: dict[str, Any]) -> dict[str, Any]:
        import polars as pl
        data = pl.DataFrame(data)
        data = data.with_columns([
            (data["age"] + 1).alias("age_next_year")
        ])
        return data.to_dicts()[0]

    @task
    def load_data(transformed_data: dict[str, Any]):
        print("Transformed Data:")
        print(transformed_data)

    d = extract_data()
    td = transform_data(d)
    load_data(td)

etl_data_processing_dag()

