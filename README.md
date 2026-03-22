## Urban Service Analytics Platform

## Overview

Urban Service Analytics is an end-to-end data engineering and analytics project designed to ingest, process, store, and visualize urban service complaint data (NYC 311).

This project demonstrates a complete modern data pipeline:
	•	Data ingestion from API(NYC 311 Dataset)
	•	Data transformation and cleaning
	•	Storage in both data lake and database
	•	Workflow orchestration using Apache Airflow
	•	Infrastructure provisioning using Terraform (Azure)
	•	Business intelligence reporting using Power BI

## Business Objective

The objective of this project is to build an end-to-end data platform that transforms raw urban service complaint data into actionable insights for decision-making.

Specifically, the solution aims to:
	•	Monitor and analyze patterns in citizen-reported issues (NYC 311 complaints)
	•	Identify high-demand service areas across boroughs
	•	Improve operational efficiency by highlighting frequently reported complaint types
	•	Enable data-driven decision-making through interactive dashboards
	•	Provide real-time or near-real-time visibility into urban service performance

   ## Architecture
![alt text](docs/architecture/urban_data_pipeline_architecture.png.png)

  ##  URBAN-SERVICE-ANALYTICS/
├── airflow/
│   └── civicpulse_pipeline.py        # Airflow DAG (ETL orchestration)
│
├── data/
│   ├── raw/
│   │   └── nyc_311_raw.csv          # Raw ingested data
│   └── processed/
│       └── nyc_311_clean.csv        # Cleaned dataset
│
├── docs/
│   └── architecture/
│       └── urban_data_pipeline_architecture.png
│
├── src/
│   ├── ingest_api.py                # Extract data from API
│   ├── transform_data.py            # Clean and transform data
│   ├── Clean_data.py                # Additional cleaning logic
│   ├── load_to_data_lake.py         # Store data in data lake
│   └── load_to_db.py                # Load data into PostgreSQL
│
├── terraform/
│   ├── main.tf                      # Infrastructure resources
│   ├── provider.tf                  # Azure provider config
│   ├── variables.tf                 # Input variables
│   └── output.tf                    # Outputs
│
├── requirements.txt
├── README.md
└── .gitignore ##

## Technologies Used
	•	Python – ETL pipeline development
	•	Apache Airflow – Workflow orchestration
	•	PostgreSQL – Structured data storage
	•	Terraform (AzureRM) – Infrastructure as Code
	•	Power BI – Data visualization & reporting
	•	REST API – Data ingestion

 ##   Data Pipeline (End-to-End)

    Data Ingestion (ingest_api.py)
	•	Connects to NYC 311 API
	•	Retrieves raw JSON data
	•	Converts to structured format (CSV)

##    Data Transformation (transform_data.py, Clean_data.py)
	•	Handles missing values
	•	Standardizes formats
	•	Selects relevant columns:
	•	complaint_type
	•	borough
	•	status
	•	created_date
	•	latitude & longitude 

  ##  Data Storage

📁 Data Lake (load_to_data_lake.py)
Stores cleaned data in:
data/processed/nyc_311_clean.csv

Database (load_to_db.py)
	•	Loads structured data into PostgreSQL
	•	Supports querying for analytics


## Workflow Orchestration (Airflow)

DAG: civicpulse_pipeline.py
Pipeline stages:
	1.	Extract → API ingestion
	2.	Transform → Data cleaning
	3.	Load → Data lake + Database
Features:
	•	Scheduled execution
	•	Retry mechanism
	•	Logging and monitoring


    Infrastructure as Code (Terraform - Azure)
Terraform automates:
	•	Cloud resource provisioning
	•	Database setup
	•	Environment configuration

Key Files:
	•	main.tf → Core resources:Complaint volume varies significantly across boroughs
	•	provider.tf → Azure configuration:A small number of complaint types dominate total volume
	•	variables.tf → Parameterization:Trends reveal temporal spikes in service demand
	•	output.tf → Outputs:Geographic clustering highlights service pressure areas

## Power BI Dashboard

The final layer delivers insights through an interactive dashboard.

Key Features:

📈 Complaints Over Time
![alt text](docs/architecture/NYC_311_Complaints_Over_Time.png)
📊 Top Complaint Types
![alt text](<docs/architecture/Top_Complaint_Types _In_NYC.png>)
🥧 Complaints by Borough
![alt text](docs/architecture/NYC_Complaint_by_Borough.png)
🍩 Complaint Status Distribution
![alt text](docs/architecture/Complaint_of_Status_Distribution.png)
🗺 NYC Complaint Map
![alt text](docs/architecture/NYC_311_Complaint_Overview.png)
🎛 Dropdown Slicer (Interactive Filter)
![alt text](docs/architecture/Dropdown_Slicer.png)

## Key Insights
	•	Complaint volume varies significantly across boroughs
	•	A few complaint types dominate overall volume
	•	Temporal trends reveal spikes in service demand
	•	Geographic clustering highlights urban service pressure areas

    How to Run this Project
    1. Install dependencies
    pip install -r requirements.txt

    2. Run ETL manually
    python src/ingest_api.py
    python src/transform_data.py
    python src/load_to_data_lake.py
    python src/load_to_db.py

    3. Run Airflow
    airflow scheduler
    airflow webserver

    4. Deploy Infrastructure (Terraform)
    cd terraform
    terraform init
    terraform apply

    5. Open Power BI
	•	Load .pbix file
	•	Connect to database or CSV
	•	Explore 
![alt text](docs/architecture/count_complaints_for_each_location_type.png)
![alt text](docs/architecture/Complian_by_Complaints_type.png)
![alt text](<docs/architecture/Most frequent_descriptor_for_noise-residential.png>)


    Future Improvements
	•	Real-time streaming pipeline (Kafka / Spark)
	•	Cloud data warehouse (Snowflake / BigQuery)
	•	CI/CD pipeline for automation
	•	Advanced analytics & ML integration
	•	Dashboard auto-refresh

    Author
Kwabena Agyei Asamoah
📍 Birmingham, UK
