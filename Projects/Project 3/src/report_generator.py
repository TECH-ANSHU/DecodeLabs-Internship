"""
Report Generator module for compiling a multi-page PDF executive report
with text documentation and embedded visualizations.
"""

import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from config import REPORT_PATH, IMAGES_DIR
from helper import logger

def wrap_text(text, max_chars=80):
    """
    Wraps text to a maximum number of characters per line.
    """
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        if len(" ".join(current_line + [word])) > max_chars:
            lines.append(" ".join(current_line))
            current_line = [word]
        else:
            current_line.append(word)
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def create_pdf_report():
    """
    Compiles the complete E-Commerce Data Analytics Executive Report PDF.
    """
    logger.info(f"Initiating PDF report creation at: {REPORT_PATH}")

    # Verify if visualizations exist
    required_charts = [
        "sales_trend.png", "monthly_revenue.png", "top_products.png",
        "revenue_by_referral.png", "revenue_by_payment.png", 
        "coupon_performance.png", "order_status_distribution.png"
    ]
    for chart in required_charts:
        chart_path = os.path.join(IMAGES_DIR, chart)
        if not os.path.exists(chart_path):
            logger.error(f"Required chart not found for report: {chart_path}")
            raise FileNotFoundError(f"Missing visualization asset: {chart_path}")

    # Set up PDF document
    with PdfPages(REPORT_PATH) as pdf:
        
        # ----------------------------------------------------
        # PAGE 1: COVER PAGE
        # ----------------------------------------------------
        logger.info("Writing PDF Cover Page...")
        fig, ax = plt.subplots(figsize=(8.5, 11), facecolor="#0F172A")
        ax.axis("off")
        
        # Decorative shapes/lines
        ax.plot([0.1, 0.9], [0.8, 0.8], color="#38BDF8", transform=ax.transAxes, linewidth=4)
        ax.plot([0.1, 0.9], [0.2, 0.2], color="#38BDF8", transform=ax.transAxes, linewidth=2)
        
        # Text annotations
        fig.text(0.5, 0.65, "E-COMMERCE DATA ANALYTICS &\nBUSINESS INTELLIGENCE REPORT", 
                 color="#FFFFFF", fontsize=24, fontweight="bold", ha="center", va="center")
        fig.text(0.5, 0.55, "Data Auditing, SQLite Ingestion, SQL Analysis, and Python Automation", 
                 color="#94A3B8", fontsize=12, style="italic", ha="center", va="center")
        
        fig.text(0.5, 0.35, "PREPARED FOR: DECODELABS INTERNSHIP PROGRAM", 
                 color="#38BDF8", fontsize=11, fontweight="semibold", ha="center", va="center")
        fig.text(0.5, 0.28, "Prepared by: Portfolio Candidate\nRole: Senior Data Analyst & SQL Developer\nDate: July 2026", 
                 color="#E2E8F0", fontsize=10, ha="center", va="center", linespacing=1.6)
        
        pdf.savefig(fig, facecolor=fig.get_facecolor())
        plt.close()

        # ----------------------------------------------------
        # PAGE 2: INTRODUCTION & OBJECTIVES
        # ----------------------------------------------------
        logger.info("Writing PDF Page 2: Intro & Objectives...")
        fig, ax = plt.subplots(figsize=(8.5, 11), facecolor="#F8FAFC")
        ax.axis("off")
        
        # Title banner
        fig.text(0.1, 0.9, "1. Introduction & Project Objectives", color="#1E3A8A", fontsize=18, fontweight="bold")
        ax.plot([0.1, 0.9], [0.88, 0.88], color="#0D9488", transform=ax.transAxes, linewidth=1.5)
        
        intro_text = (
            "This project presents an end-to-end industry-grade analytics workflow "
            "designed to convert raw transactional E-Commerce data into strategic, "
            "actionable business intelligence. Modern online retail operations generate "
            "massive volumes of customer touchpoints daily. Harnessing this data "
            "through structured query languages and automated python pipelines is "
            "essential for maintaining competitive advantages, identifying leakages, and "
            "optimizing resource allocation."
        )
        
        obj_text = (
            "The primary objectives of this analytical initiative are:\n"
            "• Clean and audit raw transaction records for accuracy and formatting anomalies.\n"
            "• Design a relational schema and migrate datasets to an optimized SQLite database.\n"
            "• Engineer 46 business queries to extract descriptive and window-based analytics.\n"
            "• Develop dynamic data visualizations to illustrate sales trends and customer segments.\n"
            "• Automate operational reports to bridge technical analysis and stakeholder actions."
        )
        
        y = 0.82
        for line in wrap_text(intro_text, 75):
            fig.text(0.1, y, line, color="#1E293B", fontsize=11, family="sans-serif")
            y -= 0.025
        
        y -= 0.03
        fig.text(0.1, y, "Key Project Goals:", color="#0F172A", fontsize=13, fontweight="bold")
        y -= 0.04
        
        for line in obj_text.split("\n"):
            wrapped_lines = wrap_text(line, 75)
            for wl in wrapped_lines:
                fig.text(0.1, y, wl, color="#1E293B", fontsize=11)
                y -= 0.025
            y -= 0.01
            
        pdf.savefig(fig, facecolor=fig.get_facecolor())
        plt.close()

        # ----------------------------------------------------
        # PAGE 3: METHODOLOGY & DATABASE DESIGN
        # ----------------------------------------------------
        logger.info("Writing PDF Page 3: Methodology...")
        fig, ax = plt.subplots(figsize=(8.5, 11), facecolor="#F8FAFC")
        ax.axis("off")
        
        fig.text(0.1, 0.9, "2. Analytical Methodology & Database Design", color="#1E3A8A", fontsize=18, fontweight="bold")
        ax.plot([0.1, 0.9], [0.88, 0.88], color="#0D9488", transform=ax.transAxes, linewidth=1.5)
        
        meth_text = (
            "Our data analytics pipeline consists of four major stages: "
            "Data Extraction/Ingestion, Data Cleansing, Database Normalization/Indexing, "
            "and Business Intelligence Automation. Data is loaded from raw formats, stripped of "
            "whitespaces, audited for calculation errors (validating TotalPrice = Quantity * UnitPrice), "
            "and imported into SQLite."
        )
        
        schema_text = (
            "The database design implements a structured schema to facilitate relational lookups:\n\n"
            "• Table [orders]: Houses transactional metrics (OrderID [PK], Date, CustomerID, Product, "
            "Quantity, UnitPrice, TotalPrice, ShippingAddress, PaymentMethod, OrderStatus, TrackingNumber, "
            "ItemsInCart, CouponCode [FK], ReferralSource).\n\n"
            "• Table [coupons]: Holds promotional metadata (CouponCode [PK], DiscountPercent, Description).\n\n"
            "• Indexes: Created on CustomerID, Product, and Date to speed up aggregations.\n\n"
            "• Views: Pre-compiled SQL views for Monthly Sales, Customer Lifetime Value, and "
            "Product Performance were deployed for optimized dashboard queries."
        )
        
        y = 0.82
        for line in wrap_text(meth_text, 75):
            fig.text(0.1, y, line, color="#1E293B", fontsize=11)
            y -= 0.025
            
        y -= 0.03
        fig.text(0.1, y, "Database Architecture & Tables:", color="#0F172A", fontsize=13, fontweight="bold")
        y -= 0.04
        
        for line in schema_text.split("\n"):
            wrapped_lines = wrap_text(line, 75)
            for wl in wrapped_lines:
                fig.text(0.1, y, wl, color="#1E293B", fontsize=11)
                y -= 0.025
            y -= 0.005
            
        pdf.savefig(fig, facecolor=fig.get_facecolor())
        plt.close()

        # ----------------------------------------------------
        # PAGE 4: SQL CONCEPTS OVERVIEW
        # ----------------------------------------------------
        logger.info("Writing PDF Page 4: SQL Concepts...")
        fig, ax = plt.subplots(figsize=(8.5, 11), facecolor="#F8FAFC")
        ax.axis("off")
        
        fig.text(0.1, 0.9, "3. Core SQL Concepts & Techniques Used", color="#1E3A8A", fontsize=18, fontweight="bold")
        ax.plot([0.1, 0.9], [0.88, 0.88], color="#0D9488", transform=ax.transAxes, linewidth=1.5)
        
        sql_intro = (
            "To unlock advanced insights, this project leveraged a broad array of "
            "SQL keywords and concepts, mapping standard aggregations to advanced window analytics."
        )
        
        concepts = [
            "✔ DDL & Schema Enforcement: CREATE TABLE with constraints (CHECK, PRIMARY KEY, FOREIGN KEY).",
            "✔ Aggregations & Filtering: WHERE, GROUP BY, HAVING, COUNT(), SUM(), AVG(), MAX(), MIN().",
            "✔ Conditional Logic: CASE WHEN blocks to categorize customer tiers and week names.",
            "✔ Date & String Manipulation: strftime() to parse monthly patterns; SUBSTR() and INSTR() to split addresses.",
            "✔ Relational Joins: JOINing orders with coupons to audit revenue leakages and discount costs.",
            "✔ Subqueries & CTEs: CTEs for multi-step window calculations and MoM growth metrics.",
            "✔ Analytical Window Functions: RANK(), DENSE_RANK(), SUM() OVER (cumulative running totals), and AVG() OVER (rolling averages) to analyze trend changes."
        ]
        
        y = 0.82
        for line in wrap_text(sql_intro, 75):
            fig.text(0.1, y, line, color="#1E293B", fontsize=11)
            y -= 0.025
            
        y -= 0.03
        fig.text(0.1, y, "Inventory of Implemented Concepts:", color="#0F172A", fontsize=13, fontweight="bold")
        y -= 0.04
        
        for concept in concepts:
            wrapped_lines = wrap_text(concept, 75)
            for wl in wrapped_lines:
                fig.text(0.1, y, wl, color="#1E293B", fontsize=11)
                y -= 0.025
            y -= 0.015
            
        pdf.savefig(fig, facecolor=fig.get_facecolor())
        plt.close()

        # ----------------------------------------------------
        # PAGE 5: DASHBOARD 1 (Sales Trend & Monthly Revenue)
        # ----------------------------------------------------
        logger.info("Writing PDF Page 5: Dashboard 1...")
        fig = plt.figure(figsize=(8.5, 11), facecolor="#F8FAFC")
        
        # Draw background and title
        ax_title = fig.add_axes([0, 0, 1, 1])
        ax_title.axis("off")
        ax_title.text(0.1, 0.92, "4. Sales Trends & Monthly Revenue Performance", color="#1E3A8A", fontsize=16, fontweight="bold")
        ax_title.plot([0.1, 0.9], [0.90, 0.90], color="#0D9488", transform=ax_title.transAxes, linewidth=1.5)
        
        # Load and embed image 1 (Sales Trend)
        img1 = plt.imread(os.path.join(IMAGES_DIR, "sales_trend.png"))
        ax_img1 = fig.add_axes([0.1, 0.50, 0.8, 0.35])
        ax_img1.imshow(img1)
        ax_img1.axis("off")
        
        # Load and embed image 2 (Monthly Revenue)
        img2 = plt.imread(os.path.join(IMAGES_DIR, "monthly_revenue.png"))
        ax_img2 = fig.add_axes([0.1, 0.10, 0.8, 0.35])
        ax_img2.imshow(img2)
        ax_img2.axis("off")
        
        pdf.savefig(fig)
        plt.close()

        # ----------------------------------------------------
        # PAGE 6: DASHBOARD 2 (Products & Referral Channels)
        # ----------------------------------------------------
        logger.info("Writing PDF Page 6: Dashboard 2...")
        fig = plt.figure(figsize=(8.5, 11), facecolor="#F8FAFC")
        
        ax_title = fig.add_axes([0, 0, 1, 1])
        ax_title.axis("off")
        ax_title.text(0.1, 0.92, "5. Product Performance & Marketing Acquisition Share", color="#1E3A8A", fontsize=16, fontweight="bold")
        ax_title.plot([0.1, 0.9], [0.90, 0.90], color="#0D9488", transform=ax_title.transAxes, linewidth=1.5)
        
        # Embed product revenue
        img3 = plt.imread(os.path.join(IMAGES_DIR, "top_products.png"))
        ax_img3 = fig.add_axes([0.1, 0.50, 0.8, 0.35])
        ax_img3.imshow(img3)
        ax_img3.axis("off")
        
        # Embed referral revenue
        img4 = plt.imread(os.path.join(IMAGES_DIR, "revenue_by_referral.png"))
        ax_img4 = fig.add_axes([0.1, 0.10, 0.8, 0.35])
        ax_img4.imshow(img4)
        ax_img4.axis("off")
        
        pdf.savefig(fig)
        plt.close()

        # ----------------------------------------------------
        # PAGE 7: DASHBOARD 3 (Coupons & Payment Channels)
        # ----------------------------------------------------
        logger.info("Writing PDF Page 7: Dashboard 3...")
        fig = plt.figure(figsize=(8.5, 11), facecolor="#F8FAFC")
        
        ax_title = fig.add_axes([0, 0, 1, 1])
        ax_title.axis("off")
        ax_title.text(0.1, 0.92, "6. Coupon Performance & Order Distribution", color="#1E3A8A", fontsize=16, fontweight="bold")
        ax_title.plot([0.1, 0.9], [0.90, 0.90], color="#0D9488", transform=ax_title.transAxes, linewidth=1.5)
        
        # Embed coupon performance
        img5 = plt.imread(os.path.join(IMAGES_DIR, "coupon_performance.png"))
        ax_img5 = fig.add_axes([0.1, 0.50, 0.8, 0.35])
        ax_img5.imshow(img5)
        ax_img5.axis("off")
        
        # Embed order status distribution
        img6 = plt.imread(os.path.join(IMAGES_DIR, "order_status_distribution.png"))
        ax_img6 = fig.add_axes([0.1, 0.10, 0.8, 0.35])
        ax_img6.imshow(img6)
        ax_img6.axis("off")
        
        pdf.savefig(fig)
        plt.close()

        # ----------------------------------------------------
        # PAGE 8: BUSINESS INSIGHTS & RECOMMENDATIONS
        # ----------------------------------------------------
        logger.info("Writing PDF Page 8: Recommendations...")
        fig, ax = plt.subplots(figsize=(8.5, 11), facecolor="#F8FAFC")
        ax.axis("off")
        
        fig.text(0.1, 0.9, "7. Strategic Business Insights & Recommendations", color="#1E3A8A", fontsize=18, fontweight="bold")
        ax.plot([0.1, 0.9], [0.88, 0.88], color="#0D9488", transform=ax.transAxes, linewidth=1.5)
        
        insights = [
            "1. Focus Marketing on Top Referral Channels:\n"
            "Google SEO and Email newsletters drive the highest volume of repeat buyers. Instagram, while lower "
            "in volume, converted a higher percentage of premium electronic transactions. Action: Shift paid marketing "
            "spend toward Google search terms and Instagram influencer sponsorships targeting high-ticket buyers.",
            
            "2. Optimize Promotional Coupon Strategy:\n"
            "Coupons like SAVE10 and WINTER15 increase transaction frequency and cart size. However, unfettered use of "
            "15% off coupons on premium laptops and desks can result in substantial margin erosion. Action: Set absolute "
            "discount caps (e.g. maximum $150 discount per order) to protect margins on high-value products.",
            
            "3. Target B2B / Workstation Buyers:\n"
            "Bulk orders (quantity >= 5) are frequently monitors and office chairs, indicating corporate setup purchases. "
            "Action: Offer customized 'workstation bundles' and assign B2B account managers to cater to corporate sales."
        ]
        
        y = 0.82
        for insight in insights:
            lines = insight.split("\n")
            title_line = lines[0]
            body_line = lines[1]
            
            fig.text(0.1, y, title_line, color="#0F172A", fontsize=12, fontweight="bold")
            y -= 0.03
            
            wrapped_body = wrap_text(body_line, 75)
            for wl in wrapped_body:
                fig.text(0.1, y, wl, color="#1E293B", fontsize=11)
                y -= 0.025
            y -= 0.02
            
        pdf.savefig(fig, facecolor=fig.get_facecolor())
        plt.close()

        # ----------------------------------------------------
        # PAGE 9: CONCLUSION & FUTURE SCOPE
        # ----------------------------------------------------
        logger.info("Writing PDF Page 9: Conclusion...")
        fig, ax = plt.subplots(figsize=(8.5, 11), facecolor="#F8FAFC")
        ax.axis("off")
        
        fig.text(0.1, 0.9, "8. Future Scope & Conclusion", color="#1E3A8A", fontsize=18, fontweight="bold")
        ax.plot([0.1, 0.9], [0.88, 0.88], color="#0D9488", transform=ax.transAxes, linewidth=1.5)
        
        conclusion = (
            "This E-Commerce analytics project establishes a robust baseline for data-driven "
            "decision-making. By cleaning and organizing raw transactions, constructing an indexed "
            "SQLite database, running 46 targeted queries, and establishing automatic dashboards, we have "
            "provided operational and financial visibility to stakeholders."
        )
        
        future = (
            "Future analytical scopes include:\n"
            "• Predictive Modeling: Integrating machine learning to forecast demand and detect customer churn risks.\n"
            "• Real-Time Processing: Transitioning from batch SQLite to distributed Postgres or cloud warehouses.\n"
            "• Customer Segmentation: Refining customer clustering using RFM (Recency, Frequency, Monetary) algorithms.\n"
            "• Multi-Touch Attribution: Tracking complex marketing touchpoints to measure customer paths."
        )
        
        y = 0.82
        for line in wrap_text(conclusion, 75):
            fig.text(0.1, y, line, color="#1E293B", fontsize=11)
            y -= 0.025
            
        y -= 0.04
        fig.text(0.1, y, "Future Technical Roadmap:", color="#0F172A", fontsize=13, fontweight="bold")
        y -= 0.04
        
        for line in future.split("\n"):
            wrapped_lines = wrap_text(line, 75)
            for wl in wrapped_lines:
                fig.text(0.1, y, wl, color="#1E293B", fontsize=11)
                y -= 0.025
            y -= 0.01
            
        pdf.savefig(fig, facecolor=fig.get_facecolor())
        plt.close()

    logger.info("PDF report successfully written and compiled!")

if __name__ == "__main__":
    create_pdf_report()
