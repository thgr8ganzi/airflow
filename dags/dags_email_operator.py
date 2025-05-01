from airflow import DAG
import datetime
import pendulum
from airflow.providers.standard.operators.email import EmailOperator

with DAG(
    dag_id="dags_email_operator",
    schedule="0 8 1 * *",
    start_date=pendulum.datetime(2023, 10, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    send_email_task = EmailOperator(
        task_id="send_email_task",
        to="q33as@naver.com",
        subject="Airflow Email Operator Test",
        html_content="<h3>Test Email from Airflow</h3><p>This is a test email sent from Airflow using the EmailOperator.</p>",
    )