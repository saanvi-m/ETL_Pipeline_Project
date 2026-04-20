Crypto Price ETL Pipeline with Power BI Dashboard  

End‑to‑end Data Engineering mini‑project for ETL automation and visual analytics  

---

 Project Objective  
Build a simple, yet scalable ETL pipeline to extract daily cryptocurrency price data, transform it into a structured format, and load it into a database for analysis using Power BI.  

The dashboard tracks price trends and volume patterns across major currencies like Bitcoin, Ethereum, and Solana.

---

 Tech Stack  

| Layer | Tools / Libraries |
|-------|--------------------|
| **Extraction** | Python requests / REST API (call CoinMarketCap or CryptoCompare) |
| **Transformation** | Pandas for cleaning, formatting, and aggregating prices |
| **Loading** | SQLite / PostgreSQL (`to_sql`) for storage |
| **Reporting** | Power BI for visual dashboard and KPIs |
| **Automation** | Python logging + Windows Task Scheduler (optional Cron job) |

---

 Workflow Overview  
1️⃣ Extract: Fetch JSON data from Crypto API → parse fields (price_usd, volume, timestamp)  
2️⃣ Transform: Clean null values, convert timestamps, calculate daily averages  
3️⃣ Load: Write data into SQL table `crypto_prices` for downstream use  
4️⃣ Visualize: Connect Power BI to database → build trend charts, KPIs and filters  
