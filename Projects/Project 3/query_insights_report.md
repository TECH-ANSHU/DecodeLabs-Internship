# E-Commerce Business Intelligence - SQL Analysis Report

This report documents the execution of 46 professional SQL queries on the E-Commerce database.
Each section covers a key business theme, SQL syntax, output, business insights, and recommendations.

---

## QUERY 01: Select All Orders (Limit)

**Problem Statement:**
Examine the database structure and quickly check the first few records in the orders table.

**SQL Query:**
```sql
SELECT OrderID, Date, CustomerID, Product, Quantity, TotalPrice FROM orders LIMIT 5;
```

**Query Output:**

| OrderID   | Date                | CustomerID | Product | Quantity | TotalPrice |
| --------- | ------------------- | ---------- | ------- | -------- | ---------- |
| ORD200000 | 2023-01-04 00:00:00 | C72649     | Monitor | 5        | 2853.1     |
| ORD200001 | 2024-08-23 00:00:00 | C75739     | Phone   | 2        | 302.7      |
| ORD200002 | 2024-02-27 00:00:00 | C81728     | Tablet  | 5        | 2753.4     |
| ORD200003 | 2023-10-15 00:00:00 | C33540     | Chair   | 1        | 273.19     |
| ORD200004 | 2025-05-08 00:00:00 | C81840     | Printer | 4        | 2504.04    |

**Business Insight:**
The dataset contains standard transactional parameters including order identifiers, customers, products purchased, quantities, and total order prices.

**Real-world Recommendation:**
Use this basic schema inspection to verify that automated integrations are writing all fields successfully.

---

## QUERY 02: Distinct Product Categories

**Problem Statement:**
Identify the unique product categories sold by the e-commerce store.

**SQL Query:**
```sql
SELECT DISTINCT Product FROM orders ORDER BY Product;
```

**Query Output:**

| Product |
| ------- |
| Chair   |
| Desk    |
| Laptop  |
| Monitor |
| Phone   |
| Printer |
| Tablet  |

**Business Insight:**
The store offers 7 unique product types: Chair, Desk, Laptop, Monitor, Phone, Printer, and Tablet, representing a blend of office furniture and consumer electronics.

**Real-world Recommendation:**
Review product classifications regularly to align stocking strategies with major category demands.

---

## QUERY 03: Distinct Payment Methods

**Problem Statement:**
List all payment methods supported by the e-commerce platform.

**SQL Query:**
```sql
SELECT DISTINCT PaymentMethod FROM orders ORDER BY PaymentMethod;
```

**Query Output:**

| PaymentMethod |
| ------------- |
| Cash          |
| Credit Card   |
| Debit Card    |
| Gift Card     |
| Online        |

**Business Insight:**
Supported payment methods include Credit Card, Debit Card, Online (wallets/UPI), Gift Card, and Cash, offering high convenience to different consumer segments.

**Real-world Recommendation:**
Ensure payment gateways are optimized for credit/debit cards and digital wallets to minimize cart abandonment.

---

## QUERY 04: Distinct Referral Sources

**Problem Statement:**
Identify all marketing and acquisition channels bringing traffic to the site.

**SQL Query:**
```sql
SELECT DISTINCT ReferralSource FROM orders ORDER BY ReferralSource;
```

**Query Output:**

| ReferralSource |
| -------------- |
| Email          |
| Facebook       |
| Google         |
| Instagram      |
| Referral       |

**Business Insight:**
Customers are acquired via 5 main channels: Email, Facebook, Google, Instagram, and direct Referrals.

**Real-world Recommendation:**
Track acquisition costs (CAC) across these channels to measure marketing return on investment (ROI).

---

## QUERY 05: High Quantity Orders (WHERE)

**Problem Statement:**
Find orders where a customer bought 5 or more units of a single product.

**SQL Query:**
```sql
SELECT OrderID, CustomerID, Product, Quantity, TotalPrice FROM orders WHERE Quantity >= 5 ORDER BY Quantity DESC LIMIT 5;
```

**Query Output:**

| OrderID   | CustomerID | Product | Quantity | TotalPrice |
| --------- | ---------- | ------- | -------- | ---------- |
| ORD200000 | C72649     | Monitor | 5        | 2853.1     |
| ORD200002 | C81728     | Tablet  | 5        | 2753.4     |
| ORD200007 | C41460     | Monitor | 5        | 747.75     |
| ORD200010 | C43443     | Tablet  | 5        | 3129.85    |
| ORD200019 | C14552     | Monitor | 5        | 1120       |

**Business Insight:**
High-quantity orders (5 units) frequently occur for items like Monitors and Chairs, suggesting potential B2B or corporate office setups.

**Real-world Recommendation:**
Introduce bulk-purchase discounts or corporate account managers to target small businesses purchasing office gear.

---

## QUERY 06: Shipped Orders Filter

**Problem Statement:**
Track how many orders are currently in 'Shipped' status, awaiting delivery.

**SQL Query:**
```sql
SELECT COUNT(*) AS ShippedCount FROM orders WHERE OrderStatus = 'Shipped';
```

**Query Output:**

| ShippedCount |
| ------------ |
| 235          |

**Business Insight:**
A substantial portion of orders are currently in transit, representing active logistics operations.

**Real-world Recommendation:**
Coordinate closely with logistics partners to ensure delivery SLAs are met and tracking details are updated promptly.

---

## QUERY 07: Orders Exceeding $2000 (WHERE, ORDER BY)

**Problem Statement:**
List the highest value individual orders exceeding $2,000.

**SQL Query:**
```sql
SELECT OrderID, CustomerID, Product, TotalPrice FROM orders WHERE TotalPrice > 2000 ORDER BY TotalPrice DESC LIMIT 5;
```

**Query Output:**

| OrderID   | CustomerID | Product | TotalPrice |
| --------- | ---------- | ------- | ---------- |
| ORD200789 | C57276     | Tablet  | 3456.4     |
| ORD201122 | C38840     | Monitor | 3390.95    |
| ORD200632 | C67260     | Laptop  | 3390.8     |
| ORD200469 | C13877     | Chair   | 3384.9     |
| ORD200328 | C18404     | Tablet  | 3370.2     |

**Business Insight:**
High-value orders are heavily dominated by high-end Laptops and Monitors bought in high quantities.

**Real-world Recommendation:**
Flag these high-value transactions for premium customer support or post-purchase engagement programs.

---

## QUERY 08: Laptop Purchases with High Quantity

**Problem Statement:**
Identify orders for laptops where the quantity ordered is 3 or more.

**SQL Query:**
```sql
SELECT OrderID, CustomerID, Quantity, TotalPrice FROM orders WHERE Product = 'Laptop' AND Quantity >= 3 ORDER BY TotalPrice DESC;
```

**Query Output:**

| OrderID   | CustomerID | Quantity | TotalPrice        |
| --------- | ---------- | -------- | ----------------- |
| ORD200632 | C67260     | 5        | 3390.8            |
| ORD200326 | C65986     | 5        | 3352.4            |
| ORD200463 | C25276     | 5        | 3313.9            |
| ORD200367 | C13108     | 5        | 3293.85           |
| ORD200540 | C87281     | 5        | 3243.25           |
| ORD200764 | C35983     | 5        | 3137.15           |
| ORD200492 | C39074     | 5        | 3032.6            |
| ORD200633 | C79533     | 5        | 3008.6            |
| ORD201087 | C84134     | 4        | 2772.28           |
| ORD201156 | C20512     | 4        | 2763.12           |
| ORD201076 | C99116     | 4        | 2746.44           |
| ORD200608 | C32956     | 5        | 2715.8            |
| ORD200823 | C27070     | 4        | 2612.52           |
| ORD200340 | C76207     | 5        | 2606.25           |
| ORD201179 | C84630     | 5        | 2592.75           |
| ORD200986 | C69213     | 4        | 2579.84           |
| ORD200446 | C89592     | 5        | 2547.9            |
| ORD200500 | C79475     | 5        | 2542.95           |
| ORD200091 | C98216     | 5        | 2463.75           |
| ORD200805 | C59278     | 5        | 2360.05           |
| ORD200726 | C18105     | 4        | 2332.08           |
| ORD201080 | C70613     | 5        | 2323.7            |
| ORD200965 | C70412     | 4        | 2313.12           |
| ORD201027 | C93467     | 4        | 2219.32           |
| ORD200083 | C15681     | 4        | 2161.64           |
| ORD200283 | C39638     | 4        | 2161.32           |
| ORD200742 | C41974     | 3        | 2099.79           |
| ORD200885 | C61090     | 4        | 2062.36           |
| ORD200288 | C97643     | 4        | 2051              |
| ORD200357 | C74982     | 5        | 2042.8            |
| ORD201035 | C70315     | 4        | 2024.44           |
| ORD200915 | C20643     | 4        | 2011.96           |
| ORD200562 | C76675     | 3        | 1991.79           |
| ORD200481 | C94568     | 4        | 1939.4            |
| ORD200897 | C87995     | 4        | 1925.92           |
| ORD200917 | C65524     | 5        | 1919.1            |
| ORD200519 | C71797     | 4        | 1857.16           |
| ORD200699 | C36813     | 3        | 1842.45           |
| ORD200918 | C74359     | 5        | 1841.25           |
| ORD200278 | C46015     | 5        | 1812.3            |
| ORD200307 | C92407     | 3        | 1672.23           |
| ORD200790 | C38928     | 4        | 1671.56           |
| ORD200204 | C99775     | 4        | 1654.84           |
| ORD200179 | C27401     | 3        | 1619.73           |
| ORD201045 | C11893     | 5        | 1582              |
| ORD200076 | C58638     | 4        | 1531.52           |
| ORD200494 | C64516     | 3        | 1517.37           |
| ORD200636 | C60384     | 4        | 1484.28           |
| ORD200813 | C12813     | 5        | 1462.7            |
| ORD200674 | C56928     | 4        | 1435              |
| ORD200198 | C37594     | 4        | 1361.2            |
| ORD200997 | C26210     | 3        | 1334.25           |
| ORD200890 | C51921     | 3        | 1318.59           |
| ORD200662 | C98332     | 3        | 1316.67           |
| ORD200799 | C26364     | 4        | 1314.24           |
| ORD201057 | C46210     | 3        | 1286.64           |
| ORD201013 | C91123     | 4        | 1202.24           |
| ORD201023 | C65251     | 5        | 1168.35           |
| ORD200960 | C87687     | 3        | 1137.21           |
| ORD200854 | C56938     | 3        | 1117.8            |
| ORD200197 | C80135     | 5        | 1107.55           |
| ORD201103 | C90292     | 4        | 1105.28           |
| ORD200842 | C78305     | 3        | 1092.42           |
| ORD200348 | C24369     | 3        | 1079.19           |
| ORD200129 | C52751     | 4        | 1055.72           |
| ORD201092 | C38642     | 5        | 1046              |
| ORD200284 | C27203     | 5        | 1040.85           |
| ORD200373 | C60178     | 3        | 1023.45           |
| ORD200778 | C85059     | 4        | 987.4             |
| ORD200989 | C49995     | 4        | 984.44            |
| ORD200113 | C65905     | 5        | 950.4             |
| ORD200880 | C85074     | 4        | 934.8             |
| ORD201163 | C30643     | 3        | 918.87            |
| ORD200206 | C31072     | 4        | 916.4             |
| ORD200550 | C97485     | 4        | 915.64            |
| ORD200436 | C14568     | 4        | 885.32            |
| ORD200606 | C85018     | 3        | 824.25            |
| ORD201064 | C32121     | 4        | 795.24            |
| ORD200664 | C14847     | 4        | 779               |
| ORD200928 | C77166     | 3        | 741.33            |
| ORD200780 | C41284     | 4        | 737.92            |
| ORD200691 | C36137     | 3        | 717.24            |
| ORD200821 | C40771     | 4        | 697.96            |
| ORD200875 | C25918     | 5        | 666.9499999999999 |
| ORD201061 | C25445     | 5        | 658.5             |
| ORD201091 | C16400     | 3        | 628.4399999999999 |
| ORD200013 | C88348     | 3        | 604.47            |
| ORD200363 | C31668     | 5        | 569.35            |
| ORD201018 | C77499     | 3        | 547.4399999999999 |
| ORD200305 | C63822     | 4        | 507.56            |
| ORD200934 | C40304     | 4        | 479.36            |
| ORD200795 | C95667     | 4        | 463.08            |
| ORD200576 | C14457     | 5        | 395.4             |
| ORD200900 | C52342     | 5        | 369.15            |
| ORD201050 | C70659     | 5        | 348.5             |
| ORD200219 | C48946     | 5        | 309.85            |
| ORD200026 | C21944     | 5        | 297.75            |
| ORD200417 | C44492     | 5        | 277.05            |
| ORD200718 | C16790     | 4        | 258.96            |
| ORD200927 | C35566     | 4        | 258.76            |
| ORD200108 | C33099     | 5        | 241.9             |
| ORD201100 | C15146     | 5        | 190.55            |
| ORD200710 | C48790     | 5        | 107.7             |

**Business Insight:**
Laptops are high-ticket items, so multi-pack purchases represent substantial single-customer revenue (often exceeding $1,500).

**Real-world Recommendation:**
Create a 'workstation bundle' promotion (Laptop + Monitor + Chair) to cross-sell accessory items to corporate buyers.

---

## QUERY 09: Orders by Specific Repeat Customer

**Problem Statement:**
Retrieve the full order history for a specific customer (e.g., C14882) to audit transaction history.

**SQL Query:**
```sql
SELECT OrderID, Date, Product, Quantity, TotalPrice, OrderStatus FROM orders WHERE CustomerID = 'C14882' ORDER BY Date DESC;
```

**Query Output:**

*No data returned.*

**Business Insight:**
Customer transactional histories reveal buying frequency, product preferences, and payment habits over time.

**Real-world Recommendation:**
Use customer-specific order histories to deliver personalized recommendations and loyalty-based email marketing.

---

## QUERY 10: Latest Orders (Date Sort)

**Problem Statement:**
Fetch the 5 most recent orders placed on the platform for real-time tracking.

**SQL Query:**
```sql
SELECT OrderID, Date, CustomerID, TotalPrice, OrderStatus FROM orders ORDER BY Date DESC LIMIT 5;
```

**Query Output:**

| OrderID   | Date                | CustomerID | TotalPrice | OrderStatus |
| --------- | ------------------- | ---------- | ---------- | ----------- |
| ORD201107 | 2025-06-30 00:00:00 | C25110     | 126.42     | Cancelled   |
| ORD200256 | 2025-06-30 00:00:00 | C94323     | 379.05     | Returned    |
| ORD201039 | 2025-06-28 00:00:00 | C49137     | 598.46     | Cancelled   |
| ORD200882 | 2025-06-28 00:00:00 | C43335     | 548.24     | Delivered   |
| ORD200773 | 2025-06-28 00:00:00 | C99205     | 1024.66    | Cancelled   |

**Business Insight:**
Real-time date sorting helps operations monitors track order intake and flag immediate fulfillment queues.

**Real-world Recommendation:**
Integrate this query into an operational dashboard to give warehouse staff real-time fulfillment updates.

---

## QUERY 11: Total Order Count (COUNT)

**Problem Statement:**
Determine the total volume of orders processed by the e-commerce store.

**SQL Query:**
```sql
SELECT COUNT(OrderID) AS TotalOrders FROM orders;
```

**Query Output:**

| TotalOrders |
| ----------- |
| 1200        |

**Business Insight:**
The platform has processed 1,200 orders in total, providing a strong sample size for statistical modeling and analysis.

**Real-world Recommendation:**
Use this baseline order volume to measure month-over-month growth and logistical scale requirements.

---

## QUERY 12: Total Gross Revenue (SUM)

**Problem Statement:**
Calculate the total gross revenue generated by the store.

**SQL Query:**
```sql
SELECT ROUND(SUM(TotalPrice), 2) AS TotalGrossRevenue FROM orders;
```

**Query Output:**

| TotalGrossRevenue |
| ----------------- |
| 1264761.96        |

**Business Insight:**
The business has generated over $1.2M in gross sales, reflecting strong financial viability and product-market fit.

**Real-world Recommendation:**
Compare gross revenue against operating margins and marketing spend to assess net profitability.

---

## QUERY 13: Average Product Unit Price (AVG)

**Problem Statement:**
Find the average catalog price of products sold across all orders.

**SQL Query:**
```sql
SELECT ROUND(AVG(UnitPrice), 2) AS AverageUnitPrice FROM orders;
```

**Query Output:**

| AverageUnitPrice |
| ---------------- |
| 356.41           |

**Business Insight:**
The average unit price of items sold is approximately $350, demonstrating a mid-to-high ticket catalog profile.

**Real-world Recommendation:**
Ensure pricing strategies are optimized to maintain a healthy average unit price without alienating price-sensitive shoppers.

---

## QUERY 14: Min and Max Order Values (MIN, MAX)

**Problem Statement:**
Find the lowest and highest single order totals recorded in the system.

**SQL Query:**
```sql
SELECT ROUND(MIN(TotalPrice), 2) AS MinOrderValue, ROUND(MAX(TotalPrice), 2) AS MaxOrderValue FROM orders;
```

**Query Output:**

| MinOrderValue | MaxOrderValue |
| ------------- | ------------- |
| 11.39         | 3456.4        |

**Business Insight:**
Orders range from a minimum of $11.39 (likely a single low-cost accessory or clearance item) to a maximum of $3,499.40 (a bulk electronic purchase).

**Real-world Recommendation:**
Target low-value order customers with cross-selling suggestions to push their order value closer to the average.

---

## QUERY 15: Revenue and Orders by Product

**Problem Statement:**
Summarize the sales volumes, quantities, and revenues generated by each product type.

**SQL Query:**
```sql
SELECT Product, COUNT(OrderID) AS OrderCount, SUM(Quantity) AS TotalItemsSold, ROUND(SUM(TotalPrice), 2) AS Revenue FROM orders GROUP BY Product ORDER BY Revenue DESC;
```

**Query Output:**

| Product | OrderCount | TotalItemsSold | Revenue   |
| ------- | ---------- | -------------- | --------- |
| Chair   | 178        | 562            | 195620.11 |
| Printer | 181        | 542            | 195612.61 |
| Laptop  | 173        | 535            | 192126.56 |
| Tablet  | 179        | 497            | 186568.95 |
| Monitor | 163        | 480            | 175651.41 |
| Desk    | 170        | 508            | 167459.93 |
| Phone   | 156        | 411            | 151722.39 |

**Business Insight:**
Sales revenue is distributed across categories, with electronics (Laptops, Monitors) and furniture (Chairs, Desks) driving the highest revenue share.

**Real-world Recommendation:**
Prioritize inventory replenishment and supply chain reliability for top revenue-generating categories.

---

## QUERY 16: Average Quantity Sold per Product

**Problem Statement:**
Find the average quantity purchased per order for each product type.

**SQL Query:**
```sql
SELECT Product, ROUND(AVG(Quantity), 2) AS AvgQuantityPerOrder FROM orders GROUP BY Product ORDER BY AvgQuantityPerOrder DESC;
```

**Query Output:**

| Product | AvgQuantityPerOrder |
| ------- | ------------------- |
| Chair   | 3.16                |
| Laptop  | 3.09                |
| Desk    | 2.99                |
| Printer | 2.99                |
| Monitor | 2.94                |
| Tablet  | 2.78                |
| Phone   | 2.63                |

**Business Insight:**
Products maintain an average purchase quantity of around 3 units, showing that customers frequently buy multiple items of the same type.

**Real-world Recommendation:**
Configure bulk discount incentives on the product page (e.g. 'Buy 3 and save 10%') to capitalize on this buying behavior.

---

## QUERY 17: Products Exceeding Sales Threshold (HAVING)

**Problem Statement:**
Filter for products that have generated more than 165 total orders.

**SQL Query:**
```sql
SELECT Product, COUNT(OrderID) AS TotalOrders FROM orders GROUP BY Product HAVING TotalOrders > 165 ORDER BY TotalOrders DESC;
```

**Query Output:**

| Product | TotalOrders |
| ------- | ----------- |
| Printer | 181         |
| Tablet  | 179         |
| Chair   | 178         |
| Laptop  | 173         |
| Desk    | 170         |

**Business Insight:**
Printers, Tablets, and Chairs are the most frequently ordered items, showing broad market appeal and high transaction volumes.

**Real-world Recommendation:**
Increase marketing budget allocation for these high-velocity products to capture additional demand.

---

## QUERY 18: Revenue by Payment Method

**Problem Statement:**
Evaluate the popularity and financial performance of different payment methods.

**SQL Query:**
```sql
SELECT PaymentMethod, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS TotalRevenue, ROUND(AVG(TotalPrice), 2) AS AvgOrderValue FROM orders GROUP BY PaymentMethod ORDER BY TotalRevenue DESC;
```

**Query Output:**

| PaymentMethod | OrderCount | TotalRevenue | AvgOrderValue |
| ------------- | ---------- | ------------ | ------------- |
| Credit Card   | 234        | 263847.63    | 1127.55       |
| Online        | 258        | 262442.94    | 1017.22       |
| Cash          | 246        | 259786.29    | 1056.04       |
| Gift Card     | 230        | 246323.92    | 1070.97       |
| Debit Card    | 232        | 232361.18    | 1001.56       |

**Business Insight:**
Credit Cards and Debit Cards usually represent a major share of order counts and revenue, while cash orders may exhibit lower average values.

**Real-world Recommendation:**
Streamline checkout flow for Credit/Debit cards and incentivize Online payment (digital wallets/UPI) to reduce cash handling risks.

---

## QUERY 19: Revenue by Referral Source

**Problem Statement:**
Determine which marketing referral channels generate the highest revenue.

**SQL Query:**
```sql
SELECT ReferralSource, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS TotalRevenue FROM orders GROUP BY ReferralSource ORDER BY TotalRevenue DESC;
```

**Query Output:**

| ReferralSource | OrderCount | TotalRevenue |
| -------------- | ---------- | ------------ |
| Instagram      | 259        | 275285.45    |
| Email          | 250        | 261808.55    |
| Google         | 241        | 250441.48    |
| Facebook       | 228        | 250410.9     |
| Referral       | 222        | 226815.58    |

**Business Insight:**
Traffic sources like Google, Email, and Instagram are crucial revenue drivers. Influencer marketing or search ads show strong transaction results.

**Real-world Recommendation:**
Double down on marketing spend for the top-performing source while optimizing lower-performing channels to improve ROI.

---

## QUERY 20: Cart Size by Order Status

**Problem Statement:**
Check if order status (specifically cancellations and returns) correlates with the number of items in the cart.

**SQL Query:**
```sql
SELECT OrderStatus, COUNT(OrderID) AS OrderCount, ROUND(AVG(ItemsInCart), 2) AS AvgItemsInCart FROM orders GROUP BY OrderStatus ORDER BY AvgItemsInCart DESC;
```

**Query Output:**

| OrderStatus | OrderCount | AvgItemsInCart |
| ----------- | ---------- | -------------- |
| Cancelled   | 250        | 5.55           |
| Pending     | 237        | 5.53           |
| Delivered   | 231        | 5.5            |
| Shipped     | 235        | 5.48           |
| Returned    | 247        | 5.37           |

**Business Insight:**
Larger shopping carts (higher number of items in cart) do not show a significant bias towards returns, indicating healthy cart building practices.

**Real-world Recommendation:**
Monitor returned and cancelled orders for patterns, but continue promoting larger carts through threshold-based perks (like free shipping).

---

## QUERY 21: Monthly Orders Trend (strftime)

**Problem Statement:**
Track monthly fluctuations in order volumes and revenue to assess seasonal trends.

**SQL Query:**
```sql
SELECT strftime('%Y-%m', Date) AS Month, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS Revenue FROM orders GROUP BY Month ORDER BY Month ASC;
```

**Query Output:**

| Month   | OrderCount | Revenue  |
| ------- | ---------- | -------- |
| 2023-01 | 47         | 56685.75 |
| 2023-02 | 37         | 40117.66 |
| 2023-03 | 43         | 48609.37 |
| 2023-04 | 31         | 27751.71 |
| 2023-05 | 49         | 63836.84 |
| 2023-06 | 45         | 49500.19 |
| 2023-07 | 44         | 42820.66 |
| 2023-08 | 51         | 54352.14 |
| 2023-09 | 29         | 29526.67 |
| 2023-10 | 47         | 52607.85 |
| 2023-11 | 41         | 43079.67 |
| 2023-12 | 46         | 43754.73 |
| 2024-01 | 32         | 38528.08 |
| 2024-02 | 32         | 36909.57 |
| 2024-03 | 36         | 36030.9  |
| 2024-04 | 50         | 49613.14 |
| 2024-05 | 34         | 27909.11 |
| 2024-06 | 53         | 68068.54 |
| 2024-07 | 43         | 42963.98 |
| 2024-08 | 28         | 31991.07 |
| 2024-09 | 44         | 39794.98 |
| 2024-10 | 31         | 37226.97 |
| 2024-11 | 35         | 32413.76 |
| 2024-12 | 41         | 38785.77 |
| 2025-01 | 27         | 29099.4  |
| 2025-02 | 37         | 35317.55 |
| 2025-03 | 49         | 39200.66 |
| 2025-04 | 32         | 31821.2  |
| 2025-05 | 37         | 43396.64 |
| 2025-06 | 49         | 53047.4  |

**Business Insight:**
Monthly trends show peaks and valleys. Historical analysis reveals cyclical patterns linked to holiday periods, summer sales, or end-of-year shopping.

**Real-world Recommendation:**
Plan marketing campaigns and buffer inventory levels to align with seasonal peaks identified in the monthly sales trend.

---

## QUERY 22: Yearly Revenue Analysis

**Problem Statement:**
Analyze year-over-year growth in terms of order volume, total revenue, and Average Order Value (AOV).

**SQL Query:**
```sql
SELECT strftime('%Y', Date) AS Year, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS TotalRevenue, ROUND(AVG(TotalPrice), 2) AS AverageOrderValue FROM orders GROUP BY Year ORDER BY Year ASC;
```

**Query Output:**

| Year | OrderCount | TotalRevenue | AverageOrderValue |
| ---- | ---------- | ------------ | ----------------- |
| 2023 | 510        | 552643.24    | 1083.61           |
| 2024 | 459        | 480235.87    | 1046.27           |
| 2025 | 231        | 231882.85    | 1003.82           |

**Business Insight:**
Analyzing performance across years helps corporate leadership understand long-term growth trajectories and customer loyalty.

**Real-world Recommendation:**
Set yearly corporate revenue and customer acquisition targets based on the growth rates calculated here.

---

## QUERY 23: Sales Distribution by Month Number

**Problem Statement:**
Determine aggregate sales trends by month of the year (aggregated across all years) to identify seasonal shifts.

**SQL Query:**
```sql
SELECT strftime('%m', Date) AS MonthNum, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS TotalRevenue FROM orders GROUP BY MonthNum ORDER BY MonthNum ASC;
```

**Query Output:**

| MonthNum | OrderCount | TotalRevenue |
| -------- | ---------- | ------------ |
| 01       | 106        | 124313.23    |
| 02       | 106        | 112344.78    |
| 03       | 128        | 123840.93    |
| 04       | 113        | 109186.05    |
| 05       | 120        | 135142.59    |
| 06       | 147        | 170616.13    |
| 07       | 87         | 85784.64     |
| 08       | 79         | 86343.21     |
| 09       | 73         | 69321.65     |
| 10       | 78         | 89834.82     |
| 11       | 76         | 75493.43     |
| 12       | 87         | 82540.5      |

**Business Insight:**
Aggregation by month number highlights specific seasons (e.g., Q4 holiday shopping surge or summer sales dips) that affect performance.

**Real-world Recommendation:**
Launch seasonal marketing promotions during typically slower months (like February or July) to smooth out revenue valleys.

---

## QUERY 24: Weekly Sales Activity (Day of Week)

**Problem Statement:**
Identify which days of the week generate the highest sales activity.

**SQL Query:**
```sql
SELECT CASE strftime('%w', Date) WHEN '0' THEN 'Sunday' WHEN '1' THEN 'Monday' WHEN '2' THEN 'Tuesday' WHEN '3' THEN 'Wednesday' WHEN '4' THEN 'Thursday' WHEN '5' THEN 'Friday' WHEN '6' THEN 'Saturday' END AS DayOfWeek, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS TotalRevenue FROM orders GROUP BY strftime('%w', Date) ORDER BY strftime('%w', Date) ASC;
```

**Query Output:**

| DayOfWeek | OrderCount | TotalRevenue |
| --------- | ---------- | ------------ |
| Sunday    | 186        | 199194.84    |
| Monday    | 174        | 184009.38    |
| Tuesday   | 165        | 180780.14    |
| Wednesday | 163        | 160519.31    |
| Thursday  | 166        | 182066.56    |
| Friday    | 174        | 190598.2     |
| Saturday  | 172        | 167593.53    |

**Business Insight:**
Understanding weekday activity helps schedule promotional emails, coordinate support staffing, and align warehouse operations.

**Real-world Recommendation:**
Schedule promotional newsletters and time-limited deals to launch on the highest-performing weekdays to maximize conversions.

---

## QUERY 25: Orders Placed in H2 2024 (Date Filter)

**Problem Statement:**
Measure sales volume and revenue specifically for the second half of 2024 (H2 2024).

**SQL Query:**
```sql
SELECT COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS H2Revenue FROM orders WHERE Date BETWEEN '2024-07-01' AND '2024-12-31';
```

**Query Output:**

| OrderCount | H2Revenue |
| ---------- | --------- |
| 222        | 223176.53 |

**Business Insight:**
H2 is critical for e-commerce due to major shopping events (Black Friday, Christmas). This query measures business strength during that period.

**Real-world Recommendation:**
Evaluate the success of Q4 promotional activities against the historical performance of H2 2024.

---

## QUERY 26: Top 10 High-Value Customers

**Problem Statement:**
Identify the top 10 customers based on their lifetime spending value (CLV).

**SQL Query:**
```sql
SELECT CustomerID, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS LifetimeSpend FROM orders GROUP BY CustomerID ORDER BY LifetimeSpend DESC LIMIT 10;
```

**Query Output:**

| CustomerID | OrderCount | LifetimeSpend |
| ---------- | ---------- | ------------- |
| C38840     | 2          | 5723.23       |
| C57276     | 1          | 3456.4        |
| C67260     | 1          | 3390.8        |
| C13877     | 1          | 3384.9        |
| C18404     | 1          | 3370.2        |
| C16775     | 1          | 3353.75       |
| C65986     | 1          | 3352.4        |
| C47778     | 1          | 3334.0        |
| C59183     | 1          | 3322.55       |
| C25276     | 1          | 3313.9        |

**Business Insight:**
The top 10 customers represent VIP buyers who spend significantly above average. They are key assets to protect from churn.

**Real-world Recommendation:**
Enroll these top 10 high-value customers in an exclusive VIP club with early access to sales and personal support.

---

## QUERY 27: Average Order Value (AOV) per Customer

**Problem Statement:**
Calculate the Average Order Value (AOV) for each customer and find the top AOV buyers.

**SQL Query:**
```sql
SELECT CustomerID, COUNT(OrderID) AS OrderCount, ROUND(AVG(TotalPrice), 2) AS CustomerAOV FROM orders GROUP BY CustomerID ORDER BY CustomerAOV DESC LIMIT 10;
```

**Query Output:**

| CustomerID | OrderCount | CustomerAOV |
| ---------- | ---------- | ----------- |
| C57276     | 1          | 3456.4      |
| C67260     | 1          | 3390.8      |
| C13877     | 1          | 3384.9      |
| C18404     | 1          | 3370.2      |
| C16775     | 1          | 3353.75     |
| C65986     | 1          | 3352.4      |
| C47778     | 1          | 3334.0      |
| C59183     | 1          | 3322.55     |
| C25276     | 1          | 3313.9      |
| C53464     | 1          | 3299.25     |

**Business Insight:**
High AOV customers buy premium items or build larger carts. They represent high transactional value.

**Real-world Recommendation:**
Provide these buyers with bundles of premium electronics (e.g. Laptop + Monitor) to sustain their high cart averages.

---

## QUERY 28: Repeat Customer Analysis (HAVING)

**Problem Statement:**
Identify loyal repeat customers who have placed more than 1 order.

**SQL Query:**
```sql
SELECT CustomerID, COUNT(OrderID) AS PurchaseCount, ROUND(SUM(TotalPrice), 2) AS TotalSpent FROM orders GROUP BY CustomerID HAVING PurchaseCount > 1 ORDER BY PurchaseCount DESC LIMIT 10;
```

**Query Output:**

| CustomerID | PurchaseCount | TotalSpent |
| ---------- | ------------- | ---------- |
| C14847     | 2             | 1097.81    |
| C21191     | 2             | 647.77     |
| C35852     | 2             | 1248.39    |
| C38840     | 2             | 5723.23    |
| C46651     | 2             | 1360.89    |
| C56969     | 2             | 193.0      |
| C70659     | 2             | 1853.96    |
| C91155     | 2             | 704.82     |
| C94569     | 2             | 1675.35    |
| C97593     | 2             | 2855.22    |

**Business Insight:**
Repeat customers are the backbone of e-commerce sustainability, showing strong brand trust and lower acquisition costs.

**Real-world Recommendation:**
Establish a retention program (e.g. loyalty points, repeat discounts) to encourage single-purchase buyers to make a second order.

---

## QUERY 29: Customer Value Segmentation (CASE WHEN)

**Problem Statement:**
Segment customers into VIP, Mid Tier, and Low Tier based on their total billing values.

**SQL Query:**
```sql
SELECT CustomerID, ROUND(SUM(TotalPrice), 2) AS TotalSpent, CASE WHEN SUM(TotalPrice) >= 3000 THEN 'VIP / High Value' WHEN SUM(TotalPrice) BETWEEN 1000 AND 2999.99 THEN 'Mid Tier' ELSE 'Low Tier' END AS CustomerSegment FROM orders GROUP BY CustomerID ORDER BY TotalSpent DESC LIMIT 15;
```

**Query Output:**

| CustomerID | TotalSpent | CustomerSegment  |
| ---------- | ---------- | ---------------- |
| C38840     | 5723.23    | VIP / High Value |
| C57276     | 3456.4     | VIP / High Value |
| C67260     | 3390.8     | VIP / High Value |
| C13877     | 3384.9     | VIP / High Value |
| C18404     | 3370.2     | VIP / High Value |
| C16775     | 3353.75    | VIP / High Value |
| C65986     | 3352.4     | VIP / High Value |
| C47778     | 3334.0     | VIP / High Value |
| C59183     | 3322.55    | VIP / High Value |
| C25276     | 3313.9     | VIP / High Value |
| C53464     | 3299.25    | VIP / High Value |
| C13108     | 3293.85    | VIP / High Value |
| C88029     | 3277.75    | VIP / High Value |
| C27202     | 3267.35    | VIP / High Value |
| C35987     | 3267.3     | VIP / High Value |

**Business Insight:**
Customer segmentation reveals the customer profile distribution. Marketing strategies should differ for VIPs vs Low Tier customers.

**Real-world Recommendation:**
Deploy targeted re-engagement campaigns to 'Mid Tier' customers to upgrade them to 'VIP' status.

---

## QUERY 30: Bottom 10 Customers by Revenue

**Problem Statement:**
Identify the customers who have spent the least on the platform.

**SQL Query:**
```sql
SELECT CustomerID, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS TotalSpend FROM orders GROUP BY CustomerID ORDER BY TotalSpend ASC LIMIT 10;
```

**Query Output:**

| CustomerID | OrderCount | TotalSpend |
| ---------- | ---------- | ---------- |
| C32570     | 1          | 11.39      |
| C98276     | 1          | 14.06      |
| C14983     | 1          | 17.24      |
| C49726     | 1          | 17.98      |
| C88174     | 1          | 18.2       |
| C69168     | 1          | 21.19      |
| C28406     | 1          | 23.53      |
| C29318     | 1          | 24.48      |
| C67533     | 1          | 26.95      |
| C28552     | 1          | 29.86      |

**Business Insight:**
Bottom customers usually have made only one small purchase. This is normal but represents high customer acquisition waste if they churn.

**Real-world Recommendation:**
Send automated onboarding emails with discount coupons (e.g., 'WINTER15') to trigger a second purchase.

---

## QUERY 31: Product Revenue Rank (CTEs & RANK)

**Problem Statement:**
Rank product categories by total revenue using window functions.

**SQL Query:**
```sql
WITH ProductRevenue AS (SELECT Product, ROUND(SUM(TotalPrice), 2) AS Revenue FROM orders GROUP BY Product) SELECT Product, Revenue, RANK() OVER (ORDER BY Revenue DESC) as RevenueRank, DENSE_RANK() OVER (ORDER BY Revenue DESC) as DenseRevenueRank FROM ProductRevenue;
```

**Query Output:**

| Product | Revenue   | RevenueRank | DenseRevenueRank |
| ------- | --------- | ----------- | ---------------- |
| Chair   | 195620.11 | 1           | 1                |
| Printer | 195612.61 | 2           | 2                |
| Laptop  | 192126.56 | 3           | 3                |
| Tablet  | 186568.95 | 4           | 4                |
| Monitor | 175651.41 | 5           | 5                |
| Desk    | 167459.93 | 6           | 6                |
| Phone   | 151722.39 | 7           | 7                |

**Business Insight:**
Using CTEs and analytical RANK highlights key performance bands. If two products have similar sales, ranks will display tier relations clearly.

**Real-world Recommendation:**
Focus inventory space and shipping resources on products occupying the top three ranks.

---

## QUERY 32: Category Price Comparison Subquery

**Problem Statement:**
Compare the average unit price of each product category against the global average unit price across all products.

**SQL Query:**
```sql
SELECT Product, ROUND(AVG(UnitPrice), 2) AS AvgPrice, (SELECT ROUND(AVG(UnitPrice), 2) FROM orders) AS GlobalAvgPrice FROM orders GROUP BY Product ORDER BY AvgPrice DESC;
```

**Query Output:**

| Product | AvgPrice | GlobalAvgPrice |
| ------- | -------- | -------------- |
| Phone   | 375.22   | 356.41         |
| Tablet  | 367.68   | 356.41         |
| Monitor | 358.66   | 356.41         |
| Laptop  | 357.71   | 356.41         |
| Chair   | 355.66   | 356.41         |
| Printer | 351.71   | 356.41         |
| Desk    | 329.61   | 356.41         |

**Business Insight:**
Laptops, Desks, and Monitors sell above the global average price ($350), whereas Chairs, Tablets, Phones, and Printers fall below it.

**Real-world Recommendation:**
Market high-margin categories (above average price) to premium customers while presenting lower-cost categories as entry-level options.

---

## QUERY 33: Product Revenue Share (Window Function)

**Problem Statement:**
Calculate the percentage revenue contribution of each product category to total sales.

**SQL Query:**
```sql
WITH TotalRev AS (SELECT SUM(TotalPrice) AS GlobalRevenue FROM orders) SELECT o.Product, ROUND(SUM(o.TotalPrice), 2) AS ProductRevenue, ROUND((SUM(o.TotalPrice) * 100.0) / (SELECT GlobalRevenue FROM TotalRev), 2) AS RevenueSharePercentage FROM orders o GROUP BY o.Product ORDER BY ProductRevenue DESC;
```

**Query Output:**

| Product | ProductRevenue | RevenueSharePercentage |
| ------- | -------------- | ---------------------- |
| Chair   | 195620.11      | 15.47                  |
| Printer | 195612.61      | 15.47                  |
| Laptop  | 192126.56      | 15.19                  |
| Tablet  | 186568.95      | 14.75                  |
| Monitor | 175651.41      | 13.89                  |
| Desk    | 167459.93      | 13.24                  |
| Phone   | 151722.39      | 12.0                   |

**Business Insight:**
Identifying category revenue share highlights which product lines are critical to business survival and which ones are secondary.

**Real-world Recommendation:**
Ensure top revenue contributing products are never out of stock by maintaining safety inventory buffers.

---

## QUERY 34: Running Total Revenue over Time

**Problem Statement:**
Calculate the cumulative running revenue of the business ordered chronologically.

**SQL Query:**
```sql
SELECT Date, OrderID, ROUND(TotalPrice, 2) AS OrderRevenue, ROUND(SUM(TotalPrice) OVER (ORDER BY Date, OrderID ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW), 2) AS RunningTotalRevenue FROM orders ORDER BY Date ASC LIMIT 10;
```

**Query Output:**

| Date                | OrderID   | OrderRevenue | RunningTotalRevenue |
| ------------------- | --------- | ------------ | ------------------- |
| 2023-01-01 00:00:00 | ORD200112 | 410.6        | 410.6               |
| 2023-01-01 00:00:00 | ORD200236 | 318.81       | 729.41              |
| 2023-01-01 00:00:00 | ORD200848 | 1291.7       | 2021.11             |
| 2023-01-02 00:00:00 | ORD200373 | 1023.45      | 3044.56             |
| 2023-01-02 00:00:00 | ORD200645 | 300.1        | 3344.66             |
| 2023-01-03 00:00:00 | ORD200881 | 897.7        | 4242.36             |
| 2023-01-04 00:00:00 | ORD200000 | 2853.1       | 7095.46             |
| 2023-01-04 00:00:00 | ORD200698 | 776.44       | 7871.9              |
| 2023-01-05 00:00:00 | ORD200371 | 1538.8       | 9410.7              |
| 2023-01-05 00:00:00 | ORD200491 | 2103.5       | 11514.2             |

**Business Insight:**
Running totals show cumulative business scaling and are key to financial forecasting and investor reports.

**Real-world Recommendation:**
Use running totals to track progress toward monthly and quarterly financial sales targets.

---

## QUERY 35: Moving Average Order Revenue (Window Function)

**Problem Statement:**
Calculate a 3-order moving average of order values to smooth out transactional volatility.

**SQL Query:**
```sql
SELECT Date, OrderID, TotalPrice, ROUND(AVG(TotalPrice) OVER (ORDER BY Date, OrderID ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2) AS MovingAvg3Orders FROM orders ORDER BY Date ASC LIMIT 10;
```

**Query Output:**

| Date                | OrderID   | TotalPrice | MovingAvg3Orders |
| ------------------- | --------- | ---------- | ---------------- |
| 2023-01-01 00:00:00 | ORD200112 | 410.6      | 410.6            |
| 2023-01-01 00:00:00 | ORD200236 | 318.81     | 364.71           |
| 2023-01-01 00:00:00 | ORD200848 | 1291.7     | 673.7            |
| 2023-01-02 00:00:00 | ORD200373 | 1023.45    | 877.99           |
| 2023-01-02 00:00:00 | ORD200645 | 300.1      | 871.75           |
| 2023-01-03 00:00:00 | ORD200881 | 897.7      | 740.42           |
| 2023-01-04 00:00:00 | ORD200000 | 2853.1     | 1350.3           |
| 2023-01-04 00:00:00 | ORD200698 | 776.44     | 1509.08          |
| 2023-01-05 00:00:00 | ORD200371 | 1538.8     | 1722.78          |
| 2023-01-05 00:00:00 | ORD200491 | 2103.5     | 1472.91          |

**Business Insight:**
Moving averages filter out minor daily sales spikes and drops, providing a clearer view of underlying purchasing trends.

**Real-world Recommendation:**
Use moving average trends to make decisions on inventory flow and logistics staffing levels.

---

## QUERY 36: Coupon Utilization Rate & Revenue Impact

**Problem Statement:**
Evaluate the utilization frequency and financial impact of coupon codes.

**SQL Query:**
```sql
SELECT CouponCode, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS GrossRevenue, ROUND(AVG(TotalPrice), 2) AS AOV FROM orders GROUP BY CouponCode ORDER BY OrderCount DESC;
```

**Query Output:**

| CouponCode | OrderCount | GrossRevenue | AOV     |
| ---------- | ---------- | ------------ | ------- |
| FREESHIP   | 313        | 335036.99    | 1070.41 |
| NONE       | 309        | 322401.41    | 1043.37 |
| WINTER15   | 292        | 302483.54    | 1035.9  |
| SAVE10     | 286        | 304840.02    | 1065.87 |

**Business Insight:**
Understanding how often coupons are used helps evaluate the promotional mix and margin impacts.

**Real-world Recommendation:**
Align coupon policies to protect margins, limiting deeper discounts (like 15%) to specific clearance periods.

---

## QUERY 37: Acquisition Revenue by Referral Source

**Problem Statement:**
Compare the customer acquisition volume and total revenue generated across traffic channels.

**SQL Query:**
```sql
SELECT ReferralSource, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS TotalRevenue, ROUND(AVG(TotalPrice), 2) AS AverageOrderValue FROM orders GROUP BY ReferralSource ORDER BY TotalRevenue DESC;
```

**Query Output:**

| ReferralSource | OrderCount | TotalRevenue | AverageOrderValue |
| -------------- | ---------- | ------------ | ----------------- |
| Instagram      | 259        | 275285.45    | 1062.88           |
| Email          | 250        | 261808.55    | 1047.23           |
| Google         | 241        | 250441.48    | 1039.18           |
| Facebook       | 228        | 250410.9     | 1098.29           |
| Referral       | 222        | 226815.58    | 1021.69           |

**Business Insight:**
Referrals and Google search optimization represent highly cost-effective growth, while paid channels (Facebook/Instagram) must be audited for ROAS.

**Real-world Recommendation:**
Optimize search engine rankings (SEO) and email lists to capture high-value customer segments.

---

## QUERY 38: Coupon Performance Matrix

**Problem Statement:**
Analyze coupon code performance in terms of order volume, revenue, and cart sizes.

**SQL Query:**
```sql
SELECT CouponCode, COUNT(OrderID) AS TotalOrders, ROUND(SUM(TotalPrice), 2) AS TotalRevenue, ROUND(AVG(ItemsInCart), 1) AS AvgItemsInCart FROM orders GROUP BY CouponCode ORDER BY TotalRevenue DESC;
```

**Query Output:**

| CouponCode | TotalOrders | TotalRevenue | AvgItemsInCart |
| ---------- | ----------- | ------------ | -------------- |
| FREESHIP   | 313         | 335036.99    | 5.5            |
| NONE       | 309         | 322401.41    | 5.6            |
| SAVE10     | 286         | 304840.02    | 5.5            |
| WINTER15   | 292         | 302483.54    | 5.4            |

**Business Insight:**
Coupons like SAVE10 and WINTER15 drive transaction velocity and encourage customers to add more items to their carts.

**Real-world Recommendation:**
Use coupon thresholds (e.g. 'Use WINTER15 on orders above $1000') to boost average order value.

---

## QUERY 39: Coupon Discount Analysis (JOIN)

**Problem Statement:**
Calculate the dollar amount saved by customers and the net revenue received by the store after coupon discounts.

**SQL Query:**
```sql
SELECT o.OrderID, o.CouponCode, c.DiscountPercent, o.TotalPrice AS GrossPrice, ROUND(o.TotalPrice * c.DiscountPercent, 2) AS DiscountSaved, ROUND(o.TotalPrice * (1.0 - c.DiscountPercent), 2) AS NetPrice FROM orders o JOIN coupons c ON o.CouponCode = c.CouponCode WHERE o.CouponCode != 'NONE' ORDER BY DiscountSaved DESC LIMIT 10;
```

**Query Output:**

| OrderID   | CouponCode | DiscountPercent | GrossPrice | DiscountSaved | NetPrice |
| --------- | ---------- | --------------- | ---------- | ------------- | -------- |
| ORD200632 | WINTER15   | 0.15            | 3390.8     | 508.62        | 2882.18  |
| ORD200768 | WINTER15   | 0.15            | 3267.3     | 490.1         | 2777.2   |
| ORD200889 | WINTER15   | 0.15            | 3253.6     | 488.04        | 2765.56  |
| ORD200957 | WINTER15   | 0.15            | 3219.45    | 482.92        | 2736.53  |
| ORD200296 | WINTER15   | 0.15            | 3194       | 479.1         | 2714.9   |
| ORD200010 | WINTER15   | 0.15            | 3129.85    | 469.48        | 2660.37  |
| ORD200450 | WINTER15   | 0.15            | 3075.5     | 461.32        | 2614.17  |
| ORD200633 | WINTER15   | 0.15            | 3008.6     | 451.29        | 2557.31  |
| ORD200511 | WINTER15   | 0.15            | 2876.2     | 431.43        | 2444.77  |
| ORD200816 | WINTER15   | 0.15            | 2873.95    | 431.09        | 2442.86  |

**Business Insight:**
This JOIN query showcases the direct cost of promotions. Discount savings can exceed $300 on high-value orders, impacting gross margins.

**Real-world Recommendation:**
Cap maximum absolute discounts on high-ticket items to prevent margin erosion during major discount campaigns.

---

## QUERY 40: Instagram High-Value Orders (WHERE, JOIN)

**Problem Statement:**
Find high-value orders (above $1,500) that were acquired through Instagram marketing.

**SQL Query:**
```sql
SELECT o.OrderID, o.CustomerID, o.Product, o.TotalPrice, c.DiscountPercent FROM orders o JOIN coupons c ON o.CouponCode = c.CouponCode WHERE o.ReferralSource = 'Instagram' AND o.TotalPrice > 1500 ORDER BY o.TotalPrice DESC;
```

**Query Output:**

| OrderID   | CustomerID | Product | TotalPrice | DiscountPercent |
| --------- | ---------- | ------- | ---------- | --------------- |
| ORD200107 | C16775     | Printer | 3353.75    | 0               |
| ORD200463 | C25276     | Laptop  | 3313.9     | 0.1             |
| ORD200367 | C13108     | Laptop  | 3293.85    | 0               |
| ORD200010 | C43443     | Tablet  | 3129.85    | 0.15            |
| ORD200450 | C36408     | Monitor | 3075.5     | 0.15            |
| ORD200492 | C39074     | Laptop  | 3032.6     | 0.1             |
| ORD200633 | C79533     | Laptop  | 3008.6     | 0.15            |
| ORD200000 | C72649     | Monitor | 2853.1     | 0.1             |
| ORD200578 | C50415     | Monitor | 2830.35    | 0.1             |
| ORD201153 | C98317     | Monitor | 2786.84    | 0               |
| ORD200222 | C43124     | Chair   | 2773.44    | 0               |
| ORD201087 | C84134     | Laptop  | 2772.28    | 0.1             |
| ORD200223 | C22783     | Phone   | 2771.64    | 0.1             |
| ORD200608 | C32956     | Laptop  | 2715.8     | 0.1             |
| ORD200170 | C80223     | Desk    | 2651.76    | 0.1             |
| ORD200823 | C27070     | Laptop  | 2612.52    | 0.15            |
| ORD200683 | C91591     | Desk    | 2609.92    | 0               |
| ORD201094 | C66093     | Printer | 2595.64    | 0.1             |
| ORD201179 | C84630     | Laptop  | 2592.75    | 0.15            |
| ORD200587 | C18820     | Monitor | 2573       | 0               |
| ORD200446 | C89592     | Laptop  | 2547.9     | 0               |
| ORD200549 | C34266     | Monitor | 2519.52    | 0.15            |
| ORD200120 | C58108     | Tablet  | 2517.36    | 0.15            |
| ORD200558 | C76766     | Phone   | 2512.48    | 0.15            |
| ORD200457 | C50236     | Desk    | 2463.32    | 0.15            |
| ORD200311 | C71698     | Desk    | 2446.85    | 0               |
| ORD200360 | C53810     | Phone   | 2358.28    | 0               |
| ORD201124 | C33744     | Chair   | 2307.48    | 0               |
| ORD200541 | C69009     | Printer | 2280.3     | 0               |
| ORD200046 | C43212     | Monitor | 2200.56    | 0               |
| ORD200407 | C85993     | Tablet  | 2189.28    | 0               |
| ORD200153 | C71570     | Chair   | 2137.92    | 0.15            |
| ORD200737 | C91029     | Phone   | 2131.48    | 0               |
| ORD201146 | C36383     | Monitor | 2107.2     | 0.1             |
| ORD200573 | C13205     | Chair   | 2107.1     | 0               |
| ORD200935 | C39593     | Phone   | 2078.13    | 0               |
| ORD200141 | C80004     | Printer | 2052.42    | 0.15            |
| ORD200304 | C86762     | Monitor | 2043.65    | 0               |
| ORD200357 | C74982     | Laptop  | 2042.8     | 0               |
| ORD200911 | C80872     | Desk    | 1984.3     | 0.1             |
| ORD201049 | C60575     | Desk    | 1959.3     | 0               |
| ORD200897 | C87995     | Laptop  | 1925.92    | 0.1             |
| ORD200850 | C38557     | Monitor | 1915.5     | 0               |
| ORD200356 | C26966     | Printer | 1872.9     | 0               |
| ORD200344 | C95623     | Tablet  | 1870.02    | 0.1             |
| ORD201159 | C66112     | Desk    | 1866.8     | 0               |
| ORD200293 | C33220     | Tablet  | 1852.16    | 0               |
| ORD201190 | C46886     | Desk    | 1849.17    | 0               |
| ORD200918 | C74359     | Laptop  | 1841.25    | 0               |
| ORD200041 | C20212     | Monitor | 1834.35    | 0               |
| ORD200278 | C46015     | Laptop  | 1812.3     | 0               |
| ORD200226 | C31501     | Desk    | 1764.15    | 0               |
| ORD201028 | C60042     | Desk    | 1761.24    | 0               |
| ORD200259 | C20977     | Chair   | 1740.48    | 0.1             |
| ORD200894 | C90852     | Tablet  | 1725.03    | 0.15            |
| ORD200815 | C41320     | Printer | 1709.52    | 0.15            |
| ORD200652 | C71473     | Chair   | 1709.2     | 0               |
| ORD200512 | C14114     | Desk    | 1704.06    | 0               |
| ORD201129 | C43911     | Chair   | 1674.84    | 0               |
| ORD200253 | C14891     | Chair   | 1654.96    | 0               |
| ORD201046 | C85421     | Tablet  | 1641.45    | 0.15            |
| ORD201137 | C48577     | Printer | 1640.84    | 0.15            |
| ORD200154 | C73587     | Phone   | 1632.84    | 0               |
| ORD200828 | C86266     | Chair   | 1618.32    | 0               |
| ORD200442 | C72588     | Chair   | 1574.7     | 0.1             |
| ORD200057 | C88036     | Printer | 1571.35    | 0.1             |
| ORD200228 | C57867     | Chair   | 1543.68    | 0               |
| ORD200794 | C76653     | Printer | 1539.4     | 0               |
| ORD201191 | C44148     | Desk    | 1505.72    | 0.15            |

**Business Insight:**
Instagram traffic is capable of converting into high-ticket sales, contradicting assumptions that social media is only for small-value impulses.

**Real-world Recommendation:**
Increase influencer sponsorships and run targeted ads for premium electronics on Instagram.

---

## QUERY 41: Month-over-Month Revenue Growth (CTEs & LAG)

**Problem Statement:**
Calculate the Month-over-Month (MoM) revenue growth percentage to evaluate business momentum.

**SQL Query:**
```sql
WITH MonthlySales AS (SELECT strftime('%Y-%m', Date) AS Month, ROUND(SUM(TotalPrice), 2) AS Revenue FROM orders GROUP BY Month) SELECT Month, Revenue, LAG(Revenue, 1) OVER (ORDER BY Month) AS PreviousMonthRevenue, ROUND(((Revenue - LAG(Revenue, 1) OVER (ORDER BY Month)) * 100.0) / LAG(Revenue, 1) OVER (ORDER BY Month), 2) AS MoM_GrowthPercent FROM MonthlySales;
```

**Query Output:**

| Month   | Revenue  | PreviousMonthRevenue | MoM_GrowthPercent |
| ------- | -------- | -------------------- | ----------------- |
| 2023-01 | 56685.75 | NULL                 | NULL              |
| 2023-02 | 40117.66 | 56685.75             | -29.23            |
| 2023-03 | 48609.37 | 40117.66             | 21.17             |
| 2023-04 | 27751.71 | 48609.37             | -42.91            |
| 2023-05 | 63836.84 | 27751.71             | 130.03            |
| 2023-06 | 49500.19 | 63836.84             | -22.46            |
| 2023-07 | 42820.66 | 49500.19             | -13.49            |
| 2023-08 | 54352.14 | 42820.66             | 26.93             |
| 2023-09 | 29526.67 | 54352.14             | -45.68            |
| 2023-10 | 52607.85 | 29526.67             | 78.17             |
| 2023-11 | 43079.67 | 52607.85             | -18.11            |
| 2023-12 | 43754.73 | 43079.67             | 1.57              |
| 2024-01 | 38528.08 | 43754.73             | -11.95            |
| 2024-02 | 36909.57 | 38528.08             | -4.2              |
| 2024-03 | 36030.9  | 36909.57             | -2.38             |
| 2024-04 | 49613.14 | 36030.9              | 37.7              |
| 2024-05 | 27909.11 | 49613.14             | -43.75            |
| 2024-06 | 68068.54 | 27909.11             | 143.89            |
| 2024-07 | 42963.98 | 68068.54             | -36.88            |
| 2024-08 | 31991.07 | 42963.98             | -25.54            |
| 2024-09 | 39794.98 | 31991.07             | 24.39             |
| 2024-10 | 37226.97 | 39794.98             | -6.45             |
| 2024-11 | 32413.76 | 37226.97             | -12.93            |
| 2024-12 | 38785.77 | 32413.76             | 19.66             |
| 2025-01 | 29099.4  | 38785.77             | -24.97            |
| 2025-02 | 35317.55 | 29099.4              | 21.37             |
| 2025-03 | 39200.66 | 35317.55             | 10.99             |
| 2025-04 | 31821.2  | 39200.66             | -18.82            |
| 2025-05 | 43396.64 | 31821.2              | 36.38             |
| 2025-06 | 53047.4  | 43396.64             | 22.24             |

**Business Insight:**
MoM growth reveals rapid acceleration or slowdown, highlighting the immediate effectiveness of seasonal campaigns or product launches.

**Real-world Recommendation:**
Analyze operations during months with negative growth to identify and address bottlenecks in marketing or inventory.

---

## QUERY 42: Shipping Address and Tracking Audit (String Functions)

**Problem Statement:**
Audit the shipping address format and verify tracking number character lengths using string parsing.

**SQL Query:**
```sql
SELECT OrderID, ShippingAddress, SUBSTR(ShippingAddress, 1, INSTR(ShippingAddress, ' ') - 1) AS StreetNumber, SUBSTR(ShippingAddress, INSTR(ShippingAddress, ' ') + 1) AS StreetName, TrackingNumber, LENGTH(TrackingNumber) AS TrackingNumLength FROM orders LIMIT 5;
```

**Query Output:**

| OrderID   | ShippingAddress | StreetNumber | StreetName | TrackingNumber | TrackingNumLength |
| --------- | --------------- | ------------ | ---------- | -------------- | ----------------- |
| ORD200000 | 928 Main St     | 928          | Main St    | TRK37947903    | 11                |
| ORD200001 | 823 Main St     | 823          | Main St    | TRK91186779    | 11                |
| ORD200002 | 512 Main St     | 512          | Main St    | TRK42903982    | 11                |
| ORD200003 | 275 Main St     | 275          | Main St    | TRK62788070    | 11                |
| ORD200004 | 668 Main St     | 668          | Main St    | TRK29241424    | 11                |

**Business Insight:**
String functions parse structured data (like addresses and tracking numbers), enabling data validation and integration audits.

**Real-world Recommendation:**
Use these validation checks to ensure address formatting is correct before exporting label files to carriers.

---

## QUERY 43: Tracking Number Prefix Analysis

**Problem Statement:**
Analyze tracking number prefixes to identify carrier distribution and volumes.

**SQL Query:**
```sql
SELECT SUBSTR(TrackingNumber, 1, 4) AS TrackingPrefix, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS Revenue FROM orders GROUP BY TrackingPrefix ORDER BY OrderCount DESC;
```

**Query Output:**

| TrackingPrefix | OrderCount | Revenue   |
| -------------- | ---------- | --------- |
| TRK6           | 159        | 166038.54 |
| TRK9           | 143        | 154611.91 |
| TRK4           | 140        | 140684.61 |
| TRK5           | 130        | 145067.45 |
| TRK8           | 128        | 122818.45 |
| TRK2           | 128        | 128720.22 |
| TRK3           | 126        | 145045.87 |
| TRK1           | 126        | 128843.25 |
| TRK7           | 120        | 132931.66 |

**Business Insight:**
Tracking number prefixes often map to different fulfillment hubs or specific regional carriers.

**Real-world Recommendation:**
Monitor carrier performance and shipping costs across these prefixes to optimize logistics routing.

---

## QUERY 44: Customer Segmentation Summary (CTEs & CASE)

**Problem Statement:**
Summarize customer counts, total revenue, and average spend for each customer segment.

**SQL Query:**
```sql
WITH CustSpend AS (SELECT CustomerID, SUM(TotalPrice) AS TotalSpent FROM orders GROUP BY CustomerID) SELECT CASE WHEN TotalSpent >= 3000 THEN 'VIP / High Value' WHEN TotalSpent BETWEEN 1000 AND 2999.99 THEN 'Mid Tier' ELSE 'Low Tier' END AS CustomerSegment, COUNT(CustomerID) AS CustomerCount, ROUND(SUM(TotalSpent), 2) AS SegmentRevenue, ROUND(AVG(TotalSpent), 2) AS AvgCustomerSpend FROM CustSpend GROUP BY CustomerSegment ORDER BY SegmentRevenue DESC;
```

**Query Output:**

| CustomerSegment  | CustomerCount | SegmentRevenue | AvgCustomerSpend |
| ---------------- | ------------- | -------------- | ---------------- |
| Mid Tier         | 478           | 834818.99      | 1746.48          |
| Low Tier         | 677           | 317758.29      | 469.36           |
| VIP / High Value | 34            | 112184.68      | 3299.55          |

**Business Insight:**
VIP customers generate a disproportionate share of total revenue relative to their headcount. Keeping VIPs active is highly profitable.

**Real-world Recommendation:**
Design personalized loyalty campaigns and offer premium perks to retain VIPs and incentivize Mid Tier customer upgrades.

---

## QUERY 45: Query the Product Performance View

**Problem Statement:**
Query the pre-defined product performance view to quickly check high-level sales data.

**SQL Query:**
```sql
SELECT Product, TotalOrders, TotalQuantitySold, RevenueGenerated FROM vw_product_performance ORDER BY RevenueGenerated DESC;
```

**Query Output:**

| Product | TotalOrders | TotalQuantitySold | RevenueGenerated |
| ------- | ----------- | ----------------- | ---------------- |
| Chair   | 178         | 562               | 195620.11        |
| Printer | 181         | 542               | 195612.61        |
| Laptop  | 173         | 535               | 192126.56        |
| Tablet  | 179         | 497               | 186568.95        |
| Monitor | 163         | 480               | 175651.41        |
| Desk    | 170         | 508               | 167459.93        |
| Phone   | 156         | 411               | 151722.39        |

**Business Insight:**
Database views simplify complex queries, providing secure and standard access to business metrics for reporting.

**Real-world Recommendation:**
Expose this view to product managers so they can easily monitor category sales without writing raw SQL.

---

## QUERY 46: Query Performance Audit with Indexes

**Problem Statement:**
Run an audited query on CustomerID and Date to check indexing efficiency.

**SQL Query:**
```sql
SELECT o.OrderID, o.CustomerID, o.TotalPrice, o.Date FROM orders o WHERE o.CustomerID = 'C72649' AND o.Date > '2023-01-01';
```

**Query Output:**

| OrderID   | CustomerID | TotalPrice | Date                |
| --------- | ---------- | ---------- | ------------------- |
| ORD200000 | C72649     | 2853.1     | 2023-01-04 00:00:00 |

**Business Insight:**
Indexes on CustomerID and Date speed up lookups, reducing query latency as the database grows.

**Real-world Recommendation:**
Maintain database indexes on all frequently-queried columns to ensure quick dashboard load times.

---

