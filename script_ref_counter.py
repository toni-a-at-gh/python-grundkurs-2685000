import sys

# Liste von Zahlen
x = [1, 2, 3]

# Ausgeben der Referenzanzahl
print("Reference count of x:", sys.getrefcount(x))

# del x
# print("Reference count of x:", sys.getrefcount(x))

y = [4, 5, 6]
y.append(x)

# Ausgeben der Referenzanzahl
print(y)
print("Reference count of x:", sys.getrefcount(x))
# Änderen des Wertes von x[0]
y[3][0] = 100
print(f"y: {y}")
print(f"x: {x}")

del y
print("Reference count of x:", sys.getrefcount(x))



