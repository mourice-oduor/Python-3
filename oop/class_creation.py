class student:
    def details(self,name,age):
        #setting the data using SELF key word
        self.name = name
        self.age = age
        print("The name is {} and the age is {}".format(name,age))

'''to call the function on the console,
we set object by s1 = student() press entr
the we key in details by say
s1.details("moryso",25) then entr'''
#Also we can display the name after setting
#the data by self.name or age
