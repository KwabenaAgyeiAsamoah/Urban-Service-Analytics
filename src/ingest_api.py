import os
import requests
import pandas as pd

API_URL = "https://data.cityofnewyork.us/resource/erm2-nwe9.json?$limit=5000"

def fetch_nyc_311_data():
    os.makedirs("data/raw", exist_ok=True)

    print("Fetching data from NYC Open Data API...")

    response = requests.get(API_URL, timeout=600)
    response.raise_for_status()

    data = response.json()
    df = pd.DataFrame(data)

    output_file = "data/raw/nyc_311_raw.csv"
    df.to_csv(output_file, index=False)

    print(f"Data saved successfully to {output_file}")
    print(f"Rows fetched: {len(df)}")

    return data


