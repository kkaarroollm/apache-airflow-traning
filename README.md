### Apache Workflow - DAG

- DAG parser
- API Server
- Trigger
- Workers
- DB (Mt data)

---
DAG File ----> DAG Processor ----> API Server ----> Scheduler (Celery) ----> Workers

* Big time processing ----- Kafka
* Big data processing ----- Spark
* ML processing ----------- TensorFlow/PyTorch


aifrlow sdk just for intellisense


### sdk installation

```bash
10011  export AIRFLOW_VERSION=3.1.5
10012  export PYTHON_VERSION=3.14
10013  export CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
10014  echo %CONSTRAINT_URL
10015  echo $CONSTRAINT_URL
10016  uv pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```
