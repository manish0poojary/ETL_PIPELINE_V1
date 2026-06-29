# GDP ETL Pipeline using Python

## Overview

This project demonstrates a complete **ETL (Extract, Transform, Load)** pipeline built in Python. The pipeline extracts GDP data from a Wikipedia archive page, transforms and cleans the extracted data, and loads the processed data into both a SQLite database and a JSON file. A logging system records each stage of the pipeline execution.

This project was developed to practice core data engineering concepts such as web scraping, data transformation, structured data storage, and pipeline organization.

---

## Features

- Extracts GDP data from a Wikipedia archive using **Requests** and **BeautifulSoup**.
- Parses HTML tables and converts them into structured tabular data.
- Cleans and transforms GDP values.
- Handles missing values using Pandas.
- Converts GDP values into billions of USD (rounded to two decimal places).
- Loads processed data into a **SQLite** database.
- Exports the final dataset as a **JSON** file.
- Records ETL execution events in a log file with timestamps.

---

## Project Structure

```
gdp-etl-pipeline/
│── etl_pipeline.py          # Main ETL pipeline
│── Countries_by_GDP.json    # JSON output
│── World_economic.db        # SQLite database
│── etl_project_log.txt      # Execution logs
│── requirements.txt
│── README.md
```

---

## Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- Pandas
- SQLite3
- Datetime

---

## ETL Workflow

```
Extract
   │
   ▼
Retrieve GDP table from Wikipedia

   │
   ▼
Transform
   • Parse HTML
   • Validate rows
   • Clean GDP values
   • Handle missing values
   • Convert GDP values to billions

   │
   ▼
Load
   • SQLite Database
   • JSON File

   │
   ▼
Logging
```

---

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/<your-username>/gdp-etl-pipeline.git
```

2. Navigate to the project directory.

```bash
cd gdp-etl-pipeline
```

3. Install the required dependencies.

```bash
pip install -r requirements.txt
```

4. Execute the pipeline.

```bash
python etl_pipeline.py
```

---

## Output

The pipeline generates:

- **Countries_by_GDP.json** – Processed GDP dataset in JSON format.
- **World_economic.db** – SQLite database containing the processed table.
- **etl_project_log.txt** – Timestamped execution log.

---

## Future Improvements

- Add exception handling using `try-except-finally`.
- Replace the custom logging function with Python's `logging` module.
- Read configuration values from a configuration file.
- Add automated unit tests.
- Schedule pipeline execution using Apache Airflow or Cron.

---

## Learning Outcomes

Through this project, I gained practical experience with:

- ETL pipeline design
- Web scraping using BeautifulSoup
- Data cleaning and transformation with Pandas
- SQLite database integration
- JSON data export
- Logging and pipeline orchestration
- Git and GitHub workflow
