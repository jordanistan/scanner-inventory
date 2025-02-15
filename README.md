
<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Scanner Inventory" />

  &#xa0;
</div>

<h1 align="center">Scanner Inventory</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/jordanistan/scanner-inventory?color=56BEB8">
  <img alt="Github language count" src="https://img.shields.io/github/languages/count/jordanistan/scanner-inventory?color=56BEB8">
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/jordanistan/scanner-inventory?color=56BEB8">
  <img alt="License" src="https://img.shields.io/github/license/jordanistan/scanner-inventory?color=56BEB8">
</p>

## :dart: About ##

This repository contains a Python-based scanner inventory system that catalogs files and directories, capturing metadata including timestamps, file sizes, and MD5 hashes for forensic analysis.

## :sparkles: Features ##

:heavy_check_mark: Scans directories for file metadata;
:heavy_check_mark: Generates CSV reports;
:heavy_check_mark: Detects duplicate files based on MD5 hashes.

## :rocket: Technologies ##

The following tools were used in this project:
- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, ensure you have Python installed.

## :checkered_flag: Starting ##

```bash
# Clone this project
git clone https://github.com/jordanistan/scanner-inventory

# Access
test cd scanner-inventory

# Install dependencies
pip install -r requirements.txt

# Run the scanner
python scanner.py

# Run the dashboard
streamlit run dashboard.py --server.address=0.0.0.0 --server.port=8501
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE.md) file.

Made with :heart: by <a href="https://github.com/jordanistan" target="_blank">jordan</a>

&#xa0;

<a href="#top">Back to top</a>
