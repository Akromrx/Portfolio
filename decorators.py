# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called.")
#         # print(x)
#         func(*args, **kwargs)
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello(x):
#     print(f"Hello!: {x}")

# say_hello(5)
import random

def my_decorator(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                print(f'Trial: {i+1}')
                x = func(*args, **kwargs)
            except:
                if i == 2:
                    raise
        return x
    return wrapper

@my_decorator
def f():
    z= random.random()
    if z < 0.7:
        raise ValueError("bad luck")
    return "success"

x = f()
print(x)