import zipfile
import os
from pathlib import Path


zip_path = "/content/drive/My Drive/THESIS/3D/BdSL.zip"



extract_path = '/content/drive/MyDrive/THESIS/3D/Data_BdSL47'


os.makedirs(extract_path, exist_ok=True)

print("Extracting 3D sign language dataset...")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
print("✅ Extraction complete!")


csv_files = list(Path(extract_path).glob('**/*.csv')) + list(Path(extract_path).glob('**/*.CSV'))
print(f"Found {len(csv_files)} CSV files with 3D coordinate data")
