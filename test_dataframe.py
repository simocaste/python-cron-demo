import pandas as pd

# Creazione del DataFrame
data = {
    "top_adunit": ["corriere.it"],
    "impressions": [1000]
}

df = pd.DataFrame(data)

# Scrittura su CSV
df.to_csv("adunits.csv", index=False)

print("CSV creato con successo!")
