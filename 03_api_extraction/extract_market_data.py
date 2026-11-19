import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "inr",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

response = requests.get(url, params=params, timeout=10)
response.raise_for_status()
data = response.json()

records = [
    {
        "rank": item["market_cap_rank"],
        "symbol": item["symbol"].upper(),
        "name": item["name"],
        "current_price_inr": item["current_price"],
        "market_cap_inr": item["market_cap"],
        "total_volume_24h": item["total_volume"],
        "price_change_pct_24h": round(item["price_change_percentage_24h"] or 0, 2)
    }
    for item in data
]

df = pd.DataFrame(records)
df.to_csv("market_data_output.csv", index=False)
print("Saved market_data_output.csv successfully!\n")
print(df)