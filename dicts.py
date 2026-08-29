d = {"x": 5, "y": 7, "z": 10}
c = {"s": 2, "f": 1}
d.update(c)
print(d)
print(d.setdefault("z"))