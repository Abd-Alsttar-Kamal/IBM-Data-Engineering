8- ETL and Data Pipelines with Shell, Airflow and Kafka

Final Assignment


Project Overview
Instructions
Now that you are equipped with the knowledge and skills to extract, transform and load data you will use these skills to perform ETL, create a pipeline and upload the data into a database. 

You will be using the BashOperator with Airflow in the mandatory hands-on lab.

The following labs are optional:

[Optional] Hands-on Lab: Build an ETL Pipeline using PythonOperator with Apache Airflow

[Optional] Hands-on Lab: Build a Streaming ETL Pipeline using Kafka

Please note that these optional labs are not considered for final grading.

Scenario
You are a data engineer at data analytics consulting company. You have been assigned a project to decongest the national highways by analyzing the road traffic data from different toll plazas. Each highway is operated by a different toll operator with a different IT setup that uses different file formats. Your job is to collect data available in different formats and consolidate it into a single file.

In this assignment, you will develop an Apache Airflow DAG that will:

Extract data from a csv file

Extract data from a tsv file

Extract data from a fixed-width file

Transform the data

Load the transformed data into the staging area

Grading Criteria
There are a total of 25 points for 13 tasks in this final project spread in one hands-on lab. 

Your final assignment will be evaluated through both AI-based grading and peer review, involving learners who are completing the assignment in the same session. Your grade will be determined based on the following tasks:

Exercise 1: Create imports, DAG argument and definition

Task 1.1: Define DAG arguments (2pts)

Task 1.2: Define the DAG (2pts)

Exercise 2: Create the tasks using BashOperator

Task 2.1: Create a task to unzip data. (2pts)

Task 2.2: Create a task to extract data from csv file (2pts)

Task 2.3: Create a task to extract data from tsv file (2pts)

Task 2.4: Create a task to extract data from fixed width file (2pts)

Task 2.5: Create a task to consolidate data extracted from previous tasks (2pts)

Task 2.6: Transform the data (2 pts)

Task 2.7: Define the task pipeline (1pt)

Exercise 3: Getting the DAG operational

Task 3.1: Submit the DAG (1pt)

Task3.2: Unpause and trigger the DAG (3pt)

Task 3.3: List the DAG tasks (2 pt)

Task 3.4: Monitor the DAG (2pt)

How to submit
You are required to save screenshots of all tasks, including the code and corresponding outputs, in a folder for submission. All screenshots must be in JPEG or PNG format and will need to be uploaded during the Final Project submission. Throughout the labs, you will be prompted to capture these screenshots, and the same files should be submitted later for the AI Grading (or) Peer Review sections of the course. 

----------------------------------------------------------------

Set up the lab environment
1- Start Apache Airflow.

2- Open a terminal and create a directory structure for the staging area as follows:
/home/project/airflow/dags/finalassignment/staging.
sudo mkdir -p /home/project/airflow/dags/finalassignment/staging


3- Execute the following commands to give appropriate permission to the directories.
sudo chmod -R 777 /home/project/airflow/dags/finalassignment


4- Download the data set from the source to the following destination using the curl command.
sudo curl https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz -o /home/project/airflow/dags/finalassignment/tolldata.tgz

