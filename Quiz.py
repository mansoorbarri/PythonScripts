
print("Welcome to my Quiz")

score = 0

answwer = input("QUESTION1 ")
if answwer == "ANSWER1":
    print("Correct!")
    score += 1
else: print("Incorrect!")


answwer = input("QUESTION2 ")
if answwer == "ANSWER2":
    print("Correct!")
    score += 1 
else: print("Incorrect!")

answwer = input("QUESTION3 ")
if answwer == "ANSWER3":
    print("Correct!")
    score += 1 
else: print("Incorrect!")

print("You got " + str(score) + " questions correct!")