from datetime import datetime
import os

def generate_log(data):
    # TODO: Implement log generation logic

    # STEP 1: Validate input
    if not isinstance(data, list):
        raise TypeError("data must be a list of strings")
    if not all(isinstance(entry, str) for entry in data):
        raise ValueError("All entries in data must be strings")

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    today_str = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today_str}.txt"
    

    # STEP 3: Write the log entries to a file using File I/O
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename
    print(f"Log written to {filename}")
