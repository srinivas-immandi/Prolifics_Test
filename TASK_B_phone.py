import re

file_path = r"C:\Users\ABC\Downloads\library_records.txt"

with open(file_path, "r") as f:
    content = f.read()

    numbers = re.findall(r"\d{10}","content")

print(content)

print('numbers:',numbers)

for i in numbers:
    print(i)
