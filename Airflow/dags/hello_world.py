from __future__ import annotations
from datetime import datetime, timedelta

# 1. 사용할 Operator import
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

# 2. DAG 정의
with DAG(
    dag_id="dag_hello_world",  
    default_args={                   
        "depends_on_past": False,
        "retries": 2,
        "retry_delay": timedelta(seconds=5),
    },
    description="DAG Hello World 예제", 
    schedule=timedelta(days=1),      
    start_date=datetime(2026, 1, 1), 
    catchup=False,   
    tags=["task_hi"],
) as dag:

    # python 함수 정의
    def print_hello():
        print("hello World!")

    # Task 정의 (Operator 사용)
    task_1 = PythonOperator(
        task_id="task_1",
        python_callable=print_hello, 
        retries=3,
    )

    # 4. 의존성 정의 (실행 순서)
    task_1