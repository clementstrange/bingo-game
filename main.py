import random
import time
import os 
bingo = []
used_numbers = []
win_numbers = []
draw = 1
def ran():
    number = random.randint(1,90)
    return number

def prettyPrint():
    print("Here is your card: \n")
    print("-----------------------")
    for row in bingo:
        print("|", end="")
        for item in row:
            print(f" {str(item).center(4)} | ", end="")
        print()
        print("-----------------------")
    print(f"\nYour lucky numbers: {win_numbers}")

def createCard():
    numbers = []
    for i in range(8):
        numbers.append(ran())

    numbers.sort()

    global bingo  
    bingo = [
        [numbers[0], numbers[1], numbers[2]],
        [numbers[3], "BINGO", numbers[4]],
        [numbers[5], numbers[6], numbers[7]]
    ]

    return numbers, bingo

createCard()

print("Welcome to Bingo!")

prettyPrint()

start = input("\nPress enter to draw the first number: ")

os.system("clear")
exes = 0
while True:
    match = 0
    
    while True: 
        next_number = random.randint(1,90)
        if next_number not in used_numbers:
            break
    
    print(f"Draw: {draw}")
    
    prettyPrint()
    
    print(f"\nNumber drawn is {next_number}!")
    
    for j in range(len(bingo)):
        for k in range(len(bingo[j])):
            if next_number == bingo[j][k]:
                match = 1
                bingo[j][k] = "X"
                exes +=1
                break
   
    if match==1:
        print("You've got one!")
        used_numbers.append(next_number)
        win_numbers.append(next_number)
        input("Press enter for next round: ")
        
    elif match==0:
        print("Better luck next time!")
        used_numbers.append(next_number)
        input("Press enter for next round: ")

    if exes == 8:
        os.system("clear")
        print("\033[1;32m")
        print("BINGO! You've won!\n")
        prettyPrint()
        print("\033[0m")
        break
    draw+=1
    os.system("clear")

