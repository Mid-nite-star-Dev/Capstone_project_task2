import pyodbc
import pandas as pd
pyodbc.drivers()
pyodbc.dataSources()

def get_accessbase_conn():
    return pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:/Users/Collins/Desktop/PUB150/WPI.mdb')
conn = get_accessbase_conn()
cursor = conn.cursor()
# Get the list of table names
table_names = [table.table_name for table in cursor.tables(tableType="TABLE")]
# Print the table names
for name in table_names:
    print(name)


def query_accessdb_table(query, conn):
    table_result = pd.read_sql(query, conn)
    return table_result
query = """
SELECT * FROM "Wpi Data"

"""
table_result = query_accessdb_table(query, conn)
print(table_result)

#l0ading to the postgres database

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:01ajstyles@localhost:5432/World_Port_Index_Data_Migration')
engine.connect()
table_result.to_sql('World_Port_Index',con=engine,if_exists='replace')


#Question 1
#Establish the five nearest ports to Singapore's JURONG ISLAND port (country =
#'SG', port_name = 'JURONG ISLAND'). The output should encompass 'port_name'
#and 'distance_in_meters' exclusively.


# This connection will be used to run queries on the PostgreSQL database
import psycopg2
import pandas as pd

def nearest_ports_to_jurong_island():

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname="World_Port_Index_Data_Migration",
        user="postgres",
        password={"My_password"},
        host="localhost",
        port="5432"
    )

    # Run SQL query to find the 5 nearest ports to JURONG ISLAND
    sql_query = """
    SELECT
        "Main_port_name",
        (
            6371000 *
            acos(
                cos(radians(1)) * cos(radians("Latitude_degrees")) * cos(radians("Longitude_degrees") - radians(103.98765)) +
                sin(radians(1)) * sin(radians("Latitude_degrees"))
            )
        ) AS distance_in_meters
    FROM
        "World_Port_Index"
    WHERE
        "Wpi_country_code" = 'SG'
        AND "Main_port_name" != 'JURONG ISLAND'
    ORDER BY
        distance_in_meters
    LIMIT 5;
    """

    # Execute the query and fetch the result into a DataFrame
    result = pd.read_sql_query(sql_query, conn)

    # Close the connection
    conn.close()

    return result

# Call the function to find and display the nearest ports to JURONG ISLAND
nearest_ports = nearest_ports_to_jurong_island()
print(nearest_ports)



#Question 2

#Determine the country with the highest count of ports boasting a cargo_wharf.
#The outcome should encapsulate 'country' and 'port_count' solely.

# This connection will be used to run queries on the PostgreSQL database
import psycopg2
import pandas as pd
def largest_cargo_wharf_ports():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname="World_Port_Index_Data_Migration",
        user="postgres",
        password={"My_password"},
        host="localhost",
        port="5432"
    )
# Run SQL query to find which country has the largest number of ports with a cargo_wharf.
     sql_query = """
    SELECT
        "Wpi_country_code" as country,
        count("Main_port_name") as port_count
    FROM
        "World_Port_Index" 
    GROUP BY
        "Wpi_country_code"
    ORDER BY
        port_count DESC
    LIMIT 1
    """
    # Execute the query and fetch the result into a DataFrame
    result_2 = pd.read_sql_query(sql_query, conn)
    # Close the connection
    conn.close()
    return result_2
# Call the function to find and display the country with the largest number of cargo wharf ports
largest_cargo_country = largest_cargo_wharf_ports()
print(largest_cargo_country)


#Question 3
#Respond to a distress call situated at lat: 32.610982, long: -38.706256 within the
#middle of the North Atlantic Ocean. The caller requires the nearest port offering
#provisions, water, fuel oil, and diesel. Your solution should encompass 'country',
#'port_name', 'port_latitude', and 'port_longitude'.

import psycopg2
import pandas as pd
def nearest_provision_ports(latitude, longitude):
    # Connect to the PostgreSQL database
     conn = psycopg2.connect(
        dbname="World_Port_Index_Data_Migration",
        user="postgres",
        password={"My_password"},
        host="localhost",
        port="5432"
    )
    # Run SQL query to find the nearest port with provisions, water, fuel_oil, and diesel.
    sql_query = f"""
    SELECT "Wpi_country_code" AS country, "Main_port_name" AS port_name, "Latitude_degrees" AS port_latitude, "Longitude_degrees" AS port_longitude,
        (6371000 *
            acos(
                cos(radians({latitude})) * cos(radians("Latitude_degrees")) * cos(radians("Longitude_degrees") - radians({longitude})) +
                sin(radians({latitude})) * sin(radians("Latitude_degrees"))
            )
        ) AS distance_in_meters
    FROM "World_Port_IndexS"
    WHERE "Supplies_provisions" = 'Y' AND "Supplies_water" = 'Y'
    AND "Supplies_fuel_oil" = 'Y' AND "Supplies_diesel_oil" = 'Y'
    ORDER BY distance_in_meters
    LIMIT 1;
    """
    # Execute the query and fetch the result into a DataFrame
    result_3 = pd.read_sql_query(sql_query, conn)
    # Close the connection
    conn.close()
    return result_3
# Call the function to find and display the nearest port with provisions, water, fuel_oil, and diesel
latitude = 32.610982
longitude = -38.706256
provision_ports = nearest_provision_ports(latitude, longitude)
print(provision_ports)