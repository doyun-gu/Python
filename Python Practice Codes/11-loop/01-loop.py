# for variable in target:
#   command1
#   command2
#   ...

for waiting_no in [1, 2, 3, 4, 5]:
    print("Number: {0}".format(waiting_no))

# range(Number)
# range(Starting Number, Ending Number)
# range(Starting Number, Ending NUmber, Difference)

for waiting_no in range(5):
    print("Number: {0}".format(waiting_no))

for waiting_no in range(1, 6, 2):
    print("Number:{0}".format(waiting_no))

orders = ["Doyun GU", "Damian GU", "GU"]
for customer in orders:
    print("{0}'s Order is ready. Pls Take it".format(customer))

# while condition:
#   command1
#   command2

customer = "Doyun GU"
index = 5

while index >= 1:
    print("{}'s Order is ready".format(customer))
    index -= 1
    print("{} left!".format(index))
    if index == 0:
        print("Coffee Disposed")

#customer = "Doyun GU"
#index = 1

# Infinite Loop -> To exit, press Ctrl(Command) + C
#while True:
#    print("{0}'s Order is Ready! It's {1} time".format(customer, index))
#    index += 1

customer = "Doyun GU"
person = None

while person != customer:
    print("{0}'s Order is Ready!".format(customer))
    person = input("Input ur Name ")

absent = [2, 5]

for student in range(1, 11):
    if student in absent:
        continue
    print("Read a Book Student {0}".format(student))

absent = [2, 5]
no_book = [7]

for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("We end here, Follow me student {0}".format(student))
        break
    print("Student {0}, read a Book".format(student))

# [action for varaible in target]

students = [1, 2, 3, 4, 5]
print(students)

students = [i+100 for i in students]
print(students)

students = ['Doyun GU', 'Damian GU', "GU"]
print(students)

students = [len(i) for i in students]
print(students)

students = ["doyun gu", "damian gu", "gu"]
print(students)

students = [i.upper() for i in students]
print(students)
