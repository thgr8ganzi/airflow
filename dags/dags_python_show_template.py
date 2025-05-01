from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG (
    dag_id="dags_bash_with_template",
    schedule="30 9 * * * ",
    start_date=pendulum.datetime(2025, 4, 30, tz="Asia/Seoul"),
    catchup=True,
) as dag:

    @task(task_id='python_task')
    def show_templates(**kwargs):
        from pprint import pprint
        pprint(kwargs)

    show_templates()