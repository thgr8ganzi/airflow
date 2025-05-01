from airflow import DAG
import pendulum
from airflow.decorators import task
from airflow.operators.python import PythonOperator

with DAG (
    dag_id="dags_python_template",
    schedule="30 9 * * * *",
    start_date=pendulum.datetime(2023, 10, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    def python_function(start_date, end_date):
        print(f"start_date: {start_date}")
        print(f"end_date: {end_date}")

    python_t1 = PythonOperator(
        task_id="python_t1",
        python_callable=python_function,
        op_kwargs={'start_date': '{{ data_interval_start | ds }}', 'end_date': '{{ data_interval_end | ds }}'},
    )

    @task(task_id="python_t2")
    def python_function2(**kwargs):
        print(kwargs)
        print('ds: ' + str(kwargs['ds']))
        print('ts: ' + str(kwargs['ts']))
        print('data_interval_start: ' + str(kwargs['data_interval_start']))
        print('data_interval_end: ' + str(kwargs['data_interval_end']))
        print('task_instance: ' + str(kwargs['ti']))

    python_t1 >> python_function2()