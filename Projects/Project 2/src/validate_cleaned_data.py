#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
validate_cleaned_data.py
---------------------------------------------
Automated Data Validation and Quality Assurance Suite.
This script checks that the processed dataset conforms to all logical,
mathematical, and supply chain constraints before proceeding to analysis.

Author: Senior Data Analyst
DecodeLabs Data Analytics Internship
"""

import os
import pandas as pd
import numpy as np

# Set paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "cleaned_dataset.csv")

def validate_data():
    print("=== STARTING QA DATA VALIDATION CHECKS ===")
    
    # 1. Load Processed Dataset
    if not os.path.exists(PROCESSED_DATA_PATH):
        raise FileNotFoundError(f"Processed dataset not found at: {PROCESSED_DATA_PATH}. Please run clean_data.py first.")
        
    df = pd.read_csv(PROCESSED_DATA_PATH)
    rows_count = len(df)
    
    # Assert row count
    assert rows_count == 1200, f"Assertion Error: Expected 1200 rows, got {rows_count}."
    print(f"[PASS] Loaded {rows_count} rows of processed transaction data.")
    
    # 2. Assert Financial Integrity (TotalPrice Correction Check)
    # TotalPrice = Quantity * UnitPrice * (1 - DiscountPercent / 100)
    expected_price = df['Quantity'] * df['UnitPrice'] * (1 - df['DiscountPercent'] / 100.0)
    mismatches = (df['TotalPrice'] - expected_price).abs() >= 0.01
    mismatch_count = mismatches.sum()
    
    assert mismatch_count == 0, f"Assertion Error: Found {mismatch_count} rows where TotalPrice doesn't match discount math."
    print("[PASS] Checked 1200 rows: Financial calculations are mathematically correct.")
    
    # 3. Assert Logistics Integrity (TrackingNumber check)
    # Pending and Cancelled orders must have null (NaN) TrackingNumber
    pending_cancelled = df[df['OrderStatus'].isin(['Pending', 'Cancelled'])]
    invalid_pending_tracking = pending_cancelled['TrackingNumber'].notnull().sum()
    
    assert invalid_pending_tracking == 0, f"Assertion Error: Found {invalid_pending_tracking} Pending/Cancelled orders with active tracking numbers."
    print("[PASS] Checked 1200 rows: Pending and Cancelled orders do not have tracking numbers.")
    
    # Shipped, Delivered, Returned must have non-null tracking numbers
    active_fulfillment = df[df['OrderStatus'].isin(['Shipped', 'Delivered', 'Returned'])]
    missing_active_tracking = active_fulfillment['TrackingNumber'].isnull().sum()
    
    assert missing_active_tracking == 0, f"Assertion Error: Found {missing_active_tracking} Shipped/Delivered/Returned orders without tracking numbers."
    print("[PASS] Checked 1200 rows: Shipped, Delivered, and Returned orders have active tracking numbers.")
    
    # 4. Range and Data Domain Checks
    assert (df['Quantity'] <= 0).sum() == 0, "Assertion Error: Found negative or zero quantities."
    assert (df['UnitPrice'] < 0).sum() == 0, "Assertion Error: Found negative unit prices."
    assert (df['TotalPrice'] < 0).sum() == 0, "Assertion Error: Found negative total prices."
    print("[PASS] Checked 1200 rows: No domain or sign violations in numerical values.")
    
    # 5. Schema check
    expected_columns = [
        'OrderID', 'Date', 'CustomerID', 'Product', 'Quantity', 'UnitPrice', 
        'ShippingAddress', 'PaymentMethod', 'OrderStatus', 'TrackingNumber', 
        'ItemsInCart', 'CouponCode', 'ReferralSource', 'TotalPrice', 
        'DiscountPercent', 'OrderYear', 'OrderMonth', 'OrderQuarter', 
        'DayName', 'IsWeekend', 'DiscountApplied', 'OrderValueCategory', 
        'BasketSizeCategory', 'HighValueOrder'
    ]
    for col in expected_columns:
        assert col in df.columns, f"Assertion Error: Missing expected column '{col}' in processed schema."
    print(f"[PASS] Schema Validation: All {len(expected_columns)} columns exist in output file.")
    
    print("\n==================================================")
    print("VALIDATION COMPLETE: Dataset is 100% compliant with business rules!")
    print("==================================================\n")

if __name__ == "__main__":
    validate_data()
