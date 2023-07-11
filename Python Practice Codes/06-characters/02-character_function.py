python = "Python is interesting"

# Convert All Characters into lowercase
print(python.lower())

# Convert All Characters into Uppercase
print(python.upper())

# Check index 0 is uppercase or not. If True return True otherwise, False
print(python[0].isupper())

# Check index 1, 2 are lowercase or not. If True return True otherwise, False
print(python[1:3].islower())

# Change Python to Java
print(python.replace("Python", "Java"))

# find(targeting Character, Beginning Character, Ending Character)
# : if there's no targetting value in the given characters, it returns -1 and continue

# index(targeting character, Beginning Character, Ending Character)
# : if there;s no targetting value in the given characters, it returns ValueError:~ and exit

# Return the index number where it found 'n' for the first time
find = python.find("n")
print(find)

# Return where it found 'n' after index 6 (find: index 5)
find = python.find("n", find+1)
print(find)

# Return '-1' since there's no 'Java'
find = python.find("Java")
print(find)

# Return the index number where it found 'n' for the first time
index = python.index("n")
print(index)

# Return where it found 'n' after index 6 (index: index 5)
index = python.index("n", index + 1)
print(index)

# From second index and right before the 6th index(5) Return index number where it found 'n' 
index = python.index("n", 2, 6)
print(index)

# Return ValueError:~ and exit the code since  there's no 'Java' in the given sentence
index = python.index("Java")
print(index)

#--------------------------------------------------------------------------------------------------
# From this line will not be executed since 'python.index' exit the code

# Return the number of times "n" or "v" characters are in the given character (python)
print(python.count("n"))
print(python.count("v"))

# Return the length of given Data (Can be used in characters)
print(len(python))
