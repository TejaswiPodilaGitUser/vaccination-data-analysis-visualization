import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

def create_connection():
    """
    Establishes a connection to the MySQL database.

    Returns:
        connection (mysql.connector.connection): MySQL connection object if successful, else None.
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "vaccination_analysis_db"),
        )
        if connection.is_connected():
            print("Successfully connected to the database.")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def close_connection(connection):
    """
    Closes the database connection.

    Args:
        connection (mysql.connector.connection): MySQL connection object.
    """
    if connection and connection.is_connected():
        connection.close()
        print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    # Create a connection to the database
    conn = create_connection()

    # Perform your database operations here...

    # Close the connection
    close_connection(conn)
