# -*- coding: utf-8 -*-
"""
Download image
Do face detection and cut out the face
Save face to an output location
"""
from pathlib import Path

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from air.utils.io import download_to_filename

url = 'https://i1-vnexpress.vnecdn.net/2020/12/07/Le-Ho-ng-Nam-1-7360-1607352350.jpg' \
      '?w=680&h=0&q=100&dpr=2&fit=crop&s=y8Y0l3K84HmvBk8-J061Vw'

module_dir = Path(__file__)
image_path = module_dir.with_name("image.jpg")
# download_to_filename(url, image_path)

default_args = {
      'start_date': days_ago(2),
}

dag = DAG(
      dag_id='face_dag',
      description='Download and extract face of image to output location',
      default_args=default_args
)

task_download_image = PythonOperator(
      task_id='download_image',
      python_callable=download_to_filename,
      op_args=(url, image_path),
      dag=dag
)



