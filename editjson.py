import json

fp = "Advanced python/data1.json"

with open(fp, "r", encoding="utf-8") as f:
    config = json.load(f)

new_Student = {
    "name": "Alan",
    "gpa": 86,
    "major": "Geschaftsmann"
}
config["students"].append(new_Student)
config["Author"] = "Akrom"

with open(fp, "w", encoding="utf-8") as f:
    json.dump(config, f, indent=8)