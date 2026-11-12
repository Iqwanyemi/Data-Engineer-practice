1. on_failure_callback   # Runs when task fails
on_success_callback   # Runs when task succeeds

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def my_task():
    print("Task executed")

def success_alert(context):
    print(f"Task {context['task_instance'].task_id} succeeded!")

def failure_alert(context):
    print(f"Task {context['task_instance'].task_id} failed!")

task = PythonOperator(
    task_id="sample_task",
    python_callable=my_task,
    on_success_callback=success_alert,
    on_failure_callback=failure_alert
)
=========================================================================
2. depends_on_past:if true,a task cant run unless the previous schedule succeeded
========================================================================
  3. sample dag with dependencies:
    from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def task_a():
    print("Task a is done")

def task_b():
    print("Task b is done")

def task_c():
    print("Task c is done")

with DAG(
    dag_id="sample_dag",
    start_date=datetime(2026, 1, 1),
    schedule="@daily"
) as dag:

    a = PythonOperator(
        task_id="task_a",
        python_callable=task_a
    )

    b = PythonOperator(
        task_id="task_b",
        python_callable=task_b
    )

    c = PythonOperator(
        task_id="task_c",
        python_callable=task_c
    )

    [a, b] >> c

=====================================
4.Create an Airflow DAG named weekday_half_hour_dag that 
runs every 30 minutes on weekdays (Monday-Friday), executes the run_the_data_pipeline task which calls run_job(), retries failed executions up to 3 times, and waits 5 minutes between retries.

  from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def run_job():
    print("run the pipeline")

default_args = {
    "retries": 3,
    "retry_delay": timedelta(minutes=5)
}

with DAG(
    dag_id="weekday_half_hour_dag",
    start_date=datetime(2026, 1, 1),
    schedule="*/30 * * * 1-5",
    catchup=False,
    default_args=default_args
) as dag:

    task = PythonOperator(
        task_id="run_the_data_pipeline",
        python_callable=run_job
    )
  ===============================================
5.Interview Answer: How to Run DAG2 After DAG1 in Airflow?
We can use TriggerDagRunOperator to trigger DAG2 after DAG1 completes successfully.
    Interview Answer: "In Cloud Composer, I use TriggerDagRunOperator to trigger
    the second DAG after the first DAG's tasks complete successfully. Alternatively, I can use ExternalTaskSensor when DAG2 needs to wait for DAG1."

