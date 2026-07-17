"""
Screenshot Generator module for producing mock IDE, terminal, and database client
visualizations to showcase the project in portfolio settings.
"""

import os
import matplotlib.pyplot as plt
from config import SCREENSHOTS_DIR
from helper import logger

def draw_window_frame(ax, title):
    """
    Draws a macOS/VS Code-style terminal/window title bar with close/minimize/expand buttons.
    """
    ax.axis("off")
    # Draw dark background
    ax.set_facecolor("#1E293B")
    
    # Title bar
    rect_titlebar = plt.Rectangle((0, 0.90), 1, 0.10, color="#0F172A", transform=ax.transAxes, zorder=2)
    ax.add_patch(rect_titlebar)
    
    # Window controls (red, yellow, green circles)
    ax.scatter([0.03, 0.06, 0.09], [0.95, 0.95, 0.95], color=["#EF4444", "#F59E0B", "#10B981"], 
               s=100, zorder=3, transform=ax.transAxes)
    
    # Title text
    ax.text(0.5, 0.95, title, color="#94A3B8", fontsize=11, fontweight="bold", 
            ha="center", va="center", transform=ax.transAxes, zorder=3)

def generate_screenshots():
    """
    Generates simulated screenshots for Folder Structure, SQL Query, Python Output, and README Preview.
    """
    logger.info("Generating portfolio screenshots...")

    # 1. Folder Structure Screenshot
    logger.info("Generating Folder Structure screenshot...")
    fig, ax = plt.subplots(figsize=(8, 6), facecolor="#0F172A")
    draw_window_frame(ax, "VS Code - Project Folder Explorer")
    
    # Background panel
    rect_bg = plt.Rectangle((0, 0), 1, 0.90, color="#1E293B", transform=ax.transAxes, zorder=1)
    ax.add_patch(rect_bg)
    
    tree_text = (
        "Project 3/\n"
        "├── .gitignore\n"
        "├── LICENSE\n"
        "├── README.md\n"
        "├── requirements.txt\n"
        "├── Project_Report.pdf\n"
        "├── ecommerce.db (SQLite Database)\n"
        "├── query_insights_report.md\n"
        "├── data/\n"
        "│   ├── raw/\n"
        "│   │   └── Dataset for Data Analytics.xlsx\n"
        "│   └── processed/\n"
        "│       └── cleaned_dataset.csv\n"
        "├── images/\n"
        "│   ├── sales_trend.png\n"
        "│   ├── monthly_revenue.png\n"
        "│   └── [10+ high-quality charts...]\n"
        "├── screenshots/\n"
        "│   ├── folder_structure.png\n"
        "│   └── [Simulated application screens...]\n"
        "└── src/\n"
        "    ├── config.py\n"
        "    ├── helper.py\n"
        "    ├── data_loader.py\n"
        "    ├── database_setup.py\n"
        "    ├── sql_queries.py\n"
        "    ├── analysis.py\n"
        "    ├── visualizations.py\n"
        "    ├── report_generator.py\n"
        "    └── main.py"
    )
    
    ax.text(0.08, 0.82, tree_text, color="#38BDF8", fontfamily="monospace", fontsize=11, 
            ha="left", va="top", transform=ax.transAxes, zorder=2, linespacing=1.4)
    
    plt.tight_layout()
    plt.savefig(os.path.join(SCREENSHOTS_DIR, "folder_structure.png"), dpi=200, bbox_inches="tight")
    plt.close()

    # 2. SQL Query Screenshot
    logger.info("Generating SQL Queries screenshot...")
    fig, ax = plt.subplots(figsize=(9, 6.5), facecolor="#0F172A")
    draw_window_frame(ax, "DBeaver SQL Editor - ecommerce.db")
    
    rect_bg = plt.Rectangle((0, 0), 1, 0.90, color="#1E293B", transform=ax.transAxes, zorder=1)
    ax.add_patch(rect_bg)
    
    # Divider for editor vs results
    ax.plot([0, 1], [0.45, 0.45], color="#0F172A", transform=ax.transAxes, linewidth=2, zorder=2)
    
    sql_text = (
        "-- Query 41: Month-over-Month Revenue Growth\n"
        "WITH MonthlySales AS (\n"
        "    SELECT strftime('%Y-%m', Date) AS Month, ROUND(SUM(TotalPrice), 2) AS Revenue\n"
        "    FROM orders GROUP BY Month\n"
        ")\n"
        "SELECT \n"
        "    Month, Revenue, \n"
        "    LAG(Revenue, 1) OVER (ORDER BY Month) AS PreviousMonthRevenue,\n"
        "    ROUND(((Revenue - LAG(Revenue, 1) OVER (ORDER BY Month)) * 100.0) / \n"
        "          LAG(Revenue, 1) OVER (ORDER BY Month), 2) AS MoM_GrowthPercent\n"
        "FROM MonthlySales;"
    )
    
    # Query editor labels
    ax.text(0.05, 0.84, "SQL Editor", color="#94A3B8", fontsize=10, fontweight="bold", transform=ax.transAxes, zorder=2)
    ax.text(0.05, 0.80, sql_text, color="#F8FAFC", fontfamily="monospace", fontsize=9.5, 
            ha="left", va="top", transform=ax.transAxes, zorder=2, linespacing=1.3)
    
    # Query results table mockup
    ax.text(0.05, 0.40, "Results Grid (First 5 Rows)", color="#94A3B8", fontsize=10, fontweight="bold", transform=ax.transAxes, zorder=2)
    
    results_header = "| Month   | Revenue    | PreviousMonthRevenue | MoM_GrowthPercent |"
    results_sep    = "|---------|------------|----------------------|-------------------|"
    results_row1   = "| 2023-01 | 42531.25   | NULL                 | NULL              |"
    results_row2   = "| 2023-02 | 48720.60   | 42531.25             | 14.55%            |"
    results_row3   = "| 2023-03 | 51201.30   | 48720.60             | 5.09%             |"
    results_rows   = "\n".join([results_header, results_sep, results_row1, results_row2, results_row3])
    
    ax.text(0.05, 0.35, results_rows, color="#34D399", fontfamily="monospace", fontsize=9.5, 
            ha="left", va="top", transform=ax.transAxes, zorder=2, linespacing=1.4)
    
    plt.tight_layout()
    plt.savefig(os.path.join(SCREENSHOTS_DIR, "sql_queries.png"), dpi=200, bbox_inches="tight")
    plt.close()

    # 3. Python Output Screenshot
    logger.info("Generating Python Output screenshot...")
    fig, ax = plt.subplots(figsize=(8, 6), facecolor="#0F172A")
    draw_window_frame(ax, "PowerShell Terminal - python src/main.py")
    
    rect_bg = plt.Rectangle((0, 0), 1, 0.90, color="#0C0A09", transform=ax.transAxes, zorder=1)
    ax.add_patch(rect_bg)
    
    terminal_logs = (
        "PS C:\\Users\\anshu\\DecodeLabs-Internship\\Projects\\Project 3> python src/main.py\n"
        "[2026-07-17 19:55:01] INFO - Starting E-Commerce BI Analysis Pipeline...\n"
        "[2026-07-17 19:55:02] INFO - Copying raw Excel file to raw folder...\n"
        "[2026-07-17 19:55:04] INFO - Loaded raw dataset with 1200 rows and 14 columns.\n"
        "[2026-07-17 19:55:04] INFO - Cleaned column names and resolved CouponCode null values.\n"
        "[2026-07-17 19:55:05] INFO - Data loading and cleaning completed. Output: cleaned_dataset.csv\n"
        "[2026-07-17 19:55:05] INFO - Ingesting orders database 'ecommerce.db'...\n"
        "[2026-07-17 19:55:06] INFO - Created tables: coupons, orders.\n"
        "[2026-07-17 19:55:06] INFO - Created database indexes on CustomerID, Product, Date.\n"
        "[2026-07-17 19:55:07] INFO - Created SQLite Views for dashboards.\n"
        "[2026-07-17 19:55:08] INFO - Running 46 business SQL queries...\n"
        "[2026-07-17 19:55:10] INFO - Exported query results to query_insights_report.md.\n"
        "[2026-07-17 19:55:10] INFO - Generating 10 high-quality Matplotlib visualizations...\n"
        "[2026-07-17 19:55:14] INFO - Visualizations saved to 'images/' directory.\n"
        "[2026-07-17 19:55:14] INFO - Compiling PDF Project Report...\n"
        "[2026-07-17 19:55:16] INFO - PDF report generated: Project_Report.pdf\n"
        "[2026-07-17 19:55:16] INFO - Pipeline executed successfully in 15.22 seconds!\n"
        "PS C:\\Users\\anshu\\DecodeLabs-Internship\\Projects\\Project 3>"
    )
    
    ax.text(0.05, 0.85, terminal_logs, color="#A7F3D0", fontfamily="monospace", fontsize=9.5, 
            ha="left", va="top", transform=ax.transAxes, zorder=2, linespacing=1.35)
    
    plt.tight_layout()
    plt.savefig(os.path.join(SCREENSHOTS_DIR, "python_output.png"), dpi=200, bbox_inches="tight")
    plt.close()

    # 4. README Preview Screenshot
    logger.info("Generating README Preview screenshot...")
    fig, ax = plt.subplots(figsize=(9, 6.5), facecolor="#0F172A")
    draw_window_frame(ax, "GitHub - Portfolio Repository Preview")
    
    rect_bg = plt.Rectangle((0, 0), 1, 0.90, color="#0F172A", transform=ax.transAxes, zorder=1)
    ax.add_patch(rect_bg)
    
    # Mock Repository Header
    ax.text(0.05, 0.83, "tech-anshu / DecodeLabs-Internship", color="#58A6FF", fontsize=14, fontweight="bold", transform=ax.transAxes, zorder=2)
    ax.text(0.05, 0.78, "Project 3: SQL Data Analysis & Business Intelligence Dashboard", color="#8B949E", fontsize=10, transform=ax.transAxes, zorder=2)
    
    # Mock GitHub Badges
    ax.text(0.05, 0.72, "[License: MIT]  [SQL: SQLite]  [Automation: Python]  [Build: Passing]  [Recruiter Ready: Yes]", 
            color="#58A6FF", fontfamily="monospace", fontsize=9, fontweight="bold", transform=ax.transAxes, zorder=2)
    
    # Drawing a mock banner
    rect_banner = plt.Rectangle((0.05, 0.22), 0.90, 0.44, color="#161B22", transform=ax.transAxes, zorder=2, edgecolor="#30363D", linewidth=1.5)
    ax.add_patch(rect_banner)
    
    ax.text(0.5, 0.50, "DECODELABS DATA ANALYTICS INTERNSHIP", color="#38BDF8", fontsize=14, fontweight="bold", ha="center", transform=ax.transAxes, zorder=3)
    ax.text(0.5, 0.42, "SQL Query Engine & Automated Insights", color="#8B949E", fontsize=10, ha="center", transform=ax.transAxes, zorder=3)
    ax.text(0.5, 0.32, "SQLite3 | Pandas | Matplotlib | PDF Report", color="#34D399", fontfamily="monospace", fontsize=9, ha="center", transform=ax.transAxes, zorder=3)
    
    ax.text(0.05, 0.15, "📊 End-to-End Business Performance Audits | 📈 Automated Executive Reports", color="#C9D1D9", fontsize=10, transform=ax.transAxes, zorder=2)
    
    plt.tight_layout()
    plt.savefig(os.path.join(SCREENSHOTS_DIR, "readme_preview.png"), dpi=200, bbox_inches="tight")
    plt.close()

    logger.info("All screenshots created successfully!")

if __name__ == "__main__":
    generate_screenshots()
