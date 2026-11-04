# Data Profiling and Quality Report

**Profiled:** 2026-11-04  
**Sources:** `Data/Raw/train.csv` and `Data/Cleaned/sales_customer_cleaned.csv`

## Executive summary

Both CSV files contain 9,800 records and 18 columns in the same row order. The cleaned CSV standardizes the raw day/month/year dates to ISO `YYYY-MM-DD`; all other field values are preserved. There are no blank values other than 11 missing postal codes, no duplicate rows, and no duplicate row IDs. Dates parse successfully and no ship date is earlier than its order date.

Two consistency issues merit review before using the affected fields for detailed lookups: 32 product IDs map to multiple product names, and postal code `92024` maps to two cities. The missing postal codes all belong to Burlington, Vermont. Preserve these values as missing or unresolved rather than guessing replacements.

## Dataset structure

| Measure | Result |
|---|---:|
| Records | 9,800 |
| Columns | 18 |
| Row ID values | 9,800 unique; sequential from 1 to 9,800 |
| Distinct orders | 4,922 |
| Distinct customers | 793 |
| Distinct products | 1,861 |
| Exact duplicate rows | 0 |
| Blank/whitespace-only cells | 11, all in `Postal Code` |

This is transaction-line data: an order can have multiple rows. Repeated `Order ID` values are expected and do not by themselves indicate duplicate records.

## Field-level profile

CSV fields are physically read as text; the types below are inferred semantic/import types. “Distinct” counts non-missing values.

Each field is listed with its suggested type, missing-value count, and distinct-value count:

- `Row ID` — integer identifier; 0 missing; 9,800 distinct.
- `Order ID` — text identifier; 0 missing; 4,922 distinct.
- `Order Date` — date (`DD/MM/YYYY`); 0 missing; 1,230 distinct.
- `Ship Date` — date (`DD/MM/YYYY`); 0 missing; 1,326 distinct.
- `Ship Mode` — category; 0 missing; 4 distinct.
- `Customer ID` — text identifier; 0 missing; 793 distinct.
- `Customer Name` — text; 0 missing; 793 distinct.
- `Segment` — category; 0 missing; 3 distinct.
- `Country` — category; 0 missing; 1 distinct.
- `City` — text; 0 missing; 529 distinct.
- `State` — category/text; 0 missing; 49 distinct.
- `Postal Code` — text identifier; 11 missing; 626 distinct non-missing values.
- `Region` — category; 0 missing; 4 distinct.
- `Product ID` — text identifier; 0 missing; 1,861 distinct.
- `Category` — category; 0 missing; 3 distinct.
- `Sub-Category` — category; 0 missing; 17 distinct.
- `Product Name` — text; 0 missing; 1,849 distinct.
- `Sales` — decimal number; 0 missing; 5,757 distinct.

Postal codes should be imported as text, not numeric values, so formatting (including any leading zeroes) is not lost.

## Value domains and numeric/date checks

- `Ship Mode`: First Class, Same Day, Second Class, Standard Class.
- `Segment`: Consumer, Corporate, Home Office.
- `Region`: Central, East, South, West.
- `Category`: Furniture, Office Supplies, Technology.
- The data contains one country: United States.
- The 17 sub-categories each map to exactly one category.
- `Order Date` ranges from 2015-01-03 through 2018-12-30; `Ship Date` ranges from 2015-01-07 through 2019-01-05. All 19,600 date values parsed using day/month/year format; none were invalid, and no shipment predates its order.
- `Sales` parses for all 9,800 rows; minimum 0.444, maximum 22,638.48, total 2,261,536.78. There are no zero or negative sales values.
- No leading or trailing whitespace was found in the CSV cells.

## Quality findings and recommended handling

1. **Missing postal codes (11 rows, 0.11%).** All occur for Burlington, Vermont. Retain them as null/blank unless an authoritative source supplies the postal code; do not impute it from city alone.
2. **Product ID/name conflicts (32 IDs).** A single `Product ID` maps to multiple `Product Name` values. Product IDs consistently map to one category and sub-category, but names should not be treated as a reliable one-to-one product lookup until reconciled against an authoritative product catalog.
3. **Postal code/city conflict (one postal code).** `92024` appears with both Encinitas and San Diego, California. Review with a trusted geographic reference before using postal code as a unique city key.
4. **CSV date standardization.** The raw source dates use `DD/MM/YYYY`; the cleaned CSV stores them in ISO `YYYY-MM-DD` format for consistent downstream imports. The Excel workbook stores these as date values, and the SQLite database stores ISO date text.
5. **Available measures.** Profit, quantity, discount, and delivery date are not present. Do not infer profitability, units sold, discount effects, or delivery performance from these records.

## Profiling basis

Checks were run against both CSVs for record/column counts, per-field missing and distinct values, full-row and row-ID duplicates, type/date parsing, sales range, whitespace, and selected identifier-to-description relationships. A row-by-row comparison confirmed the same records and order, with only the two date fields reformatted in the cleaned CSV.
