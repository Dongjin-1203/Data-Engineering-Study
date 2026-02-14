# 데이터 엔지니어링 1달차 주간 계획표

> **목표**: Airflow 기초 + 데이터 모델링 & ETL 마스터  
> **학습 시간**: 월~금 3-4시간 (주 15-20시간)  
> **기간**: 4주

---

## 📅 Week 1: Airflow 환경 구축 & 기본 개념

### 월요일 (3시간)(26.02.10 완료)
**주제**: Airflow 개요 및 환경 설정
- [x] Airflow 공식 문서 읽기 (1시간)
  - 핵심 개념: DAG, Operator, Task, Executor
  - https://airflow.apache.org/docs/apache-airflow/stable/concepts/index.html
- [x] Docker로 Airflow 로컬 환경 구축 (2시간)
  - `docker-compose.yaml` 설정
  - Airflow UI 접속 및 탐색
  - 참고: https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

### 화요일 (4시간)(26.02.13 완료)
**주제**: 첫 번째 DAG 작성
- [x] 기본 DAG 구조 이해 (1시간)
  - DAG 파라미터: `start_date`, `schedule_interval`, `catchup`
- [x] PythonOperator로 간단한 DAG 작성 (2시간)
  - 예제: Hello World DAG
  - Task 간 의존성 설정 (`>>` 연산자)
- [x] DAG 실행 및 로그 확인 (1시간)
  - UI에서 Task 상태 모니터링
  - 로그 디버깅 연습

### 수요일 (3.5시간)(26.02.13 완료)
**주제**: 다양한 Operator 실습
- [x] BashOperator 사용법 (1시간)
  - Shell 명령어 실행
- [x] PythonOperator 심화 (1.5시간)
  - 함수에 인자 전달 (`op_kwargs`)
  - 반환값 활용
- [x] 실습 과제 (1시간)
  - DAG 1: 데이터 다운로드 → 전처리 → 저장 (3개 Task)

### 목요일 (4시간)(26.02.14 완료)
**주제**: 스케줄링 & 백필
- [x] Cron 표현식 학습 (1시간)
  - `@daily`, `@hourly`, 커스텀 스케줄
  - https://crontab.guru/ 활용
- [ ] `catchup` 파라미터 이해 (1시간)
  - 과거 데이터 재처리 전략
- [X] 실습 (2시간)
  - 매일 자정 실행되는 배치 DAG 작성
  - 백필 테스트 (과거 7일치 데이터 처리)

### 금요일 (3.5시간)(26.02.13 완료)
**주제**: Task 간 데이터 전달 (XCom)
- [x] XCom 개념 및 사용법 (1.5시간)
  - `ti.xcom_push()`, `ti.xcom_pull()`
  - XCom의 한계점 이해 (크기 제한)
- [x] 실습 (2시간)
  - DAG 2: Task A에서 계산 → Task B에서 결과 활용
  - AdGen AI 시나리오: 이미지 개수 카운트 → 알림 Task

**주말 복습 과제**
- [x] Week 1 내용 정리 (노션/블로그)
- [ ] Airflow Best Practices 문서 읽기
- [x] 막힌 부분 재학습

---

## 📅 Week 2: Airflow 심화 & AdGen AI 파이프라인 설계

### 월요일 (4시간)
**주제**: TaskFlow API (최신 방식)
- [ ] TaskFlow API 개념 (1시간)
  - `@task` 데코레이터
  - 자동 XCom 처리
- [ ] 기존 DAG를 TaskFlow로 재작성 (2시간)
- [ ] 실습 (1시간)
  - Week 1 실습 과제를 TaskFlow로 변환

### 화요일 (3.5시간)(26.02.13 완료)
**주제**: 에러 핸들링 & 재시도
- [x] Task 실패 시나리오 (1시간)
  - `retries`, `retry_delay` 파라미터
  - `on_failure_callback` 설정
- [x] 실습 (2.5시간)
  - 일부러 실패하는 Task 만들기
  - 재시도 로직 테스트
  - Slack/Email 알림 설정 (선택)

### 수요일 (4시간)
**주제**: AdGen AI 파이프라인 설계 (1) - 분석
- [ ] AdGen AI 현재 워크플로우 분석 (1.5시간)
  - 이미지 업로드 → Vision AI 분석 → 결과 저장
  - 병목 지점 파악
- [ ] 파이프라인 아키텍처 설계 (1.5시간)
  - DAG 구조 스케치
  - Task 단위 나누기 (Extract → Transform → Load)
- [ ] 필요한 Operator 조사 (1시간)
  - PostgresOperator, GoogleCloudStorageOperator 등

### 목요일 (4시간)
**주제**: AdGen AI 파이프라인 설계 (2) - 구현
- [ ] PostgreSQL 연동 설정 (1시간)
  - Airflow Connection 설정
  - PostgresHook 사용법
- [ ] 이미지 처리 Task 작성 (2시간)
  - Task 1: 미처리 이미지 목록 조회 (PostgreSQL)
  - Task 2: Vision AI 호출 (Python)
  - Task 3: 결과 DB 저장
- [ ] 로컬 테스트 (1시간)

### 금요일 (3.5시간)
**주제**: 파이프라인 최적화 & 문서화
- [ ] Dynamic Task 생성 (1.5시간)
  - 여러 이미지를 병렬 처리
  - `expand()` 메서드 활용 (TaskFlow)
- [ ] 파이프라인 문서화 (1시간)
  - DAG 설명 (`doc_md`)
  - Task별 주석 작성
- [ ] Week 2 회고 (1시간)
  - 잘된 점 / 개선할 점
  - 다음 주 계획 조정

**주말 복습 과제**
- [ ] Airflow 실전 예제 찾아보기 (Medium, GitHub)
- [ ] AdGen AI 파이프라인 리팩토링
- [ ] Week 1-2 내용 정리 문서 작성

---

## 📅 Week 3: 데이터 모델링 기초 & dbt 시작

### 월요일 (4시간)
**주제**: 데이터 웨어하우스 모델링 이론
- [ ] Star Schema vs Snowflake Schema (1.5시간)
  - Fact 테이블 vs Dimension 테이블
  - 정규화 vs 비정규화
  - 참고 강의: "Data Warehouse Fundamentals" (YouTube)
- [ ] AdGen AI 데이터 모델링 설계 (2.5시간)
  - 엔티티 파악: 사용자, 광고, 이미지, Vision 결과
  - ERD 작성 (draw.io 또는 dbdiagram.io)
  - Fact 테이블: `fact_ad_generation`, `fact_vision_analysis`
  - Dimension 테이블: `dim_users`, `dim_products`, `dim_dates`

### 화요일 (3.5시간)
**주제**: dbt 환경 설정
- [ ] dbt 개념 이해 (1시간)
  - ELT vs ETL
  - dbt의 역할 (T - Transform)
- [ ] dbt 설치 및 초기화 (1.5시간)
  - `pip install dbt-postgres`
  - `dbt init adgen_analytics`
  - `profiles.yml` 설정 (PostgreSQL 연결)
- [ ] 첫 번째 모델 작성 (1시간)
  - `models/staging/stg_users.sql`
  - `dbt run` 실행

### 수요일 (4시간)
**주제**: dbt 모델 작성 기초
- [ ] Staging 레이어 모델 작성 (2시간)
  - `stg_images.sql`: Raw 이미지 데이터 정제
  - `stg_vision_results.sql`: Vision AI 결과 정제
  - 네이밍 컨벤션, 타입 캐스팅
- [ ] ref() 함수 이해 (1시간)
  - 모델 간 의존성 설정
  - Lineage 그래프 확인 (`dbt docs generate`)
- [ ] 실습 (1시간)
  - Staging 모델 3개 이상 작성

### 목요일 (4시간)
**주제**: Intermediate & Mart 레이어
- [ ] Intermediate 모델 작성 (2시간)
  - `int_user_ad_summary.sql`: 사용자별 광고 생성 통계
  - `int_vision_accuracy.sql`: Vision AI 정확도 계산
- [ ] Mart 모델 작성 (2시간)
  - `mart_daily_performance.sql`: 일별 성과 대시보드용
  - `mart_user_behavior.sql`: 사용자 행동 분석용
  - Materialization 전략 (`table` vs `view`)

### 금요일 (3.5시간)
**주제**: dbt 테스트 & 문서화
- [ ] Schema 테스트 작성 (1.5시간)
  - `schema.yml` 파일 생성
  - `unique`, `not_null`, `accepted_values` 테스트
  - 커스텀 테스트 작성 (예: 정확도는 0-1 사이)
- [ ] 문서화 (1시간)
  - 모델별 `description` 작성
  - 컬럼 설명 추가
  - `dbt docs generate && dbt docs serve`
- [ ] 전체 파이프라인 실행 (1시간)
  - `dbt run` → `dbt test`
  - 에러 디버깅

**주말 복습 과제**
- [ ] dbt Best Practices 문서 읽기
- [ ] AdGen AI 데이터 모델 개선안 작성
- [ ] Week 3 학습 내용 블로그 정리

---

## 📅 Week 4: dbt 심화 & Airflow 통합

### 월요일 (4시간)
**주제**: dbt 고급 기능
- [ ] Jinja 템플릿 활용 (2시간)
  - `{{ }}` 문법, 변수, 반복문
  - `{% if %}` 조건문으로 동적 SQL 생성
- [ ] Macros 작성 (2시간)
  - 재사용 가능한 SQL 함수
  - 예: `get_date_range()`, `calculate_accuracy()`
  - `macros/` 폴더에 저장

### 화요일 (3.5시간)
**주제**: Incremental 모델
- [ ] Incremental 전략 이해 (1.5시간)
  - 전체 재계산 vs 증분 업데이트
  - `is_incremental()` 매크로
- [ ] 실습 (2시간)
  - `fact_ad_generation` 테이블을 incremental로 변환
  - `unique_key` 설정
  - 백필 테스트

### 수요일 (4시간)
**주제**: dbt + Airflow 통합 (1)
- [ ] BashOperator로 dbt 실행 (1.5시간)
  - Airflow DAG에서 `dbt run` 호출
  - 로그 확인 방법
- [ ] dbt 전용 Operator 사용 (2시간)
  - `pip install airflow-dbt`
  - `DbtRunOperator`, `DbtTestOperator` 설정
- [ ] 실습 (0.5시간)
  - Airflow → dbt 파이프라인 테스트

### 목요일 (4시간)
**주제**: dbt + Airflow 통합 (2) - End-to-End 파이프라인
- [ ] 전체 파이프라인 설계 (1시간)
  - Task 1: 이미지 처리 (Airflow)
  - Task 2: Raw 데이터 적재 (Airflow)
  - Task 3: dbt 모델 실행 (dbt via Airflow)
  - Task 4: 테스트 실행 (dbt test)
- [ ] 구현 (2.5시간)
  - DAG 작성 및 테스트
  - Task 의존성 설정
- [ ] 에러 처리 (0.5시간)
  - dbt 실패 시 알림

### 금요일 (3.5시간)
**주제**: Month 1 총정리 & 포트폴리오 문서화
- [ ] 전체 파이프라인 최종 점검 (1시간)
  - 엔드투엔드 실행 테스트
  - 성능 측정 (실행 시간 기록)
- [ ] 문서화 (1.5시간)
  - README.md 작성 (아키텍처 다이어그램 포함)
  - 트러블슈팅 경험 정리
- [ ] Month 1 회고 (1시간)
  - 학습 성과 정리
  - Month 2 계획 조정
  - 부족한 부분 파악

**주말 복습 과제**
- [ ] Month 1 전체 내용 복습
- [ ] 블로그 포스팅: "Airflow + dbt로 데이터 파이프라인 구축하기"
- [ ] GitHub에 코드 정리 및 푸시

---

## 📚 추천 학습 자료

### Airflow
- **공식 문서**: https://airflow.apache.org/docs/
- **튜토리얼**: "Apache Airflow Tutorial for Beginners" (YouTube, 2시간)
- **책**: "Data Pipelines with Apache Airflow" (Manning)

### dbt
- **공식 문서**: https://docs.getdbt.com/
- **무료 강의**: dbt Learn Courses (https://courses.getdbt.com/)
- **예제**: dbt Labs GitHub (jaffle_shop 프로젝트)

### 데이터 모델링
- **강의**: "The Data Warehouse Toolkit" by Kimball (책/영상)
- **도구**: dbdiagram.io, draw.io

---

## ✅ Month 1 체크리스트

### 기술 스킬
- [ ] Airflow DAG 작성 능력
- [ ] Task 간 의존성 관리
- [ ] XCom 활용
- [ ] 에러 핸들링 및 재시도 전략
- [ ] dbt 모델 작성 (Staging → Mart)
- [ ] dbt 테스트 및 문서화
- [ ] Airflow + dbt 통합

### 산출물
- [ ] AdGen AI 이미지 처리 파이프라인 (Airflow)
- [ ] AdGen AI 데이터 모델 (ERD)
- [ ] dbt 프로젝트 (5개 이상 모델)
- [ ] End-to-End 파이프라인 (Airflow + dbt)
- [ ] 기술 블로그 포스팅 1-2개

### 포트폴리오
- [ ] GitHub 레포지토리 정리
- [ ] README.md 작성 (아키텍처, 실행 방법)
- [ ] 회고록 (학습 과정, 트러블슈팅)

---

## 💡 학습 팁

1. **매일 학습 일지 작성**: 노션이나 블로그에 TIL(Today I Learned) 기록
2. **실습 중심**: 이론 30%, 실습 70% 비율 유지
3. **막힐 때**: Stack Overflow, Airflow Slack, dbt Discourse 활용
4. **주말 활용**: 평일에 못한 부분 보충, 심화 학습
5. **건강 관리**: 과도한 학습보다 꾸준함이 중요

---

**작성일**: 2025년 2월  
**목표**: Airflow + dbt 마스터로 데이터 엔지니어링 기초 완성

> 화이팅입니다! 궁금한 점이 있으면 언제든 물어보세요 🚀
