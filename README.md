# capstone Covid_19 project 

## Project Overview


# EXTRACTING THE DATA FILE FROM MS ACCESS DATABASE
This code extracts the data file from an MS Access database and loads it into a Pandas DataFrame. The code first connects to the MS Access database using the pyodbc module. Then, it uses the cursor object to get the list of table names in the database. Finally, it uses the query_accessdb_table() function to convert the data file to a Pandas DataFrame.

# LOADING THE DATA FILE TO THE POSTGRES DATABASE
This code loads the data file from the Pandas DataFrame into a Postgres database. The code first creates an engine for the Postgres database using the sqlalchemy module. Then, it uses the table_result.to_sql() function to load the data file into the database.


The purpose of the code is to extract the data file from an MS Access database and load it into a Postgres database.
The data source used by the code is the MS Access database WPI.mdb.


## operational guidelines.

The steps involved in the code are as follows:
Connect to the MS Access database.
Get the list of table names in the database.
Convert the data file to a Pandas DataFrame.
Load the data file into the Postgres database.
The output of the code is a Pandas DataFrame containing the data from the MS Access database.
The known limitations of the code are as follows:
The code only works with MS Access databases that have a table named Wpi Data.
The code does not handle errors gracefully.

## Query task

The purpose of the query execution is to be establish using the PostgreSQL database.
The data source used by the query code is the PostgreSQL database World_Port_Index_Data_Migration.
The steps involved in the code are as follows:

Connect to the PostgreSQL database.
Run a SQL query task from the question.
Store the results of the query in a Pandas DataFrame.
Print the DataFrame to the console.
The output of the code is a Pandas DataFrame

The code only works with the PostgreSQL database World_Port_Index_Data_Migration.


## Prerequisites
Ms Access database
Python
psycopg2 module
Pandas library
SQLAlchemy library
PostgreSQL database



## Contribution and Feedback

Contributions are welcomed to enhance and extend this postgreSql task further. Feel free to submit pull requests, raise issues, or provide feedback to help us improve the project.
