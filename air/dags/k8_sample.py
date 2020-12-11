# -*- coding: utf-8 -*-
"""
Download image
Do face detection and cut out the face
Save face to an output location
"""
from time import sleep

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

default_args = {
    'start_date': days_ago(2),
}


def print_and_sleep():
    print("Hey this the fhe func print and sleep")
    sleep(60)


dag = DAG(
    dag_id='k8_sample',
    default_args=default_args
)

task_print = PythonOperator(
    task_id='print',
    python_callable=print_and_sleep,
    dag=dag,
    executor_config={"KubernetesExecutor": {"image": "apache/airflow:latest"}}
)
