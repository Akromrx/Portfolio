# lc = [i *  j for i in range(1, 4) for j in range(1, 4)]
# print(lc)

# Dict comrehension
names = ['Akrom', 'John', 'Billie', 'Alan', 'Aiden']
grades = [98, 87, 90, 89, 79]

dict1 = {x[0]: x[1] for x in zip(names, grades)}
print(dict1)