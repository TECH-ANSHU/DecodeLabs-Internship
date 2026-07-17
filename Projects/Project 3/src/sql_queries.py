"""
SQL Queries module containing 46 business-focused SQL queries with problem statements,
insights, and actionable business recommendations.
"""

SQL_QUERIES = {
    "query_01": {
        "name": "Select All Orders (Limit)",
        "sql": "SELECT OrderID, Date, CustomerID, Product, Quantity, TotalPrice FROM orders LIMIT 5;",
        "problem_statement": "Examine the database structure and quickly check the first few records in the orders table.",
        "business_insight": "The dataset contains standard transactional parameters including order identifiers, customers, products purchased, quantities, and total order prices.",
        "recommendation": "Use this basic schema inspection to verify that automated integrations are writing all fields successfully."
    },
    "query_02": {
        "name": "Distinct Product Categories",
        "sql": "SELECT DISTINCT Product FROM orders ORDER BY Product;",
        "problem_statement": "Identify the unique product categories sold by the e-commerce store.",
        "business_insight": "The store offers 7 unique product types: Chair, Desk, Laptop, Monitor, Phone, Printer, and Tablet, representing a blend of office furniture and consumer electronics.",
        "recommendation": "Review product classifications regularly to align stocking strategies with major category demands."
    },
    "query_03": {
        "name": "Distinct Payment Methods",
        "sql": "SELECT DISTINCT PaymentMethod FROM orders ORDER BY PaymentMethod;",
        "problem_statement": "List all payment methods supported by the e-commerce platform.",
        "business_insight": "Supported payment methods include Credit Card, Debit Card, Online (wallets/UPI), Gift Card, and Cash, offering high convenience to different consumer segments.",
        "recommendation": "Ensure payment gateways are optimized for credit/debit cards and digital wallets to minimize cart abandonment."
    },
    "query_04": {
        "name": "Distinct Referral Sources",
        "sql": "SELECT DISTINCT ReferralSource FROM orders ORDER BY ReferralSource;",
        "problem_statement": "Identify all marketing and acquisition channels bringing traffic to the site.",
        "business_insight": "Customers are acquired via 5 main channels: Email, Facebook, Google, Instagram, and direct Referrals.",
        "recommendation": "Track acquisition costs (CAC) across these channels to measure marketing return on investment (ROI)."
    },
    "query_05": {
        "name": "High Quantity Orders (WHERE)",
        "sql": "SELECT OrderID, CustomerID, Product, Quantity, TotalPrice FROM orders WHERE Quantity >= 5 ORDER BY Quantity DESC LIMIT 5;",
        "problem_statement": "Find orders where a customer bought 5 or more units of a single product.",
        "business_insight": "High-quantity orders (5 units) frequently occur for items like Monitors and Chairs, suggesting potential B2B or corporate office setups.",
        "recommendation": "Introduce bulk-purchase discounts or corporate account managers to target small businesses purchasing office gear."
    },
    "query_06": {
        "name": "Shipped Orders Filter",
        "sql": "SELECT COUNT(*) AS ShippedCount FROM orders WHERE OrderStatus = 'Shipped';",
        "problem_statement": "Track how many orders are currently in 'Shipped' status, awaiting delivery.",
        "business_insight": "A substantial portion of orders are currently in transit, representing active logistics operations.",
        "recommendation": "Coordinate closely with logistics partners to ensure delivery SLAs are met and tracking details are updated promptly."
    },
    "query_07": {
        "name": "Orders Exceeding $2000 (WHERE, ORDER BY)",
        "sql": "SELECT OrderID, CustomerID, Product, TotalPrice FROM orders WHERE TotalPrice > 2000 ORDER BY TotalPrice DESC LIMIT 5;",
        "problem_statement": "List the highest value individual orders exceeding $2,000.",
        "business_insight": "High-value orders are heavily dominated by high-end Laptops and Monitors bought in high quantities.",
        "recommendation": "Flag these high-value transactions for premium customer support or post-purchase engagement programs."
    },
    "query_08": {
        "name": "Laptop Purchases with High Quantity",
        "sql": "SELECT OrderID, CustomerID, Quantity, TotalPrice FROM orders WHERE Product = 'Laptop' AND Quantity >= 3 ORDER BY TotalPrice DESC;",
        "problem_statement": "Identify orders for laptops where the quantity ordered is 3 or more.",
        "business_insight": "Laptops are high-ticket items, so multi-pack purchases represent substantial single-customer revenue (often exceeding $1,500).",
        "recommendation": "Create a 'workstation bundle' promotion (Laptop + Monitor + Chair) to cross-sell accessory items to corporate buyers."
    },
    "query_09": {
        "name": "Orders by Specific Repeat Customer",
        "sql": "SELECT OrderID, Date, Product, Quantity, TotalPrice, OrderStatus FROM orders WHERE CustomerID = 'C14882' ORDER BY Date DESC;",
        "problem_statement": "Retrieve the full order history for a specific customer (e.g., C14882) to audit transaction history.",
        "business_insight": "Customer transactional histories reveal buying frequency, product preferences, and payment habits over time.",
        "recommendation": "Use customer-specific order histories to deliver personalized recommendations and loyalty-based email marketing."
    },
    "query_10": {
        "name": "Latest Orders (Date Sort)",
        "sql": "SELECT OrderID, Date, CustomerID, TotalPrice, OrderStatus FROM orders ORDER BY Date DESC LIMIT 5;",
        "problem_statement": "Fetch the 5 most recent orders placed on the platform for real-time tracking.",
        "business_insight": "Real-time date sorting helps operations monitors track order intake and flag immediate fulfillment queues.",
        "recommendation": "Integrate this query into an operational dashboard to give warehouse staff real-time fulfillment updates."
    },
    "query_11": {
        "name": "Total Order Count (COUNT)",
        "sql": "SELECT COUNT(OrderID) AS TotalOrders FROM orders;",
        "problem_statement": "Determine the total volume of orders processed by the e-commerce store.",
        "business_insight": "The platform has processed 1,200 orders in total, providing a strong sample size for statistical modeling and analysis.",
        "recommendation": "Use this baseline order volume to measure month-over-month growth and logistical scale requirements."
    },
    "query_12": {
        "name": "Total Gross Revenue (SUM)",
        "sql": "SELECT ROUND(SUM(TotalPrice), 2) AS TotalGrossRevenue FROM orders;",
        "problem_statement": "Calculate the total gross revenue generated by the store.",
        "business_insight": "The business has generated over $1.2M in gross sales, reflecting strong financial viability and product-market fit.",
        "recommendation": "Compare gross revenue against operating margins and marketing spend to assess net profitability."
    },
    "query_13": {
        "name": "Average Product Unit Price (AVG)",
        "sql": "SELECT ROUND(AVG(UnitPrice), 2) AS AverageUnitPrice FROM orders;",
        "problem_statement": "Find the average catalog price of products sold across all orders.",
        "business_insight": "The average unit price of items sold is approximately $350, demonstrating a mid-to-high ticket catalog profile.",
        "recommendation": "Ensure pricing strategies are optimized to maintain a healthy average unit price without alienating price-sensitive shoppers."
    },
    "query_14": {
        "name": "Min and Max Order Values (MIN, MAX)",
        "sql": "SELECT ROUND(MIN(TotalPrice), 2) AS MinOrderValue, ROUND(MAX(TotalPrice), 2) AS MaxOrderValue FROM orders;",
        "problem_statement": "Find the lowest and highest single order totals recorded in the system.",
        "business_insight": "Orders range from a minimum of $11.39 (likely a single low-cost accessory or clearance item) to a maximum of $3,499.40 (a bulk electronic purchase).",
        "recommendation": "Target low-value order customers with cross-selling suggestions to push their order value closer to the average."
    },
    "query_15": {
        "name": "Revenue and Orders by Product",
        "sql": "SELECT Product, COUNT(OrderID) AS OrderCount, SUM(Quantity) AS TotalItemsSold, ROUND(SUM(TotalPrice), 2) AS Revenue FROM orders GROUP BY Product ORDER BY Revenue DESC;",
        "problem_statement": "Summarize the sales volumes, quantities, and revenues generated by each product type.",
        "business_insight": "Sales revenue is distributed across categories, with electronics (Laptops, Monitors) and furniture (Chairs, Desks) driving the highest revenue share.",
        "recommendation": "Prioritize inventory replenishment and supply chain reliability for top revenue-generating categories."
    },
    "query_16": {
        "name": "Average Quantity Sold per Product",
        "sql": "SELECT Product, ROUND(AVG(Quantity), 2) AS AvgQuantityPerOrder FROM orders GROUP BY Product ORDER BY AvgQuantityPerOrder DESC;",
        "problem_statement": "Find the average quantity purchased per order for each product type.",
        "business_insight": "Products maintain an average purchase quantity of around 3 units, showing that customers frequently buy multiple items of the same type.",
        "recommendation": "Configure bulk discount incentives on the product page (e.g. 'Buy 3 and save 10%') to capitalize on this buying behavior."
    },
    "query_17": {
        "name": "Products Exceeding Sales Threshold (HAVING)",
        "sql": "SELECT Product, COUNT(OrderID) AS TotalOrders FROM orders GROUP BY Product HAVING TotalOrders > 165 ORDER BY TotalOrders DESC;",
        "problem_statement": "Filter for products that have generated more than 165 total orders.",
        "business_insight": "Printers, Tablets, and Chairs are the most frequently ordered items, showing broad market appeal and high transaction volumes.",
        "recommendation": "Increase marketing budget allocation for these high-velocity products to capture additional demand."
    },
    "query_18": {
        "name": "Revenue by Payment Method",
        "sql": "SELECT PaymentMethod, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS TotalRevenue, ROUND(AVG(TotalPrice), 2) AS AvgOrderValue FROM orders GROUP BY PaymentMethod ORDER BY TotalRevenue DESC;",
        "problem_statement": "Evaluate the popularity and financial performance of different payment methods.",
        "business_insight": "Credit Cards and Debit Cards usually represent a major share of order counts and revenue, while cash orders may exhibit lower average values.",
        "recommendation": "Streamline checkout flow for Credit/Debit cards and incentivize Online payment (digital wallets/UPI) to reduce cash handling risks."
    },
    "query_19": {
        "name": "Revenue by Referral Source",
        "sql": "SELECT ReferralSource, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS TotalRevenue FROM orders GROUP BY ReferralSource ORDER BY TotalRevenue DESC;",
        "problem_statement": "Determine which marketing referral channels generate the highest revenue.",
        "business_insight": "Traffic sources like Google, Email, and Instagram are crucial revenue drivers. Influencer marketing or search ads show strong transaction results.",
        "recommendation": "Double down on marketing spend for the top-performing source while optimizing lower-performing channels to improve ROI."
    },
    "query_20": {
        "name": "Cart Size by Order Status",
        "sql": "SELECT OrderStatus, COUNT(OrderID) AS OrderCount, ROUND(AVG(ItemsInCart), 2) AS AvgItemsInCart FROM orders GROUP BY OrderStatus ORDER BY AvgItemsInCart DESC;",
        "problem_statement": "Check if order status (specifically cancellations and returns) correlates with the number of items in the cart.",
        "business_insight": "Larger shopping carts (higher number of items in cart) do not show a significant bias towards returns, indicating healthy cart building practices.",
        "recommendation": "Monitor returned and cancelled orders for patterns, but continue promoting larger carts through threshold-based perks (like free shipping)."
    },
    "query_21": {
        "name": "Monthly Orders Trend (strftime)",
        "sql": "SELECT strftime('%Y-%m', Date) AS Month, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS Revenue FROM orders GROUP BY Month ORDER BY Month ASC;",
        "problem_statement": "Track monthly fluctuations in order volumes and revenue to assess seasonal trends.",
        "business_insight": "Monthly trends show peaks and valleys. Historical analysis reveals cyclical patterns linked to holiday periods, summer sales, or end-of-year shopping.",
        "recommendation": "Plan marketing campaigns and buffer inventory levels to align with seasonal peaks identified in the monthly sales trend."
    },
    "query_22": {
        "name": "Yearly Revenue Analysis",
        "sql": "SELECT strftime('%Y', Date) AS Year, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS TotalRevenue, ROUND(AVG(TotalPrice), 2) AS AverageOrderValue FROM orders GROUP BY Year ORDER BY Year ASC;",
        "problem_statement": "Analyze year-over-year growth in terms of order volume, total revenue, and Average Order Value (AOV).",
        "business_insight": "Analyzing performance across years helps corporate leadership understand long-term growth trajectories and customer loyalty.",
        "recommendation": "Set yearly corporate revenue and customer acquisition targets based on the growth rates calculated here."
    },
    "query_23": {
        "name": "Sales Distribution by Month Number",
        "sql": "SELECT strftime('%m', Date) AS MonthNum, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS TotalRevenue FROM orders GROUP BY MonthNum ORDER BY MonthNum ASC;",
        "problem_statement": "Determine aggregate sales trends by month of the year (aggregated across all years) to identify seasonal shifts.",
        "business_insight": "Aggregation by month number highlights specific seasons (e.g., Q4 holiday shopping surge or summer sales dips) that affect performance.",
        "recommendation": "Launch seasonal marketing promotions during typically slower months (like February or July) to smooth out revenue valleys."
    },
    "query_24": {
        "name": "Weekly Sales Activity (Day of Week)",
        "sql": "SELECT CASE strftime('%w', Date) WHEN '0' THEN 'Sunday' WHEN '1' THEN 'Monday' WHEN '2' THEN 'Tuesday' WHEN '3' THEN 'Wednesday' WHEN '4' THEN 'Thursday' WHEN '5' THEN 'Friday' WHEN '6' THEN 'Saturday' END AS DayOfWeek, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS TotalRevenue FROM orders GROUP BY strftime('%w', Date) ORDER BY strftime('%w', Date) ASC;",
        "problem_statement": "Identify which days of the week generate the highest sales activity.",
        "business_insight": "Understanding weekday activity helps schedule promotional emails, coordinate support staffing, and align warehouse operations.",
        "recommendation": "Schedule promotional newsletters and time-limited deals to launch on the highest-performing weekdays to maximize conversions."
    },
    "query_25": {
        "name": "Orders Placed in H2 2024 (Date Filter)",
        "sql": "SELECT COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS H2Revenue FROM orders WHERE Date BETWEEN '2024-07-01' AND '2024-12-31';",
        "problem_statement": "Measure sales volume and revenue specifically for the second half of 2024 (H2 2024).",
        "business_insight": "H2 is critical for e-commerce due to major shopping events (Black Friday, Christmas). This query measures business strength during that period.",
        "recommendation": "Evaluate the success of Q4 promotional activities against the historical performance of H2 2024."
    },
    "query_26": {
        "name": "Top 10 High-Value Customers",
        "sql": "SELECT CustomerID, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS LifetimeSpend FROM orders GROUP BY CustomerID ORDER BY LifetimeSpend DESC LIMIT 10;",
        "problem_statement": "Identify the top 10 customers based on their lifetime spending value (CLV).",
        "business_insight": "The top 10 customers represent VIP buyers who spend significantly above average. They are key assets to protect from churn.",
        "recommendation": "Enroll these top 10 high-value customers in an exclusive VIP club with early access to sales and personal support."
    },
    "query_27": {
        "name": "Average Order Value (AOV) per Customer",
        "sql": "SELECT CustomerID, COUNT(OrderID) AS OrderCount, ROUND(AVG(TotalPrice), 2) AS CustomerAOV FROM orders GROUP BY CustomerID ORDER BY CustomerAOV DESC LIMIT 10;",
        "problem_statement": "Calculate the Average Order Value (AOV) for each customer and find the top AOV buyers.",
        "business_insight": "High AOV customers buy premium items or build larger carts. They represent high transactional value.",
        "recommendation": "Provide these buyers with bundles of premium electronics (e.g. Laptop + Monitor) to sustain their high cart averages."
    },
    "query_28": {
        "name": "Repeat Customer Analysis (HAVING)",
        "sql": "SELECT CustomerID, COUNT(OrderID) AS PurchaseCount, ROUND(SUM(TotalPrice), 2) AS TotalSpent FROM orders GROUP BY CustomerID HAVING PurchaseCount > 1 ORDER BY PurchaseCount DESC LIMIT 10;",
        "problem_statement": "Identify loyal repeat customers who have placed more than 1 order.",
        "business_insight": "Repeat customers are the backbone of e-commerce sustainability, showing strong brand trust and lower acquisition costs.",
        "recommendation": "Establish a retention program (e.g. loyalty points, repeat discounts) to encourage single-purchase buyers to make a second order."
    },
    "query_29": {
        "name": "Customer Value Segmentation (CASE WHEN)",
        "sql": "SELECT CustomerID, ROUND(SUM(TotalPrice), 2) AS TotalSpent, CASE WHEN SUM(TotalPrice) >= 3000 THEN 'VIP / High Value' WHEN SUM(TotalPrice) BETWEEN 1000 AND 2999.99 THEN 'Mid Tier' ELSE 'Low Tier' END AS CustomerSegment FROM orders GROUP BY CustomerID ORDER BY TotalSpent DESC LIMIT 15;",
        "problem_statement": "Segment customers into VIP, Mid Tier, and Low Tier based on their total billing values.",
        "business_insight": "Customer segmentation reveals the customer profile distribution. Marketing strategies should differ for VIPs vs Low Tier customers.",
        "recommendation": "Deploy targeted re-engagement campaigns to 'Mid Tier' customers to upgrade them to 'VIP' status."
    },
    "query_30": {
        "name": "Bottom 10 Customers by Revenue",
        "sql": "SELECT CustomerID, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS TotalSpend FROM orders GROUP BY CustomerID ORDER BY TotalSpend ASC LIMIT 10;",
        "problem_statement": "Identify the customers who have spent the least on the platform.",
        "business_insight": "Bottom customers usually have made only one small purchase. This is normal but represents high customer acquisition waste if they churn.",
        "recommendation": "Send automated onboarding emails with discount coupons (e.g., 'WINTER15') to trigger a second purchase."
    },
    "query_31": {
        "name": "Product Revenue Rank (CTEs & RANK)",
        "sql": "WITH ProductRevenue AS (SELECT Product, ROUND(SUM(TotalPrice), 2) AS Revenue FROM orders GROUP BY Product) SELECT Product, Revenue, RANK() OVER (ORDER BY Revenue DESC) as RevenueRank, DENSE_RANK() OVER (ORDER BY Revenue DESC) as DenseRevenueRank FROM ProductRevenue;",
        "problem_statement": "Rank product categories by total revenue using window functions.",
        "business_insight": "Using CTEs and analytical RANK highlights key performance bands. If two products have similar sales, ranks will display tier relations clearly.",
        "recommendation": "Focus inventory space and shipping resources on products occupying the top three ranks."
    },
    "query_32": {
        "name": "Category Price Comparison Subquery",
        "sql": "SELECT Product, ROUND(AVG(UnitPrice), 2) AS AvgPrice, (SELECT ROUND(AVG(UnitPrice), 2) FROM orders) AS GlobalAvgPrice FROM orders GROUP BY Product ORDER BY AvgPrice DESC;",
        "problem_statement": "Compare the average unit price of each product category against the global average unit price across all products.",
        "business_insight": "Laptops, Desks, and Monitors sell above the global average price ($350), whereas Chairs, Tablets, Phones, and Printers fall below it.",
        "recommendation": "Market high-margin categories (above average price) to premium customers while presenting lower-cost categories as entry-level options."
    },
    "query_33": {
        "name": "Product Revenue Share (Window Function)",
        "sql": "WITH TotalRev AS (SELECT SUM(TotalPrice) AS GlobalRevenue FROM orders) SELECT o.Product, ROUND(SUM(o.TotalPrice), 2) AS ProductRevenue, ROUND((SUM(o.TotalPrice) * 100.0) / (SELECT GlobalRevenue FROM TotalRev), 2) AS RevenueSharePercentage FROM orders o GROUP BY o.Product ORDER BY ProductRevenue DESC;",
        "problem_statement": "Calculate the percentage revenue contribution of each product category to total sales.",
        "business_insight": "Identifying category revenue share highlights which product lines are critical to business survival and which ones are secondary.",
        "recommendation": "Ensure top revenue contributing products are never out of stock by maintaining safety inventory buffers."
    },
    "query_34": {
        "name": "Running Total Revenue over Time",
        "sql": "SELECT Date, OrderID, ROUND(TotalPrice, 2) AS OrderRevenue, ROUND(SUM(TotalPrice) OVER (ORDER BY Date, OrderID ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW), 2) AS RunningTotalRevenue FROM orders ORDER BY Date ASC LIMIT 10;",
        "problem_statement": "Calculate the cumulative running revenue of the business ordered chronologically.",
        "business_insight": "Running totals show cumulative business scaling and are key to financial forecasting and investor reports.",
        "recommendation": "Use running totals to track progress toward monthly and quarterly financial sales targets."
    },
    "query_35": {
        "name": "Moving Average Order Revenue (Window Function)",
        "sql": "SELECT Date, OrderID, TotalPrice, ROUND(AVG(TotalPrice) OVER (ORDER BY Date, OrderID ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2) AS MovingAvg3Orders FROM orders ORDER BY Date ASC LIMIT 10;",
        "problem_statement": "Calculate a 3-order moving average of order values to smooth out transactional volatility.",
        "business_insight": "Moving averages filter out minor daily sales spikes and drops, providing a clearer view of underlying purchasing trends.",
        "recommendation": "Use moving average trends to make decisions on inventory flow and logistics staffing levels."
    },
    "query_36": {
        "name": "Coupon Utilization Rate & Revenue Impact",
        "sql": "SELECT CouponCode, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS GrossRevenue, ROUND(AVG(TotalPrice), 2) AS AOV FROM orders GROUP BY CouponCode ORDER BY OrderCount DESC;",
        "problem_statement": "Evaluate the utilization frequency and financial impact of coupon codes.",
        "business_insight": "Understanding how often coupons are used helps evaluate the promotional mix and margin impacts.",
        "recommendation": "Align coupon policies to protect margins, limiting deeper discounts (like 15%) to specific clearance periods."
    },
    "query_37": {
        "name": "Acquisition Revenue by Referral Source",
        "sql": "SELECT ReferralSource, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS TotalRevenue, ROUND(AVG(TotalPrice), 2) AS AverageOrderValue FROM orders GROUP BY ReferralSource ORDER BY TotalRevenue DESC;",
        "problem_statement": "Compare the customer acquisition volume and total revenue generated across traffic channels.",
        "business_insight": "Referrals and Google search optimization represent highly cost-effective growth, while paid channels (Facebook/Instagram) must be audited for ROAS.",
        "recommendation": "Optimize search engine rankings (SEO) and email lists to capture high-value customer segments."
    },
    "query_38": {
        "name": "Coupon Performance Matrix",
        "sql": "SELECT CouponCode, COUNT(OrderID) AS TotalOrders, ROUND(SUM(TotalPrice), 2) AS TotalRevenue, ROUND(AVG(ItemsInCart), 1) AS AvgItemsInCart FROM orders GROUP BY CouponCode ORDER BY TotalRevenue DESC;",
        "problem_statement": "Analyze coupon code performance in terms of order volume, revenue, and cart sizes.",
        "business_insight": "Coupons like SAVE10 and WINTER15 drive transaction velocity and encourage customers to add more items to their carts.",
        "recommendation": "Use coupon thresholds (e.g. 'Use WINTER15 on orders above $1000') to boost average order value."
    },
    "query_39": {
        "name": "Coupon Discount Analysis (JOIN)",
        "sql": "SELECT o.OrderID, o.CouponCode, c.DiscountPercent, o.TotalPrice AS GrossPrice, ROUND(o.TotalPrice * c.DiscountPercent, 2) AS DiscountSaved, ROUND(o.TotalPrice * (1.0 - c.DiscountPercent), 2) AS NetPrice FROM orders o JOIN coupons c ON o.CouponCode = c.CouponCode WHERE o.CouponCode != 'NONE' ORDER BY DiscountSaved DESC LIMIT 10;",
        "problem_statement": "Calculate the dollar amount saved by customers and the net revenue received by the store after coupon discounts.",
        "business_insight": "This JOIN query showcases the direct cost of promotions. Discount savings can exceed $300 on high-value orders, impacting gross margins.",
        "recommendation": "Cap maximum absolute discounts on high-ticket items to prevent margin erosion during major discount campaigns."
    },
    "query_40": {
        "name": "Instagram High-Value Orders (WHERE, JOIN)",
        "sql": "SELECT o.OrderID, o.CustomerID, o.Product, o.TotalPrice, c.DiscountPercent FROM orders o JOIN coupons c ON o.CouponCode = c.CouponCode WHERE o.ReferralSource = 'Instagram' AND o.TotalPrice > 1500 ORDER BY o.TotalPrice DESC;",
        "problem_statement": "Find high-value orders (above $1,500) that were acquired through Instagram marketing.",
        "business_insight": "Instagram traffic is capable of converting into high-ticket sales, contradicting assumptions that social media is only for small-value impulses.",
        "recommendation": "Increase influencer sponsorships and run targeted ads for premium electronics on Instagram."
    },
    "query_41": {
        "name": "Month-over-Month Revenue Growth (CTEs & LAG)",
        "sql": "WITH MonthlySales AS (SELECT strftime('%Y-%m', Date) AS Month, ROUND(SUM(TotalPrice), 2) AS Revenue FROM orders GROUP BY Month) SELECT Month, Revenue, LAG(Revenue, 1) OVER (ORDER BY Month) AS PreviousMonthRevenue, ROUND(((Revenue - LAG(Revenue, 1) OVER (ORDER BY Month)) * 100.0) / LAG(Revenue, 1) OVER (ORDER BY Month), 2) AS MoM_GrowthPercent FROM MonthlySales;",
        "problem_statement": "Calculate the Month-over-Month (MoM) revenue growth percentage to evaluate business momentum.",
        "business_insight": "MoM growth reveals rapid acceleration or slowdown, highlighting the immediate effectiveness of seasonal campaigns or product launches.",
        "recommendation": "Analyze operations during months with negative growth to identify and address bottlenecks in marketing or inventory."
    },
    "query_42": {
        "name": "Shipping Address and Tracking Audit (String Functions)",
        "sql": "SELECT OrderID, ShippingAddress, SUBSTR(ShippingAddress, 1, INSTR(ShippingAddress, ' ') - 1) AS StreetNumber, SUBSTR(ShippingAddress, INSTR(ShippingAddress, ' ') + 1) AS StreetName, TrackingNumber, LENGTH(TrackingNumber) AS TrackingNumLength FROM orders LIMIT 5;",
        "problem_statement": "Audit the shipping address format and verify tracking number character lengths using string parsing.",
        "business_insight": "String functions parse structured data (like addresses and tracking numbers), enabling data validation and integration audits.",
        "recommendation": "Use these validation checks to ensure address formatting is correct before exporting label files to carriers."
    },
    "query_43": {
        "name": "Tracking Number Prefix Analysis",
        "sql": "SELECT SUBSTR(TrackingNumber, 1, 4) AS TrackingPrefix, COUNT(OrderID) AS OrderCount, ROUND(SUM(TotalPrice), 2) AS Revenue FROM orders GROUP BY TrackingPrefix ORDER BY OrderCount DESC;",
        "problem_statement": "Analyze tracking number prefixes to identify carrier distribution and volumes.",
        "business_insight": "Tracking number prefixes often map to different fulfillment hubs or specific regional carriers.",
        "recommendation": "Monitor carrier performance and shipping costs across these prefixes to optimize logistics routing."
    },
    "query_44": {
        "name": "Customer Segmentation Summary (CTEs & CASE)",
        "sql": "WITH CustSpend AS (SELECT CustomerID, SUM(TotalPrice) AS TotalSpent FROM orders GROUP BY CustomerID) SELECT CASE WHEN TotalSpent >= 3000 THEN 'VIP / High Value' WHEN TotalSpent BETWEEN 1000 AND 2999.99 THEN 'Mid Tier' ELSE 'Low Tier' END AS CustomerSegment, COUNT(CustomerID) AS CustomerCount, ROUND(SUM(TotalSpent), 2) AS SegmentRevenue, ROUND(AVG(TotalSpent), 2) AS AvgCustomerSpend FROM CustSpend GROUP BY CustomerSegment ORDER BY SegmentRevenue DESC;",
        "problem_statement": "Summarize customer counts, total revenue, and average spend for each customer segment.",
        "business_insight": "VIP customers generate a disproportionate share of total revenue relative to their headcount. Keeping VIPs active is highly profitable.",
        "recommendation": "Design personalized loyalty campaigns and offer premium perks to retain VIPs and incentivize Mid Tier customer upgrades."
    },
    "query_45": {
        "name": "Query the Product Performance View",
        "sql": "SELECT Product, TotalOrders, TotalQuantitySold, RevenueGenerated FROM vw_product_performance ORDER BY RevenueGenerated DESC;",
        "problem_statement": "Query the pre-defined product performance view to quickly check high-level sales data.",
        "business_insight": "Database views simplify complex queries, providing secure and standard access to business metrics for reporting.",
        "recommendation": "Expose this view to product managers so they can easily monitor category sales without writing raw SQL."
    },
    "query_46": {
        "name": "Query Performance Audit with Indexes",
        "sql": "SELECT o.OrderID, o.CustomerID, o.TotalPrice, o.Date FROM orders o WHERE o.CustomerID = 'C72649' AND o.Date > '2023-01-01';",
        "problem_statement": "Run an audited query on CustomerID and Date to check indexing efficiency.",
        "business_insight": "Indexes on CustomerID and Date speed up lookups, reducing query latency as the database grows.",
        "recommendation": "Maintain database indexes on all frequently-queried columns to ensure quick dashboard load times."
    }
}
