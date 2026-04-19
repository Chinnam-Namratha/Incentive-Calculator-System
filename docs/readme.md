# Incentive Calculator System

## What We're Building

This project calculates **sales incentives** for team members based on their sales performance. It processes raw sales data, validates it, transforms it into meaningful insights, and stores the results for reporting and analysis.

## How We're Achieving It

### Technology Stack
- **Apache Spark**: For large-scale data processing and transformations
- **Python**: Core programming language for data pipeline
- **MySQL**: Relational database for storing transactional and analytical data
- **AWS S3**: Cloud storage for data files and backups
- **SQL**: For complex data transformations and aggregations

### Data Pipeline Approach

1. **Extract**: Retrieve sales data from AWS S3 and MySQL databases
2. **Validate**: Check data quality and ensure mandatory columns exist
3. **Transform**: 
   - Calculate incentives based on sales metrics
   - Join dimension tables (customers, stores, sales teams)
   - Create data marts for analytics (Customer Data Mart, Sales Data Mart)
4. **Load**: Store processed results back into MySQL for reporting and analysis
5. **Secure**: All credentials managed via environment variables (no hardcoded secrets)

### Project Structure

```
├── src/main/
│   ├── read/              # Data extraction from S3 and databases
│   ├── transformations/   # ETL jobs for incentive calculations
│   ├── write/             # Data loading to databases and storage
│   ├── upload/            # Upload results back to S3
│   ├── utility/           # Helper functions (logging, encryption, connections)
│   └── delete/            # Data cleanup operations
├── resources/
│   ├── __init__.py
│   ├── dev/
│   │    ├── config.py
│   │    └── requirement.txt
│   └── qa/
│   │    ├── config.py
│   │    └── requirement.txt
│   └── prod/
│   │    ├── config.py
│   │    └── requirement.txt
│   ├── sql_scripts/
│   │    └── table_scripts.sql
├── src/
│   ├── main/
│   │    ├── __init__.py
│   │    └── delete/
│   │    │      ├── aws_delete.py
│   │    │      ├── database_delete.py
│   │    │      └── local_file_delete.py
│   │    └── download/
│   │    │      └── aws_file_download.py
│   │    └── move/
│   │    │      └── move_files.py
│   │    └── read/
│   │    │      ├── aws_read.py
│   │    │      └── database_read.py
│   │    └── transformations/
│   │    │      └── jobs/
│   │    │      │     ├── customer_mart_sql_transform_write.py
│   │    │      │     ├── dimension_tables_join.py
│   │    │      │     ├── main.py
│   │    │      │     └──sales_mart_sql_transform_write.py
│   │    └── upload/
│   │    │      └── upload_to_s3.py
│   │    └── utility/
│   │    │      ├── encrypt_decrypt.py
│   │    │      ├── logging_config.py
│   │    │      ├── s3_client_object.py
│   │    │      ├── spark_session.py
│   │    │      └── my_sql_session.py
│   │    └── write/
│   │    │      ├── database_write.py
│   │    │      └── parquet_write.py
│   ├── test/
│   │    ├── scratch_pad.py.py
│   │    └── generate_csv_data.py

```


## Key Achievements

✅ **Automated Incentive Calculation** - Processes hundreds of sales records efficiently  
✅ **Data Security** - Environment-based credentials, no secrets in code  
✅ **Scalable Architecture** - Modular design ready for production deployment  
✅ **Multiple Environments** - Dev, QA, and Production configurations  
✅ **Data Validation** - Ensures data quality before processing  
✅ **Clean Code** - Professional project structure and best practices  