# from datetime import datetime, timedelta
# from airflow import DAG
# from airflow.operators.bash import BashOperator

# default_args = {
#     'owner': 'johnwell',
#     'retries': 5,
#     'retry_delay': timedelta(minutes=2)
# }

# with DAG(
#     dag_id='our_first_dag_v3',
#     default_args=default_args,
#     description='This is our first dag that I write',
#     start_date=datetime(2024, 10, 14, 00, 00),
#     schedule_interval='@daily',
#     catchup=False  # Optional: disable backfilling for the missed dates
# ) as dag:

#     task1 = BashOperator(
#         task_id='first_task',
#         bash_command="echo hello world, this is the first task!"
#     )

#     task2 = BashOperator(
#         task_id='second_task',
#         bash_command="echo hey, I am the second task after task 1"
#     )
#     task3 = BashOperator(
#         task_id='third_task',
#         bash_command="echo this is task 3"
#     )

#     # Set task dependencies
#     task1 >> [task2,task3]
