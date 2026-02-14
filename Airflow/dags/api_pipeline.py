from __future__ import annotations
from datetime import datetime, timedelta
import requests

# 1. 사용할 Operator import
from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator

# python 함수 정의
def fetch_func():

    # API 호출하여 데이터 가져오기
    api_url = "https://api.open-meteo.com/v1/forecast?latitude=37.5665&longitude=126.9780&current=temperature_2m,wind_speed_10m"
    response = requests.get(api_url)

    if response.status_code != 200:
        raise Exception(f"API 호출 실패: {response.status_code}")

    return response.json()

def parse_func(**context):
    data = context['ti'].xcom_pull(task_ids='task_fetch')

    temperature = data['current']['temperature_2m']
    wind_speed = data['current']['wind_speed_10m']

    temperature_unit = data['current_units']['temperature_2m']
    wind_speed_unit = data['current_units']['wind_speed_10m']

    print(f"서울시 현재 온도: {temperature} {temperature_unit}")
    print(f"서울시 현재 풍속: {wind_speed} {wind_speed_unit}")

    temp_speed_info = {
        "기온": f"{temperature} {temperature_unit}", 
        "풍속": f"{wind_speed} {wind_speed_unit}"
        }
    
    return temp_speed_info

def save_func(**context):
    parse_data = context['ti'].xcom_pull(task_ids='task_parse')
    file_path = "/opt/airflow/dags/api_output.txt"
    
    with open(file_path, "w") as f:
        f.write("데이터 파싱 결과 \n")
        for k in parse_data.keys():
            f.write(f"{k}: {parse_data[k]}\n")

    return file_path

# 2. DAG 정의
with DAG(
    dag_id="API_pipeline",  
    default_args={                   
        "depends_on_past": False,
        "retries": 2,
        "retry_delay": timedelta(seconds=5),
    },
    description="API 호출 예제", 
    schedule=timedelta(days=1),      
    start_date=datetime(2026, 1, 1), 
    catchup=False,   
    tags=["API_pipeline"],
) as dag:

    # Task 정의 (Operator 사용)
    task_1 = PythonOperator(
        task_id="task_fetch",
        python_callable=fetch_func,
        retries=3,
    )

    task_2 = PythonOperator(
        task_id="task_parse",
        python_callable=parse_func,
        retries=3,
    )
    
    task_3 = PythonOperator(
        task_id="task_save",
        python_callable=save_func,
        retries=3,
    )

    # 4. 의존성 정의 (실행 순서)
    task_1 >> task_2 >> task_3