from __future__ import annotations
from datetime import datetime, timedelta

# 1. 사용할 Operator import
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

# python 함수 정의
def write_func():
    file_path = "/tmp/airflow_test.txt"
    f = open(file_path, 'w')
    f.write("Airflow 파일 생성 테스트")
    f.close()
    return file_path

def read_func(**context):
    file_path = context['ti'].xcom_pull(task_ids='task_write')
    with open(file_path, 'r') as f:
        content = f.read()  # readline → read (전체 읽기)
        print(content)

def save_func(**context):
    file_path = context['ti'].xcom_pull(task_ids='task_write')
    with open(file_path, "w") as f:
        f.write("내용추가하여 저장")
    f.close()

# 2. DAG 정의
with DAG(
    dag_id="file_pipeline",  
    default_args={                   
        "depends_on_past": False,
        "retries": 2,
        "retry_delay": timedelta(seconds=5),
    },
    description="파일 읽기/쓰기 예제", 
    schedule=timedelta(days=1),      
    start_date=datetime(2026, 1, 1), 
    catchup=False,   
    tags=["file_pipeline"],
) as dag:

    # Task 정의 (Operator 사용)
    task_1 = PythonOperator(
        task_id="task_write",
        python_callable=write_func,
        retries=3,
    )

    task_2 = PythonOperator(
        task_id="task_read",
        python_callable=read_func,
        retries=3,
    )

    task_3 = PythonOperator(
        task_id="task_save",
        python_callable=save_func,
        retries=3,
    )

    # 4. 의존성 정의 (실행 순서)
    task_1 >> task_2 >> task_3