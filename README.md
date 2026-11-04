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

The cleaned CSV and SQLite database are included in `Data/Cleaned/`.

### SQLiteStudio

1. Open SQLiteStudio and add `Data/Cleaned/sales_customer.db` as a database.
2. Open the `sales` table to inspect the prepared records, or use the SQL editor to run analysis queries.
3. Use `sql/schema.sql` as the reference for the table structure and indexes.

