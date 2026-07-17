"""
Visualizations module for generating 10+ professional, portfolio-grade charts
representing E-Commerce business metrics.
"""

import os
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from config import DB_PATH, IMAGES_DIR
from helper import logger

# Set global matplotlib parameters for clean, premium design
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "Helvetica"]
plt.rcParams["text.color"] = "#1E293B"
plt.rcParams["axes.labelcolor"] = "#475569"
plt.rcParams["xtick.color"] = "#64748B"
plt.rcParams["ytick.color"] = "#64748B"
plt.rcParams["grid.color"] = "#E2E8F0"
plt.rcParams["grid.linestyle"] = "--"
plt.rcParams["grid.linewidth"] = 0.5

# Premium Color Palette
COLORS = ["#0F172A", "#2563EB", "#0D9488", "#F59E0B", "#DC2626", "#7C3AED", "#EC4899"]
GRADIENT_TEAL_BLUE = ["#1E3A8A", "#2563EB", "#3B82F6", "#60A5FA", "#0D9488", "#14B8A6", "#2DD4BF"]

def save_plot(filename):
    """
    Saves the active plot to the images directory.
    """
    path = os.path.join(IMAGES_DIR, filename)
    plt.tight_layout()
    plt.savefig(path, dpi=300, bbox_inches="tight")
    plt.close()
    logger.info(f"Saved visualization to: {path}")

def generate_visualizations():
    """
    Queries database and generates all 10 required business charts.
    """
    logger.info("Starting visualization generation...")

    if not os.path.exists(DB_PATH):
        logger.error(f"Database not found at: {DB_PATH}. Run database_setup.py first.")
        raise FileNotFoundError(f"Database not found at: {DB_PATH}")

    conn = sqlite3.connect(DB_PATH)

    # Chart 1: Sales Trend (Daily Sales Trend over time)
    logger.info("Generating Chart 1: Sales Trend...")
    df_daily = pd.read_sql_query("""
        SELECT Date, SUM(TotalPrice) AS DailyRevenue 
        FROM orders 
        GROUP BY Date 
        ORDER BY Date ASC;
    """, conn)
    df_daily["Date"] = pd.to_datetime(df_daily["Date"])
    # Group by week or 14-day rolling average to smooth trend
    df_daily = df_daily.set_index("Date").resample("W").sum().reset_index()
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_daily["Date"], df_daily["DailyRevenue"], color="#2563EB", linewidth=2.5, marker="o", markersize=4, label="Weekly Revenue")
    ax.fill_between(df_daily["Date"], df_daily["DailyRevenue"], color="#2563EB", alpha=0.1)
    
    # 4-week rolling average
    df_daily["RollingAvg"] = df_daily["DailyRevenue"].rolling(window=4).mean()
    ax.plot(df_daily["Date"], df_daily["RollingAvg"], color="#F59E0B", linewidth=2, linestyle="--", label="4-Week Rolling Trend")
    
    ax.set_title("E-Commerce Revenue Trend Over Time (Weekly Aggregation)", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Order Date", fontsize=11, labelpad=10)
    ax.set_ylabel("Revenue ($)", fontsize=11, labelpad=10)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    ax.grid(True)
    ax.legend(frameon=True, facecolor="#F8FAFC", edgecolor="#E2E8F0")
    save_plot("sales_trend.png")

    # Chart 2: Monthly Revenue
    logger.info("Generating Chart 2: Monthly Revenue...")
    df_monthly = pd.read_sql_query("""
        SELECT Month, GrossRevenue FROM vw_monthly_sales ORDER BY Month ASC;
    """, conn)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.bar(df_monthly["Month"], df_monthly["GrossRevenue"], color=GRADIENT_TEAL_BLUE[:len(df_monthly)], width=0.6, edgecolor="#E2E8F0")
    ax.set_title("Gross Revenue by Month", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Month", fontsize=11, labelpad=10)
    ax.set_ylabel("Gross Revenue ($)", fontsize=11, labelpad=10)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    ax.grid(True, axis="y")
    plt.xticks(rotation=45)
    
    # Add value labels on top of the bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 2000, "${:,.0f}".format(yval), ha="center", va="bottom", fontsize=9, fontweight="bold")
    
    save_plot("monthly_revenue.png")

    # Chart 3: Top Products by Revenue
    logger.info("Generating Chart 3: Top Products...")
    df_products = pd.read_sql_query("""
        SELECT Product, RevenueGenerated FROM vw_product_performance ORDER BY RevenueGenerated ASC;
    """, conn)
    
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(df_products["Product"], df_products["RevenueGenerated"], color="#0D9488", height=0.6)
    ax.set_title("Revenue by Product Category", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Revenue Generated ($)", fontsize=11, labelpad=10)
    ax.set_ylabel("Product Category", fontsize=11, labelpad=10)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    ax.grid(True, axis="x")
    
    for bar in bars:
        xval = bar.get_width()
        ax.text(xval + 3000, bar.get_y() + bar.get_height()/2, "${:,.0f}".format(xval), ha="left", va="center", fontsize=9, fontweight="bold")
        
    save_plot("top_products.png")

    # Chart 4: Revenue by Referral Source
    logger.info("Generating Chart 4: Revenue by Referral Source...")
    df_referral = pd.read_sql_query("""
        SELECT ReferralSource, SUM(TotalPrice) AS Revenue 
        FROM orders 
        GROUP BY ReferralSource 
        ORDER BY Revenue DESC;
    """, conn)
    
    fig, ax = plt.subplots(figsize=(6, 6))
    pie_result = ax.pie(
        df_referral["Revenue"], 
        labels=df_referral["ReferralSource"], 
        autopct="%1.1f%%", 
        startangle=140, 
        colors=COLORS,
        textprops=dict(color="#1E293B"),
        wedgeprops=dict(width=0.4, edgecolor="white", linewidth=2) # Donut chart!
    )
    autotexts = pie_result[2]
    plt.setp(autotexts, size=10, weight="bold")
    ax.set_title("Revenue Share by Referral Source", fontsize=14, fontweight="bold", pad=15)
    save_plot("revenue_by_referral.png")

    # Chart 5: Revenue by Payment Method
    logger.info("Generating Chart 5: Revenue by Payment Method...")
    df_payment = pd.read_sql_query("""
        SELECT PaymentMethod, SUM(TotalPrice) AS Revenue 
        FROM orders 
        GROUP BY PaymentMethod 
        ORDER BY Revenue DESC;
    """, conn)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(df_payment["PaymentMethod"], df_payment["Revenue"], color="#7C3AED", width=0.5)
    ax.set_title("Revenue Contribution by Payment Method", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Payment Method", fontsize=11, labelpad=10)
    ax.set_ylabel("Revenue ($)", fontsize=11, labelpad=10)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    ax.grid(True, axis="y")
    
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 2000, "${:,.0f}".format(yval), ha="center", va="bottom", fontsize=9, fontweight="bold")
        
    save_plot("revenue_by_payment.png")

    # Chart 6: Coupon Performance (Total Orders and AOV)
    logger.info("Generating Chart 6: Coupon Performance...")
    df_coupon = pd.read_sql_query("""
        SELECT CouponCode, COUNT(OrderID) AS TotalOrders, AVG(TotalPrice) AS AOV 
        FROM orders 
        GROUP BY CouponCode 
        ORDER BY TotalOrders DESC;
    """, conn)
    
    fig, ax1 = plt.subplots(figsize=(9, 5))
    color_orders = "#2563EB"
    ax1.set_xlabel("Coupon Code", fontsize=11, labelpad=10)
    ax1.set_ylabel("Total Orders", color=color_orders, fontsize=11, labelpad=10)
    bars = ax1.bar(df_coupon["CouponCode"], df_coupon["TotalOrders"], color=color_orders, alpha=0.6, width=0.4, label="Total Orders")
    ax1.tick_params(axis="y", labelcolor=color_orders)
    ax1.grid(True, axis="y")
    
    ax2 = ax1.twinx()  
    color_aov = "#D97706"
    ax2.set_ylabel("Average Order Value (AOV) ($)", color=color_aov, fontsize=11, labelpad=10)
    ax2.plot(df_coupon["CouponCode"], df_coupon["AOV"], color=color_aov, marker="D", linewidth=2.5, markersize=6, label="AOV ($)")
    ax2.tick_params(axis="y", labelcolor=color_aov)
    
    plt.title("Coupon Code Performance Analysis", fontsize=14, fontweight="bold", pad=15)
    save_plot("coupon_performance.png")

    # Chart 7: Order Status Distribution
    logger.info("Generating Chart 7: Order Status Distribution...")
    df_status = pd.read_sql_query("""
        SELECT OrderStatus, COUNT(OrderID) AS Count 
        FROM orders 
        GROUP BY OrderStatus 
        ORDER BY Count DESC;
    """, conn)
    
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(
        df_status["Count"], 
        labels=df_status["OrderStatus"], 
        autopct="%1.1f%%", 
        startangle=90, 
        colors=["#0D9488", "#2563EB", "#F59E0B", "#EF4444", "#8B5CF6"],
        wedgeprops=dict(width=0.4, edgecolor="white", linewidth=2)
    )
    ax.set_title("Order Status Distribution", fontsize=14, fontweight="bold", pad=15)
    save_plot("order_status_distribution.png")

    # Chart 8: Top 10 Customers by Spend
    logger.info("Generating Chart 8: Top Customers...")
    df_cust = pd.read_sql_query("""
        SELECT CustomerID, LifetimeSpent 
        FROM vw_customer_lifetime_value 
        ORDER BY LifetimeSpent DESC 
        LIMIT 10;
    """, conn)
    # Reverse to plot largest on top in horizontal bar
    df_cust = df_cust.iloc[::-1]
    
    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(df_cust["CustomerID"], df_cust["LifetimeSpent"], color="#3B82F6", height=0.5)
    ax.set_title("Top 10 High-Value VIP Customers", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Lifetime Spent ($)", fontsize=11, labelpad=10)
    ax.set_ylabel("Customer ID", fontsize=11, labelpad=10)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    ax.grid(True, axis="x")
    
    for bar in bars:
        xval = bar.get_width()
        ax.text(xval + 100, bar.get_y() + bar.get_height()/2, "${:,.0f}".format(xval), ha="left", va="center", fontsize=9, fontweight="bold")
        
    save_plot("top_customers.png")

    # Chart 9: Average Order Value (AOV) by Product
    logger.info("Generating Chart 9: Average Order Value by Product...")
    df_aov = pd.read_sql_query("""
        SELECT Product, AVG(TotalPrice) AS ProductAOV 
        FROM orders 
        GROUP BY Product 
        ORDER BY ProductAOV DESC;
    """, conn)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(df_aov["Product"], df_aov["ProductAOV"], color="#EC4899", width=0.5)
    ax.set_title("Average Order Value (AOV) by Product Category", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Product Category", fontsize=11, labelpad=10)
    ax.set_ylabel("AOV ($)", fontsize=11, labelpad=10)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    ax.grid(True, axis="y")
    
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 15, "${:,.0f}".format(yval), ha="center", va="bottom", fontsize=9, fontweight="bold")
        
    save_plot("average_order_value.png")

    # Chart 10: Product Frequency (Total Units Sold)
    logger.info("Generating Chart 10: Product Frequency...")
    df_freq = pd.read_sql_query("""
        SELECT Product, TotalQuantitySold FROM vw_product_performance ORDER BY TotalQuantitySold DESC;
    """, conn)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(df_freq["Product"], df_freq["TotalQuantitySold"], color="#14B8A6", width=0.5)
    ax.set_title("Total Units Sold by Product Category", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Product Category", fontsize=11, labelpad=10)
    ax.set_ylabel("Quantity Sold (Units)", fontsize=11, labelpad=10)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    ax.grid(True, axis="y")
    
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 10, "{:,}".format(int(yval)), ha="center", va="bottom", fontsize=9, fontweight="bold")
        
    save_plot("product_frequency.png")

    conn.close()
    logger.info("All visualizations generated and saved successfully!")

if __name__ == "__main__":
    generate_visualizations()
