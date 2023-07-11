# All Koreans have their own ID number and 7th place indicates gender; 1 - Male (~1,999), 2- Female(~1,999) 3 - Male(~2,000), 4 - Female(~2,000)

KOR_ID='990229-1234567'
print("Gender: " + KOR_ID[7])

print("Year:" + KOR_ID[0:2])
print("Moth:" + KOR_ID[2:4])
print("Date:" + KOR_ID[4:6])

print("Birth Year, Month, Date:" + KOR_ID[:6])
print("Second Part of ID:" + KOR_ID[7:])

print("Second Part of ID:" + KOR_ID[-7:])
