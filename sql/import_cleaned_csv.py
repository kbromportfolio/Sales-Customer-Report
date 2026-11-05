import csv
import datetime
import math
import os
import sqlite3
import tempfile
from decimal import Decimal, InvalidOperation
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "Data" / "Cleaned" / "sales_customer_cleaned.csv"
DATABASE_PATH = ROOT / "Data" / "Cleaned" / "sales_customer.db"
SCHEMA_PATH = Path(__file__).with_name("schema.sql")

CSV_COLUMNS = (
    "Row ID",
    "Order ID",
    "Order Date",
    "Ship Date",
    "Ship Mode",
    "Customer ID",
    "Customer Name",
    "Segment",
    "Country",
    "City",
    "State",
    "Postal Code",
    "Region",
    "Product ID",
    "Category",
    "Sub-Category",
    "Product Name",
    "Sales",
)


def parse_date(value, field, row_number):
    try:
        parsed = datetime.date.fromisoformat(value)
    except ValueError as error:
        raise ValueError(f"Invalid {field} on CSV record {row_number}: {value!r}") from error
    if parsed.isoformat() != value:
        raise ValueError(f"Invalid {field} on CSV record {row_number}: {value!r}")
    return value


def read_records():
    records = []
    with CSV_PATH.open("r", newline="", encoding="utf-8-sig") as source:
        reader = csv.DictReader(source)
        if tuple(reader.fieldnames or ()) != CSV_COLUMNS:
            raise ValueError("Cleaned CSV columns do not match the expected 18-column schema")

        for row_number, row in enumerate(reader, start=2):
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"Malformed CSV record at line {row_number}")
            for field, value in row.items():
                if field != "Postal Code" and (not value or value != value.strip()):
                    raise ValueError(
                        f"Missing or whitespace-padded {field} on CSV record {row_number}"
                    )

            try:
                row_id = int(row["Row ID"])
                order_date = parse_date(row["Order Date"], "Order Date", row_number)
                ship_date = parse_date(row["Ship Date"], "Ship Date", row_number)
                sales_value = Decimal(row["Sales"])
            except (ValueError, InvalidOperation) as error:
                raise ValueError(f"Invalid value on CSV record {row_number}: {error}") from error

            if row_id <= 0:
                raise ValueError(f"Row ID must be positive on CSV record {row_number}")
            if datetime.date.fromisoformat(ship_date) < datetime.date.fromisoformat(order_date):
                raise ValueError(f"Ship Date precedes Order Date on CSV record {row_number}")
            if not sales_value.is_finite() or sales_value < 0:
                raise ValueError(f"Sales must be finite and non-negative on CSV record {row_number}")

            try:
                sales = float(sales_value)
            except OverflowError as error:
                raise ValueError(f"Sales is outside SQLite REAL range on CSV record {row_number}") from error
            if not math.isfinite(sales):
                raise ValueError(f"Sales is outside SQLite REAL range on CSV record {row_number}")

            records.append(
                (
                    row_id,
                    row["Order ID"],
                    order_date,
                    ship_date,
                    row["Ship Mode"],
                    row["Customer ID"],
                    row["Customer Name"],
                    row["Segment"],
                    row["Country"],
                    row["City"],
                    row["State"],
                    row["Postal Code"] or None,
                    row["Region"],
                    row["Product ID"],
                    row["Category"],
                    row["Sub-Category"],
                    row["Product Name"],
                    sales,
                )
            )

    if len(records) != 9800:
        raise ValueError(f"Expected 9,800 CSV records, found {len(records)}")
    if len({record[0] for record in records}) != len(records):
        raise ValueError("Duplicate Row ID values found in the cleaned CSV")
    if sum(record[11] is None for record in records) != 11:
        raise ValueError("Expected 11 missing postal codes in the cleaned CSV")
    return records


def main():
    records = read_records()
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            prefix=".sales_customer_", suffix=".db", dir=DATABASE_PATH.parent, delete=False
        ) as temporary_file:
            temporary_path = Path(temporary_file.name)

        connection = sqlite3.connect(temporary_path)
        try:
            connection.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
            connection.executemany(
                """
                INSERT INTO sales (
                    row_id, order_id, order_date, ship_date, ship_mode,
                    customer_id, customer_name, segment, country, city, state,
                    postal_code, region, product_id, category, sub_category,
                    product_name, sales
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                records,
            )
            connection.commit()

            row_count = connection.execute("SELECT COUNT(*) FROM sales").fetchone()[0]
            row_id_count = connection.execute(
                "SELECT COUNT(DISTINCT row_id) FROM sales"
            ).fetchone()[0]
            missing_postal_count = connection.execute(
                "SELECT COUNT(*) FROM sales WHERE postal_code IS NULL"
            ).fetchone()[0]
            integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
            if (row_count, row_id_count, missing_postal_count, integrity) != (
                9800,
                9800,
                11,
                "ok",
            ):
                raise RuntimeError("Imported database failed its post-load validation")
        finally:
            connection.close()

        os.replace(temporary_path, DATABASE_PATH)
        temporary_path = None
        print(f"Imported {row_count:,} records into {DATABASE_PATH}")
        print(f"Distinct row IDs: {row_id_count:,}; missing postal codes: {missing_postal_count}")
        print(f"SQLite integrity check: {integrity}")
    finally:
        if temporary_path is not None and temporary_path.exists():
            temporary_path.unlink()


if __name__ == "__main__":
    main()
