num = int(input("Enter any number: "))
exp = int(input("Enter the exponant: "))

result = 1
for i in range(1,(exp+1)):
    result = result * num
print("The result is: ", result) 
