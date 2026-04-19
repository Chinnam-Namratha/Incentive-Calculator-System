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
│   ├── dev/config.py      # Development configuration
│   ├── qa/config.py       # QA configuration  
│   ├── prod/config.py     # Production configuration
│   └── sql_scripts/       # Database initialization
└── docs/
    └── readme.md          # This file
```

## Key Achievements

✅ **Automated Incentive Calculation** - Processes hundreds of sales records efficiently  
✅ **Data Security** - Environment-based credentials, no secrets in code  
✅ **Scalable Architecture** - Modular design ready for production deployment  
✅ **Multiple Environments** - Dev, QA, and Production configurations  
✅ **Data Validation** - Ensures data quality before processing  
✅ **Clean Code** - Professional project structure and best practices  

---

**Repository**: https://github.com/Chinnam-Namratha/Incentive-Calculator-System
