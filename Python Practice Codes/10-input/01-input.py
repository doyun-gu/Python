weather = input("How's it Weather Today?:")
print(weather)

if weather == "Rain":
    print("Take ur Umbrella!")
elif weather == "Fine Dust":
    print("Take ur Facial Mask!")
else:
    print("Good! Go for a walk around u!")

# Can add Operator between conditions
if weather == "Rainy" or weather == "Snowy":
    print("Take ur Umbrella!")
elif weather == "Fine Dust":
    print("Take ur Facial Mask!")
else:
    print("Good! Go for a walk around u!")

temp = int(input("How's the temperature today?"))

if 30 <= temp:
    print("It's rlly hot outside. Should stay indoor")
elif 10 <= temp and temp < 30:
    print("Take ur Coat!")
else:
    print("It's rlly Cold outiside! Take care!")
