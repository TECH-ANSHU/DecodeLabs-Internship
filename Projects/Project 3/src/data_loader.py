"""
Data Loader module for loading, cleaning, and validating the raw E-Commerce Excel dataset.
"""

import os
import shutil
import pandas as pd
from config import RAW_DATA_PATH, PROCESSED_DATA_PATH, PROJECT_DIR
from helper import logger

def clean_data():
    """
    Loads raw Excel data, performs comprehensive cleaning and audits, and exports cleaned CSV.
    """
    logger.info("Starting data loading and cleaning process...")

    # Validate raw data path
    if not os.path.exists(RAW_DATA_PATH):
        logger.error(f"Raw data file not found at: {RAW_DATA_PATH}")
        raise FileNotFoundError(f"Raw data file not found at: {RAW_DATA_PATH}")

    # Set up raw data directory and copy raw Excel file to raw folder to follow project structures
    raw_dir = os.path.join(PROJECT_DIR, "data", "raw")
    os.makedirs(raw_dir, exist_ok=True)
    target_raw_path = os.path.join(raw_dir, "Dataset for Data Analytics.xlsx")
    if not os.path.exists(target_raw_path):
        logger.info(f"Copying raw Excel file to {target_raw_path} to organize folders...")
        shutil.copy2(RAW_DATA_PATH, target_raw_path)

    # Load dataset
    logger.info(f"Loading raw dataset from: {RAW_DATA_PATH}")
    df = pd.read_excel(RAW_DATA_PATH)
    logger.info(f"Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")

    # 1. Clean column names
    df.columns = df.columns.str.strip()
    logger.info("Cleaned column names: stripped surrounding whitespace.")

    # 2. Handle null values
    null_counts = df.isnull().sum()
    logger.info(f"Initial null counts:\n{null_counts[null_counts > 0]}")

    # For CouponCode: fill NaN with 'NONE' (string)
    df["CouponCode"] = df["CouponCode"].fillna("NONE").astype(str).str.strip().str.upper()
    logger.info("Filled missing CouponCode values with 'NONE' and standardized to upper case.")

    # Verify other columns don't have nulls, if they do, drop or impute
    other_nulls = df.isnull().sum()
    if other_nulls.sum() > 0:
        logger.warning(f"Unresolved null values remain:\n{other_nulls[other_nulls > 0]}")
        # Drop rows where critical fields are null (none expected based on initial analysis)
        df.dropna(subset=["OrderID", "Date", "CustomerID", "Product", "Quantity", "UnitPrice", "TotalPrice"], inplace=True)

    # 3. Standardize and clean text/category data types
    df["OrderID"] = df["OrderID"].astype(str).str.strip().str.upper()
    df["CustomerID"] = df["CustomerID"].astype(str).str.strip().str.upper()
    df["Product"] = df["Product"].astype(str).str.strip().str.title()
    df["ShippingAddress"] = df["ShippingAddress"].astype(str).str.strip()
    df["PaymentMethod"] = df["PaymentMethod"].astype(str).str.strip().str.title()
    df["OrderStatus"] = df["OrderStatus"].astype(str).str.strip().str.title()
    df["TrackingNumber"] = df["TrackingNumber"].astype(str).str.strip().str.upper()
    df["ReferralSource"] = df["ReferralSource"].astype(str).str.strip().str.title()

    # 4. Standardize numeric data types
    df["Quantity"] = df["Quantity"].astype(int)
    df["UnitPrice"] = df["UnitPrice"].astype(float)
    df["TotalPrice"] = df["TotalPrice"].astype(float)
    df["ItemsInCart"] = df["ItemsInCart"].astype(int)

    # 5. Clean and format Date column
    df["Date"] = pd.to_datetime(df["Date"])
    # Format Date column as YYYY-MM-DD
    df["Date_str"] = df["Date"].dt.strftime("%Y-%m-%d")

    # 6. Audit & Validation check: TotalPrice = Quantity * UnitPrice
    calculated_total = (df["Quantity"] * df["UnitPrice"]).round(2)
    mismatches = df[df["TotalPrice"].round(2) != calculated_total]
    if not mismatches.empty:
        logger.warning(f"Found {len(mismatches)} price mismatches. Recalculating TotalPrice based on Quantity * UnitPrice.")
        df["TotalPrice"] = calculated_total
    else:
        logger.info("Validated: TotalPrice matches Quantity * UnitPrice in all records.")

    # 7. Check for duplicated rows
    duplicates_count = df.duplicated(subset=["OrderID"]).sum()
    if duplicates_count > 0:
        logger.warning(f"Found {duplicates_count} duplicate OrderIDs. Dropping duplicates.")
        df.drop_duplicates(subset=["OrderID"], keep="first", inplace=True)
    else:
        logger.info("Validated: No duplicate OrderIDs found.")

    # Reorder columns to standard and drop the temporary date string column if not needed
    cols = ["OrderID", "Date", "CustomerID", "Product", "Quantity", "UnitPrice", "TotalPrice", 
            "ShippingAddress", "PaymentMethod", "OrderStatus", "TrackingNumber", "ItemsInCart", 
            "CouponCode", "ReferralSource"]
    
    cleaned_df = df[cols].copy()
    # Format the Date column as string for CSV export to maintain clean format in SQLite ingestion
    cleaned_df["Date"] = cleaned_df["Date"].dt.strftime("%Y-%m-%d %H:%M:%S")

    # Save to CSV
    logger.info(f"Saving cleaned dataset to: {PROCESSED_DATA_PATH}")
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    cleaned_df.to_csv(PROCESSED_DATA_PATH, index=False)
    logger.info("Data loading and cleaning completed successfully!")
    return cleaned_df

if __name__ == "__main__":
    clean_data()
