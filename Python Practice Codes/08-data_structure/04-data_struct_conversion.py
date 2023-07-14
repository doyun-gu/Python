menu = {"Coffee", "Milk", "Juice"}

# Set: {}, List: [], Tuple: ()

# Give the values in menu
print(menu)

# Give the Type of Data structure
print(type(menu))

# Set -> List
menu = list(menu)
print(menu, type(menu))

# List -> Tuple
menu = tuple(menu)
print(menu, type(menu))

# Tuple -> Set
menu = set(menu)
print(menu, type(menu))
