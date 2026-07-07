password = input("Enter password:")
   print("welcome Thanu himaaaa")
else:
   print("wrong password")

################################


marks = int(input("enter the marks"))
if marks >= 90:
  print("A grade")
elif marks >= 75:
  print("B grade")
elif marks >= 50:
  print("C grade")
else:
   print("fail")

age = 20
salary = 10000000000000000
if age > 18 and salary > 30000000000000:
    print("loan approved")

day = "sunday"
if day == "saturday" or day =="sunday":
    print("holiday")

login = False

if not login:
    print("print login")

Pin = 1234
balance = 100000
pin = int(input("enter pin:"))
if pin == Pin:
    print("current balance:",balance)
    amount = int(input("enter amount:"))
    if amount <= balance:
        balance = balance - amount
        print("Transaction successful")
        print("balance=",balance)
    else:
        print("no balance")
else:
    print("wrong pin")


