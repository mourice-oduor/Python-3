'''type dir(__builtins__) to see all the available functions'''
'''ALSO type help(function name) to see what it does'''
'''ALSO MODULES type help("modules")'''
'''Example help(math) to see all the modules available inside math'''

def nameit():
    print("my name is moryso")
'''to run it on IDE print nameit()'''
print("enter to quit")

def name():
    n = input("enter the name: ")
    print(n)
print("enter to quit")

#User Defined Functions
def addition():
    n1 = int(input("enter number 1: "))
    n2 = int(input("enter number 2: "))
    n3 = n1 + n2
    print(n3)
print("enter to quit")

def subtraction():
    n1 = int(input("enter number 1: "))
    n2 = int(input("enter number 2: "))
    n3 = n1 - n2
    print(n3)
print("enter to quit")

#Functions with arguments
def addition2(n1,n2):
    n3 = n1 + n2
    print(n1,"+",n2,"=", n3)
print("enter to quit")   

def subtraction2(n1,n2):
    n3 = n1 - n2
    print("subtraction =", n3)
