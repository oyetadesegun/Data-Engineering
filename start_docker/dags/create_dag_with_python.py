from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'johnwell',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name',key='first_name')
    last_name= ti.xcom_pull(task_ids='get_name', key='last_name')
    age= ti.xcom_pull(task_ids='get_ageTask',key='get_ageKey')
    print(f"Hello World! My name is {first_name} {last_name}, and I am {age} years old.")

def get_age(ti):
    ti.xcom_push(key='get_ageKey',value= 30)
def get_name(ti):
    ti.xcom_push(key='first_name',value='Jerry')
    ti.xcom_push(key='last_name',value='Fridman')

with DAG(
    dag_id='our_dag_with_python_operator_V3',
    description='Our first dag using python operator',
    default_args=default_args,  # Moved default_args inside DAG()
    start_date=datetime(2024, 11, 1),
    schedule_interval='@daily'
) as dag:
    task0 = PythonOperator(
        task_id='get_ageTask',
        python_callable=get_age
    )
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet
       # op_kwargs={'age':20}
    )
    task2= PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )

[task2, task0] >> task1