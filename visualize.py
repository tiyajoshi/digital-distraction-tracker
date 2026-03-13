import json
import os
import matplotlib.pyplot as plt
from collections import defaultdict

DATA_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def show_graphs():
    tasks = load_tasks()

    if not tasks:
        print("No tasks tracked yet!")
        return

    dates = defaultdict(lambda: {"productive": 0, "distracting": 0})

    for t in tasks:
        date = t["date"].split(" ")[0]
        dates[date][t["type"]] += t["minutes"]

    sorted_dates = sorted(dates.keys())
    productive = [dates[d]["productive"] for d in sorted_dates]
    distracting = [dates[d]["distracting"] for d in sorted_dates]

    x = range(len(sorted_dates))

    plt.figure(figsize=(10, 5))
    plt.bar(x, productive, width=0.4, label="Productive", color="green", align="center")
    plt.bar([i + 0.4 for i in x], distracting, width=0.4, label="Distracting", color="red", align="center")
    plt.xticks([i + 0.2 for i in x], sorted_dates, rotation=45)
    plt.xlabel("Date")
    plt.ylabel("Minutes")
    plt.title("Your Productivity Over Time")
    plt.legend()
    plt.tight_layout()
    plt.show()

show_graphs()