# Greater Number Checker...........
number1=int(input("enter 1st number :"))
number2=int(input("enter 2nd number :"))
number3=int(input("enter 3rd number :"))
if number1>number2 and number1>number3:
    print("First number is greater")  
elif number2>number1:
    print("second number is greate")
else:
    print("Both numbers are equal")
