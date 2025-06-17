from airflow import DAG
from airflow.decorators import task, task_group
from airflow.utils.task_group import TaskGroup
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG(
    dag_id='dags_python_with_task_group',
    start_date=datetime(2023, 4, 1),
    schedule=None,
    catchup=False,
) as dag:
    def inner_func(**kwargs):
        msg = kwargs.get('msg') or ''
        print(f'인자로 받은 메시지: {msg}')

    # 첫 번째 TaskGroup: 데코레이터 방식
    @task_group(group_id='first_group')
    def group_1():
        """task_group 데코레이터를 이용한 첫 번째 그룹입니다."""

        @task(task_id='inner_function1')
        def inner_func1(**kwargs):
            print("첫 번째 TaskGroup 내 첫 번째 task입니다.")

        inner_function2 = PythonOperator(
            task_id='inner_function2',
            python_callable=inner_func,
            op_kwargs={'msg': '첫 번째 TaskGroup내 두 번째 task입니다.'}
        )

        inner_func1() >> inner_function2

    # 두 번째 TaskGroup: 컨텍스트 매니저 방식
    with TaskGroup(group_id='second_group', tooltip='두 번째 그룹입니다.') as group_2:
        """TaskGroup 컨텍스트 매니저를 이용한 두 번째 그룹입니다."""
        @task(task_id='inner_function1')
        def inner_func1(**kwargs):
            print('두 번째 TaskGroup 내 첫 번째 task입니다.')

        inner_function2 = PythonOperator(
            task_id='inner_function2',
            python_callable=inner_func,
            op_kwargs={'msg': '두 번째 TaskGroup내 두 번째 task입니다.'}
        )

        inner_func1() >> inner_function2

    # TaskGroup 실행 선언
    group_1() >> group_2
    # group_2는 with 블록에서 이미 DAG에 등록됨
