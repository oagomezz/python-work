print("Welcome to my computer Quiz")
playing = input("Do you want to play my game? ")


if playing != "yes":
    print("Sorry to see you go!")
    quit()

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!, Good job ")
else:
    print("Better luck next time")

answer = input("What does 3 + 3 = ")
if answer == "6":
    print("Correct!, Good job ")
else: 
    print("Better luck next time")