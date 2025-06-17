from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_with_macro_eg2",
    schedule="10 0 * * 6#2",
    start_date=pendulum.datetime(2023, 10, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    bash_task_2 = BashOperator(
        task_id="bash_task_2",
        env={
            "START_DATE": "{{ macros.ds_add(ds, -1) }}",
            "END_DATE": "{{ macros.ds_add(ds, 1) }}",
        }
        bash_command='echo "START_DATE: $START_DATE" && echo "END_DATE: $END_DATE"'
    )