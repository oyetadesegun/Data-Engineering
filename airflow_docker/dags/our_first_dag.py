from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'johnwell',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag2',
    default_args=default_args,
    description='This is our first dag that I write',
    start_date=datetime(2024,10,14,00,00),
    schedule_interval='@daily'
) as dag:
    task1= BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is th first task!"
    )
    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo het, i am the second task after task 1"
    )
    task1.set_downstream(task2)