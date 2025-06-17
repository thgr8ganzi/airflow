from random import choice

from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task
from airflow.providers.email.operators.email import EmailOperator

with DAG (
    dag_id="dags_python_email_xcom",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2023, 10, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    @task(task_id="something_task_id")
    def some_logic(**kwargs):
        from random import choice
        return choice(["success", "fail"])

    send_email = EmailOperator(
        task_id="send_email",
        to="q33as@naver.com",
        subject="{{ data_interval_end.in_timezone('Asia/Seoul') | ds }} - Airflow XCom Email",
        html_content="{{ data_interval_end.in_timezone('Asia/Seoul') | ds }} 처리 결과 <br> \ {{ ti.xcom_pull(task_ids='some_logic') }}",
    )

    some_logic() >> send_email