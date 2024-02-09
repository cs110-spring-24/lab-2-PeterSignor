import random
num = random.randint(1, 100)
user = 0
guess = 0 
while user != num:
    user = input("Enter your guess: ")
    user = int(user)  
    guess = guess + 1  
    if user > num:
        print("Too high")
    elif user < num:
        print("Too low" )
    else:
        print("You got it!")
        print("it took", guess, "tries!")
    print()
