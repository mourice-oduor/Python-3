'''class student:
    def details(self,name,age):
        self.name = name
        self.age = age
        print("The name is {} and the age is {}".format(name,age))
    def __init__(self):
        print("You are welcome")'''

#Also constructor can be created in this way
'''class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.balance = 0.0
        self.credit = 100.0
        print("The name is {} and the age is {}".format(name,age))'''

#An example showing how class_constructor is used
'''class student:
    def __init__(self,name):
        self.name = name
        self.attend = 0
        self.marks = []
        print("Welcome {} to our institution".format(name))

    def addmarks(self,ma):
        self.marks.append(ma)
    def attenddays(self):
        self.attend += 1
    def getavg(self):
        return sum(self.marks)/len(self.marks)'''

#special functions _str_ & _del_
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Welcome {}".format(name))
    def __str__(self):
        return("name: {}\n age: {}".format(self.name,self.age))
    def __del__(self):
        print("{} is deleted and memory is free".format(self.name))

#to be executed as:
p1 = person('Moryso',27)
p2 = person('Moryn',23)

print(p1)
print(p2)

del(p1)
del(p2)
