
import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect('../data/berlin_airbnb.db')

print("=== BERLIN AIRBNB ANALYSIS ===\n")

# Basic stats
query1 = "SELECT COUNT(*) as total_listings FROM listings WHERE price_cleaned > 0"
result1 = pd.read_sql_query(query1, conn)
print(f"Total listings with valid prices: {result1['total_listings'].iloc[0]:,}")

# Average price
query2 = "SELECT ROUND(AVG(price_cleaned), 2) as avg_price FROM listings WHERE price_cleaned > 0"
result2 = pd.read_sql_query(query2, conn)
print(f"Average price per night: €{result2['avg_price'].iloc[0]}")

# Most expensive neighborhoods
query3 = """
SELECT neighbourhood_cleansed, 
       COUNT(*) as count,
       ROUND(AVG(price_cleaned), 2) as avg_price
FROM listings 
WHERE price_cleaned > 0 
GROUP BY neighbourhood_cleansed 
ORDER BY avg_price DESC 
LIMIT 5
"""
result3 = pd.read_sql_query(query3, conn)
print("\nTop 5 most expensive neighborhoods:")
print(result3.to_string(index=False))

conn.close()
print("\nAnalysis complete!")
