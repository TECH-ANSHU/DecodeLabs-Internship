"""
Database Setup module for creating the SQLite database, defining schemas, loading data,
building indexes, and creating views.
"""

import os
import sqlite3
import pandas as pd
from config import DB_PATH, PROCESSED_DATA_PATH, COUPONS_DATA
from helper import logger

def setup_database():
    """
    Initializes the SQLite database, creates tables, indexes, views, and loads cleaned data.
    """
    logger.info("Starting database setup...")

    # Validate processed data path
    if not os.path.exists(PROCESSED_DATA_PATH):
        logger.error(f"Cleaned CSV data not found at: {PROCESSED_DATA_PATH}")
        raise FileNotFoundError(f"Cleaned CSV data not found at: {PROCESSED_DATA_PATH}")

    # Remove old database file if it exists
    if os.path.exists(DB_PATH):
        logger.info(f"Removing existing database file at: {DB_PATH}")
        os.remove(DB_PATH)

    # Connect to SQLite
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    logger.info(f"Connected to database at: {DB_PATH}")

    try:
        # Enable Foreign Keys
        cursor.execute("PRAGMA foreign_keys = ON;")

        # 1. Create 'coupons' table
        logger.info("Creating 'coupons' table...")
        cursor.execute("""
            CREATE TABLE coupons (
                CouponCode VARCHAR(50) PRIMARY KEY,
                DiscountPercent DECIMAL(3, 2) NOT NULL,
                Description VARCHAR(255)
            );
        """)

        # 2. Create 'orders' table
        logger.info("Creating 'orders' table...")
        cursor.execute("""
            CREATE TABLE orders (
                OrderID VARCHAR(50) PRIMARY KEY,
                Date DATETIME NOT NULL,
                CustomerID VARCHAR(50) NOT NULL,
                Product VARCHAR(100) NOT NULL,
                Quantity INTEGER NOT NULL CHECK (Quantity > 0),
                UnitPrice DECIMAL(10, 2) NOT NULL CHECK (UnitPrice >= 0),
                TotalPrice DECIMAL(10, 2) NOT NULL CHECK (TotalPrice >= 0),
                ShippingAddress VARCHAR(255) NOT NULL,
                PaymentMethod VARCHAR(50) NOT NULL,
                OrderStatus VARCHAR(50) NOT NULL,
                TrackingNumber VARCHAR(50) NOT NULL,
                ItemsInCart INTEGER NOT NULL CHECK (ItemsInCart >= 0),
                CouponCode VARCHAR(50) NOT NULL,
                ReferralSource VARCHAR(50) NOT NULL,
                FOREIGN KEY (CouponCode) REFERENCES coupons(CouponCode)
            );
        """)

        # 3. Populate 'coupons' table
        logger.info("Inserting records into 'coupons' table...")
        for coupon in COUPONS_DATA:
            cursor.execute("""
                INSERT INTO coupons (CouponCode, DiscountPercent, Description)
                VALUES (?, ?, ?);
            """, (coupon["CouponCode"], coupon["DiscountPercent"], coupon["Description"]))

        # 4. Ingest orders from cleaned_dataset.csv
        logger.info(f"Ingesting orders from cleaned CSV: {PROCESSED_DATA_PATH}")
        df_orders = pd.read_csv(PROCESSED_DATA_PATH)
        
        # Insert rows using executemany for high efficiency
        orders_data = df_orders.values.tolist()
        cursor.executemany("""
            INSERT INTO orders (
                OrderID, Date, CustomerID, Product, Quantity, UnitPrice, TotalPrice, 
                ShippingAddress, PaymentMethod, OrderStatus, TrackingNumber, ItemsInCart, 
                CouponCode, ReferralSource
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, orders_data)
        logger.info(f"Successfully inserted {cursor.rowcount} orders into the 'orders' table.")

        # 5. Create database indexes (Bonus)
        logger.info("Creating performance indexes...")
        cursor.execute("CREATE INDEX idx_orders_customer ON orders(CustomerID);")
        cursor.execute("CREATE INDEX idx_orders_product ON orders(Product);")
        cursor.execute("CREATE INDEX idx_orders_date ON orders(Date);")
        logger.info("Indexes created successfully.")

        # 6. Create Database Views (Bonus)
        logger.info("Creating database views...")
        
        # View 1: Monthly Sales Trend
        cursor.execute("""
            CREATE VIEW vw_monthly_sales AS
            SELECT 
                strftime('%Y-%m', Date) AS Month,
                COUNT(OrderID) AS TotalOrders,
                SUM(Quantity) AS TotalItemsSold,
                ROUND(SUM(TotalPrice), 2) AS GrossRevenue
            FROM orders
            GROUP BY Month;
        """)

        # View 2: Customer Lifetime Value (CLV)
        cursor.execute("""
            CREATE VIEW vw_customer_lifetime_value AS
            SELECT 
                CustomerID,
                COUNT(OrderID) AS OrderCount,
                SUM(Quantity) AS TotalItemsBought,
                ROUND(SUM(TotalPrice), 2) AS LifetimeSpent,
                ROUND(AVG(TotalPrice), 2) AS AverageOrderValue
            FROM orders
            GROUP BY CustomerID;
        """)

        # View 3: Product Performance View
        cursor.execute("""
            CREATE VIEW vw_product_performance AS
            SELECT 
                Product,
                COUNT(OrderID) AS TotalOrders,
                SUM(Quantity) AS TotalQuantitySold,
                ROUND(SUM(TotalPrice), 2) AS RevenueGenerated,
                ROUND(AVG(UnitPrice), 2) AS AvgPrice
            FROM orders
            GROUP BY Product;
        """)

        conn.commit()
        logger.info("Database commit successful. Views created.")

    except sqlite3.Error as e:
        logger.error(f"SQLite database setup error: {e}")
        conn.rollback()
        raise e
    finally:
        conn.close()

    logger.info("Database setup completed successfully!")

if __name__ == "__main__":
    setup_database()
