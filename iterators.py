# my_list = [1, 2, 3]
# my_iter = iter(my_list)
# print(my_iter)

# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

squares = (x**2 for x in range(1_000_000))
print(squares)
print(next(squares))