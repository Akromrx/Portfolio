# def f(*args):
#     print(type(args))
#     for i in args:
#         print(i)

# f([1, 2, 3, 4], [5, 6, 7, 8])

def f(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for i in kwargs.keys():
        print(f"{i}: {kwargs[i]}")

# f(name="Akrom", age=15, gender="M")
f(1, 2, 3)