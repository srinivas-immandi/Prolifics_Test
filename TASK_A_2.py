import re

file_path = r"C:\Users\ABC\Downloads\library_records.txt"

with open(file_path, "r") as f:
    lines = f.readlines()

# Match lines like: SECTION 1: MEMBER REGISTRY
pattern = r'^SECTION\s+\d+:\s+.*$'

section_headers = []
for line in lines:
    line = line.strip()
    if re.match(pattern, line):
        section_headers.append(line)

print("Section Headers:")
for i, header in enumerate(section_headers, start=1):
    print(f"{i}. {header}")

