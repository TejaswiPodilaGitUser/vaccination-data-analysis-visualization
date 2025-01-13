import pandas as pd
from scripts.db_connection import create_connection, close_connection

def load_data_from_db(query):
    connection = create_connection()
    df = pd.read_sql(query, connection)
    close_connection(connection)
    return df

def handle_missing_data(df):
    # For numeric columns: Impute with the mean
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    
    # For categorical columns: Impute with the most frequent value
    for col in df.select_dtypes(include=['object']).columns:
        df[col].fillna(df[col].mode()[0], inplace=True)
    
    print(f"Missing data handled. Remaining nulls: {df.isnull().sum().sum()}")
    return df

def normalize_units(df):
    # Example: Ensure coverage_percentage is between 0 and 100
    if 'coverage_percentage' in df.columns:
        df['coverage_percentage'] = df['coverage_percentage'].clip(0, 100)
    
    # Example: Normalize reported cases to total population basis
    if 'cases' in df.columns:
        df['cases'] = df['cases'].apply(lambda x: max(x, 0))  # Remove negative values if any

    print("Units normalized.")
    return df

def standardize_date_format(df):
    # Ensure date columns are in the correct format
    if 'date_of_birth' in df.columns:
        df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], errors='coerce')
    
    if 'year' in df.columns:
        df['year'] = pd.to_datetime(df['year'], format='%Y', errors='coerce')
    
    print("Date format standardized.")
    return df

def clean_data():
    # Load the data
    users_query = "SELECT * FROM users;"
    coverage_query = "SELECT * FROM coverage_data;"
    incidence_query = "SELECT * FROM incidence_rate;"
    reported_cases_query = "SELECT * FROM reported_cases;"
    
    users_df = load_data_from_db(users_query)
    coverage_df = load_data_from_db(coverage_query)
    incidence_df = load_data_from_db(incidence_query)
    reported_cases_df = load_data_from_db(reported_cases_query)
    
    # Handle missing data
    users_df = handle_missing_data(users_df)
    coverage_df = handle_missing_data(coverage_df)
    incidence_df = handle_missing_data(incidence_df)
    reported_cases_df = handle_missing_data(reported_cases_df)
    
    # Normalize units
    coverage_df = normalize_units(coverage_df)
    reported_cases_df = normalize_units(reported_cases_df)
    
    # Standardize date format
    users_df = standardize_date_format(users_df)
    coverage_df = standardize_date_format(coverage_df)
    incidence_df = standardize_date_format(incidence_df)
    reported_cases_df = standardize_date_format(reported_cases_df)
    
    return users_df, coverage_df, incidence_df, reported_cases_df

if __name__ == "__main__":
    cleaned_data = clean_data()
