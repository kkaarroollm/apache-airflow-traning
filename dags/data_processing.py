# extract transform load
from typing import Any, TYPE_CHECKING

import pendulum
from airflow.sdk import dag, task

if TYPE_CHECKING:
    import polars as pl


@dag(
    dag_id="etl_data_processing",
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    schedule="@daily",
    catchup=False,
    tags={"etl", "data_processing"},
)
def etl_data_processing_dag():
    @task.virtualenv(requirements=["polars==1.36.1"], system_site_packages=False)
    def extract_data(data: "pl.DataFrame" = None) -> dict[str, Any]:
        import polars as pl

        if data is None:
            data = pl.DataFrame(
                {
                    "name": ["Alice", "Bob", "Charlie"],
                    "age": [25, 30, 35],
                    "city": ["New York", "Los Angeles", "Chicago"],
                }
            )
        return data.to_dicts()[0]

    @task.virtualenv(requirements=["polars==1.36.1"], system_site_packages=False)
    def transform_data(data: dict[str, Any]) -> dict[str, Any]:
        import polars as pl

        df = pl.DataFrame([data])
        df = df.with_columns([(pl.col("age") + 1).alias("age_next_year")])
        return df.to_dicts()[0]

    @task
    def load_data(transformed_data: dict[str, Any]):
        print("Transformed Data:")
        print(transformed_data)

    d = extract_data()
    td = transform_data(d)
    load_data(td)


etl_data_processing_dag()
