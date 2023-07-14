# tuple title = (Value 1, Value 2, ... , Value N)
# Once tuples are defined, ANY values cannot be changed or added. 
# But it's faster than 'List'

menu = ("Chicken", "Pizza")
print(menu[0])
print(menu[1])

name = "Doyun GU"
age = 21
hobby = "Coding"
print(name, age, hobby)

(name, age, hobby) = ("Doyun GU", "21", "Coding")
print(name, age, hobby)

(departure, arrival) = ("Incheon", "Manchester")
print(departure, ">", arrival) # Incheon > Manchester
(departure, arrival) = (arrival, departure)
print(departure, ">", arrival) # Manchester> Incheon
