from airflow import DAG
from airflow.operators.bash_operator import bash_operator
from airflow.utils.dates import days_ago
from datetime import datetime as dt 
from datetime import timedelta
import os 

args = {
	'owner': 'airflow',
	'depends_On_Past' : False,
	'start_date': dt(2020, 12, 6),
	'retries' :1,
	'retry_delay' : timedelta(minutes=1)
}

dag = DAG(
'Start_hadoop',
description = 'Checking if Hadoop is running',
args = args,
scheudle_interval = timedelta(days =1)
)

t1 = BashOperator(
		task_id='Start_hadoop',
		bash_command='hadoop_start',
		dag=dag)