print("{0}".format(500))

# Leave spaces, Right aligned, Make 10 spaces
print("{0:>10}".format(500))

# +10 makes 10 spaces and add + if format number is positive number
print("{0: >+10}" .format(500))
print("{0: >+10}" .format(-500))

# 0:_<10 adds "_" on the spaces until it reached to 10th spaces
print("{0:_<10}" .format(500))

# Adds "," after every three digits
print("{0:,}".format(1000000000000))

# Addes "+" if it is positive number and "," after every three digits
print("{0:+,}".format(1000000000000))
print("{0:+,}".format(-1000000000000))

# Addes "+" if it is positive number and "," after every three digits. Also, adds "^" on spaces until 30th digits
print("{0:^<+30}".format(1000000000000))

# How to Round Up when prints out
print("{0}".format(5/3))
print("{0:.2f}" .format(5/3))
