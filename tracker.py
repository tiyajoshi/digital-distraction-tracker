import time

tasks = []

def track_task():
    task_name = input("What are you working on? ")
    task_type = input("Is this productive or distracting? (p/d): ")
    
    print("Tracking... press Enter when you stop.")
    input("Press Enter to start...")
    start = time.time()
    input("Press Enter to stop...")
    end = time.time()
    
    duration = round((end - start) / 60, 2)
    
    tasks.append({
        "task": task_name,
        "type": "productive" if task_type == "p" else "distracting",
        "minutes": duration
    })
    
    print(f"You spent {duration} minutes on {task_name}")

def show_summary():
    productive = sum(t["minutes"] for t in tasks if t["type"] == "productive")
    distracting = sum(t["minutes"] for t in tasks if t["type"] == "distracting")
    
    print("\\n--- Your Summary ---")
    print(f"Productive minutes: {productive}")
    print(f"Distracting minutes: {distracting}")

while True:
    print("\\n1. Track a task")
    print("2. Show summary")
    print("3. Quit")
    choice = input("Choose: ")
    
    if choice == "1":
        track_task()
    elif choice == "2":
        show_summary()
    elif choice == "3":
        break