from __future__ import annotations
from datetime import datetime, timedelta

# 1. 사용할 Operator import
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

# python 함수 정의
def fail_func():
    raise Exception("의도적 실패!")

def success_func():
    print("Task succeeded!")

# 2. DAG 정의
with DAG(
    dag_id="retry_example",  
    default_args={                   
        "depends_on_past": False,
        "retries": 2,
        "retry_delay": timedelta(seconds=5),
    },
    description="Retry 예제", 
    schedule=timedelta(days=1),      
    start_date=datetime(2026, 1, 1), 
    catchup=False,   
    tags=["task_retry"],
) as dag:

    # Task 정의 (Operator 사용)
    task_1 = PythonOperator(
        task_id="task_success",
        python_callable=success_func,
        retries=3,
    )

    task_2 = PythonOperator(
        task_id="task_fail",
        python_callable=fail_func,
        retries=3,
    )

    # 4. 의존성 정의 (실행 순서)
    task_1 >> task_2