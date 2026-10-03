from pathlib import Path
import re

# Get the current folder
current_dir = Path.cwd()

print("INCOMPLETE PROBLEMS:")
counter = 0

# Files to exclude
excluded_files = {"FIND_INCOMPLETE.py"}

# Get all files, excluding the scripts
files = [
    f for f in current_dir.iterdir()
    if f.is_file() and f.name not in excluded_files
]

# Get the number from the filename
def get_number(file_path):
    match = re.search(r'\d+', file_path.stem)
    return int(match.group()) if match else float('inf')

# Sort numerically
files.sort(key=get_number)

for file_path in files:
    try:
        content = file_path.read_text(encoding='utf-8')

        # Check if there are any letters
        has_letters = bool(re.search(r'[a-zA-Z]', content))

        if not has_letters:
            print(file_path.name)
            counter += 1

    except Exception:
        pass

print(f"You completed {30-counter}/30 problems ({(30-counter)/30:.2f})")
