-- ==================================================
-- Marketing Campaign Analysis
-- Author: Layla
-- Database: PostgreSQL 17
-- ==================================================

-- ==================================================
-- 1. DATA EXPLORATION
-- ==================================================

-- Question 1: Total Dataset Overview (Row count, Min, Max, and Avg Income)


    SELECT
    COUNT(*) AS total_customers,
    MIN(income) AS minimum_income,
    MAX(income) AS maximum_income,
    ROUND(AVG(income), 2) AS overall_avg_income,

    -- Average income excluding the extreme outlier ($666,666) for accurate business insights

    ROUND(AVG(CASE WHEN income < 600000 THEN income END), 2) AS adjusted_avg_income
    FROM marketing_campaign;



-- Question 2: Preview top 10 rows of the dataset
    SELECT *
    FROM marketing_campaign
    LIMIT 10;


-- ==================================================
-- 2. CUSTOMER PROFILE ANALYSIS
-- ==================================================

-- Question 3: Customer Breakdown & Average Income by Education Level
    SELECT
    education,
    COUNT(*) AS total_customers,
    ROUND(AVG(income), 2) AS average_income
    FROM marketing_campaign
    GROUP BY education
    ORDER BY total_customers DESC;

-- Question 4: Customer Breakdown & Average Income by Marital Status
    SELECT
    marital_status,
    COUNT(*) AS total_customers,
    ROUND(AVG(income), 2) AS average_income
    FROM marketing_campaign
    GROUP BY marital_status
    ORDER BY total_customers DESC;


-- ==================================================
-- 3. CUSTOMER BEHAVIOR & SEGMENTATION
-- ==================================================

-- Question 5:  Average purchases by channel
SELECT
ROUND(AVG(numwebpurchases), 2) AS avg_web_purchases,
ROUND(AVG(numstorepurchases), 2) AS avg_store_purchases,
ROUND(AVG(numcatalogpurchases), 2) AS avg_catalog_purchases
FROM marketing_campaign;



-- Question 6: Customer Distribution by Income segment
    SELECT
    CASE
    WHEN income >= 80000 THEN 'High Income'
    WHEN income >= 40000 THEN 'Medium Income'
    ELSE'Low Income'
    END AS income_group,

    count(*) AS total_customers,
    ROUND(Avg (income),2) AS average_income

    FROM marketing_campaign
    WHERE income IS NOT NULL
    GROUP BY income_group
    ORDER BY average_income DESC;
 

--Question 7: Customer Purchase Frequency 

    SELECT 
    ROUND(AVG(numdealspurchases),2) AS avg_discount_purchases,

    ROUND(AVG(numwebpurchases),2) AS avg_web_purchases,

    ROUND(AVG(numcatalogpurchases),2) AS avg_catalog_purchases,

    ROUND(AVG(numstorepurchases),2) AS avg_store_purchases
    
    FROM marketing_campaign;


--Question 8 : Marketing Campaign Response Rate

SELECT

COUNT(*) AS total_customers,

SUM(response) AS accepted_campaign,

ROUND(100.0 * SUM (response)/ COUNT(*),2)
 AS response_rate

FROM marketing_campaign;




--Question 9: Total purchases by Channel 

    SELECT
    'web purchases' AS purchase_channel,
    SUM(numwebpurchases) AS total_purchases

    FROM marketing_campaign
    UNION ALL

    SELECT

    'store purchases' ,
    SUM(numstorepurchases) 

    FROM marketing_campaign
    UNION ALL

    SELECT
    'catalog purchases' ,
    SUM(numcatalogpurchases) 

    FROM marketing_campaign

    ORDER BY total_purchases DESC





--Question 10: Customers With vs Without Children

    SELECT
    CASE
    WHEN kidhome + teenhome = 0 THEN 'No Children'
    ELSE 'Has Children'
    END AS family_type,

    COUNT (*) AS total_customers,
    ROUND (avg(income),2) AS average_income 

    FROM marketing_campaign 
    GROUP BY family_type;





--Question 11: Top 10 Highest Spending Customers 

SELECT
 id,
 income,
 (
    mntwines +
    mntfruits +
    mntmeatproducts +
    mntfishproducts +
    mntsweetproducts +
    mntgoldprods 
 ) AS total_spending 
 FROM marketing_campaign
 ORDER BY total_spending DESC
 LIMIT 10;



 --Question 12:Campaign Response  vs Online Customer Behavior

    SELECT 
    response AS campaign_response,
    ROUND(AVG(numwebvisitsmonth),2) AS average_web_visits,
    ROUND(AVG(numwebpurchases),2) AS average_web_purchases
    FROM marketing_campaign
    GROUP BY response
    ORDER BY response;
    
   