from datetime import datetime
import csv

with open("log.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Script eseguito", datetime.utcnow()])

print("Script eseguito!")
