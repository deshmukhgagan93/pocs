from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago


with DAG(
    dag_id='test_bash_dag',
    schedule_interval="@once",
    start_date=days_ago(2),
) as dag:

    run_this_last = BashOperator(
        task_id='run_this_last',
        bash_command='echo 1',
    )


run_this = BashOperator(
    task_id='run_after_loop',
    bash_command='echo 1 2 3 4 5',
)

run_this >> run_this_last

