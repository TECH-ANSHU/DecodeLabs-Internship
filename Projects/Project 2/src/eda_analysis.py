#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
eda_analysis.py
---------------------------------------------
Exploratory Data Analysis and Visualization Suite.
This script performs descriptive statistical analysis, univariate/bivariate/
multivariate studies, outlier profiling, and computes answers to 25 business questions.
It exports 16 high-resolution, publication-quality figures to images/.

Author: Senior Data Analyst
DecodeLabs Data Analytics Internship
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Set styling configurations
sns.set_theme(style="whitegrid")
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.titlesize': 16,
    'figure.figsize': (10, 6)
})

# Set paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "cleaned_dataset.csv")
IMAGES_DIR = os.path.join(BASE_DIR, "images")

if not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)

def load_data():
    if not os.path.exists(PROCESSED_DATA_PATH):
        raise FileNotFoundError(f"Cleaned dataset not found at: {PROCESSED_DATA_PATH}")
    return pd.read_csv(PROCESSED_DATA_PATH)

def generate_descriptive_stats(df):
    print("=== COMPUTING DESCRIPTIVE STATISTICS ===")
    num_cols = ['Quantity', 'UnitPrice', 'ItemsInCart', 'TotalPrice']
    desc_df = df[num_cols].describe().T
    
    # Calculate additional metrics
    desc_df['variance'] = df[num_cols].var()
    desc_df['skewness'] = df[num_cols].skew()
    desc_df['kurtosis'] = df[num_cols].kurt()
    desc_df['range'] = desc_df['max'] - desc_df['min']
    desc_df['IQR'] = desc_df['75%'] - desc_df['25%']
    
    # Reorder columns
    cols_order = ['count', 'mean', 'std', 'variance', 'min', '25%', '50%', '75%', 'max', 'range', 'IQR', 'skewness', 'kurtosis']
    desc_df = desc_df[cols_order]
    
    print(desc_df.to_string())
    print("========================================\n")
    return desc_df

def generate_univariate_plots(df):
    print("Generating Univariate Visualizations...")
    
    # 01. TotalPrice Distribution
    plt.figure()
    sns.histplot(df['TotalPrice'], kde=True, color='#1E3A8A', bins=30)
    plt.title("Distribution of Total Invoice Price (Corrected)")
    plt.xlabel("Adjusted Total Price (Rs.)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGES_DIR, "01_univariate_totalprice.png"), dpi=300)
    plt.close()
    
    # 02. Quantity Distribution
    plt.figure()
    sns.countplot(data=df, x='Quantity', palette='Blues_r')
    plt.title("Distribution of Sales Volumes (Quantity per Order)")
    plt.xlabel("Quantity Purchased")
    plt.ylabel("Number of Orders")
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGES_DIR, "02_univariate_quantity.png"), dpi=300)
    plt.close()
    
    # 03. ItemsInCart Distribution
    plt.figure()
    sns.histplot(df['ItemsInCart'], kde=True, color='#0D9488', bins=10)
    plt.title("Distribution of Cart Items at Checkout")
    plt.xlabel("Number of Items in Cart")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGES_DIR, "03_univariate_itemsincart.png"), dpi=300)
    plt.close()
    
    # 04. UnitPrice Distribution
    plt.figure()
    sns.histplot(df['UnitPrice'], kde=True, color='#B91C1C', bins=30)
    plt.title("Distribution of Product Unit Prices")
    plt.xlabel("Unit Price (Rs.)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGES_DIR, "04_univariate_unitprice.png"), dpi=300)
    plt.close()
    
    # 05. Product Counts
    plt.figure()
    sns.countplot(data=df, x='Product', order=df['Product'].value_counts().index, palette='viridis')
    plt.title("Sales Transaction Counts by Product SKU")
    plt.xlabel("Product Name")
    plt.ylabel("Number of Sales Transactions")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGES_DIR, "05_univariate_products.png"), dpi=300)
    plt.close()
    
    # 06. Order Status Distribution (Donut Chart)
    plt.figure(figsize=(7, 7))
    status_counts = df['OrderStatus'].value_counts()
    colors = ['#10B981', '#3B82F6', '#EF4444', '#F59E0B', '#6B7280']
    plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90, 
            colors=colors, wedgeprops=dict(width=0.4, edgecolor='w'))
    plt.title("E-Commerce Order Fulfillment States")
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGES_DIR, "06_univariate_status.png"), dpi=300)
    plt.close()

def generate_bivariate_plots(df):
    print("Generating Bivariate Visualizations...")
    
    # 07. Quantity vs. TotalPrice Scatter
    plt.figure()
    sns.scatterplot(data=df, x='Quantity', y='TotalPrice', hue='Product', alpha=0.7, palette='tab10')
    plt.title("Order Volume vs. Total Invoice Value")
    plt.xlabel("Quantity Ordered")
    plt.ylabel("Total Invoice Price (Rs.)")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGES_DIR, "07_bivariate_quantity_totalprice.png"), dpi=300)
    plt.close()
    
    # 08. ItemsInCart vs. TotalPrice Scatter
    plt.figure()
    sns.boxplot(data=df, x='ItemsInCart', y='TotalPrice', palette='crest')
    plt.title("Shopping Cart Basket Size vs. Order Value")
    plt.xlabel("Number of Items in Cart")
    plt.ylabel("Total Invoice Price (Rs.)")
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGES_DIR, "08_bivariate_itemsincart_totalprice.png"), dpi=300)
    plt.close()
    
    # 09. PaymentMethod vs. Revenue
    plt.figure()
    payment_revenue = df.groupby('PaymentMethod')['TotalPrice'].sum().sort_values(ascending=False).reset_index()
    sns.barplot(data=payment_revenue, x='PaymentMethod', y='TotalPrice', palette='Blues_d')
    plt.title("Total Store Revenue Contributed by Payment Method")
    plt.xlabel("Payment Method Selection")
    plt.ylabel("Cumulative Revenue (Rs.)")
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGES_DIR, "09_bivariate_payment_revenue.png"), dpi=300)
    plt.close()
    
    # 10. ReferralSource vs. Revenue
    plt.figure()
    referral_revenue = df.groupby('ReferralSource')['TotalPrice'].sum().sort_values(ascending=False).reset_index()
    sns.barplot(data=referral_revenue, x='ReferralSource', y='TotalPrice', palette='flare')
    plt.title("Acquisition Channel Performance (Total Revenue Generated)")
    plt.xlabel("Marketing Referral Channel")
    plt.ylabel("Cumulative Revenue (Rs.)")
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGES_DIR, "10_bivariate_referral_revenue.png"), dpi=300)
    plt.close()
    
    # 11. CouponCode vs. Average TotalPrice
    plt.figure()
    coupon_order = df.groupby('CouponCode')['TotalPrice'].mean().sort_values(ascending=False).reset_index()
    sns.barplot(data=coupon_order, x='CouponCode', y='TotalPrice', palette='rocket')
    plt.title("Impact of Coupon Campaign on Average Order Value")
    plt.xlabel("Discount Coupon Code Applied")
    plt.ylabel("Average Invoice Price (Rs.)")
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGES_DIR, "11_bivariate_coupon_revenue.png"), dpi=300)
    plt.close()
    
    # 12. Product Category Performance (Quantity & Revenue)
    prod_perf = df.groupby('Product').agg({'Quantity': 'sum', 'TotalPrice': 'sum'}).sort_values(by='TotalPrice', ascending=False).reset_index()
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    color = '#1E3A8A'
    ax1.set_xlabel('Product Catalog Item')
    ax1.set_ylabel('Total Revenue (Rs.)', color=color)
    sns.barplot(data=prod_perf, x='Product', y='TotalPrice', palette='mako', ax=ax1)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
    
    ax2 = ax1.twinx()  
    color = '#B91C1C'
    ax2.set_ylabel('Total Quantity Sold', color=color)
    sns.lineplot(data=prod_perf, x='Product', y='Quantity', color=color, marker='o', ax=ax2, sort=False, linewidth=2.5)
    ax2.tick_params(axis='y', labelcolor=color)
    
    plt.title("Dual-Axis Product SKU Sales Performance Analysis")
    fig.tight_layout()
    plt.savefig(os.path.join(IMAGES_DIR, "12_bivariate_product_revenue.png"), dpi=300)
    plt.close()
    
    # 13. Monthly Sales Revenue Over Time
    df['OrderYearMonth'] = pd.to_datetime(df['Date']).dt.to_period('M')
    monthly_rev = df.groupby('OrderYearMonth')['TotalPrice'].sum().reset_index()
    monthly_rev['OrderYearMonth'] = monthly_rev['OrderYearMonth'].astype(str)
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=monthly_rev, x='OrderYearMonth', y='TotalPrice', marker='o', color='#0F766E', linewidth=2.5)
    plt.title("E-Commerce Monthly Sales Revenue Lifecycle Trends (2023 - 2025)")
    plt.xlabel("Order Calendar Month")
    plt.ylabel("Cumulative Revenue (Rs.)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGES_DIR, "13_bivariate_monthly_revenue.png"), dpi=300)
    plt.close()

def generate_multivariate_plots(df):
    print("Generating Multivariate Visualizations...")
    
    # 14. Correlation Heatmap
    plt.figure()
    num_cols = ['Quantity', 'UnitPrice', 'ItemsInCart', 'TotalPrice', 'DiscountPercent', 'OrderYear', 'OrderMonth', 'IsWeekend']
    corr_matrix = df[num_cols].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".3f", linewidths=.5, vmin=-1, vmax=1)
    plt.title("Multi-Dimensional Numerical Correlation Heatmap Matrix")
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGES_DIR, "14_multivariate_correlation.png"), dpi=300)
    plt.close()

def generate_outlier_plots(df):
    print("Generating Outlier Visualizations...")
    
    # 15. Outlier TotalPrice Boxplot
    plt.figure()
    sns.boxplot(x=df['TotalPrice'], color='#4338CA')
    plt.title("TotalPrice Outlier IQR Distribution Profile")
    plt.xlabel("Adjusted Total Price (Rs.)")
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGES_DIR, "15_outlier_totalprice.png"), dpi=300)
    plt.close()
    
    # 16. Outlier Quantity Boxplot
    plt.figure()
    sns.boxplot(x=df['Quantity'], color='#9333EA')
    plt.title("Order Volume Quantity Boxplot Profile")
    plt.xlabel("Quantity Ordered")
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGES_DIR, "16_outlier_quantity.png"), dpi=300)
    plt.close()

def answer_business_questions(df):
    print("\n=== ANSWERING 25 STRATEGIC BUSINESS QUESTIONS ===")
    
    # Q1: Total adjusted revenue
    total_rev = df['TotalPrice'].sum()
    print(f"Q1: What is the total adjusted revenue generated by the e-commerce store?\n-> Rs. {total_rev:,.2f}")
    
    # Q2: Total orders placed
    total_orders = len(df)
    print(f"\nQ2: What is the total number of orders placed?\n-> {total_orders:,} orders")
    
    # Q3: Unique customers & repeat rate
    unique_custs = df['CustomerID'].nunique()
    repeat_custs = (df['CustomerID'].value_counts() > 1).sum()
    repeat_rate = (repeat_custs / unique_custs) * 100
    print(f"\nQ3: How many unique customers made purchases, and what is the repeat customer rate?\n-> Unique Customers: {unique_custs:,} | Repeat Customers: {repeat_custs:,} | Repeat Rate: {repeat_rate:.2f}%")
    
    # Q4: Overall Average Order Value (AOV)
    aov = df['TotalPrice'].mean()
    print(f"\nQ4: What is the overall average order value (AOV)?\n-> Rs. {aov:.2f}")
    
    # Q5: Product sold highest quantity
    highest_qty_prod = df.groupby('Product')['Quantity'].sum().idxmax()
    highest_qty_val = df.groupby('Product')['Quantity'].sum().max()
    print(f"\nQ5: Which product sold the highest quantity?\n-> {highest_qty_prod} ({highest_qty_val:,} units)")
    
    # Q6: Product generated highest revenue
    highest_rev_prod = df.groupby('Product')['TotalPrice'].sum().idxmax()
    highest_rev_val = df.groupby('Product')['TotalPrice'].sum().max()
    print(f"\nQ6: Which product generated the highest total revenue?\n-> {highest_rev_prod} (Rs. {highest_rev_val:,.2f})")
    
    # Q7: Distribution of orders by status
    status_dist = df['OrderStatus'].value_counts()
    print(f"\nQ7: What is the distribution of orders by order status?\n{status_dist.to_string()}")
    
    # Q8: Cancellation rate & revenue impact
    cancellation_cnt = (df['OrderStatus'] == 'Cancelled').sum()
    cancellation_rate = (cancellation_cnt / total_orders) * 100
    cancelled_rev = df[df['OrderStatus'] == 'Cancelled']['TotalPrice'].sum()
    print(f"\nQ8: What is the cancellation rate, and what is its revenue impact?\n-> Cancellation Rate: {cancellation_rate:.2f}% ({cancellation_cnt} orders) | Lost Gross Revenue: Rs. {cancelled_rev:,.2f}")
    
    # Q9: Return rate & revenue impact
    return_cnt = (df['OrderStatus'] == 'Returned').sum()
    return_rate = (return_cnt / total_orders) * 100
    returned_rev = df[df['OrderStatus'] == 'Returned']['TotalPrice'].sum()
    print(f"\nQ9: What is the return rate, and what is its revenue impact?\n-> Return Rate: {return_rate:.2f}% ({return_cnt} orders) | Lost Gross Revenue: Rs. {returned_rev:,.2f}")
    
    # Q10: Payment method popularity & revenue
    payment_stats = df.groupby('PaymentMethod').agg({'OrderID': 'count', 'TotalPrice': 'sum'}).rename(columns={'OrderID': 'OrderCount', 'TotalPrice': 'TotalRevenue'}).sort_values(by='OrderCount', ascending=False)
    print(f"\nQ10: Which payment method is the most popular, and how much revenue does it contribute?\n{payment_stats.to_string()}")
    
    # Q11: Referral source with most orders
    referral_cnt = df['ReferralSource'].value_counts()
    print(f"\nQ11: Which marketing referral source generates the most orders?\n{referral_cnt.to_string()}")
    
    # Q12: Referral source with highest AOV
    referral_aov = df.groupby('ReferralSource')['TotalPrice'].mean().sort_values(ascending=False)
    print(f"\nQ12: Which referral source brings in the highest Average Order Value (AOV)?\n{referral_aov.to_string()}")
    
    # Q13: Percentage of orders with coupon
    coupon_orders_pct = (df['DiscountPercent'] > 0.0).mean() * 100
    print(f"\nQ13: What percentage of orders utilized a coupon code?\n-> {coupon_orders_pct:.2f}% of orders")
    
    # Q14: Coupon code frequency & total discount
    coupon_freq = df['CouponCode'].value_counts(dropna=False)
    # Calculate discount given: discount = Quantity * UnitPrice * (DiscountPercent / 100)
    df['DiscountVal'] = df['Quantity'] * df['UnitPrice'] * (df['DiscountPercent'] / 100.0)
    coupon_discounts = df.groupby('CouponCode')['DiscountVal'].sum().sort_values(ascending=False)
    print(f"\nQ14: Which coupon code was used most frequently, and what was the total discount value given?\n-> Coupon Code Usage:\n{coupon_freq.to_string()}\n-> Cumulative Discount Values:\n{coupon_discounts.to_string()}")
    
    # Q15: Average basket size (items in cart) coupon vs no-coupon
    avg_basket_coupon = df[df['DiscountPercent'] > 0.0]['ItemsInCart'].mean()
    avg_basket_no_coupon = df[df['DiscountPercent'] == 0.0]['ItemsInCart'].mean()
    print(f"\nQ15: Is there a difference in average basket size (items in cart) between orders with coupons and without?\n-> Orders with Coupons: {avg_basket_coupon:.2f} items | Orders without Coupons: {avg_basket_no_coupon:.2f} items")
    
    # Q16: Sales revenue trends over years
    yearly_rev = df.groupby('OrderYear')['TotalPrice'].sum().rename("Revenue")
    yearly_orders = df.groupby('OrderYear')['OrderID'].count().rename("Orders")
    yearly_stats = pd.concat([yearly_orders, yearly_rev], axis=1)
    print(f"\nQ16: How does sales revenue trend over the years (2023, 2024, and 2025)?\n{yearly_stats.to_string()}")
    
    # Q17: Top 3 peak sales months
    df['YearMonth'] = df['Date'].astype(str).str[:7]
    top_months = df.groupby('YearMonth')['TotalPrice'].sum().sort_values(ascending=False).head(3)
    print(f"\nQ17: What are the top 3 peak sales months across the entire dataset?\n{top_months.to_string()}")
    
    # Q18: Weekend vs Weekday revenue split
    weekend_split = df.groupby('IsWeekend')['TotalPrice'].sum().rename(index={0: 'Weekday', 1: 'Weekend'})
    print(f"\nQ18: What is the revenue split between weekends and weekdays?\n{weekend_split.to_string()}")
    
    # Q19: Distribution of order value categories
    value_cat_dist = df['OrderValueCategory'].value_counts()
    print(f"\nQ19: What is the distribution of order value categories (Low, Medium, High)?\n{value_cat_dist.to_string()}")
    
    # Q20: Correlation between ItemsInCart and TotalPrice
    corr_cart_price = df['ItemsInCart'].corr(df['TotalPrice'])
    print(f"\nQ20: Do customers who put more items in their cart also tend to spend more per order (correlation)?\n-> Pearson Correlation Coefficient: {corr_cart_price:.4f} (indicating very weak or negligible direct linear correlation due to pricing model)")
    
    # Q21: Average quantity purchased per order
    avg_qty = df['Quantity'].mean()
    print(f"\nQ21: What is the average quantity of items purchased per order?\n-> {avg_qty:.2f} units per order line")
    
    # Q22: Cancelled orders vs payment method
    cancelled_by_pm = df[df['OrderStatus'] == 'Cancelled'].groupby('PaymentMethod')['OrderID'].count().sort_values(ascending=False)
    print(f"\nQ22: Are orders placed through specific payment methods more prone to cancellation?\n{cancelled_by_pm.to_string()}")
    
    # Q23: High-value orders (> Rs. 1000) count and share
    high_val_cnt = (df['TotalPrice'] > 1000.0).sum()
    high_val_rev = df[df['TotalPrice'] > 1000.0]['TotalPrice'].sum()
    high_val_rev_share = (high_val_rev / total_rev) * 100
    print(f"\nQ23: How many high-value orders (> Rs. 1,000) occurred, and what share of total revenue do they represent?\n-> High-Value Count: {high_val_cnt} | Cumulative Revenue: Rs. {high_val_rev:,.2f} ({high_val_rev_share:.2f}% of total store revenue)")
    
    # Q24: Revenue contribution of each product category
    product_rev = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False)
    print(f"\nQ24: What is the revenue contribution of each product category?\n{product_rev.to_string()}")
    
    # Q25: Referral source vs Return rate
    returned_orders = df[df['OrderStatus'] == 'Returned']
    returns_by_source = returned_orders.groupby('ReferralSource')['OrderID'].count()
    total_by_source = df.groupby('ReferralSource')['OrderID'].count()
    return_rate_by_source = ((returns_by_source / total_by_source) * 100).sort_values(ascending=False)
    print(f"\nQ25: Which marketing referral source has the highest return rate (potential quality/ad-mismatch issue)?\n{return_rate_by_source.to_string()}")
    
    print("=================================================\n")

def main():
    print("=== STARTING EXPLORATORY DATA ANALYSIS AND PLOTTING ===")
    df = load_data()
    generate_descriptive_stats(df)
    generate_univariate_plots(df)
    generate_bivariate_plots(df)
    generate_multivariate_plots(df)
    generate_outlier_plots(df)
    answer_business_questions(df)
    print("EDA Complete. All 16 visualization plots exported successfully.")

if __name__ == "__main__":
    main()
