num1 = int(input("enter number one: "))
num2 = int(input("enter number two: "))
try:
    num3 = num1/num2
except:
    print("you can\'t divide the number by zero")
else:
    print(num3)
