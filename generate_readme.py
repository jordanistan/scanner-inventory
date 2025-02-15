import os
import re
import glob


def extract_docstrings(file_path):
    """Extracts module-level docstrings and function docstrings."""
    docstrings = []
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract module-level docstring
    module_doc = re.findall(r'"""(.*?)"""', content, re.DOTALL)
    if module_doc:
        docstrings.append(module_doc[0].strip())
    
    # Extract function docstrings
    function_docs = re.findall(r'def (\w+)\(.*?\):\s*"""(.*?)"""', content, re.DOTALL)
    for func_name, doc in function_docs:
        docstrings.append(f"### {func_name}\n{doc.strip()}")
    
    return "\n\n".join(docstrings)


def generate_readme(repo_path, github_username, author_name):
    """Generates a README.md file based on Python scripts in the repository."""
    readme_content = f"""
<div align="center" id="top"> 
  <img src="./.github/app.gif" alt="Scanner Inventory" />

  &#xa0;
</div>

<h1 align="center">Scanner Inventory</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/{github_username}/scanner-inventory?color=56BEB8">
  <img alt="Github language count" src="https://img.shields.io/github/languages/count/{github_username}/scanner-inventory?color=56BEB8">
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/{github_username}/scanner-inventory?color=56BEB8">
  <img alt="License" src="https://img.shields.io/github/license/{github_username}/scanner-inventory?color=56BEB8">
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
git clone https://github.com/{github_username}/scanner-inventory

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

Made with :heart: by <a href="https://github.com/{github_username}" target="_blank">{author_name}</a>

&#xa0;

<a href="#top">Back to top</a>
"""

    # Save README.md
    readme_path = os.path.join(repo_path, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print(f"README.md generated at {readme_path}")


if __name__ == "__main__":
    repo_directory = os.getcwd()  # Use the current directory as the repo path
    github_username = input("Enter your GitHub username: ")
    author_name = input("Enter your name: ")
    generate_readme(repo_directory, github_username, author_name)

