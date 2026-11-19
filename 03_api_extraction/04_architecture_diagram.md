# Software Architecture & End-to-End Data Flow

## 1. Visual Data Flow Diagram (User Action to Analytics Dashboard)

```mermaid
flowchart LR
    A["1. Web / Mobile App<br/>(Frontend UI)"] -->|"HTTPS / JSON<br/>(REST API: POST / GET)"| B["2. Backend Server<br/>(Auth, Validation & Logic)"]
    B -->|"SQL Write / Read"| C["3. Transactional DB (OLTP)<br/>(PostgreSQL / MySQL)"]
    B -->|"Structured Events"| D["4. Logging & Error Monitoring<br/>(ELK Stack / CloudWatch)"]
    C -->|"ETL / CDC Pipeline<br/>(Airflow / dbt)"| E["5. Data Warehouse (OLAP)<br/>(BigQuery / Snowflake)"]
    E -->|"SQL Queries"| F["6. Analytics Dashboard<br/>(Power BI / Tableau)"]