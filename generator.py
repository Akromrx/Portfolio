import numpy as np 

def generator(examples):
    for i in examples:
        yield i ** 2

ls = np.arange(1, 10000)
for i in generator(ls):
    print(i)