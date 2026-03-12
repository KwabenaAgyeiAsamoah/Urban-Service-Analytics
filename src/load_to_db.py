import os
import pandas as pd
import psycopg2


DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "civicpulse_db",
    "user": "postgres",
    "password": "admin123"
}


def load_csv_to_postgres():
    input_file = "data/processed/nyc_311_clean.csv"

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"File not found: {input_file}")

    df = pd.read_csv(input_file)

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS nyc_311_requests (
        unique_key TEXT,
        created_date TIMESTAMP,
        closed_date TIMESTAMP,
        agency TEXT,
        complaint_type TEXT,
        descriptor TEXT,
        borough TEXT,
        status TEXT,
        incident_zip TEXT,
        latitude DOUBLE PRECISION,
        longitude DOUBLE PRECISION
    );
    """
    cur.execute(create_table_query)
    conn.commit()

    insert_query = """
    INSERT INTO nyc_311_requests (
        unique_key,
        created_date,
        closed_date,
        agency,
        complaint_type,
        descriptor,
        borough,
        status,
        incident_zip,
        latitude,
        longitude
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    for _, row in df.iterrows():
        cur.execute(insert_query, tuple(row.where(pd.notnull(row), None)))

    conn.commit()
    cur.close()
    conn.close()

    print(f"Loaded {len(df)} rows into PostgreSQL successfully.")


if __name__ == "__main__":
    load_csv_to_postgres()