CREATE TABLE sales (
    row_id INTEGER PRIMARY KEY,
    order_id TEXT NOT NULL,
    order_date TEXT NOT NULL,
    ship_date TEXT NOT NULL,
    ship_mode TEXT NOT NULL,
    customer_id TEXT NOT NULL,
    customer_name TEXT NOT NULL,
    segment TEXT NOT NULL,
    country TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    postal_code TEXT,
    region TEXT NOT NULL,
    product_id TEXT NOT NULL,
    category TEXT NOT NULL,
    sub_category TEXT NOT NULL,
    product_name TEXT NOT NULL,
    sales REAL NOT NULL CHECK (sales >= 0)
);

CREATE INDEX idx_sales_customer_id ON sales(customer_id);
CREATE INDEX idx_sales_order_date ON sales(order_date);
CREATE INDEX idx_sales_order_id ON sales(order_id);
CREATE INDEX idx_sales_product_id ON sales(product_id);
