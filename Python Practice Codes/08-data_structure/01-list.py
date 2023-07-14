# Assume the number of each subway indicates the number of people in every car
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["Doyun", "Damian", "GU"]
print(subway)
print(subway.index("Damian"))

subway.append("FarmTech")
print(subway)

subway.insert(1, "Bilbo")
print(subway)

# Right most one gets off every single 'pop()' function
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# Clear the Variable in 'subway'
subway.clear()
print(subway)

# Count the number of specific Word in the list
company = ["Doyun", "Damian", "GU"]
company.append("Damian")
print(company)
print(company.count("Damian"))

# Ascending & Descending Order
num_list = [4, 9, 6, 3, 5, 2, 1, 7, 8]

# Ascending Order
num_list.sort()
print(num_list)

# Descending Order
num_list.sort(reverse=True)
print(num_list)

num_list.reverse()
print(num_list)

# Mixed
mix_list = ["Doyun", "GU", "Damian", True, [5, 2, 3, 4, 1, 0]]
print(mix_list)

# Combine two different lists
mix_list = ["Doyun", 20, True]
num_list = [1, 2, 3, 4, 5]
num_list.extend(mix_list)
print(mix_list)
print(num_list)

# Dictionary = {key: "value", key1: "Value", ...}
company = {3: "Doyun", 100: "Damian"}

print(company[3])
print(company[100])

# Get the value of key 3
print(company.get(3))
print(company.get(5))
print("Hi")
# print(company[5])
print("Hi")

print(company.get(5, "Available"))

print(3 in company)
print(5 in company)
