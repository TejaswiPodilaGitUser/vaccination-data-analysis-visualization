from db_connection import create_connection, close_connection

def create_tables():
    tables = {
        "users": """
        CREATE TABLE IF NOT EXISTS users (
            user_id VARCHAR(255) PRIMARY KEY,
            country_code CHAR(3) NOT NULL,
            country_name VARCHAR(255) NOT NULL,
            region VARCHAR(100) DEFAULT NULL,
            gender ENUM('Male', 'Female', 'Other') NOT NULL,
            date_of_birth DATE DEFAULT NULL  -- Allow NULL values for date_of_birth
        );
        """,
        "coverage_data": """
        CREATE TABLE IF NOT EXISTS coverage_data (
            coverage_id VARCHAR(20) PRIMARY KEY,
            user_id VARCHAR(255) DEFAULT NULL,
            year INT DEFAULT NULL,  -- Allow NULL values for year
            antigen_code VARCHAR(20) DEFAULT NULL,
            antigen_description VARCHAR(255),
            coverage_category VARCHAR(100),
            coverage_description VARCHAR(255),
            target_number INT(6),
            doses_administered INT(6),
            coverage_percentage DECIMAL(5, 2),
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL
        );
        """,
        "incidence_rate": """
        CREATE TABLE IF NOT EXISTS incidence_rate (
            incidence_id VARCHAR(20) PRIMARY KEY,
            user_id VARCHAR(255) DEFAULT NULL,
            year INT DEFAULT NULL,  -- Allow NULL values for year
            disease_code VARCHAR(20) DEFAULT NULL,
            disease_description VARCHAR(255),
            population_basis VARCHAR(100),
            incidence_rate DECIMAL(10, 2),
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL
        );
        """,
        "reported_cases": """
        CREATE TABLE IF NOT EXISTS reported_cases (
            case_id VARCHAR(255) PRIMARY KEY,
            user_id VARCHAR(255) DEFAULT NULL,
            year INT DEFAULT NULL,  -- Allow NULL values for year
            disease_code VARCHAR(20) DEFAULT NULL,
            disease_description VARCHAR(255),
            cases INT(6),
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE SET NULL
        );
        """
    }

    drop_statements = [
        "DROP TABLE IF EXISTS reported_cases;",
        "DROP TABLE IF EXISTS incidence_rate;",
        "DROP TABLE IF EXISTS coverage_data;",
        "DROP TABLE IF EXISTS users;"
    ]

    connection = create_connection()
    cursor = connection.cursor()

    # Drop tables if they already exist
    for drop_query in drop_statements:
        try:
            cursor.execute(drop_query)
            print(f"Executed: {drop_query}")
        except Exception as e:
            print(f"Error executing: {drop_query}. Error: {e}")

    # Create tables
    for table_name, create_query in tables.items():
        try:
            cursor.execute(create_query)
            print(f"Table `{table_name}` created successfully.")
        except Exception as e:
            print(f"Error creating table `{table_name}`: {e}")

    close_connection(connection)

if __name__ == "__main__":
    create_tables()
