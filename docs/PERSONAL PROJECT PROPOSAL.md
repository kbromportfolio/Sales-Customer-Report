# Personal Project Proposal

## Sales & Customer Report

- Project Author: Kbrom Gebremedihin
- Project Type: Personal Data Analytics
- Primary Tools: Microsoft Excel, SQLite, Power BI
- Supporting Tools: SQLiteStudio, Git, GitHub
- Project Repository: Sales-Customer-Report
- Planned Duration: 1 Week (7 Days)

## 1. Project Overview

This personal project focuses on analysing retail sales and customer data using Excel, SQLite and Power BI. It demonstrates practical skills in data preparation, data cleaning, database management, SQL querying, analytical reporting, KPI development and interactive dashboard creation.

The project aims to transform raw business data into meaningful insights that support performance monitoring and data-driven decision-making.

## 2. Project Aim & Objectives

The aim is to develop an end-to-end sales and customer analytics solution using structured data analysis and business intelligence tools.

The project objectives are to:

- Profile, clean and validate the original dataset.
- Prepare a structured Excel dataset.
- Create and manage a SQLite database.
- Develop SQL queries using SQLiteStudio.
- Analyse sales, products, categories, customers and regions.
- Develop KPIs using SQL and DAX.
- Build an interactive Power BI dashboard.
- Identify trends and business opportunities.
- Produce evidence-based findings and recommendations.
- Document and publish the project on GitHub.

## 3. Dataset Description

The project uses a Superstore-style retail dataset containing customer, order, product, geographical, shipping and sales information.

The SQLite database contains 9,800 records, 18 fields and a table named `sales`.

The available fields cover:

- Order and customer identification
- Order and shipping dates
- Customer details and segments
- Product and category information
- Geographical information
- Sales values

The dataset contains multiple product records for some orders. Therefore, individual records must be distinguished from unique orders when calculating performance measures.

The dataset will be used for educational and portfolio purposes.

## 4. Project Scope

### In Scope

- Data profiling and quality assessment.
- Excel data cleaning and validation.
- SQLite database development.
- SQL querying and analysis.
- Sales trends and performance.
- Product and category analysis.
- Customer and geographical analysis.
- Shipping-duration analysis.
- KPI development.
- Power BI dashboard development.
- Business findings and recommendations.

### Out of Scope

- Profitability analysis because profit data is unavailable.
- Quantity and discount analysis because these fields are not included.
- Customer satisfaction analysis without supporting information.
- Delivery-time analysis because a delivery date is unavailable.
- Predictive modelling and machine learning in the initial version.
- Unsupported assumptions about customer purchasing motivations.

## 5. Project Methodology

The project will follow this workflow:

Original CSV → Excel Data Cleaning → Cleaned Excel Dataset → SQLite Database → SQL Analysis using SQLiteStudio → Power BI Data Modelling → KPI Development → Interactive Dashboard → Findings → Recommendations → GitHub Publication

Excel will be used for data preparation, SQLite for database management, SQL for analytical queries and Power BI for reporting and visualisation.

The analysis will cover:

- Sales performance over time.
- Product and category performance.
- Customer purchasing activity.
- Regional and geographical performance.
- Customer segment comparisons.
- Shipping duration.

## 6. Key Performance Indicators

The project will focus on five main KPIs:

| KPI | Definition |
| --- | --- |
| Total Sales | Sum of all valid sales values. |
| Distinct Orders | Count of unique Order IDs. |
| Unique Customers | Count of distinct Customer IDs. |
| Average Order Value | Total Sales divided by Distinct Orders. |
| Average Shipping Duration | Average number of days between Order Date and Ship Date. |

These KPIs will be calculated using SQL and DAX, validated against the underlying dataset and presented through Power BI dashboard cards.

Additional supporting analysis will include:

- Monthly and yearly sales trends.
- Sales by product and category.
- Sales by region.
- Top-performing customers.
- Customer segment performance.

## 7. Tools & Technologies

| Tool | Purpose |
| --- | --- |
| Microsoft Excel | Data cleaning and preparation |
| SQLite | Database storage and management |
| SQLiteStudio | SQL querying and analysis |
| SQL | Data extraction, filtering and aggregation |
| Power BI | Data modelling and interactive dashboards |
| Power Query | Data transformation |
| DAX | KPI calculations and analytical measures |
| Git | Version control |
| GitHub | Portfolio publication |
| Microsoft Word / Markdown | Project documentation |

## 8. Expected Outcomes & Deliverables

The completed project will demonstrate practical skills in data management, SQL, analytical thinking, KPI development, data visualisation and business intelligence.

Expected deliverables:

- Original and cleaned datasets.
- Data profiling and quality report.
- SQLite database.
- SQL queries and analysis.
- Sales and customer analysis.
- Five KPI definitions and calculations.
- Power BI data model and DAX measures.
- Interactive Power BI dashboard.
- Findings and recommendations report.
- Project documentation, screenshots and GitHub repository.

## 9. Project Timeline

The project is planned over seven days.

| Day | Activities |
| --- | --- |
| Day 1 | Project planning and dataset preparation |
| Day 2 | Data profiling and quality assessment |
| Day 3 | Excel data cleaning and validation |
| Day 4 | SQLite database development |
| Day 5 | SQL querying and analysis |
| Day 6 | Power BI modelling, KPI development and dashboard |
| Day 7 | Findings, recommendations, documentation, quality assurance and GitHub publication |

Progress will be monitored through the project management tracker and Git commits.

## 10. Limitations, Future Development & Conclusion

The project depends on the quality and completeness of the supplied dataset. Profit, quantity and discount analysis will not be performed without supporting fields. Shipping duration will measure the time between order and shipment, not delivery to the customer.

Future development could include Python automation, advanced SQL, customer segmentation, sales forecasting and more advanced Power BI reporting.

The project will demonstrate an end-to-end approach to transforming raw business data into meaningful insights using Excel, SQLite, SQL and Power BI. It will provide practical portfolio evidence of skills relevant to Data Analyst and Business Intelligence opportunities.
