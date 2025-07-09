
import pandas as pd
import re

def clean_price(price_str):
   if pd.isna(price_str):
       return None
   try:
       cleaned = re.sub(r'[$,]', '', str(price_str))
       return float(cleaned)
   except:
       return None

# Read the data
print("Loading data...")
listings = pd.read_csv('../sources/listings.csv')
print(f"Loaded {len(listings)} listings")

# Clean the price column
if 'price' in listings.columns:
   listings['price_cleaned'] = listings['price'].apply(clean_price)
   print("Price column cleaned")

# Save cleaned data
listings.to_csv('../data/listings_cleaned.csv', index=False)
print("Data saved to ../data/listings_cleaned.csv")
print("Done!")
