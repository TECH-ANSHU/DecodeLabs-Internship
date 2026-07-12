# Strategic Business Recommendations — Project 2

This document translates the data insights from the e-commerce transaction audit into prioritized, concrete business actions. These strategies aim to reduce operational overhead, optimize catalog margins, reallocate marketing budgets to high-performing channels, and increase customer lifetime value.

---

## 🏛️ Priority 1: Restructuring Catalog Pricing & SKU Governance

### Priority 1 Insight

Laptops, Tablets, and Phones have the same average unit price (Rs. 350 - 375) and price ranges (Rs. 11 to Rs. 700) as Chairs and Desks. In real-world retail, selling a laptop for Rs. 50 causes severe margin loss and ruins brand positioning, while selling a plastic desk-organizer for Rs. 600 causes customer churn.

### Priority 1 Actions

1. **Tiered Pricing Architecture**: Migrate from the current flat distribution to a standardized, category-specific pricing matrix:
   * **Electronics (Laptops, Phones, Tablets)**: Rs. 15,000 – Rs. 80,000+
   * **Peripherals (Monitors, Printers)**: Rs. 8,000 – Rs. 25,000
   * **Office Furniture (Desks, Chairs)**: Rs. 2,000 – Rs. 12,000
2. **ERP Product SKU Sync**: Link the checkout catalog database to an inventory master database to ensure unit prices are locked based on SKU IDs, blocking manual overrides or system-level pricing roll-up errors.

---

## 🚨 Priority 2: Mitigating the 41.4% Operational Failure Rate

### Priority 2 Insight

41.41% of placed orders fail (20.83% Cancelled, 20.58% Returned). This causes Rs. 488,212.37 in lost revenue and drains shipping, packaging, and handling margins. Returning items double-charge shipping fees.

### Priority 2 Actions

1. **Post-Order Verification Loop**: Implement a 30-minute cooling-off phase after checkout. Send an automated SMS/WhatsApp verification asking the buyer to confirm their shipping address and order items before the order status transitions to "Shipped."
2. **Carrier Performance Audit**: Audit the logistics partners. High returns and cancellations are often caused by:
   * Long transit times (buyers purchase elsewhere and cancel/refuse delivery).
   * Bad handling causing damaged goods (returned upon arrival).
3. **Logistics System Constraints**: Ensure the ERP code mirrors the validation rule: `TrackingNumber` remains null until the status is explicitly updated to "Shipped." This prevents false delivery alerts that trigger pre-mature cancellations.

---

## 📣 Priority 3: Marketing Budget Reallocation & Channel Optimization

### Priority 3 Insight

Instagram leads in order volume (259 orders) and gross sales (Rs. 237k). Email is a high-efficiency close second (250 orders, Rs. 222k). Facebook brings in the highest Average Order Value (Rs. 1,037.08) but suffers from the highest return rate (24.56%).

### Priority 3 Actions

1. **Redirect Facebook Spend**: Divert 20% of the Facebook ad budget. Reallocate 10% to Instagram micro-influencers and 10% to Email segmentation software.
2. **Optimize Facebook Ad Copy**: High AOV coupled with a high return rate suggests Facebook ads are attracting high-intent buyers, but the actual product delivered may not match the marketing promise. Audit Facebook ad copy and media assets to ensure they accurately represent the product size, color, and specifications.
3. **Automate High-AOV Referral Triggers**: Since Facebook buyers spend more per order, create lookalike audiences based specifically on customers who spend > Rs. 1,500.

---

## 🏷️ Priority 4: Coupon Strategy Realignment

### Priority 4 Insight

Nearly half of all sales (48.17%) are driven by coupons. However, coupon use does *not* increase average basket size (items in cart is ~5.4 for coupon-users vs. ~5.5 for non-users). The `WINTER15` coupon gave away Rs. 45,372.53 in margin, and `SAVE10` gave away Rs. 30,484.00.

### Priority 4 Actions

1. **Establish Minimum Order Value (MOV) Triggers**: Stop offering unrestricted flat-percent coupons. Re-engineer the codes:
   * `SAVE10` $\to$ Applicable only for orders > Rs. 1,000.
   * `WINTER15` $\to$ Rebrand to `WINTER12` (12% off) and apply only for orders > Rs. 1,500.
2. **Leverage FREESHIP for Basket Expansion**: Introduce a dynamic free-shipping progress bar at checkout (e.g., *"Add Rs. 150 more to get FREE Shipping"*). This utilizes the zero-margin-leakage `FREESHIP` coupon to drive upsells.

---

## 🔄 Priority 5: Launching Customer Retention Loops

### Priority 5 Insight

The repeat purchase rate is a dismal **0.93%** (1,189 unique buyers across 1,200 orders). The store operates entirely as a "leaky bucket," spending marketing acquisition dollars but never retaining customers.

### Priority 5 Actions

1. **Introduce a Post-Purchase Loyalty Cycle**: Send an automated email 7 days post-delivery offering an exclusive "Welcome Back" discount code (e.g. 10% off their next purchase within 30 days).
2. **Trigger-Based Cross-Selling**: Customers who buy a Laptop should receive automated recommendations for Monitors, Chairs, or Printers within 14 days of delivery.

---

## 📅 Execution Roadmap & KPI Tracker

| Initiative | Action Item | Department Owner | Priority | Target KPI | Timeline |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Catalog Audit** | Implement category-tiered pricing structure | Product / Finance | High | Increase gross margins by 15% | Q1 (Weeks 1-4) |
| **Logistics Check** | Nullify tracking numbers for Pending/Cancelled orders | Engineering / IT | High | 100% database schema compliance | Q1 (Weeks 1-2) |
| **Address Audit** | Post-checkout address validation SMS trigger | Customer Experience | Medium | Reduce delivery returns by 30% | Q1 (Weeks 5-8) |
| **Channel Shift** | Reallocate 20% Facebook spend to Instagram/Email | Marketing | Medium | Decrease return rate below 15% | Q2 (Weeks 1-4) |
| **Retention Loop** | Launch automated post-purchase loyalty emails | Marketing / CRM | High | Increase repeat rate from 0.9% to 5.0% | Q2 (Weeks 5-8) |
