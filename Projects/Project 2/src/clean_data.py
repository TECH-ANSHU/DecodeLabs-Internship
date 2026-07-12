#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
clean_data.py
---------------------------------------------
ETL Data Cleaning and Imputation Pipeline for Project 2.
This script performs data ingestion from the raw Excel transaction file,
implements critical accounting adjustments and supply chain constraints,
performs feature engineering, and exports the final audited dataset.

Author: Senior Data Analyst
DecodeLabs Data Analytics Internship
"""

import os
import pandas as pd
import numpy as np

# Set paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "Dataset for Data Analytics.xlsx")
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, "data", "processed")
PROCESSED_DATA_PATH = os.path.join(PROCESSED_DATA_DIR, "cleaned_dataset.csv")

def run_cleaning_pipeline():
    print("=== INITIATING DATA CLEANING PIPELINE ===")
    
    # 1. Ingest Data
    if not os.path.exists(RAW_DATA_PATH):
        raise FileNotFoundError(f"Raw dataset not found at: {RAW_DATA_PATH}")
    
    print(f"Ingesting raw data from: {RAW_DATA_PATH}...")
    df = pd.read_excel(RAW_DATA_PATH)
    initial_rows, initial_cols = df.shape
    print(f"Successfully loaded {initial_rows} rows and {initial_cols} columns.")
    
    # Create copy for cleaning
    df_clean = df.copy()
    
    # 2. Date Column Conversion
    print("Standardizing Date column to datetime64[ns]...")
    df_clean['Date'] = pd.to_datetime(df_clean['Date'])
    
    # 3. Discount Mapping & TotalPrice Correction
    print("Applying discount corrections and recalculating TotalPrice...")
    # Map CouponCodes to discount percentages
    # SAVE10: 10% discount, WINTER15: 15% discount, FREESHIP: 0% discount (only shipping is free)
    discount_map = {'SAVE10': 10.0, 'WINTER15': 15.0, 'FREESHIP': 0.0}
    df_clean['DiscountPercent'] = df_clean['CouponCode'].map(discount_map).fillna(0.0)
    
    # Calculate corrected total price
    # Formula: TotalPrice = Quantity * UnitPrice * (1 - DiscountPercent / 100)
    df_clean['TotalPrice'] = (df_clean['Quantity'] * df_clean['UnitPrice'] * (1 - df_clean['DiscountPercent'] / 100.0)).round(2)
    
    # 4. Logistics Integrity Imputation
    print("Enforcing logistics tracking constraints...")
    # Tracking numbers are only valid for active logistics (Shipped, Delivered, Returned)
    # Set TrackingNumber to NaN for Pending and Cancelled orders
    df_clean.loc[df_clean['OrderStatus'].isin(['Pending', 'Cancelled']), 'TrackingNumber'] = np.nan
    
    # 5. Feature Engineering
    print("Performing feature engineering...")
    # Extract date parts
    df_clean['OrderYear'] = df_clean['Date'].dt.year
    df_clean['OrderMonth'] = df_clean['Date'].dt.month
    df_clean['OrderQuarter'] = df_clean['Date'].dt.quarter
    df_clean['DayName'] = df_clean['Date'].dt.day_name()
    df_clean['IsWeekend'] = df_clean['Date'].dt.dayofweek.isin([5, 6]).astype(int)
    
    # Discount Flags
    df_clean['DiscountApplied'] = (df_clean['DiscountPercent'] > 0.0).astype(int)
    
    # Order Value Category
    # Low: < Rs. 250, Medium: Rs. 250 - Rs. 1000, High: > Rs. 1000
    df_clean['OrderValueCategory'] = pd.cut(
        df_clean['TotalPrice'], 
        bins=[-np.inf, 250, 1000, np.inf], 
        labels=['Low', 'Medium', 'High']
    )
    
    # Basket Size Category
    # Small: 1-3 items, Medium: 4-7 items, Large: 8+ items
    df_clean['BasketSizeCategory'] = pd.cut(
        df_clean['ItemsInCart'], 
        bins=[-np.inf, 3, 7, np.inf], 
        labels=['Small', 'Medium', 'Large']
    )
    
    # High Value Order Flag
    df_clean['HighValueOrder'] = (df_clean['TotalPrice'] > 1000.0).astype(int)
    
    # 6. Save Cleaned Data
    if not os.path.exists(PROCESSED_DATA_DIR):
        os.makedirs(PROCESSED_DATA_DIR)
        print(f"Created processed data directory at: {PROCESSED_DATA_DIR}")
        
    print(f"Exporting cleaned dataset to: {PROCESSED_DATA_PATH}...")
    df_clean.to_csv(PROCESSED_DATA_PATH, index=False)
    print("ETL Pipeline complete. Data saved successfully.")
    
    # Print brief audit summary
    print("\n=== CLEANING PIPELINE STATS ===")
    print(f"Adjusted Mean TotalPrice: Rs. {df_clean['TotalPrice'].mean():.2f}")
    print(f"Total Adjusted Revenue: Rs. {df_clean['TotalPrice'].sum():.2f}")
    print(f"Fulfillment State Counts:\n{df_clean['OrderStatus'].value_counts()}")
    print(f"Imputed TrackingNumber Null Count: {df_clean['TrackingNumber'].isnull().sum()} / {len(df_clean)}")
    print("===============================\n")

if __name__ == "__main__":
    run_cleaning_pipeline()
