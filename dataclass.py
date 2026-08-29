from dataclasses import dataclass, field

@dataclass
class Point:
    x: int
    y: list[str] = field(default_factory=list)

    def AddElement(self, val: str):
        self.y.append(val)

p = Point(1, [])
p2 = Point(1, [])
print(p)
p.AddElement('Hello')
print(p.__repr__())
print(p2)