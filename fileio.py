from pathlib import Path
import csv


fp = "C:/Data Science/Math/medical_test_data.csv"
# fpe = Path(fp)

# with open(fp, "r", encoding="utf-8") as txtfile:
#     for line in txtfile:
#         line = line.strip()
#         if line: 
#             print(line)

# with open(fp, mode="w", encoding="utf-8") as edit:
#     new_lines = ["First line\n", "Second line"]
#     edit.writelines(new_lines)
    
# with open(fp, "r", encoding="utf-8") as read_file:
#     for i in read_file:
#         print(i)

# with open(fp, mode="rb") as src:
#     data = src.read()
#     print(data)

with open(fp, "r", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    print()
    for i in reader:
        print(i)