from __future__ import annotations
from datetime import datetime, timedelta

# 1. 사용할 Operator import
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

# python 함수 정의
def pipe_start():
    print("데이터 파이프라인 가동 시작!")

def pipe_a():
    print("데이터 추출 완료!")

def pipe_b():
    print("데이터 변환 완료!")

def pipe_end():
    print("데이터 파이프라인 종료!")

# 2. DAG 정의
with DAG(
    dag_id="dag_multi_tasks",  
    default_args={                   
        "depends_on_past": False,
        "retries": 2,
        "retry_delay": timedelta(seconds=5),
    },
    description="DAG Multi Task 예제", 
    schedule=timedelta(days=1),      
    start_date=datetime(2026, 1, 1), 
    catchup=False,   
    tags=["task_multi"],
) as dag:

    # Task 정의 (Operator 사용)
    task_start = PythonOperator(
        task_id="task_start",
        python_callable=pipe_start, 
        retries=3,
    )

    task_A = PythonOperator(
        task_id="task_a",
        python_callable=pipe_a, 
        retries=3,
    )

    task_B = PythonOperator(
        task_id="task_b",
        python_callable=pipe_b, 
        retries=3,
    )

    task_end = PythonOperator(
        task_id="task_end",
        python_callable=pipe_end, 
        retries=3,
    )

    # 4. 의존성 정의 (실행 순서)
    task_start >> [task_A, task_B] >> task_end