import os
import hashlib
import csv
import readline
from datetime import datetime


def get_md5_hash(file_path):
    """Generate MD5 hash of a file without modifying it."""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        return f"Error: {e}"


def get_file_info(root_dir, output_csv):
    """Walk through directories and collect file inventory for forensic analysis."""
    inventory = []
    
    for root, _, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                stats = os.stat(file_path, follow_symlinks=False)  # Avoid modifying symlinks
                created_time = datetime.fromtimestamp(stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
                modified_time = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                file_size = stats.st_size  # Size in bytes
                md5_hash = get_md5_hash(file_path)
                
                inventory.append([file, created_time, modified_time, file_size, md5_hash, file_path])
            except Exception as e:
                inventory.append([file, "Error", "Error", "Error", "Error", f"Error retrieving file: {e}"])

    # Ensure output directory exists
    output_dir = os.path.join(os.getcwd(), "output")
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate timestamped output filename
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    output_csv = os.path.join(output_dir, f"directory_inventory_{timestamp}.csv")
    
    # Write to CSV without modifying the files
    with open(output_csv, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Item Name", "Date Created", "Date Modified", "File Size (Bytes)", "MD5 Hash", "File Path"])
        writer.writerows(inventory)
    
    print(f"Inventory saved to {output_csv}")


if __name__ == "__main__":
    default_dir = os.getcwd()
    readline.set_startup_hook(lambda: readline.insert_text(default_dir))  # Auto-suggest current directory
    directory_to_scan = input("Enter the directory to scan (default is current directory): ") or default_dir
    get_file_info(directory_to_scan, None)

