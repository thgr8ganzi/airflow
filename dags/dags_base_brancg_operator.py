import pendulum
from airflow import DAG
from airflow.operators.branch import BaseBranchOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG(
    dag_id="dags_base_branch_operator",
    start_date=pendulum.datetime(2023, 10, 1, tz="UTC"),
    schedule=None,
    catchup=False,
) as dag:
    class CustomBranchOperator(BaseBranchOperator):
        def choose_branch(self, context):
            import random
            print(context)

            item_lst = ['A', 'B', 'C']
            selected_item = random.choice(item_lst)
            if selected_item == 'A':
                return 'task_a'
            elif selected_item in ['B', 'C']:
                return ['task_b', 'task_c']


    def common_func(**kwargs):
        print(kwargs['selected'])

    custom_branch_operator = CustomBranchOperator(
        task_id='python_branch_task'
    )

    task_a = PythonOperator(
        task_id="task_a",
        python_callable=common_func,
        op_kwargs={'selected': 'A'},
    )

    task_b = PythonOperator(
        task_id="task_b",
        python_callable=common_func,
        op_kwargs={'selected': 'B'},
    )

    task_c = PythonOperator(
        task_id="task_c",
        python_callable=common_func,
        op_kwargs={'selected': 'C'},
    )

    custom_branch_operator >> [task_a, task_b, task_c]
