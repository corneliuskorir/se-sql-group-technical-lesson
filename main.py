import sqlite3
import pandas as pd

conn = sqlite3.connect("data.sqlite")

q = """
SELECT 
    customerNumber,
    COUNT(*) AS number_payments,
    MIN(CAST(amount AS FLOAT)) AS min_purchase,
    MAX(CAST (amount AS FLOAT)) AS max_purchase,
AVG(CAST(amount AS FLOAT)) AS avg_purchase,
SUM(CAST(amount AS FLOAT)) AS total_spent
FROM payments
GROUP BY customerNumber;
"""
cust_count_contry = pd.read_sql(q,conn)

print(cust_count_contry)

conn.close()