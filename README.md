# Sales and Customer Analytics
## Project structure and source dataset

A retail sales analytics portfolio project using SQLiteStudio for SQL analysis and Power BI for interactive reporting.

## Project goals

- Prepare and validate the supplied sales dataset.
- Store transaction-level product records in a structured SQLite database.
- Analyse sales over time and by product, customer, segment, and geography.
- Build evidence-based KPIs, visualisations, findings, and recommendations.

## Project structure and original dataset

Organized folders for data, documentation, analysis, and reporting. The original Superstore dataset (`Data/Raw/train.csv`) contains 9,800 records across 18 fields, including 11 missing postal codes. The source file is preserved unchanged for reproducible analysis.

## Repository structure
Data/
  Raw/                    Original source data
  Cleaned/                Prepared CSV and SQLite database
docs/                     Project proposal and management tracker
powerbi/                  Power BI report files
reports/                  Profiling and analysis outputs
sql/                      SQLite schema and analysis queries

## Dataset

The source is `Data/Raw/train.csv`, a Superstore-style dataset with 9,800 product-level order records and 18 fields. It contains order and shipping details, customer and product attributes, geography, and sales. A single order can contain multiple product records; count distinct orders when reporting order KPIs.

Initial quality checks found:

- 9,800 records, 9,800 unique row IDs, and no duplicate complete rows.
- 4,922 distinct orders, 793 customers, and 1,861 products.
- 11 missing postal codes; these are retained as NULL/blank rather than discarded.
- No missing values in other fields, invalid dates, or shipments earlier than their order dates.
- Dates in the source are day/month/year and are written as ISO `YYYY-MM-DD` in the prepared outputs.

The available data does not include profit, quantity, discount, or delivery date. Do not infer profitability, units sold, discount effects, or delivery performance from this dataset.

## Use the prepared data

The cleaned CSV, Excel workbook, and SQLite database are included in `Data/Cleaned/`.

### SQLiteStudio

1. Open SQLiteStudio and add `Data/Cleaned/sales_customer.db` as a database.
2. Open the `sales` table to inspect the prepared records, or use the SQL editor to run analysis queries.

## Data Profiling

Profiled the dataset structure, field types, missing values, duplicates, and distinct values. The 9,800 records have unique row IDs and no duplicate rows; 11 postal codes are missing. The data also contains conflicting product names for some product IDs and a ZIP code linked to two cities. These issues are documented for review, with missing values preserved rather than guessed.

See [the data profiling and quality report](reports/data-profiling-quality-report.md) for field-level results and details on known source-data conflicts.

## Excel Data Cleaning & Validation

The prepared workbook is `Data/Cleaned/sales_customer_cleaned.xlsx`. Its **Sales** sheet contains the 9,800 transaction lines, **Cleaning Log** records the transformations, and **SQL Validation** lists the checks and outcomes.

Cleaning and validation decisions:

- The raw source is preserved unchanged. Source dates are parsed as day/month/year; dates in the cleaned CSV and SQLite database use ISO `YYYY-MM-DD`, while the workbook stores Excel date values.
- Row IDs are integers, sales are numeric, and postal codes are stored as text. The 11 missing postal codes are left blank and are not imputed.
- No complete duplicate rows or duplicate row IDs were found. Required fields, date parsing/order, and non-negative sales passed validation.
- Conflicting product names for 32 product IDs and the city conflict for postal code `92024` are retained and flagged for review rather than resolved by guesswork.

See the workbook's **SQL Validation** sheet and [the data profiling and quality report](reports/data-profiling-quality-report.md) for check results and limitations.
