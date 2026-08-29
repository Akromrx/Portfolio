import copy

# a = [[1, 2], [3, 4]]
# b = a.copy()

# b[0].append(99) # a changes because a is a nested object and shallow copy only copies outer list
# # fix:
# # b = copy.deepcopy(a)

# print("a:", a)
# print("b:", b)

# def add_item(lst):
#     new = copy.deepcopy(lst)
#     new.append("BUG")
#     return new

# my_list = ["OK"]
# add_item(my_list)

# print(my_list)

# matrix = [[0] * 3] * 3
# matrix[1][1] = 1

# print(matrix) # This happens because 0 is immutable while the inner lists ([0, 0, 0]) are mutable

# user = {
#     "name": "Alex",
#     "skills": ["Python", "Git"]
# }

# backup = user.copy()
# backup["skills"].append("Docker")

# print(user)
# print(backup)

# a = [[1]]
# b = a[:]
# print(b)
# print(a is b)
# print(a[0] is b[0])

a = [[1, 2, 3], [4, 5, 6]]
b = a[0]
a[0].insert(0, 0)
print(b)
print(a)