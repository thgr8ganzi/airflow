from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.decorators import task
from airflow.exceptions import AirflowException
from datetime import datetime

with DAG(
    dag_id='dags_python_with_trigger_rule_eg1',
    start_date=datetime(2023, 4, 1),
    schedule=None,
    catchup=False,
) as dag:

    bash_upstream_1 = BashOperator(
        task_id='bash_upstream_1',
        bash_command='echo upstream1'
    )

    @task(task_id='python_upstream_1')
    def python_upstream_1():
        raise AirflowException('downstream_1 Exception!')

    @task(task_id='python_upstream_2')
    def python_upstream_2():
        print('정상 처리')

    @task(task_id='python_downstream_1', trigger_rule='all_done')
    def python_downstream_1():
        print('정상 처리')

    # 의존성 설정
    [bash_upstream_1, python_upstream_1(), python_upstream_2()] >> python_downstream_1()
