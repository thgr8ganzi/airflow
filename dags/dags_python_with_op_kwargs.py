from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task
from common.common_func import regist2
from airflow.operators.python import PythonOperator

with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    regist2_t1 = PythonOperator(
        task_id="regist2_t1",
        python_callable=regist2,
        op_args=["홍길동", "남자", "서울", "대전"],
        op_kwargs={
            "email": "q33asq33as@gmail.com",
            "phone": "010-1234-5678",
        },
    )

    regist2_t1