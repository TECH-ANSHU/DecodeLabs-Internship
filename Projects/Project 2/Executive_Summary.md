# Executive Summary — Project 2: E-Commerce Data Audit & EDA

**To:** Executive Leadership Team  
**From:** Senior Data Analyst  
**Date:** July 12, 2026  
**Subject:** E-Commerce Transaction Audit & Strategic Growth Roadmap  

---

## 1. Business Context & Objective

Following a comprehensive data quality audit of 1,200 transactional records spanning January 2023 to June 2025, this report presents the verified financial baseline and exploratory insights for the e-commerce store. The audit resolved two critical systemic defects:

1. **Invoice Pricing Defect**: Corrected the gross total price calculation to deduct coupon campaigns (`SAVE10`, `WINTER15`), preventing significant fiscal over-reporting.
2. **Logistics Integrity Defect**: Nullified tracking numbers pre-allocated to `Pending` and `Cancelled` orders to align the system with actual supply chain states.

---

## 2. Verified E-Commerce Performance Dashboard (Jan 2023 - Jun 2025)

| Metric | Value / Share | Business Interpretation |
| :--- | :--- | :--- |
| **Total Audited Revenue** | **Rs. 1,188,905.42** | Adjusted baseline for tax, dividend, and inventory planning. |
| **Gross Fiscal Over-statement** | **Rs. 78,574.62 (6.2%)** | Re-captured revenue margin previously leakage due to unapplied discounts. |
| **Total Order Count** | **1,200** | Transaction throughput across the 30-month lifecycle. |
| **Average Order Value (AOV)** | **Rs. 990.75** | Baseline transaction size; 72% of store revenue comes from orders > Rs. 1,000. |
| **Customer Retention Rate** | **0.93% (1,189 unique buyers)** | Critical risk: Store operates almost entirely on one-off acquisitions. |
| **Operational Failure Rate** | **41.41% (497 orders)** | Cancelled orders (20.8%) and returned orders (20.6%) drain margins. |

---

## 3. Core Strategic Insights

### 🚨 The Operational Leakage Crisis (Cancellations & Returns)

* **Finding**: Over 41% of placed orders fail to result in final sales, split equally between Cancellations (20.8%) and Returns (20.6%). This leads to Rs. 488,212.37 in lost gross revenue and significant return-logistics processing costs.
* **Friction Source**: Facebook acquisition channels display the highest return rate (**24.56%**) and cancellation rate, representing poor audience matching.
* **Action**: Audit checkout friction, introduce SMS-based confirmation triggers for high-value orders, and redirect Facebook budget to Instagram and Email channels.

### 📈 Marketing & Acquisition Channel ROI

* **Finding**: Instagram is the store's primary engine, bringing in **259 orders** and **Rs. 237k** in revenue, followed closely by Email (**250 orders, Rs. 222k**). Together they generate **41.4%** of total revenue.
* **AOV Leader**: Facebook orders, though fewer and more prone to return, have the highest AOV (**Rs. 1,037.08**), while organic referrals have the lowest AOV (**Rs. 959.16**).
* **Action**: Launch targeted up-sell flows in Instagram ads and implement personalized email newsletters to maintain this low-acquisition-cost funnel.

### 🏷️ Coupon Campaign Efficacy

* **Finding**: **48.17% of all orders** apply a coupon. The `WINTER15` coupon gave out **Rs. 45,372.53** in discount volume, whereas `SAVE10` gave out **Rs. 30,484.00**.
* **Cart Volume Check**: Average items in cart are nearly identical for coupon-users (5.42 items) and non-coupon-users (5.55 items), proving that coupons do *not* incentivize larger basket sizes.
* **Action**: Lower the high-tier discount `WINTER15` (15%) to `WINTER12` (12%) to preserve margin, and restrict `SAVE10` to minimum orders of Rs. 800 to encourage larger baskets.

### 📦 Catalog Pricing Anomaly

* **Finding**: High-value tech items (Laptops, Phones, Tablets) display identical unit price distributions (ranging uniformly from Rs. 11 to Rs. 700) to low-value office furniture (Chairs, Desks).
* **Action**: Establish a tiered product catalog pricing structure immediately. Selling Laptops for Rs. 50 causes brand distrust and severe revenue loss.

---

## 4. Priority Roadmap

1. **Fiscal Alignment**: Update the ERP database to match the audited `cleaned_dataset.csv` values to avoid over-paying sales tax.
2. **Launch Loyalty Program**: Introduce a post-purchase rewards structure to drive repeat customers from the current 0.93% base.
3. **Logistical Guardrails**: Implement the tracking number check in the checkout database (preventing tracking number allocation before `OrderStatus` updates to `Shipped`).
