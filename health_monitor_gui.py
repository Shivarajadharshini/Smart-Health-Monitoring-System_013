import tkinter as tk
import random
from datetime import datetime

# Flag to control monitoring
monitoring = False

# Function to update values
def update_data():
    global monitoring
    if monitoring:
        heart_rate = random.randint(70, 110)
        spo2 = random.randint(90, 100)
        temperature = round(random.uniform(36.0, 38.0), 1)

        # Update labels with alert colors
        hr_label.config(
            text=f"Heart Rate: {heart_rate} BPM",
            fg="red" if heart_rate > 100 else "black"
        )

        spo2_label.config(
            text=f"SpO2: {spo2} %",
            fg="red" if spo2 < 95 else "black"
        )

        temp_label.config(
            text=f"Temperature: {temperature} °C",
            fg="red" if temperature > 37.5 else "black"
        )

        # Update timestamp
        time_label.config(
            text=f"Last update: {datetime.now().strftime('%H:%M:%S')}"
        )

        # Repeat every 2 seconds
        root.after(2000, update_data)

# Start monitoring
def start_monitoring():
    global monitoring
    monitoring = True
    update_data()

# Stop monitoring
def stop_monitoring():
    global monitoring
    monitoring = False

# Create window
root = tk.Tk()
root.title("Smart Health Monitor")
root.geometry("320x250")

# Title
title = tk.Label(root, text="Health Monitor", font=("Arial", 16))
title.pack(pady=10)

# Labels
hr_label = tk.Label(root, text="Heart Rate: --", font=("Arial", 12))
hr_label.pack()

spo2_label = tk.Label(root, text="SpO2: --", font=("Arial", 12))
spo2_label.pack()

temp_label = tk.Label(root, text="Temperature: --", font=("Arial", 12))
temp_label.pack()

time_label = tk.Label(root, text="Last update: --", font=("Arial", 10))
time_label.pack(pady=5)

# Buttons
start_btn = tk.Button(root, text="Start Monitoring", command=start_monitoring)
start_btn.pack(pady=5)

stop_btn = tk.Button(root, text="Stop Monitoring", command=stop_monitoring)
stop_btn.pack(pady=5)

# Run the application
root.mainloop()
