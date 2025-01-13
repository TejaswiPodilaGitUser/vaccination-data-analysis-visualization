SELECT 
    c.coverage_id,
    c.year,
    c.coverage_percentage,
    u.region
FROM 
    coverage_data c
JOIN 
    users u ON c.user_id = u.user_id;
