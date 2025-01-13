from faker import Faker
from db_connection import create_connection, close_connection
import random
from static_data import antigen_descriptions, coverage_descriptions, disease_descriptions, regions

fake = Faker()

def random_null_chance(probability: float = 0.1):
    return None if random.random() < probability else random.randint(2010, 2030)

def insert_users(cursor):
    users_query = """
    INSERT INTO users (user_id, country_code, country_name, region, gender, date_of_birth)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    users_data = [
        (
            f"USER-{fake.country_code().upper()}-{random.choice(['M', 'F', 'O'])}-{random.randint(10000000, 99999999)}",
            fake.country_code(),
            fake.country(),
            random.choice(regions) if random.random() > 0.2 else None,  # 80% chance for region
            random.choices(['Male', 'Female'], k=1, weights=[0.9, 0.9])[0] if random.random() < 0.9 else 'Other',  # 90% Male/Female, 10% Other
            fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d') if random.random() > 0.3 else None  # 30% chance for NULL date_of_birth
        )
        for _ in range(100)
    ]
    cursor.executemany(users_query, users_data)
    print(f"Inserted {len(users_data)} records into `users` table.")



def insert_reported_cases(cursor, user_ids):
    reported_cases_query = """
    INSERT INTO reported_cases (
        case_id, user_id, disease_code, year, disease_description, cases
    )
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    reported_cases_data = [
        (
            f"CASE_{random.randint(1000000, 9999999)}",
            random.choice(user_ids),
            f"DIS-{random.randint(100, 999)}",
            random.randint(2010, 2025),
            random.choice(disease_descriptions),
            random.randint(100, 10000)
        )
        for _ in range(200)
    ]
    try:
        cursor.executemany(reported_cases_query, reported_cases_data)
        print(f"Inserted {len(reported_cases_data)} records into `reported_cases` table.")
    except Exception as e:
        print(f"Error inserting reported cases: {e}")

if __name__ == "__main__":
    connection = create_connection()
    cursor = connection.cursor()

    insert_users(cursor)

    cursor.execute("SELECT user_id FROM users")
    user_ids = [row[0] for row in cursor.fetchall()]

    insert_reported_cases(cursor, user_ids)

    try:
        connection.commit()
        print("Data committed to the database.")
    except Exception as e:
        print(f"Error committing transaction: {e}")

    close_connection(connection)
