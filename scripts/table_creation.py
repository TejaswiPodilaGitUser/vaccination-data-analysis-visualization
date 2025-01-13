from db_connection import create_connection, close_connection

def create_tables():
    """
    Creates the necessary tables for the Vaccination Data Analysis project.
    """
    tables = {
        "vaccination_centers": """
            CREATE TABLE IF NOT EXISTS vaccination_centers (
                center_id INT AUTO_INCREMENT PRIMARY KEY,
                center_name VARCHAR(255) NOT NULL,
                location VARCHAR(255),
                total_capacity INT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """,
        "vaccination_records": """
            CREATE TABLE IF NOT EXISTS vaccination_records (
                record_id INT AUTO_INCREMENT PRIMARY KEY,
                center_id INT,
                vaccine_name VARCHAR(255),
                vaccinated_count INT,
                vaccination_date DATE,
                FOREIGN KEY (center_id) REFERENCES vaccination_centers(center_id)
                    ON DELETE CASCADE ON UPDATE CASCADE
            );
        """,
        "vaccines": """
            CREATE TABLE IF NOT EXISTS vaccines (
                vaccine_id INT AUTO_INCREMENT PRIMARY KEY,
                vaccine_name VARCHAR(255) UNIQUE,
                manufacturer VARCHAR(255),
                doses_required INT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """,
    }

    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            for table_name, table_query in tables.items():
                cursor.execute(table_query)
                print(f"Table '{table_name}' created successfully.")
            connection.commit()
        except Exception as e:
            print(f"Error creating tables: {e}")
        finally:
            cursor.close()
            close_connection(connection)

if __name__ == "__main__":
    create_tables()
