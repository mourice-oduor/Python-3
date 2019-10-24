import random
number = random.randint(1, 10)
guess = int(input("Enter your integer from1 to 1000: "))
while number!= "guess":
  if guess < number:
     print("number too small")
     guess = int(input("Enter your integer from1 to 1000: "))

  elif guess > number:
    print("number too high")
    guess = int(input("Enter your integer from1 to 1000: "))
    
  elif guess == number:
    print("you won!")
    
    break
