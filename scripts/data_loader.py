from faker import Faker
from db_connection import create_connection, close_connection
import random
from static_data import antigen_descriptions, coverage_descriptions, disease_descriptions, regions

fake = Faker()

def random_null_chance(probability: float = 0.1):
    """Randomly return None (NULL) with a given probability."""
    return None if random.random() < probability else random.randint(2010, 2030)

def insert_data():
    connection = create_connection()
    cursor = connection.cursor()

    if connection:
        print("Connection established.")
    else:
        print("Failed to connect to the database.")
        return

    # Insert data into `users`
    users_query = """
    INSERT INTO users (user_id, country_code, country_name, region, gender, date_of_birth)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    users_data = [
        (
            f"USER-{fake.country_code().upper()}-{random.choice(['M', 'F', 'O'])}-{random.randint(10000000, 99999999)}",
            fake.country_code(),
            fake.country(),
            random.choice(regions),  # Use predefined regions list for consistency
            random.choices(['Male', 'Female'], k=1, weights=[0.9, 0.9])[0] if random.random() < 0.9 else 'Other',  # 90% Male/Female, 10% Other
            fake.date_of_birth(minimum_age=18, maximum_age=80)
        )
        for _ in range(100)
    ]
    cursor.executemany(users_query, users_data)
    print("Inserted sample data into `users` table.")

    # Fetch user_ids from the `users` table
    cursor.execute("SELECT user_id FROM users")
    user_ids = [row[0] for row in cursor.fetchall()]

    # Insert data into `coverage_data`
    coverage_query = """
    INSERT INTO coverage_data (
        coverage_id, user_id, year, antigen_code, antigen_description,
        coverage_category, coverage_description, target_number,
        doses_administered, coverage_percentage
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    coverage_data = [
        (
            f"COV_{random.randint(100000, 999999)}",
            random.choice(user_ids),  # Ensure foreign key consistency
            random_null_chance(0.1),  # Year can be NULL with a 10% chance
            f"COV-{random.randint(100000, 999999)}" if random.random() < 0.9 else None,
            random.choice(antigen_descriptions) if random.random() < 0.9 else None,
            random.choice(['Administered', 'Official']) if random.random() < 0.9 else None,
            random.choice(coverage_descriptions) if random.random() < 0.9 else None,
            random.randint(1000, 9999) if random.random() < 0.9 else None,
            random.randint(500, 9999) if random.random() < 0.9 else None,
            round(random.uniform(50, 100), 2) if random.random() < 0.9 else None
        )
        for _ in range(200)
    ]
    cursor.executemany(coverage_query, coverage_data)
    print("Inserted sample data into `coverage_data` table.")

    # Insert data into `incidence_rate`
    incidence_query = """
    INSERT INTO incidence_rate (
        incidence_id, user_id, year, disease_code, disease_description,
        population_basis, incidence_rate
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    incidence_data = [
        (
            f"INC_{random.randint(1000000, 9999999)}",
            random.choice(user_ids),  # Ensure foreign key consistency
            random_null_chance(0.1),  # Year can be NULL with a 10% chance
            f"DIS-{random.randint(100, 999)}",  # Ensure the correct format: DIS-<number>
            random.choice(disease_descriptions),
            random.choice(['Per 1000 births', 'Per 1000 population']),
            round(random.uniform(0.1, 50), 2) if random.random() < 0.9 else None
        )
        for _ in range(150)
    ]
    cursor.executemany(incidence_query, incidence_data)
    print("Inserted sample data into `incidence_rate` table.")

    # Insert data into `reported_cases`
    insert_reported_cases(cursor, user_ids)

    # Commit the transaction
    connection.commit()
    print("Data committed to the database.")

    # Close the connection
    close_connection(connection)

def insert_reported_cases(cursor, user_ids):
    cases_query = """
    INSERT INTO reported_cases (
        case_id, user_id, year, disease_code, disease_description, cases
    )
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    cases_data = [
        (
            f"CASE_{random.randint(100000, 999999)}",  # Generate a random case_id
            random.choice(user_ids),  # Ensure foreign key consistency
            random.randint(2010, 2030),
            f"DIS-{random.randint(100, 999)}",
            random.choice(disease_descriptions),
            random.randint(0, 5000)
        )
        for _ in range(150)
    ]
    cursor.executemany(cases_query, cases_data)
    print("Inserted sample data into `reported_cases` table.")

if __name__ == "__main__":
    insert_data()
