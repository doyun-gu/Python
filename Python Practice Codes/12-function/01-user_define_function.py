# User Define Function Structure without inputs
# def function-title():
#   code1
#   code2
#   ...

# This only generates a new function
def introduce_myself():
    print("Hello My name is Doyun GU")

# Call Function and Execute
introduce_myself()

# User Define Function Structure with inputs
# def function-title():
#   code1
#   code2
#   ...

# Example1: Deposit
def open_account():
    print("Creating new account")

# Call User Define Function
open_account()

def deposit(balance, money):
    print("Deposit {0} GBP, and Balance is {1} GBP. Thank you.".format(money, balance+money))
    return balance + money    # Store the data of Balance

balance = 0
balance = deposit(balance, 26000)

# Example 2: Withdraw

def open_acount():
    print("Creating new account")

open_account()

def deposit(balance, money):
    print("Deposit {0} GBP, and Balance is {1} GBP. Thank you.".format(money, balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("Withdraw {0} GBP, and Balance is {1} GBP. Thank you.".format(money,balance - money))

        return balance - money

    else:
        print("Lack of Balance. Ur Balance is {0} GBP. Thank you".format(balance))

        return balance
    
balance = 0
balance = deposit(balance, 30000)

balance = withdraw(balance, 26000)
balance = withdraw(balance, 50000)

# Commission Code - For the convinience, assume that always deposit is greater than withdraw
def open_account():
    print("Creating a new account")

open_account()

def deposit(balance, money):
    print("Deposit {0} GBP, and Balance is {1} now.".format(money, balance + money))
    return balance + money

def withdraw_night(balance, money):
    commission = 100
    print("Withdraw {} GBP on non-Working Days".format(money))
    return commission , balance - money - commission

balance = 0
balance = deposit(balance, 50000)

commission, balance = withdraw_night(balance, 49000)
print("Commission is {0} GBP and Balance is {1} GBP now".format(commission, balance))
