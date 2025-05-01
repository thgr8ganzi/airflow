from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task
from common.common_func import regist
from airflow.operators.python import PythonOperator

with DAG(
    dag_id="dags_python_with_op_args",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    regist_t1 = PythonOperator(
        task_id="regist_t1",
        python_callable=regist,
        op_args=["홍길동", "남자", "서울", "대전"],
    )

    regist_t1