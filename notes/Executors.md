# Executors

[How Executor run task?](https://albertusk95.github.io/posts/2019/11/how-airflow-executes-tasks/)

## Sequential
## Local
## Celery
## Kubernetes  
PROS
- can scale to 0 when low traffic

CONS
- overhead in secs for pod to spin up

Ways of making DAGs available to executors
- Ensure image already contains DAG code - **recommended for large DAG folders**
- Mount volume with DAGs - **recommended for development and small DAGs**
