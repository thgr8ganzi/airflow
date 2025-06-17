from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task
from airflow.operators.bash import BashOperator

with DAG (
    dag_id="dags_python_with_xcom_eg2",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 10, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    @task(task_id="python_xcom_push_by_return")
    def xcom_push_result(**kwargs):
        return "Hello, Airflow with XCom!"

    @task(task_id="python_xcom_pull_1")
    def xcom_pull_1(**kwargs):
        ti = kwargs['ti']
        result = ti.xcom_pull(task_ids='python_xcom_push_by_return')
        print(f"메소드 인자값: {result}")

    @task(task_id="python_xcom_pull_2")
    def xcom_pull_2(**kwargs):
        ti = kwargs['ti']
        result = ti.xcom_pull(task_ids='python_xcom_push_by_return')
        print(f"함수 입력값: {result}")

    python_xcom_push_by_return = xcom_push_result()
    python_xcom_push_by_return >> [xcom_pull_1(), xcom_pull_2()]
