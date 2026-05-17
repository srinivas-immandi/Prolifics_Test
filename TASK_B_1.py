# email

import re

file_path = r"C:\Users\ABC\Downloads\library_records.txt"

with open(file_path, "r") as f:
    content = f.read()


pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'


emails = re.findall(pattern, content)


unique_emails = sorted(set(emails))

print("Unique Email Addresses:\n")

for i, email in enumerate(unique_emails, start=1):
    print(f"{i}. {email}")