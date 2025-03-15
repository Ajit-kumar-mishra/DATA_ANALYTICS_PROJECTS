--select * from customers_table
/*select count(*) from customers_table
where gender = 'Male';*/
/*select count(*)  - (select count(*) from customers_table where gender = 'Male')as differences
from customers_table*/

--select * from products_table
/*select product_name,category from products_table
where category = 'Electronics'*/

--select * from orders_table
/*select order_id,customer_id from orders_table
where orders_table.customer_id = 1*/

/*select orders_table.order_id,orders_table.customer_id,orderdetails_table.product_id,products_table.product_name,orders_table.orderdate
from orders_table
join orderdetails_table on orders_table.order_id = orderdetails_table.order_id
join products_table on orderdetails_table.product_id = products_table.product_id
where orders_table.customer_id = 1
order by orders_table.orderdate asc;*/

--select count(order_id) from orders_table

--select avg(rating),max(rating),min(rating) from reviews_table

/*select reviews_table.product_id,products_table.product_name,round(avg(reviews_table.rating),2) as average_rating from reviews_table
join products_table on reviews_table.product_id = products_table.product_id
group by reviews_table.product_id, products_table.product_name
order by reviews_table.product_id*/

/*SELECT 
    products_table.product_id,
    products_table.product_name
FROM 
    products_table
JOIN 
    orderdetails_table ON products_table.product_id = orderdetails_table.product_id
GROUP BY 
    products_table.product_id, products_table.product_name
ORDER BY 
    products_table.product_id;*/
	
/*select customers_table.first_name,customers_table.last_name,orders_table.customer_id,sum(orderdetails_table.totalprice) as total_sales_amount
from orders_table
join orderdetails_table on orders_table.order_id = orderdetails_table.order_id
join customers_table on orders_table.customer_id = customers_table.customer_id
group by orders_table.customer_id, customers_table.first_name,customers_table.last_name
order by customer_id asc*/

/*select rating from reviews_table
order by rating desc
limit 5*/

/*select customer_id,first_name,last_name,country,state_name,area from customers_table
where country = 'India' and state_name = 'Maharashtra'*/

/*select products_table.product_id,products_table.product_name from products_table
join orderdetails_table on orderdetails_table.product_id = products_table.product_id
group by products_table.product_id,products_table.product_name
order by products_table.product_id*/

/*SELECT 
    customers_table.customer_id,
    customers_table.first_name,
    customers_table.last_name,
    products_table.product_id,
    products_table.product_name
FROM 
    customers_table
JOIN 
    orders_table ON customers_table.customer_id = orders_table.customer_id
JOIN 
    orderdetails_table ON orders_table.order_id = orderdetails_table.order_id
JOIN 
    products_table ON orderdetails_table.product_id = products_table.product_id
ORDER BY 
    customers_table.customer_id, products_table.product_id;
*/

/*select count(order_id),customer_id from orders_table
group by customer_id
order by customer_id asc*/


/*select product_id,sum(quantity) from orderdetails_table
group by product_id
order by product_id asc*/

/* SELECT customer_id, first_name, last_name 
FROM customers_table 
WHERE customer_id NOT IN (SELECT DISTINCT customer_id FROM orders_table);
*/

/*SELECT product_id, product_name 
FROM products_table 
WHERE product_id NOT IN (SELECT DISTINCT product_id FROM reviews_table);*/

/*SELECT product_id, product_name 
FROM products_table 
WHERE product_id NOT IN (SELECT DISTINCT product_id FROM orderdetails_table);*/

/*SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    SUM(od.totalprice) AS total_purchase_amount,
    CASE 
        WHEN SUM(od.totalprice) >= 1000 THEN 'High'
        WHEN SUM(od.totalprice) BETWEEN 500 AND 999 THEN 'Medium'
        ELSE 'Low'
    END AS customer_segment
FROM 
    customers_table AS c
JOIN 
    orders_table AS o ON c.customer_id = o.customer_id
JOIN 
    orderdetails_table AS od ON o.order_id = od.order_id
GROUP BY 
    c.customer_id, c.first_name, c.last_name
ORDER BY 
    customer_id ASC;*/

/*SELECT 
    p.product_id,
    p.product_name,
    SUM(od.quantity * od.unitprice) AS total_sales
FROM 
    products_table AS p
JOIN 
    orderdetails_table AS od ON p.product_id = od.product_id
GROUP BY 
    p.product_id, p.product_name
HAVING 
    SUM(od.quantity * od.unitprice) > 3000  -- Use the SUM directly here
ORDER BY 
    total_sales DESC;
	*/
	
/*SELECT 
    EXTRACT(MONTH FROM orderdate) AS order_month,
    EXTRACT(YEAR FROM orderdate) AS order_year,
    SUM(od.totalprice) AS total_sales
FROM 
    orders_table AS o
JOIN 
    orderdetails_table AS od ON o.order_id = od.order_id
GROUP BY 
    order_year, order_month
ORDER BY 
    order_year, order_month;
	*/
	
/*SELECT 
    first_name,
    last_name,
    email,
    COUNT(*) AS occurrences
FROM 
    customers_table
GROUP BY 
    first_name, last_name, email
HAVING 
    COUNT(*) > 1;  -- Use COUNT(*) directly instead of occurrences
*/

/*SELECT 
    'customers_table' AS table_name, 
    customer_id::TEXT AS id,  -- Cast to TEXT for consistency
    first_name, 
    last_name, 
    email 
FROM 
    customers_table
WHERE 
    customer_id IS NULL OR first_name IS NULL OR last_name IS NULL OR email IS NULL

UNION ALL

SELECT 
    'orders_table' AS table_name, 
    order_id::TEXT AS id,  -- Cast to TEXT for consistency
    customer_id::TEXT AS customer_id,  -- Cast customer_id to TEXT for consistency
    orderdate::TEXT AS orderdate,  -- Cast orderdate to TEXT for consistency
    NULL AS additional_column  -- This should match the data type of the other columns
FROM 
    orders_table
WHERE 
    order_id IS NULL OR customer_id IS NULL OR orderdate IS NULL

UNION ALL

SELECT 
    'orderdetails_table' AS table_name, 
    orderdetailid::TEXT AS id,  -- Cast to TEXT for consistency
    order_id::TEXT AS order_id,  -- Cast order_id to TEXT for consistency
    product_id::TEXT AS product_id,  -- Cast product_id to TEXT for consistency
    quantity::TEXT AS quantity  -- Cast quantity to TEXT for consistency
FROM 
    orderdetails_table
WHERE 
    orderdetailid IS NULL OR order_id IS NULL OR product_id IS NULL OR quantity IS NULL;
*/
SELECT 
    p.product_name,
    SUM(od.quantity) AS frequency_sold
FROM 
    products_table AS p
JOIN 
    orderdetails_table AS od ON p.product_id = od.product_id
GROUP BY 
    p.product_name
ORDER BY 
    frequency_sold DESC;  -- This will order the results by frequency sold in descending order
