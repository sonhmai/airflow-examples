from datetime import timedelta

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.dummy_operator import DummyOperator
from airflow.contrib.operators.kubernetes_pod_operator import \
    KubernetesPodOperator

default_args = {
    'start_date': days_ago(1)
}

dag = DAG(
    'k8s_operator_sample',
    default_args=default_args,
    schedule_interval=timedelta(minutes=10)
)

start = DummyOperator(task_id='run_this_first', dag=dag)

passing = KubernetesPodOperator(
    namespace='airflow',
    image='python:3.6',
    cmds=["python", "-c"],
    arguments=["print('hello world from python')"],
    labels={"foo": "bar"},
    name="passing-test",
    task_id="passing-task",
    get_logs=True,
    dag=dag,
    in_cluster=True
)

failing = KubernetesPodOperator(
    namespace='airflow',
    image="ubuntu:16.04",
    cmds=["python", "-c"],
    arguments=["print('hello world')"],
    labels={"foo": "bar"},
    name="fail",
    task_id="failing-task",
    get_logs=True,
    dag=dag,
    in_cluster=True
)

passing.set_upstream(start)
failing.set_upstream(start)
