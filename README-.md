# Project Documentation

## Repository Overview
This repository contains a set of Python scripts for various functionalities. Below is an overview of the scripts and their purposes.

## generate_test_data.py
Creates a file with random content.

### create_random_file
Creates a file with random content.

### generate_test_data
Creates test data with a parent directory, files, and subdirectories.

## directory_inventory.py
Generate MD5 hash of a file without modifying it.

### get_md5_hash
Generate MD5 hash of a file without modifying it.

### get_file_info
Walk through directories and collect file inventory for forensic analysis.

## directory_inventory.original.py
Generate MD5 hash of a file.

### get_md5_hash
Generate MD5 hash of a file.

### get_file_info
Walk through directories and collect file inventory.

## generate_readme.py
Extracts module-level docstrings and function docstrings.

### extract_docstrings
Extracts module-level docstrings and function docstrings.

### generate_readme
Generates a README.md file based on Python scripts in the repository.

## dashboard.py
Loads the latest inventory CSV file from the output directory.

### load_latest_inventory
Loads the latest inventory CSV file from the output directory.

## How to Run
Follow these steps to execute the scripts:

1. Install dependencies (if any) using:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the desired script using:

    ```bash
    python script_name.py
    ```

