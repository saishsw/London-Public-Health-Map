import os
import zipfile

# Define the paths
zip_path = 'data/snow.zip'
extract_path = 'data/'

zip_ref = zipfile.ZipFile(zip_path, 'r')
zip_ref.extractall(extract_path)
zip_ref.close()

# Delete the original .zip file
os.remove(zip_path)

# Brief summary of extracted files
print("Files extracted successfully.")
