import random, time
from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('Roll2Dice'))
print("By: F9ki3\n")
time.sleep(1)
print("This program is simulation of 2 rolling dice")
time.sleep(1)
print('''
ACTIONS: start, exit
''')

x = 0

while x == 0:
    print("-----------------------------------------")
    user_input = input("\nEnter input here: ")
    print("\n")
    if user_input == "start":

        def loading_animation():
            frames = ["|", "/", "-", "\\"]
            for _ in range(3):
                  # Adjust the range to control the duration of the animation
                for frame in frames:
                    print(f"\rRolling 2 Dice{frame}", end="", flush=True)
                    time.sleep(0.1)  # Adjust the sleep duration for the desired speed
            print("\n")

        #get two dice list
        dice1 = [1,2,3,4,5,6]
        dice2 = [1,2,3,4,5,6]

        #lets random the dice1 and dice2
        random.shuffle(dice1)
        random.shuffle(dice2)

        # Run the loading animation function
        loading_animation()

        # get only first index
        rand1 = dice1[0]
        rand2 = dice2[0]

        print("ROLLED DICE")
        print ("Dice 1: ", rand1)
        print ("Dice 2: ", rand2)

    elif user_input == "exit":
        x = 1
    else:
        print("Invalid Input")
else:
    print("-----------------------------------------")
    print ("YOU EXIT")