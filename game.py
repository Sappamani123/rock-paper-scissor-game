import random
print("Welcome! Let's play together")
choices=["rock","paper","scissor"]
while True:
    user=input("enter your choice(rock or paper or scissor or enter quit to exit game):")
    print("User chooses:",user)
    if user=='quit':
        print("user not availble")
        break
    if user not in choices:
        print("Invalid input, Try again!")
        continue
    computer=random.choice(choices)
    print(f"computer chooses :{computer}")
    if user==computer:
        print("It's tie.")
    elif (user=="rock" and computer=="scissor") or (user=="paper" and computer=="scissor") or (user=="scissor" and computer=="paper"):
        print("User won.")
    else :
        print("computer won.")

        

