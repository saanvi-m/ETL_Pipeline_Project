import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# ==========================================
# Phase 1: EXTRACT (Get Data from Free API)
# ==========================================
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"
response = requests.get(url)
api_data = response.json()

# ==========================================
# Phase 2: TRANSFORM (Clean with Pandas)
# ==========================================
# Convert the messy JSON dictionary into a flat Pandas DataFrame
df = pd.DataFrame(api_data).T
df.reset_index(inplace=True)

# Rename the columns so they look like a clean SQL table
df.columns = ["crypto_name", "price_usd"]

# Add a timestamp so we know exactly when this price was captured
df['timestamp'] = datetime.now()

print("Data Extracted & Cleaned Successfully:")
print(df)

# ==========================================
# Phase 3: LOAD (Push to Supabase database)
# ==========================================
# WARNING: Replace this string with YOUR exact Supabase Connection URI!
DB_URL = "postgresql://postgres.vhoszwvkwqkuvmlwjcow:ERL_Portfoli@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres"

# Create a connection engine to the database
engine = create_engine(DB_URL)

try:
    # Push the dataframe directly into a new SQL table called 'crypto_prices'
    # if_exists='append' ensures that every time the script runs, it adds new rows!
    df.to_sql('crypto_prices', engine, if_exists='append', index=False)
    print("SUCCESS: New data loaded into Supabase PostgreSQL!")
except Exception as e:
    print(f"Error loading data: {e}")
