# def make_count():
#     x = 0

#     def count():
#         nonlocal x
#         # global x: int
#         x += 1 
#         return x
    
#     return count

# f = make_count()
# print(f())
# print(f())
# print(f())

funcs = []

for i in range(3):
    def f(i=i):
        print(i)
    funcs.append(f)

funcs[0]()
funcs[1]()
funcs[2]()