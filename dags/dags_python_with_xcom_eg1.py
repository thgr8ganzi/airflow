from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task
from airflow.operators.bash import BashOperator

with DAG (
    dag_id="dags_python_with_xcom_eg1",
    schedule="30 6 * * * *",
    start_date=pendulum.datetime(2023, 10, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    @task(task_id="python_xcom_push_1")
    def xcom_push1(**kwargs):
        ti = kwargs['ti']
        ti.xcom_push(key='result1', value="value_1")
        ti.xcom_push(key='result2', value=[1, 2, 3, 4, ])

    @task(task_id="python_xcom_push_2")
    def xcom_push2(**kwargs):
        ti = kwargs['ti']
        ti.xcom_push(key='result1', value="value_2")
        ti.xcom_push(key='result2', value=[1,2,3,4,])

    @task(task_id="python_xcom_pull_2")
    def  xcom_pull_1(**kwargs):
        ti = kwargs['ti']
        value1 = ti.xcom_pull(key='result1')
        value2 = ti.xcom_pull(key='result2', task_ids='python_xcom_push_1')
        print(f"Pulled XCom result 1: {value1}")
        print(f"Pulled XCom result 2: {value2}")

    xcom_push1() >> xcom_push2() >> xcom_pull_1()