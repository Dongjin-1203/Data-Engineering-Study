from __future__ import annotations
from datetime import datetime, timedelta

# 1. 사용할 Operator import
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator

# python 함수 정의
def nodash(d1):
    print(f"ds_nodash: {d1}")

# context 활용 예시
def nodash_context(**context):
    ds = context["ds"]
    ds_nodash = context["ds_nodash"]
    run_id = context["run_id"]
    print(f"ds: {ds}")
    print(f"ds_nodash: {ds_nodash}")
    print(f"run_id: {run_id}")

# 템플릿 변수 정의
templated_command = """
echo "ds: {{ds}}" 
"""

# 2. DAG 정의
with DAG(
    dag_id="dag_template_variable",  
    default_args={                   
        "depends_on_past": False,
        "retries": 2,
        "retry_delay": timedelta(seconds=5),
    },
    description="DAG template_variable 예제", 
    schedule=timedelta(days=1),      
    start_date=datetime(2026, 1, 1), 
    catchup=False,   
    tags=["task_template"],
) as dag:

    # Task 정의 (Operator 사용)
    task_1 = BashOperator(
        task_id="task_ds",
        bash_command=templated_command, 
        retries=3,
    )

    task_2 = PythonOperator(
        task_id="task_nodash",
        python_callable=nodash,
        op_kwargs={"d1": "{{ ds_nodash }}"}, 
        retries=3,
    )

    task_3 = PythonOperator(
        task_id="task_nodash_context",
        python_callable=nodash_context, 
        retries=3,
    )

    task_4 = BashOperator(
        task_id="sleep",
        depends_on_past=False,
        bash_command="sleep 5",
        retries=3,               # 이 Task만 3회 재시도 (default_args 오버라이드)
    )

    # 4. 의존성 정의 (실행 순서)
    task_1 >> [task_2, task_3, task_4]