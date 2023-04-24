print("Welcome to my computer Quiz")
playing = input("Do you want to play my game? ")

if playing != "yes":
    print("Sorry to see you go!")
    quit()
counter = 0

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!, Good job ")
    counter = counter + 1
else:
    print("Better luck next time")

answer = input("What does 3 + 3 = ")
if answer == "6":
    print("Correct!, Good job ")
    counter = counter + 1
else: 
    print("Better luck next time")

answer = input("What is the capital of California? ")
if answer == "sacramento" or "Sacramento":
    print("Correct!, Good job ")
    counter = counter + 1
else: 
    print("Better luck next time")

answer = input("What animal has the highest blood pressure? ")
if answer == "giraffe" or "Giraffe":
    print("Correct!, Good job ")
    counter = counter + 1
else: 
    print("Better luck next time")

answer = input("which animal has the thickest fur? ")
if answer == "sea otter" or "Sea Otter":
    print("Correct!, Good job ")
    counter = counter + 1
else: 
    print("Better luck next time")

answer = input("What is a group of cats called? ")
if answer == "Clowder":
    print("Correct!, Good job ")
    counter = counter + 1
else: 
    print("Better luck next time")

answer = input("What is the only mammal capable of true flight? ")
if answer == "Bats" or "bats":
    print("Correct!, Good job ")
    counter = counter + 1
else: 
    print("Better luck next time")

answer = input("What mammal has the most powerful bite? ")
if answer == "Hippo" or "hippo" or "Hippopotamus" or "hippopotamus":
    print("Correct!, Good job ")
    counter = counter + 1
else: 
    print("Better luck next time")

answer = input(" On a dartboard, what number is directly opposite No. 1? ")
if answer == "19":
    print("Correct!, Good job ")
    counter = counter + 1
else: 
    print("Better luck next time")

answer = input("How many colors are there in a rainbow? ")
if answer == "7":
    print("Correct!, Good job ")
    counter = counter + 1
else: 
    print("Better luck next time")

print(f"Contratulations you answered {counter} questions right!")
