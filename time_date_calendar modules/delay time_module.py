import time
'''print("image1")
time.sleep(3)

print("image2")
time.sleep(3)

print("image3")'''

#Delay timer in multiplication table
'''for a in range(1,11):
    print("\n")
    time.sleep(2)
    for b in range(1,11):
        print(a,"X",b,"=", a*b)'''


#using user input to delay time
#program waits for user input to
#...continue next calculations
for a in range(1,11):
    print("\n")
    input()
    for b in range(1,11):
        print(a,"X",b,"=", a*b)
