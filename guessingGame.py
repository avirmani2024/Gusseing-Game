import random 

numbers = [1,2,3,4,5,6,7,8,9]

randomChoice=random.choice(numbers)
numberOfChances = 5
chances = int(input("Guess a number between 1 and 9?"))
print(chances)
print (randomChoice)
if chances == randomChoice:
        print("Correct")

while chances  != randomChoice:     
    numberOfChances = numberOfChances - 1
    chances = int(input("Guess a number between 1 and 9?"))         
    if chances == randomChoice:
        print("Correct")
    elif chances < randomChoice:
        print("Higher;")
    elif chances > randomChoice:
        print("Lower;")
    if numberOfChances == 0:
        print("Game Over")
