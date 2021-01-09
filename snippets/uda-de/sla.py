"""
A task can take a while to execute. Sometimes we want to specify
an SLA for the operator/task for the duration we want it to
be completed in.
"""
import datetime

from airflow.operators.python_operator import PythonOperator


def copy_data_to_warehouse(*args, **kwargs):
    print('copy data to warehouse')

# need this to complete in an hour
copy_data_task = PythonOperator(
    task_id='copy_data_s3_to_warehouse',
    dag=dag,
    python_callable=copy_data_to_warehouse, 
    provide_context=True,  # pass airflow ctx to operator
    sla=datetime.timedelta(hours=1)
)