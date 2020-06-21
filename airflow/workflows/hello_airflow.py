"""A sample tutorial DAG `Hello, Airflow`.
"""
from datetime import timedelta
from textwrap import dedent

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'hello_airflow',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(minutes=1),
) as dag:
    """A simple tutorial DAG definition.
    """

    dag.doc_md = __doc__

    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t1.doc_md = dedent("""
    #### Task Documentation
    タスクノードとしての Operator インスタンスの `doc_md` 属性を利用してタスクの内容を文書化できます。
    マークダウンの他にも JSON や YAML でも記述が可能です。
    """.strip())

    t2 = BashOperator(
        task_id='sleep',
        bash_command='sleep 5',
        retries=5,
    )

    templated_command = dedent("""
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7) }}"
        echo "{{ params.my_param }}"
    {% endfor %}
    """.strip())

    t3 = BashOperator(
        task_id='templated',
        bash_command=templated_command,
        params={'my_param': 'Parameter I passed in'},
    )

    def greet(*, s: str) -> None:
        print(s)

    t4 = PythonOperator(
        task_id='python',
        python_callable=greet,
        op_kwargs={'s': 'Hello, world!'},
    )

    # Dependencies among tasks
    t1 >> [t2, t3] >> t4
