import os
import shutil

# Define the source and destination paths
source_path = 'data/'
destination_path = 'map/'

# Find and move all *.geojson files
for root, dirs, files in os.walk(source_path):
    for file in files:
        if file.endswith('.geojson'):
            filepath = os.path.join(root, file)
            shutil.move(filepath, destination_path)
            print(f"Moved {file} to {destination_path}")
