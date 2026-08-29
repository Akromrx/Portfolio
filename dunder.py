# class Example:
#     def __init__(self):
#         self.exam = [1, 2, 3]
    
#     def __len__(self): # __len__ method is used to get the lenght of an item
#         return len(self.exam)
    
#     # def __getattribute__(self, i): # __getitem__ method is used to get the i-th item
#     #     return self.exam[i]
    
#     def __setitem(self, i, x): # __setitem method is used to set i-th item to x 
#         self.exam[i] = x
    
#     def __repr__(self):
#         return f"Example(exam: {self.exam})"
    
#     def __str__(self):
#         return f"Example: {self.exam}"
    
# obj = Example()
# # print(len(obj))
# # print(obj[1])

# print(dir(Example))
# print(obj)

class Inventory:
    def __init__(self, items: list):
        self.items = items
    
    def __len__(self): # To return the length of the inventory
        return len(self.items)
    
    def __getitem__(self, i): # To get the item i from the inventiry
        return self.items[i]
    
    def __add__(self, new): # To add new items to the inventory
        return self.items.extend(new)
    
    def __str__(self): # To show the items within the inventory
        return f"Inventory has:\n{self.items}"
    
    def __bool__(self, item): # To check whether an item is in the inventory or not
        if item in self.items:
            return 1
        return -1

I1: Inventory = Inventory(['Gun', 'Bread x5', 't-Shirt'])
print(len(I1))
print(I1[2])
I1 + ['Kit', 'Rock']
print(I1)
print('Watch' in I1)

