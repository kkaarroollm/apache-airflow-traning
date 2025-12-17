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
