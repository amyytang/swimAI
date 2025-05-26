import os
import pandas as pd

# Load Excel file and filter to valid rows
df = pd.read_csv("Filtered_Sheet.csv")
df = df[df["Stroke"] != "x"].dropna(subset=["Filename", "Stroke"])

# Mappings between Excel folder names and real folder names
folder_name_map = {
    "backstroke-swimmming-race": "backstroke swimming race",
    "breastroke-swimmming-race": "breastroke swimming race",
    "butterfly-swimming": "butterfly swimming",
    "freestyle-swimming": "freestyle swimming",
}

# Reverse mapping: stroke → correct folder
label_to_folder = {
    "backstroke": "backstroke swimming race",
    "breastroke": "breastroke swimming race",
    "butterfly": "butterfly swimming",
    "freestlye": "freestyle swimming",
    "freestyle": "freestyle swimming"
}

# Dataset base folder
base_dir = "swimming_dataset"

# Build a lookup of correct stroke for each image (no extension)
correct_locations = {}
for _, row in df.iterrows():
    folder_key, file_base = row["Filename"].split("/")
    correct_stroke = row["Stroke"].strip().lower()
    correct_folder = label_to_folder[correct_stroke]
    correct_locations[file_base.lower()] = correct_folder

# Go through all folders and delete images that don’t belong
for folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder)
    if not os.path.isdir(folder_path):
        continue
    for filename in os.listdir(folder_path):
        file_base, ext = os.path.splitext(filename)
        file_base = file_base.lower()
        correct_folder = correct_locations.get(file_base)
        if correct_folder is None:
            continue  # Not in Excel sheet — already cleaned
        if correct_folder != folder:
            # Delete misplaced image
            to_delete = os.path.join(folder_path, filename)
            os.remove(to_delete)
            print(f"Deleted (wrong folder): {to_delete}")
