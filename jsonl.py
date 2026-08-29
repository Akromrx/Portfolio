import json

with open("Advanced python/data1.json", "r") as f:
    data = json.load(f)
print(data["students"])
print([u["gpa"] for u in data["students"]])
print([u for u in data["students"]])

ranked = list(sorted(data["students"], key=lambda x: x["gpa"], reverse=True))
print(ranked)