# Comprehensive E-Commerce Analytics Audit & Exploratory Analysis Report

**Prepared For**: DecodeLabs Management & Stakeholders  
**Prepared By**: Senior Data Analyst (Data Analytics & Business Intelligence)  
**Date**: July 12, 2026  
**Project**: E-Commerce Transactional Quality Audit & Exploratory Data Analysis (Project 2)

---

## Table of Contents

1. [Phase 1: Executive Summary](#phase-1-executive-summary)
2. [Phase 2: Data Quality Audit & Anomalies](#phase-2-data-quality-audit--anomalies)
3. [Phase 3: Data Cleaning & Ingestion Pipeline](#phase-3-data-cleaning--ingestion-pipeline)
4. [Phase 4: Descriptive Statistics](#phase-4-descriptive-statistics)
5. [Phase 5: Univariate Analysis Gallery](#phase-5-univariate-analysis-gallery)
6. [Phase 6: Bivariate Analysis Gallery](#phase-6-bivariate-analysis-gallery)
7. [Phase 7: Multivariate Analysis Gallery](#phase-7-multivariate-analysis-gallery)
8. [Phase 8: Outlier Profiling](#phase-8-outlier-profiling)
9. [Phase 9: Feature Engineering Schema](#phase-9-feature-engineering-schema)
10. [Phase 10: 25 Strategic Business Questions & Answers](#phase-10-25-strategic-business-questions--answers)
11. [Phase 11: Strategic Advice & Business Recommendations](#phase-11-strategic-advice--business-recommendations)
12. [Phase 12: Future Scope & Analytical Dashboard Plan](#phase-12-future-scope--analytical-dashboard-plan)
13. [Phase 13: Conclusion](#phase-13-conclusion)

---

## Phase 1: Executive Summary

A comprehensive data-driven evaluation of 1,200 transaction records spanning Jan 2023 to Jun 2025 was conducted to audit accounting irregularities, resolve supply chain synchronization concerns, and outline growth strategies.

The project successfully re-baselined the store's performance by applying discount percentages to correct invoice calculations (saving 6.2% of revenue from accounting over-statement) and aligning shipping records.

* **Total Cleaned Revenue**: Rs. 1,188,905.42 (after correcting a Rs. 78,574.62 over-reporting anomaly)
* **Average Order Value (AOV)**: Rs. 990.75
* **Repeat Purchase Rate**: 0.93% (1,189 unique buyers) — indicating a critical customer retention issue.
* **Operational Leakage**: 41.41% total order failure rate (20.8% cancelled, 20.6% returned).

---

## Phase 2: Data Quality Audit & Anomalies

During initial data profiling, two critical systemic defects were identified and cataloged:

1. **The Coupon Discount Bug (Financial)**: The store recorded transaction totals as `Quantity * UnitPrice` directly, failing to subtract discounts for active campaigns (`SAVE10` = 10% off, `WINTER15` = 15% off). This led to an artificial over-reporting of sales.
2. **Logistics Integrity Defect (Supply Chain)**: Every transaction record contained a shipping tracking number, even those that had a status of `Pending` or `Cancelled`. In real-world shipping workflows, tracking numbers are only issued when an item is packed and ready to ship.
3. **Product SKU Pricing Discrepancy (Catalog)**: High-value tech products (Laptops, Tablets, Phones) display identical unit price distributions (ranging uniformly from Rs. 11 to Rs. 700) to cheap furniture (Chairs, Desks), highlighting a synthetic data generation pattern.

---

## Phase 3: Data Cleaning & Ingestion Pipeline

An automated Python ETL pipeline was implemented in `src/clean_data.py` to sanitize the transactions:

* **Coupon Alignment**: Mapped `SAVE10` to 10% discount, `WINTER15` to 15% discount, `FREESHIP` to 0% discount, and default NaNs to 0% discount.
* **Accounting Recalculation**: Corrected the transaction total price field using:
  $$\text{TotalPrice}_{\text{corrected}} = \text{Quantity} \times \text{UnitPrice} \times \left(1.0 - \frac{\text{DiscountPercent}}{100.0}\right)$$
  Values were rounded to 2 decimal places.
* **Supply Chain Sanitization**: Forced `TrackingNumber` to null (`NaN`) for all `Pending` and `Cancelled` orders, while keeping the tracking values intact for active phases (`Shipped`, `Delivered`, `Returned`).
* **Feature Engineering**: Extracted date parameters (Year, Month, Quarter, DayName, IsWeekend) and generated customer/cart classifications.

---

## Phase 4: Descriptive Statistics

A statistical summary of the four numerical fields shows key distributions:

| Field | Count | Mean | Std Dev | Variance | Min | Median (50%) | Max | Range | IQR | Skewness | Kurtosis |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Quantity** | 1,200 | 2.95 | 1.41 | 1.98 | 1.00 | 3.00 | 5.00 | 4.00 | 2.00 | 0.0279 | -1.2946 |
| **UnitPrice** | 1,200 | Rs. 356.41 | Rs. 197.18 | 38,878.83 | Rs. 11.39 | Rs. 364.21 | Rs. 699.93 | Rs. 688.54 | Rs. 335.51 | -0.0265 | -1.1910 |
| **ItemsInCart** | 1,200 | 5.49 | 2.28 | 5.21 | 1.00 | 5.00 | 10.00 | 9.00 | 3.00 | 0.0009 | -0.7086 |
| **TotalPrice** | 1,200 | Rs. 990.75 | Rs. 774.94 | 600,527.37 | Rs. 9.68 | Rs. 766.11 | Rs. 3,390.95 | Rs. 3,381.27 | Rs. 1,093.61 | 0.9108 | 0.0211 |

* **Interpretation**: `Quantity`, `UnitPrice`, and `ItemsInCart` follow uniform distributions (skewness close to 0, kurtosis negative). `TotalPrice` shows moderate right-skewness (0.91) due to the multiplication of quantity, unit price, and discounts.

---

## Phase 5: Univariate Analysis Gallery

The univariate analysis evaluates single variables to identify baseline patterns:

* **TotalPrice (`01_univariate_totalprice.png`)**: Right-skewed, peaking near Rs. 400-800 with a long tail stretching to Rs. 3,390.
* **Quantity (`02_univariate_quantity.png`)**: Fairly uniform count across values 1 through 5, with each quantity accounting for ~20% of orders.
* **ItemsInCart (`03_univariate_itemsincart.png`)**: Concentrated between 4 and 7 items, representing mid-sized shopping baskets.
* **Product SKU count (`05_univariate_products.png`)**: The transaction count is distributed evenly among the 7 products (between 156 and 181 orders each), indicating consistent transaction density.
* **Fulfillment States (`06_univariate_status.png`)**: High operational risk: Cancelled (20.8%) and Returned (20.6%) represent 41.4% of total order events.

---

## Phase 6: Bivariate Analysis Gallery

Evaluates the relationships between two variables:

* **Product SKU vs. Revenue (`12_bivariate_product_revenue.png`)**: Chairs generated the highest total revenue (Rs. 185.3K), followed closely by Printers (Rs. 183.5K) and Laptops (Rs. 181.1K).
* **Fulfillment Month vs. Revenue Trend (`13_bivariate_monthly_revenue.png`)**: Highlight sales surges in mid-summer (June 2024 peak at Rs. 64.8K) and winter, indicating clear seasonal purchase patterns.
* **Marketing Referral vs. Revenue (`10_bivariate_referral_revenue.png`)**: Instagram leads with Rs. 237.4K in revenue, followed closely by Email (Rs. 222.0K).
* **Payment Method vs. Revenue (`09_bivariate_payment_revenue.png`)**: Online/UPI transfers and Credit Cards dominate, generating Rs. 247.7K and Rs. 246.2K respectively.

---

## Phase 7: Multivariate Analysis Gallery

* **Correlation Heatmap (`14_multivariate_correlation.png`)**:
  * Strongest positive correlation is between `Quantity` and `TotalPrice` ($r = 0.655$) and `UnitPrice` and `TotalPrice` ($r = 0.650$).
  * The correlation between `ItemsInCart` (items in basket) and `TotalPrice` (checkout spend) is moderate ($r = 0.390$).
  * `DiscountPercent` has a minor negative correlation with `TotalPrice` ($r = -0.101$) as expected since discounts lower checkout cost.

---

## Phase 8: Outlier Profiling

* **Outlier Boxplots (`15_outlier_totalprice.png`, `16_outlier_quantity.png`)**:
  * `Quantity` shows zero outliers since it is bounded between 1 and 5 items.
  * `TotalPrice` contains a few statistical outliers above Rs. 3,100. These outliers represent high-value bulk purchases (e.g. 5 units of high-unit-price products without discount codes) and represent legitimate premium orders rather than data entry errors.

---

## Phase 9: Feature Engineering Schema

To support deep business logic, we engineered the following features:

1. **Temporal Dimensions**: `OrderYear`, `OrderMonth`, `OrderQuarter`, `DayName`, and `IsWeekend` (indicating Saturday/Sunday purchases).
2. **Discount Flags**: `DiscountPercent` (numerical mapped value) and `DiscountApplied` (binary flag).
3. **Cart Classifications**:
   * `OrderValueCategory`: Low (< Rs. 250), Medium (Rs. 250 - Rs. 1000), High (> Rs. 1000).
   * `BasketSizeCategory`: Small (1-3 items), Medium (4-7 items), Large (8+ items).
   * `HighValueOrder`: Binary flag indicating orders with totals exceeding Rs. 1,000.

---

## Phase 10: 25 Strategic Business Questions & Answers

### 1. What is the total adjusted revenue generated by the e-commerce store?

* **Answer**: Rs. 1,188,905.42 (Adjusted baseline down from Rs. 1,267,480.04).

### 2. What is the total number of orders placed?

* **Answer**: 1,200 orders.

### 3. How many unique customers made purchases, and what is the repeat customer rate?

* **Answer**: 1,189 unique customers; 11 customers purchased twice. The repeat customer rate is **0.93%**.

### 4. What is the overall average order value (AOV)?

* **Answer**: Rs. 990.75 per transaction.

### 5. Which product sold the highest quantity?

* **Answer**: Chair (562 units).

### 6. Which product generated the highest total revenue?

* **Answer**: Chair (Rs. 185,379.09).

### 7. What is the distribution of orders by order status?

* **Answer**: Cancelled (250), Returned (247), Pending (237), Shipped (235), Delivered (231).

### 8. What is the cancellation rate, and what is its revenue impact?

* **Answer**: Cancellation rate is **20.83%** (250 orders), representing Rs. 258,498.90 in lost revenue.

### 9. What is the return rate, and what is its revenue impact?

* **Answer**: Return rate is **20.58%** (247 orders), representing Rs. 229,713.47 in lost revenue.

### 10. Which payment method is the most popular, and how much revenue does it contribute?

* **Answer**: Online/UPI is most popular (258 orders, Rs. 247,790.03), closely followed by Cash (246 orders, Rs. 244,603.51) and Credit Cards (234 orders, Rs. 246,282.79).

### 11. Which marketing referral source generates the most orders?

* **Answer**: Instagram (259 orders), followed by Email (250), Google (241), Facebook (228), and organic referrals (222).

### 12. Which referral source brings in the highest Average Order Value (AOV)?

* **Answer**: Facebook (Rs. 1,037.08), followed by Instagram (Rs. 997.79).

### 13. What percentage of orders utilized a coupon code?

* **Answer**: **48.17%** of transactions (578 orders).

### 14. Which coupon code was used most frequently, and what was the total discount value given?

* **Answer**: `FREESHIP` was used most frequently (313 orders, Rs. 0.00 discount on product price), followed by `WINTER15` (292 orders, Rs. 45,372.53 discount) and `SAVE10` (286 orders, Rs. 30,484.00 discount).

### 15. Is there a difference in average basket size (items in cart) between orders with coupons and without?

* **Answer**: Orders with coupons average **5.42 items**; orders without coupons average **5.55 items**. The difference is negligible.

### 16. How does sales revenue trend over the years (2023, 2024, and 2025)?

* **Answer**: 2023 generated Rs. 519,819.36 (510 orders); 2024 generated Rs. 451,204.38 (459 orders); 2025 generated Rs. 217,881.68 (231 orders).

### 17. What are the top 3 peak sales months across the entire dataset?

* **Answer**: June 2024 (Rs. 64,890.98), May 2023 (Rs. 60,028.82), and January 2023 (Rs. 52,758.54).

### 18. What is the revenue split between weekends and weekdays?

* **Answer**: Weekdays generated Rs. 843,967.78 (71.0%); Weekends generated Rs. 344,937.64 (29.0%).

### 19. What is the distribution of order value categories (Low, Medium, High)?

* **Answer**: Medium (525 orders), High (484 orders), Low (191 orders).

### 20. Do customers who put more items in their cart also tend to spend more per order (correlation)?

* **Answer**: The correlation is **0.3898** (weak linear correlation). This is due to uniform product pricing where cart size does not dictate price.

### 21. What is the average quantity of items purchased per order?

* **Answer**: **2.95 units** per transaction line.

### 22. Are orders placed through specific payment methods more prone to cancellation?

* **Answer**: Credit Cards (54 cancellations) and Online/UPI (53 cancellations) have the highest volumes, but the distribution across methods is fairly even.

### 23. How many high-value orders (> Rs. 1,000) occurred, and what share of total revenue do they represent?

* **Answer**: 484 orders, representing Rs. 861,758.10 (**72.48%** of total revenue).

### 24. What is the revenue contribution of each product category?

* **Answer**: Chairs (Rs. 185.3K), Printers (Rs. 183.5K), Laptops (Rs. 181.1K), Tablets (Rs. 173.9K), Monitors (Rs. 163.4K), Desks (Rs. 157.8K), Phones (Rs. 143.6K).

### 25. Which marketing referral source has the highest return rate (potential quality/ad-mismatch issue)?

* **Answer**: **Facebook** exhibits the highest return rate at **24.56%**.

---

## Phase 11: Strategic Advice & Business Recommendations

* **Establish Pricing Safeguards**: Restructure product SKU values so high-end electronics are not sold at the same price as low-end furniture.
* **Deploy post-checkout confirmation gates**: Build SMS/WhatsApp verification blocks for orders before they are packaged to reduce the 41.4% failure rate.
* **Budget Reallocation**: Reallocate marketing budgets away from Facebook (highest return rate of 24.56%) and towards Instagram (highest order density and lowest return rate).
* **Coupon Adjustments**: Establish Minimum Order Values (MOV) on discount coupons (e.g. `SAVE10` only on orders > Rs. 1000) to increase average basket sizes.
* **Loyalty and CRM Integration**: Develop post-purchase drip campaigns targeting the 99% of customers who never place a second order.

---

## Phase 12: Future Scope & Analytical Dashboard Plan

In the next stage of business intelligence development, we recommend:

1. **Interactive Streamlit Dashboard**: Build a dashboard featuring sidebars to filter data by date range, category, and acquisition channel.
2. **Logistics Integration**: Link our processed table directly with DHL/FedEx API states to automate tracking number validations.
3. **Customer Retention LTV Modeling**: Implement predictive churn algorithms to identify customers likely to drop off.

---

## Phase 13: Conclusion

By resolving accounting errors and supply chain anomalies, this report provides a clean, verified transaction baseline for the e-commerce store. Focusing on operational efficiency, catalog pricing adjustments, and customer retention programs will help the business scale profitably.
