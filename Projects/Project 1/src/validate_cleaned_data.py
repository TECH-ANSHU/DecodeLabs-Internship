import os
import pandas as pd
import numpy as np

def validate():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    clean_path = os.path.join(base_path, "data", "processed", "cleaned_dataset.csv")
    
    print("Loading cleaned dataset...")
    df = pd.read_csv(clean_path)
    
    errors = 0
    
    # 1. Check shape
    print(f"Shape: {df.shape}")
    if df.shape != (1200, 15):
        print("ERROR: Shape is not 1200 rows by 15 columns!")
        errors += 1
    else:
        print("SUCCESS: Shape is correct (1200, 15).")
        
    # 2. Check no percentage symbols in any column name or values
    for col in df.columns:
        if df[col].dtype == 'object':
            pct_count = df[col].astype(str).str.contains('%').sum()
            if pct_count > 0:
                print(f"ERROR: Column '{col}' contains '%' symbols in {pct_count} cells!")
                errors += 1
                
    # 3. Check price calculations: TotalPrice = Quantity * UnitPrice * (1 - DiscountPercent / 100)
    expected_totals = (df['Quantity'] * df['UnitPrice'] * (1.0 - df['DiscountPercent'] / 100.0)).round(2)
    mismatches = (df['TotalPrice'] - expected_totals).abs() >= 1e-2
    mismatches_count = mismatches.sum()
    if mismatches_count > 0:
        print(f"ERROR: Found {mismatches_count} rows with incorrect TotalPrice calculation!")
        print(df[mismatches][['OrderID', 'Quantity', 'UnitPrice', 'DiscountPercent', 'TotalPrice']].head())
        errors += 1
    else:
        print("SUCCESS: TotalPrice calculations are correct and match discounts.")
        
    # 4. Check TrackingNumber logic: Pending and Cancelled must have null/nan tracking numbers
    pending_cancelled = df[df['OrderStatus'].isin(['Pending', 'Cancelled'])]
    tracking_not_null = pending_cancelled['TrackingNumber'].notnull().sum()
    if tracking_not_null > 0:
        print(f"ERROR: Found {tracking_not_null} Pending/Cancelled orders with active tracking numbers!")
        errors += 1
    else:
        print("SUCCESS: Pending and Cancelled orders do not have tracking numbers.")
        
    # 5. Check other statuses (Shipped, Delivered, Returned): should have non-null tracking numbers
    other_statuses = df[df['OrderStatus'].isin(['Shipped', 'Delivered', 'Returned'])]
    tracking_null = other_statuses['TrackingNumber'].isnull().sum()
    if tracking_null > 0:
        print(f"ERROR: Found {tracking_null} Shipped/Delivered/Returned orders with missing tracking numbers!")
        errors += 1
    else:
        print("SUCCESS: Shipped, Delivered, and Returned orders all have tracking numbers.")
        
    print(f"\nValidation complete. Total errors found: {errors}")
    if errors == 0:
        print("DATASET IS 100% CLEAN AND CORRECT!")
    else:
        print("DATASET HAS VALIDATION FAILURES!")

if __name__ == "__main__":
    validate()
