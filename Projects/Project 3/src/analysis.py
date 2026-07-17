"""
Analysis module for executing the 46 SQL queries, formatting outputs, and generating reports.
"""

import os
import sqlite3
import pandas as pd
from config import DB_PATH, PROJECT_DIR
from helper import logger, print_separator
from sql_queries import SQL_QUERIES

def to_markdown_table(columns, rows):
    """
    Converts database query column headers and rows to a standard Markdown table string.
    """
    if not rows:
        return "*No data returned.*"
    
    # Calculate column widths
    col_widths = [len(str(col)) for col in columns]
    for row in rows:
        for idx, val in enumerate(row):
            val_str = str(val) if val is not None else "NULL"
            col_widths[idx] = max(col_widths[idx], len(val_str))
            
    # Assemble header
    header_str = "| " + " | ".join(str(col).ljust(col_widths[idx]) for idx, col in enumerate(columns)) + " |"
    sep_str = "| " + " | ".join("-" * col_widths[idx] for idx in range(len(columns))) + " |"
    
    # Assemble rows
    row_strs = []
    for row in rows:
        row_str = "| " + " | ".join((str(val) if val is not None else "NULL").ljust(col_widths[idx]) for idx, val in enumerate(row)) + " |"
        row_strs.append(row_str)
        
    return "\n".join([header_str, sep_str] + row_strs)

def run_analysis():
    """
    Executes the 46 SQL queries against the SQLite database and generates a Markdown report.
    """
    logger.info("Starting SQL queries analysis execution...")

    if not os.path.exists(DB_PATH):
        logger.error(f"Database not found at: {DB_PATH}. Run database_setup.py first.")
        raise FileNotFoundError(f"Database not found at: {DB_PATH}")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    report_path = os.path.join(PROJECT_DIR, "query_insights_report.md")
    logger.info(f"Writing query insights to: {report_path}")

    # Start writing report
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# E-Commerce Business Intelligence - SQL Analysis Report\n\n")
        f.write("This report documents the execution of 46 professional SQL queries on the E-Commerce database.\n")
        f.write("Each section covers a key business theme, SQL syntax, output, business insights, and recommendations.\n\n")
        f.write("---\n\n")

        for key in sorted(SQL_QUERIES.keys()):
            query_info = SQL_QUERIES[key]
            name = query_info["name"]
            sql_query = query_info["sql"]
            prob_statement = query_info["problem_statement"]
            insight = query_info["business_insight"]
            recommendation = query_info["recommendation"]

            logger.info(f"Executing: {key} - {name}")

            # Run query
            try:
                # For query speed comparison or index drop test, handle accordingly
                if "CREATE INDEX" in sql_query or "DROP INDEX" in sql_query:
                    cursor.execute(sql_query)
                    columns = ["Status"]
                    rows = [("Command executed successfully",)]
                else:
                    cursor.execute(sql_query)
                    columns = [description[0] for description in cursor.description]
                    rows = cursor.fetchall()
                
                # Format to Markdown Table
                md_table = to_markdown_table(columns, rows)

                # Write query block to file
                f.write(f"## {key.upper().replace('_', ' ')}: {name}\n\n")
                f.write(f"**Problem Statement:**\n{prob_statement}\n\n")
                f.write(f"**SQL Query:**\n```sql\n{sql_query}\n```\n\n")
                f.write(f"**Query Output:**\n\n{md_table}\n\n")
                f.write(f"**Business Insight:**\n{insight}\n\n")
                f.write(f"**Real-world Recommendation:**\n{recommendation}\n\n")
                f.write("---\n\n")

            except sqlite3.Error as e:
                logger.error(f"Error executing {key} ({name}): {e}")
                f.write(f"## {key.upper()}: {name}\n\n")
                f.write(f"**SQL Query:**\n```sql\n{sql_query}\n```\n\n")
                f.write(f"**Execution Error:**\n`{e}`\n\n")
                f.write("---\n\n")

    conn.close()
    logger.info("SQL queries analysis and report generation completed successfully!")
    return report_path

if __name__ == "__main__":
    run_analysis()
