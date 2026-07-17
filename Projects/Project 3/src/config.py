"""
Configuration file containing directory paths, database settings, and project constants.
"""

import os

# Root directory of Project 3
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Data Directories
DATA_DIR = os.path.join(PROJECT_DIR, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")

# Raw excel dataset path (which is already inside Project 3 folder)
# We can check if it exists in the root of Project 3 or data/raw/
# In the search we found: DecodeLabs-Internship/Projects/Project 3/Dataset for Data Analytics.xlsx
RAW_DATA_PATH = os.path.join(PROJECT_DIR, "Dataset for Data Analytics.xlsx")
PROCESSED_DATA_PATH = os.path.join(PROCESSED_DATA_DIR, "cleaned_dataset.csv")

# Database Path
DB_PATH = os.path.join(PROJECT_DIR, "ecommerce.db")

# Output Directories
IMAGES_DIR = os.path.join(PROJECT_DIR, "images")
SCREENSHOTS_DIR = os.path.join(PROJECT_DIR, "screenshots")
REPORT_PATH = os.path.join(PROJECT_DIR, "Project_Report.pdf")

# Coupon definition for the 'coupons' table
COUPONS_DATA = [
    {"CouponCode": "SAVE10", "DiscountPercent": 0.10, "Description": "10% off entire order"},
    {"CouponCode": "WINTER15", "DiscountPercent": 0.15, "Description": "15% off winter collection"},
    {"CouponCode": "FREESHIP", "DiscountPercent": 0.00, "Description": "Free shipping on orders"},
    {"CouponCode": "NONE", "DiscountPercent": 0.00, "Description": "No coupon applied"}
]

# Ensure necessary directories exist
for directory in [PROCESSED_DATA_DIR, IMAGES_DIR, SCREENSHOTS_DIR]:
    os.makedirs(directory, exist_ok=True)
