n = 'Moryso'
a = 25
print('The name is {} and the age is {}'.format(n,a))
print('The name is {} and the age is {}'.format(a,n))
#inserting index values to change format
print('The name is {1} and the age is {0}'.format(n,a))

#give the number of spaces
print('The name is {} and the age is {:4}'.format(n,a))
print("\n")

#iterating using spaces
for i in range(1,11):
    print(i,i*i,i*i*i)
print("\n")

#using well spacing format
for i in range(1,11):
    print("{:2}{:4}{:6}".format(i,i*i,i*i*i))
