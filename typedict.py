from typing import TypedDict

class User(TypedDict):
    name: str
    age: int

exm: User = {'name': 'Akrom'}
# exm['age'] = 'fifteen'
print(exm)