# list1 = [1, 2, 3, 4]

# print(list1)

# list1.append(5)
# print(list1)

# list1.insert(0, 0)
# print(list1)

exmtuple = ([1, 2, 3], 'Hello World')
print(exmtuple)

exmtuple[0].insert(0, 0)
exmtuple[0][2] = 4
print(exmtuple)

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(id(x), id(y))
print(x is y)
print(x == y)
print(x == z)
print(x is z)