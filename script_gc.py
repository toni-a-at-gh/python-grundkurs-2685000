import gc

x = 2
del x
print(f"Garbage collector: {gc.collect()} Objekte.")

class Node:
    def __init__(self):
        self.ref = None

obj1 = Node()
obj2 = Node()

# Create a cyclic reference
obj1.ref = obj2
obj2.ref = obj1

print(f"Garbage collector: {gc.collect()} Objekte.")

del obj1
del obj2

collected = gc.collect()
print(f"Garbage collector: {collected} Objekte.")