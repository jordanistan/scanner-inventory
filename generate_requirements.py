import os
import re
import glob


def generate_requirements(repo_path):
    """Generates a requirements.txt file based on detected imports."""
    requirements = set()
    python_files = glob.glob(os.path.join(repo_path, "*.py"))
    
    for py_file in python_files:
        with open(py_file, "r", encoding="utf-8") as f:
            for line in f:
                match = re.match(r'^(?:import|from)\s+([^\.\s]+)', line)
                if match:
                    requirements.add(match.group(1))
    
    # Remove built-in modules
    common_builtin_modules = {"os", "sys", "re", "datetime", "hashlib", "csv", "glob"}
    filtered_requirements = requirements - common_builtin_modules
    
    requirements_path = os.path.join(repo_path, "requirements.txt")
    with open(requirements_path, "w", encoding="utf-8") as f:
        f.write("\n".join(sorted(filtered_requirements)))
    
    print(f"requirements.txt generated at {requirements_path}")


if __name__ == "__main__":
    repo_directory = os.getcwd()  # Use the current directory as the repo path
    generate_requirements(repo_directory)

