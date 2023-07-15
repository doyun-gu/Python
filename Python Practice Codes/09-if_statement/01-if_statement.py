# If Statement Structure 1:
# If condition:
#   commands

Doyun = "GU"

if Doyun == "GU":
    print("Doyun GU")

Damian = "EEE"

if Damian == "ME":
    print("It's EEE")

Weather = "Fine Dust"

# If Statement Sturcture 2: 
# if condition1:
#   command1
# elif condition2:
#   command 2

if Weather == "Rain":
    print("Take ur Umbrella")

elif Weather == "Fine Dust":
    print("Wear a Facial Mask")

# If Statement Structure 3:
# if condition1:
#   command1
# elif condition2:
#   command2
# else:
#   command3

Weather = "Sunny"

if Weather == "Rain":
    print("Take ur Umbrella")
elif Weather == "Fine Dust":
    print("Wear a Factial Mask")
else:
    print("Nothing needs")
