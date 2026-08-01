from pathlib import Path

current_dir = Path.cwd()
current_file = Path(__file__).name

print(f"Files in {current_dir}:")

for filepath in current_dir.iterdir():
    if filepath.name == current_file:
        continue

    print(f"  - {filepath.name}")

    if filepath.is_file():
        # Added errors='ignore' so it won't crash on invalid byte sequences
        try:
            content = filepath.read_text(encoding='utf-8', errors='ignore')
            print(f"    Content: {content}")
        except Exception as e:
            print(f"    Could not read file: {e}")