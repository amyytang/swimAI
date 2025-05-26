import os
import pandas as pd

# Load filtered CSV
df = pd.read_csv("Filtered_Sheet.csv")
df = df[df["Stroke"] != "x"]
valid_paths = df["Filename"].dropna().tolist()  # e.g., backstroke swimming race/Image_1

# Convert to lowercase and set for lookup
valid_base_names = set(p.lower() for p in valid_paths)

# Root image folder
base_dir = "swimming_dataset"

# Go through all stroke subfolders
for folder_name in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder_name)
    if not os.path.isdir(folder_path):
        continue
    for filename in os.listdir(folder_path):
        file_base, ext = os.path.splitext(filename)
        full_key = f"{folder_name}/{file_base}".lower()
        if full_key not in valid_base_names:
            file_to_remove = os.path.join(folder_path, filename)
            os.remove(file_to_remove)
            print(f"Deleted: {file_to_remove}")
