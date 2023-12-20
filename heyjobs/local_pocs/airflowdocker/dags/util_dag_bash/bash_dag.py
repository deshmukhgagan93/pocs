# write airflow dag with bash operator
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2020, 10, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'bash_dag',
    default_args=default_args,
    description='A simple bash DAG',
    schedule_interval='@daily',
)

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

t2 = BashOperator(
    task_id='sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    retries=3,
    dag=dag,
)

t3 = BashOperator(
    task_id='print_hello',
    depends_on_past=False,
    bash_command='echo "hello world!!!"',
    retries=3,
    dag=dag,
)

t1 >> t2 >> t3