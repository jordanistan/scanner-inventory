import os
import hashlib
import csv
import time
from datetime import datetime


def get_md5_hash(file_path):
    """Generate MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        return f"Error: {e}"


def get_file_info(root_dir, output_csv):
    """Walk through directories and collect file inventory."""
    inventory = []
    
    for root, _, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                stats = os.stat(file_path)
                created_time = datetime.fromtimestamp(stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
                modified_time = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                file_size = stats.st_size  # Size in bytes
                md5_hash = get_md5_hash(file_path)
                
                inventory.append([file, created_time, modified_time, file_size, md5_hash, file_path])
            except Exception as e:
                inventory.append([file, "Error", "Error", "Error", "Error", f"Error retrieving file: {e}"])

    # Write to CSV
    with open(output_csv, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Item Name", "Date Created", "Date Modified", "File Size (Bytes)", "MD5 Hash", "File Path"])
        writer.writerows(inventory)
    
    print(f"Inventory saved to {output_csv}")


if __name__ == "__main__":
    directory_to_scan = input("Enter the directory to scan: ")
    output_csv_file = "directory_inventory.csv"
    get_file_info(directory_to_scan, output_csv_file)
