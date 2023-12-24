import random, time
from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('Rock Paper Scissors'))
print("By: F9ki3\n")
time.sleep(1)
print("This game is rock paper scissors, you need to pick 1 action and enter it.")
time.sleep(1)
print('''
ACTIONS: rock, paper, scissors
NOTE: to exit enter 'exit'
''')

x = 0
while x==0:
    #get the input of the user
    print("-----------------------------------------------")
    inputs = input("Enter your action: ")
    user_input = inputs.lower()

    # my_list
    actions = ["rock", "paper", "scissors"]

    # to random select from list of action
    random.shuffle(actions)

    # to call first index and store to variable
    computer = actions [0]

    a = "rock"
    b = "paper"
    c = "scissors"
    d = "exit"

    if computer == a and user_input == b:
            print("\nComputer is: ", computer,)
            print("Player is: ", user_input)
            print("YOU WIN")
    elif computer == b and user_input == c:
            print("\nComputer is: ", computer)
            print("Player is: ", user_input)
            print("YOU WIN")
    elif computer == c and user_input == a:
            print("\nComputer is: ", computer)
            print("Player is: ", user_input)
            print("YOU WIN")
    elif computer == b and user_input == a:
            print("\nComputer is: ", computer)
            print("Player is: ", user_input)
            print("YOU LOSE")
    elif computer == c and user_input == b:
            print("\nComputer is: ", computer)
            print("Player is: ", user_input)
            print("YOU LOSE")
    elif computer == a and user_input == c:
            print("\nComputer is: ", computer)
            print("Player is: ", user_input)
            print("YOU LOSE")
    elif computer == a and user_input == a:
            print("\nComputer is: ", computer)
            print("Player is: ", user_input)
            print("DRAW")
    elif computer == b and user_input == b:
            print("\nComputer is: ", computer)
            print("Player is: ", user_input)
            print("DRAW")
    elif computer == c and user_input == c:
            print("\nComputer is: ", computer)
            print("Player is: ", user_input)
            print("DRAW")
    elif user_input == d:
           x = 1
    else:
            print("Invalid Input")
else:
    print("YOU EXIT")