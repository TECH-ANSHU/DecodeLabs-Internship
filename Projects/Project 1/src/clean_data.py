import os
import pandas as pd
import numpy as np

def clean_sales_data():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_path = os.path.join(base_path, "data", "raw", "Dataset for Data Analytics.xlsx")
    processed_path = os.path.join(base_path, "data", "processed", "cleaned_dataset.csv")
    
    print("Loading raw sales data...")
    df = pd.read_excel(raw_path)
    print(f"Loaded {len(df)} rows and {len(df.columns)} columns.")
    
    # 1. Feature Engineering: Create DiscountPercent based on CouponCode
    print("\nMapping Coupon Codes to Discount Percentages...")
    discount_mapping = {
        'SAVE10': 10.0,
        'WINTER15': 15.0,
        'FREESHIP': 0.0
    }
    # For missing coupon codes, discount is 0.0
    df['DiscountPercent'] = df['CouponCode'].map(discount_mapping).fillna(0.0)
    
    # 2. Data Correction: Calculate corrected TotalPrice
    print("Recalculating TotalPrice based on discount percentages...")
    # Expected total price before discount
    df['BasePrice'] = df['Quantity'] * df['UnitPrice']
    # Corrected total price after discount
    df['TotalPrice'] = df['BasePrice'] * (1.0 - df['DiscountPercent'] / 100.0)
    df['TotalPrice'] = df['TotalPrice'].round(2)
    
    # Drop the temporary BasePrice column
    df.drop(columns=['BasePrice'], inplace=True)
    
    # 3. Logistics Integrity: Set TrackingNumber to None for Pending and Cancelled orders
    print("Adjusting Tracking Numbers for logistics integrity (Pending/Cancelled)...")
    pending_cancelled_mask = df['OrderStatus'].isin(['Pending', 'Cancelled'])
    df.loc[pending_cancelled_mask, 'TrackingNumber'] = np.nan
    
    # Save the cleaned dataset
    print(f"Saving cleaned dataset to {processed_path}...")
    df.to_csv(processed_path, index=False)
    print("Data cleaning completed successfully!")
    
    # Validate some outputs
    print("\n=== CLEAN DATA VALIDATION ===")
    print(f"Shape of cleaned data: {df.shape}")
    print("\nSample records (first 5):")
    print(df[['OrderID', 'Quantity', 'UnitPrice', 'CouponCode', 'DiscountPercent', 'TotalPrice', 'OrderStatus', 'TrackingNumber']].head(5))
    
    print("\nTracking Numbers count for Pending and Cancelled:")
    pending_count = len(df[df['OrderStatus'] == 'Pending'])
    cancelled_count = len(df[df['OrderStatus'] == 'Cancelled'])
    pending_track = df[df['OrderStatus'] == 'Pending']['TrackingNumber'].notnull().sum()
    cancelled_track = df[df['OrderStatus'] == 'Cancelled']['TrackingNumber'].notnull().sum()
    print(f"Pending orders: {pending_count} | With tracking number: {pending_track}")
    print(f"Cancelled orders: {cancelled_count} | With tracking number: {cancelled_track}")
    
    # Check if any percentages or formatted strings exist in numeric columns
    print("\nData type check:")
    print(df.dtypes)

if __name__ == "__main__":
    clean_sales_data()
