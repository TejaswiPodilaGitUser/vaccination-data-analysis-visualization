import pymysql
from db_connection import create_connection, close_connection

# Connect to the database
connection = create_connection()
cursor = connection.cursor()

# coverage_data, incidence_rate, reported_cases, users
try:
    with connection.cursor() as cursor:
        # Get the list of column names for the table
        cursor.execute("SHOW COLUMNS FROM incidence_rate")
        columns = cursor.fetchall()

        # Generate the WHERE condition for checking NULL in any column
        where_clause = " OR ".join([f"{column[0]} IS NULL" for column in columns])

        # Construct the full query
        query = f"SELECT COUNT(*) AS null_count FROM incidence_rate WHERE {where_clause}"

        # Execute the query
        cursor.execute(query)
        result = cursor.fetchone()
        print(f"Rows with any NULL value: {result[0]}")

finally:
    connection.close()
