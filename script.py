from datetime import datetime

with open("log.txt", "a") as f:
    f.write(f"Script eseguito alle {datetime.utcnow()}\n")

print("Script eseguito!")
