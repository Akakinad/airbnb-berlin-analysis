
import sqlite3
import pandas as pd

# Create database
print("Creating database...")
conn = sqlite3.connect('../data/berlin_airbnb.db')

# Read cleaned data
print("Loading cleaned data...")
listings = pd.read_csv('../data/listings_cleaned.csv')

# Save to database
print("Saving to database...")
listings.to_sql('listings', conn, if_exists='replace', index=False)

# Test the database
print("Testing database...")
result = conn.execute("SELECT COUNT(*) FROM listings").fetchone()
print(f"Database created with {result[0]} listings")

conn.close()
print("Done!")
