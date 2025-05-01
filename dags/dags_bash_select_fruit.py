from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="plugins/shell_bash_select_fruit",
    schedule="10 0 * * 6#1",
    start_date=pendulum.datetime(2023, 10, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    t1_orange = BashOperator(
        task_id="t1_orange",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh ORANGE",
    )

    t2_apple = BashOperator(
        task_id="t2_apple",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh APPLE",
    )

    t3_banana = BashOperator(
        task_id="t3_banana",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh BANANA",
    )

    t4_grape = BashOperator(
        task_id="t4_grape",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh GRAPE",
    )

    t1_orange >> t2_apple >> t3_banana >> t4_grape