# ETL with Python and SQL

## Overview

This repository contains an Apache Airflow DAG and an ETL process for loading order data into a PostgreSQL database. The primary goal is to automate the data extraction from Excel files, transformation of relevant columns, and loading into a relational database, ensuring data is always up-to-date for analysis and reporting.

## Contents

- **`orders_dag.py`**: Defines an Airflow Directed Acyclic Graph (DAG) that schedules and runs the ETL process on a daily basis. The DAG is responsible for triggering the ETL workflow, which extracts and processes the data from the source.
  
- **`orders_etl_logic.py`**: Contains the core ETL logic. It connects to a PostgreSQL database, reads the order data from an Excel file, filters relevant columns, and loads the transformed data into the PostgreSQL database.

## How It Works

1. **Extract**: The data is extracted from an Excel file located in the user's directory. The file contains order information, including fields such as Order ID, Date, Total Due, Status, Customer ID, and Salesperson ID.

2. **Transform**: The script filters out unnecessary columns, keeping only the ones relevant for analysis, such as `OrderID`, `Date`, `TotalDue`, `Status`, `CustomerID`, and `SalespersonID`.

3. **Load**: The transformed data is loaded into a PostgreSQL table called `orders`. If the table already exists, it will be replaced to ensure the data is always current.

4. **Schedule**: The Airflow DAG schedules the ETL process to run daily, ensuring that the PostgreSQL database is updated with the latest data on a regular basis. This automation reduces the need for manual intervention and ensures consistent and timely updates.

## Business Benefits

1. **Automated Data Pipeline**: By leveraging Apache Airflow, this ETL process ensures that order data is loaded automatically into the database, reducing manual data entry and increasing efficiency.
   
2. **Improved Decision Making**: The ETL process ensures that critical order information is always available in a database, enabling teams to run reports and analyses without delays. This leads to better and more timely business decisions.

3. **Scalability**: The automated nature of this solution allows for future growth. As more data sources are integrated, the ETL pipeline can be adapted to handle increased data volumes and new requirements, providing long-term scalability.

4. **Error Handling and Reliability**: With Airflow’s retry mechanisms and the ability to monitor DAG executions, the process is resilient to occasional failures. Business stakeholders can rely on timely data without concerns of missing or outdated records.

5. **Centralized Data Storage**: By storing the transformed data in a PostgreSQL database, the business can ensure that all relevant order data is in one place, making it easier to generate analytics, dashboards, and reports from a single source of truth.

## Setup Instructions

1. **Environment Setup**:
    - Install Apache Airflow: [Official Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html)
    - Install required Python libraries: `pandas`, `sqlalchemy`, `psycopg2`.
    - Ensure PostgreSQL is installed and accessible.

2. **Configuring Airflow DAG**:
    - Copy the `orders_dag.py` and `orders_etl_logic.py` to your Airflow DAGs directory.
    - Set up PostgreSQL database credentials as per your environment.

3. **Execution**:
    - Once the DAG is loaded into Airflow, enable it via the Airflow UI.
    - The ETL process will automatically execute as per the schedule defined (daily in this case).

4. **Customizations**:
    - Adjust the schedule interval in the DAG configuration if daily runs do not fit your use case.
    - Modify the data extraction logic in `orders_etl_logic.py` to accommodate changes in the data source format or additional transformations as needed.

## Conclusion

This repository offers a robust, automated solution for handling order data, providing businesses with timely access to critical data that can inform decision-making and drive business growth. With minimal setup, companies can implement this process to streamline data management and leverage real-time insights from their order transactions.

---

For more information or inquiries, please reach out to the repository maintainers.
