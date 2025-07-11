from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
import pendulum

with DAG(
    dag_id="dags_trigger_dag_run_operator",
    start_date=pendulum.datetime(2023, 10, 1, tz="Asia/Seoul"),
    schedule="0 0 * * *",
    catchup=False,
) as dag:
    start_task = BashOperator(
        task_id="start_task",
        bash_command='echo start',
    )

    trigger_task = TriggerDagRunOperator(
        task_id="trigger_dag_task",
        trigger_dag_id="dags_python_operator",
        trigger_run_id=None,
        logical_date='{{data_interval_start}}',  # 또는 실제 datetime 객체/문자열
        reset_dag_run=True,
        wait_for_completion=False,
        poke_interval=60,
        allowed_states=['success'],
        failed_states=['failed'],
    )

    start_task >> trigger_task

