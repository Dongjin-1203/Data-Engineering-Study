from __future__ import annotations
from datetime import datetime, timedelta

# 1. 사용할 Operator import
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator

# python 함수 정의
def push_func():
    return "xcom test"

# context 활용 예시
def pull_func(**context):
    value = context['ti'].xcom_pull(task_ids='task_push')
    print(value)

# 2. DAG 정의
with DAG(
    dag_id="xcom_example",  
    default_args={                   
        "depends_on_past": False,
        "retries": 2,
        "retry_delay": timedelta(seconds=5),
    },
    description="XCom 예제", 
    schedule=timedelta(days=1),      
    start_date=datetime(2026, 1, 1), 
    catchup=False,   
    tags=["task_xcom"],
) as dag:

    # Task 정의 (Operator 사용)
    task_1 = PythonOperator(
        task_id="task_push",
        python_callable=push_func,
        retries=3,
    )

    task_2 = PythonOperator(
        task_id="task_pull",
        python_callable=pull_func,
        retries=3,
    )

    # 4. 의존성 정의 (실행 순서)
    task_1 >> task_2