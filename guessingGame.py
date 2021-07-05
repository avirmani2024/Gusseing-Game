import random 

numbers = [1,2,3,4,5,6,7,8,9]

randomChoice=random.choice(numbers)
numberOfChances = 0
#print (randomChoice)


while numberOfChances  < 5:   
     numberOfChances += 1
     chances = int(input("Guess a number between 1 and 9?"))    

     if chances == randomChoice:
        print("Correct")
        break

     elif chances > randomChoice:
         print("Your guess was to high")

     else:
         print("Your guess was too low")



if not numberOfChances < 5:
    print("You Lose")


 
     