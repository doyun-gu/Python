# Set Title = {Value1, Value2, ... ValueN}
my_set = {1, 2, 3, 3, 3}
print(my_set)

# Java Version
Java = {"Doyun", "Damian", "GU"}

# Python Version
Python = set(["Doyun", "Kim"])

# '&' or 'Intersection()'
print(Java & Python)
print(Java.intersection(Python))

# '|' or 'union()'
print(Java | Python)
print(Java.union(Python))

# '-' or 'difference()'
print(Java - Python)
print(Java.difference(Python))

# 'add()'
Python.add("Kim")
print(Python)

# 'remove()'
Java.remove("Doyun")
print(Java)
