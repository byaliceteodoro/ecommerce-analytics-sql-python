SELECT 
    YEAR(created_at) AS ano,
    MONTH(created_at) AS mes,
    SUM(price_usd) AS receita
FROM order_items
GROUP BY YEAR(created_at), MONTH(created_at)
ORDER BY ano, mes;

SELECT 
    p.product_name,
    COUNT(*) AS total_vendido
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_vendido DESC;

SELECT 
    COUNT(DISTINCT o.order_id) * 1.0 /
    COUNT(DISTINCT ws.website_session_id) AS conversao
FROM website_sessions ws
LEFT JOIN orders o
    ON ws.website_session_id = o.website_session_id;

-- Top 5 produtos
SELECT TOP 5 
    p.product_name,
    COUNT(*) AS total_vendido
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_vendido DESC;
