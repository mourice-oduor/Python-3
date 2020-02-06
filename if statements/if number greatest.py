num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
num3 = int(input("Enter the number3: "))

if((num1>num2) & (num1>num3)):
    print(num1, "is the greatest among the three")
    
elif((num2>num1) & (num2>num3)):
    print(num2, "is the greatest among the three")

else:
    print(num3, "is the greatest among the three")
