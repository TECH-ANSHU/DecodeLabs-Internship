"""
Helper utilities for logging setup, directory creation, and CLI/output formatting.
"""

import logging
import os
import sys

def setup_logging():
    """
    Configures logging to write to both console and a log file.
    """
    log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "project.log")

    logger = logging.getLogger("ecommerce_analytics")
    logger.setLevel(logging.INFO)

    # Clean existing handlers
    if logger.handlers:
        logger.handlers.clear()

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # File Handler
    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Console Handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

logger = setup_logging()

def print_separator(title=None):
    """
    Prints a separator line with an optional title.
    """
    width = 80
    if title:
        padding = (width - len(title) - 2) // 2
        print("=" * padding + f" {title} " + "=" * padding)
    else:
        print("=" * width)

def format_currency(value):
    """
    Formats a numeric value as a currency string.
    """
    if value is None:
        return "$0.00"
    return f"${value:,.2f}"
