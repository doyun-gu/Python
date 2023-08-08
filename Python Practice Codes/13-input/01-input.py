# To Install 
# variable = input ("Comments" )

answer = input ("Input: ")
print("Your Input is " + answer)

# Check the Data Type of Answer: <class 'str'>
print(type(answer))

# <class 'int'>
print(type(int(answer)))
answer = 10

print(type(answer))

import sys

information = {"website": "doyungu.com", "title": "GU Robotics", "Number": "1"}

for subject, information in information.items():
    print(subject, information)

information = {"website": "doyungu.com", "title": "GU Robotics", "Number": "1"}

for subject, information in information.items():
    print(subject.ljust(8), information.rjust(4), sep=":")

# Fill 0 for spacing with "0"
for num in range (1, 21):
    print("Your Number is " + str(num).zfill(3))
