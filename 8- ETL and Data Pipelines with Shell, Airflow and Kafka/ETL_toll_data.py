# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow.models import DAG
# Operators; you need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Abd Alsttar',
    'start_date': days_ago(0),
    'email': ['abdalsttar.work@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# defining the DAG

# define the DAG
dag = DAG(
    dag_id='ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(days=1),
)

# define the tasks

# Task 2.1: Create a task to unzip data.

unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -xzvf /home/project/airflow/dags/finalassignment/tolldata.tgz --overwrite',
    dag=dag,
)

# Task 2.2: Create a task to extract data from csv file

extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cut -d"," -f1-4 /home/project/airflow/dags/finalassignment/vehicle-data.csv > /home/project/airflow/dags/finalassignment/csv_data.csv',
    dag=dag,
)

# Task 2.3: Create a task to extract data from tsv file
extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command='cut -d"   " -f5-7 /home/project/airflow/dags/finalassignment/tollplaza-data.tsv > /home/project/airflow/dags/finalassignment/tsv_data.csv',
    dag=dag,
)

# Task 2.4: Create a task to extract data from fixed width file
extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command="""awk '{print substr($0,59,3) "," substr($0,63,5)}' /home/project/airflow/dags/finalassignment/payment-data.txt > /home/project/airflow/dags/finalassignment/fixed_width_data.csv""",
    dag=dag,
)

# Task 2.5: Create a task to consolidate data extracted from previous tasks
consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command="""
    cat /home/project/airflow/dags/finalassignment/csv_data.csv\
    /home/project/airflow/dags/finalassignment/tsv_data.csv\
    /home/project/airflow/dags/finalassignment/fixed_width_data.csv\
    > /home/project/airflow/dags/finalassignment/extracted_data.csv
    """,
    dag=dag,
)

# Task 2.6: Transform the data
transform_data = BashOperator(
    task_id='transform_data',
    bash_command="""cut -d"," -f1-3 /home/project/airflow/dags/finalassignment/extracted_data.csv cut -d"," -f4 /home/project/airflow/dags/finalassignment/extracted_data.csv | tr 'a-z' 'A-Z' cut -d"," -f5-9 /home/project/airflow/dags/finalassignment/extracted_data.csv > /home/project/airflow/dags/finalassignment/staging/transformed_data.csv""",
    dag=dag,
)

# Task 2.7: Define the task pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data


# must check syntax errors in the terminal yourself
# use the line below
# airflow dags list-import-errors