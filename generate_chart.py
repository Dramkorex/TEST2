import pandas as pd
import matplotlib.pyplot as plt

# Wczytaj dane
data = pd.read_csv("data.csv")

# Tworzymy wykres
plt.figure(figsize=(8,5))
plt.plot(data["date"], data["value"], marker="o", linestyle="-", label="Value")
plt.xlabel("Date")
plt.ylabel("Value")
plt.title("Example CSV Chart")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Zapis do pliku PNG
plt.savefig("chart.png")
