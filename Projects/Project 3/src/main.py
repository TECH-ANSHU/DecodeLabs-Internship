"""
Main Execution Orchestrator for the E-Commerce SQL Data Analytics & Business Intelligence project.
Runs data loading, cleaning, database creation, SQL analysis, chart rendering, and report compilation.
"""

import os
import sys
import time

# Ensure src directory is in Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from helper import logger, print_separator
from data_loader import clean_data
from database_setup import setup_database
from sql_queries import SQL_QUERIES
from analysis import run_analysis
from visualizations import generate_visualizations
from screenshot_generator import generate_screenshots
from report_generator import create_pdf_report

def main():
    """
    Orchestrates the entire E-Commerce SQL analytics pipeline.
    """
    start_time = time.time()
    
    print_separator("E-COMMERCE DATA ANALYTICS & BI PIPELINE START")
    logger.info("Initializing analytics workflow...")

    try:
        # Step 1: Data Loader & Cleansing
        print_separator("STEP 1: DATA CLEANING & PREPARATION")
        clean_data()
        
        # Step 2: Database Setup
        print_separator("STEP 2: DATABASE INITIALIZATION & INGESTION")
        setup_database()
        
        # Step 3: SQL Queries Analysis Execution
        print_separator("STEP 3: RUNNING SQL ANALYSIS (46 QUERIES)")
        report_path = run_analysis()
        logger.info(f"Analysis complete. Insights report saved to: {report_path}")
        
        # Step 4: Visualizations Rendering
        print_separator("STEP 4: GENERATING BUSINESS CHARTS")
        generate_visualizations()
        
        # Step 5: Screenshot Capturing
        print_separator("STEP 5: CAPTURING PORTFOLIO SCREENSHOTS")
        generate_screenshots()
        
        # Step 6: Compilation of Executive PDF Report
        print_separator("STEP 6: COMPILING EXECUTIVE PDF REPORT")
        create_pdf_report()

        duration = time.time() - start_time
        print_separator("PIPELINE EXECUTION COMPLETED")
        logger.info(f"All project deliverables generated successfully in {duration:.2f} seconds!")
        logger.info("Deliverables Inventory:")
        logger.info("- Processed CSV: data/processed/cleaned_dataset.csv")
        logger.info("- SQLite DB: ecommerce.db")
        logger.info("- Markdown Insights Report: query_insights_report.md")
        logger.info("- 10 Visualizations: images/")
        logger.info("- 4 Mock Screenshots: screenshots/")
        logger.info("- PDF Project Report: Project_Report.pdf")
        print_separator()

    except Exception as e:
        logger.critical(f"Pipeline execution failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
