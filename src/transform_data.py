import os
import pandas as pd


def transform_nyc_311_data():
    input_file = "data/raw/nyc_311_raw.csv"
    output_dir = "data/processed"
    output_file = "data/processed/nyc_311_clean.csv"

    os.makedirs(output_dir, exist_ok=True)

    df = pd.read_csv(input_file)

    keep_columns = [
        "unique_key",
        "created_date",
        "closed_date",
        "agency",
        "complaint_type",
        "descriptor",
        "borough",
        "status",
        "incident_zip",
        "latitude",
        "longitude",
    ]

    existing_columns = [col for col in keep_columns if col in df.columns]
    df = df[existing_columns].copy()

    if "created_date" in df.columns:
        df["created_date"] = pd.to_datetime(df["created_date"], errors="coerce")

    if "closed_date" in df.columns:
        df["closed_date"] = pd.to_datetime(df["closed_date"], errors="coerce")

    if "borough" in df.columns:
        df["borough"] = df["borough"].fillna("UNKNOWN").str.upper()

    if "status" in df.columns:
        df["status"] = df["status"].fillna("UNKNOWN").str.upper()

    df = df.drop_duplicates()

    df.to_csv(output_file, index=False)

    print(f"Clean data saved successfully to {output_file}")
    print(f"Rows after cleaning: {len(df)}")


if __name__ == "__main__":
    transform_nyc_311_data()                        