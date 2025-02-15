import os
import random
import string


def create_random_file(file_path, size_kb=1):
    """Creates a file with random content."""
    with open(file_path, 'w') as f:
        f.write(''.join(random.choices(string.ascii_letters + string.digits, k=size_kb * 1024)))


def generate_test_data(base_dir="test-data"):
    """Creates test data with a parent directory, files, and subdirectories."""
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # Create 10 files in the parent directory
    for i in range(1, 11):
        file_path = os.path.join(base_dir, f"file_{i}.txt")
        create_random_file(file_path)

    # Create 3 child directories, each with 10 files
    for j in range(1, 4):
        child_dir = os.path.join(base_dir, f"child_folder_{j}")
        os.makedirs(child_dir, exist_ok=True)
        
        for i in range(1, 11):
            file_path = os.path.join(child_dir, f"file_{i}.txt")
            create_random_file(file_path)

    print(f"Test data created in {base_dir}")


if __name__ == "__main__":
    generate_test_data()

