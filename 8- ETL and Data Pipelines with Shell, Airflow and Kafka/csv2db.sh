# This script
# Extracts data from /etc/passwd file into a CSV file.

# The csv data file contains the user name, user id and
# home directory of each user account defined in /etc/passwd

# Transforms the text delimiter from ":" to ",".
# Loads the data from the CSV file into a table in PostgreSQL database.

# Exercise 4 - Create a table
# In this exercise we will create a table called users in the PostgreSQL database using PostgresSQL CLI. This table will hold the user account information.

# The table users will have the following columns:
# uname
# uid
# home

# You will connect to template1 database which is already available by default. To connect to this database, run the following command at the 'postgres=#' prompt.


# plaintext
# \c template1
# You will get the following message.

# You are now connected to database "template1" as user "postgres".

# Also, your prompt will change to 'template1=#'.

# Run the following statement at the 'template1=#' prompt to create the table.

# plaintext
# create table users(username varchar(50),userid int,homedirectory varchar(100));
# If the table is created successfully, you will get the message below.
# CREATE TABLE


# start of the script 👇

# Extract phase

echo "Extracting data ..."

# Extract the columns 1 (user name), 2 (user id) and 
# 6 (home directory path) from /etc/passwd

cut -d":" -f1,3,6 /etc/passwd > extracted-data.txt

# Transform phase
echo "Transforming data ..."
# read the extracted data and replace the colons with commas.

tr ":"  "," < extracted-data.txt >transformed-data.csv

# Load phase
echo "Loading data"
# Set the PostgreSQL password environment variable.
# Replace <yourpassword> with your actual PostgreSQL password.
export PGPASSWORD=ctLYdAygQoMl1anCothKWyQl;
# Send the instructions to connect to 'template1' and
# copy the file to the table 'users' through command pipeline.
echo "\c template1;\COPY users  FROM '/home/project/transformed-data.csv' DELIMITERS ',' CSV;" | psql --username=postgres --host=postgres

echo "SELECT * FROM users;" | psql --username=postgres --host=postgres template1