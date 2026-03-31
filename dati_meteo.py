import pandas as pd
import requests
from datetime import datetime

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
data = requests.get(url).json()

price = data["bpi"]["USD"]["rate_float"]

df = pd.DataFrame({
    "timestamp": [datetime.utcnow()],
    "btc_price": [price]
})

df.to_csv("btc_price.csv", index=False)
