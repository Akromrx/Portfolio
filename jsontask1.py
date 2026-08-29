import json
py_dict = json.loads('[{"name":"Alice","score":90},{"name":"Bob","score":65},{"name":"Zara","score":88},{"name":"Ivan","score":72}]')
print([i["name"] if i["score"] >= 80 else pass for i in py_dict])