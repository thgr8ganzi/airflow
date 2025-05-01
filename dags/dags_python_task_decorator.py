from airflow import DAG
import pendulum
from airflow.decorators import task
from common.common_func import get_sftp
from airflow.operators.python import PythonOperator

with DAG(
    dag_id="dags_python_task_decorator",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2023, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    @task(task_id="task_get_sftp")
    def task_get_sftp_wrapper():
        get_sftp()  # 외부 함수 호출

    @task(task_id="python_task_1")
    def print_context(some_input):
        print(f"some_input: {some_input}")


    task_get_sftp_wrapper() >> print_context("task_decorator 실행")