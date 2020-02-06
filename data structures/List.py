from tkinter import *
List1 = [12, 4, 56, 17, 8, 99]
print(max(List1))

def Mean(list2): 
    return sum(list2) / len(list2) 
list2 = [12, 4, 56, 17, 8, 99]
mean = Mean(list2)
print("Mean of the list2 =", round(mean,2))
