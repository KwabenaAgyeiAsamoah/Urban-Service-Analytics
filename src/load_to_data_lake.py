import os
import pandas as pd
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

from ingest_api import fetch_nyc_311_data
from transform_data import transform_nyc_311_data

load_dotenv()


def upload_raw_to_lake(data):
    df = pd.DataFrame(data)

    account_name = os.getenv("AZURE_STORAGE_ACCOUNT")
    account_key = os.getenv("AZURE_STORAGE_KEY")

    container_name = "raw-data"
    blob_name = "urban_raw_data.csv"

    if not account_name or not account_key:
        raise ValueError("AZURE_STORAGE_ACCOUNT or AZURE_STORAGE_KEY is missing in .env")

    csv_data = df.to_csv(index=False).encode("utf-8")

    blob_service_client = BlobServiceClient(
        account_url=f"https://{account_name}.blob.core.windows.net",
        credential=account_key
    )

    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name
    )

    blob_client.upload_blob(csv_data, overwrite=True)

    print("Raw data uploaded to Data Lake")
    print(f"Uploaded file: {blob_name}")
    print(f"Rows uploaded: {len(df)}")


def upload_clean_to_lake():
    account_name = os.getenv("AZURE_STORAGE_ACCOUNT")
    account_key = os.getenv("AZURE_STORAGE_KEY")

    container_name = "processed-data"
    blob_name = "nyc_311_clean.csv"
    file_path = "data/processed/nyc_311_clean.csv"

    if not account_name or not account_key:
        raise ValueError("AZURE_STORAGE_ACCOUNT or AZURE_STORAGE_KEY is missing in .env")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Clean file not found: {file_path}")

    blob_service_client = BlobServiceClient(
        account_url=f"https://{account_name}.blob.core.windows.net",
        credential=account_key
    )

    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name
    )

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    print("Clean data uploaded to Data Lake")
    print(f"Uploaded file: {blob_name}")


if __name__ == "__main__":
    data = fetch_nyc_311_data()
    upload_raw_to_lake(data)
    transform_nyc_311_data()
    upload_clean_to_lake()