password = "moryso"
for i in range(3):
    pwd = input("enter the password: ")
    j = 2
    if(pwd==password):
        print("welcome")
        break
    else:
        print("wrong password, chances left:", j-i)
        continue
else:
    print("try next time")
