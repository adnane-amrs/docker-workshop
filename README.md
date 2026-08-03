# 🚕 Data Engineering Zoomcamp - Docker & Data Ingestion Workshop

This repository contains the code and environment configuration for **Module 1 (Containerization & Infrastructure)** of the Data Engineering Zoomcamp. It demonstrates setting up a local database infrastructure with PostgreSQL and pgAdmin using Docker Compose, as well as building containerized Python data ingestion pipelines.

---

## 🛠️ Tech Stack & Tools

- **Containers & Orchestration**: Docker, Docker Compose
- **Database & Management**: PostgreSQL 15, pgAdmin 4
- **Data Engineering & Libraries**: Python 3.13+, Pandas, SQLAlchemy, PyArrow, psycopg2, tqdm
- **Package Management**: [uv](https://github.com/astral-sh/uv)

---

## 📁 Repository Structure

```text
de-zoomcamp/
├── docker-compose.yml       # Docker Compose service definition for Postgres & pgAdmin
├── pipeline/
│   ├── Dockerfile           # Docker configuration for containerizing the pipeline
│   ├── ingest_data.py       # Script to download and stream NYC Taxi CSV data into Postgres
│   ├── pipeline.py          # Sample CLI data processing pipeline exporting Parquet files
│   ├── notebook.ipynb       # Jupyter notebook for interactive data exploration
│   ├── pyproject.toml       # Project configuration and dependencies (uv)
│   └── uv.lock              # Lockfile ensuring reproducible environment installs
└── test/
    └── script.py            # Utility script for inspecting filesystem paths
```

---

## 🚀 Getting Started

### 1. Launch Services (PostgreSQL & pgAdmin)

Start the database and administration web app in the background:

```bash
docker-compose up -d
```

- **PostgreSQL**: Runs on `localhost:5432` (`User: root`, `Password: rootpassword`, `DB: ny_taxi`)
- **pgAdmin**: Accessible at [http://localhost:8080](http://localhost:8080) (`Email: admin@admin.com`, `Password: root`)

---

### 2. Ingest Data into PostgreSQL

To stream and ingest the NYC Yellow Taxi dataset into PostgreSQL:

```bash
cd pipeline
python ingest_data.py
```

---

### 3. Build & Run Containerized Pipeline

To build and execute the containerized pipeline:

```bash
# Build Docker Image
docker build -t taxi_pipeline:v01 ./pipeline

# Run Container
docker run -it taxi_pipeline:v01 1
```

---

## 📊 Data Source

The pipeline ingests the official NYC TLC Yellow Taxi Dataset:
- **Source**: `https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow`
- **Table Name**: `yellow_taxi_data`
