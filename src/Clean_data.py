from ingest_api import fetch_nyc_311_data
from load_to_data_lake import upload_raw_to_lake
from transform_data import transform_nyc_311_data

def upload_clean_to_lake():
    from dotenv import load_dotenv
    load_dotenv()

    import os
    from azure.storage.blob import BlobServiceClient

    account_name = os.getenv("AZURE_STORAGE_ACCOUNT")
    account_key = os.getenv("AZURE_STORAGE_KEY")

    container_name = "processed-data"
    blob_name = "nyc_311_clean.csv"
    file_path = "data/processed/nyc_311_clean.csv"

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

    if __name__ == "__main__":
        data = fetch_nyc_311_data()
    upload_raw_to_lake(data)
    transform_nyc_311_data()     # ← ADD THIS
    upload_clean_to_lake()       # ← AND THIS