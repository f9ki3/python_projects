def main():
    print('''
-----------------------------------------------
| welcome to pula and puti guessing game.     |
| In this game you will select a guess        |
| either "pula" or "puti." If the guess       |
| is correct then your bet will be double.    |
|                                             | 
| INSTRUCTION:                                |              
| press (s) to start                          |
| press (e) to exit                           |
-----------------------------------------------
    ''')
    
    while True:
        action = input("action: ")
        
        if action == "s":
            print('''
-----------------------------------------------
| Select guess color:                         |
| press (1) to select pula                    |
| press (2) to select puti                    |
-----------------------------------------------
        
            ''')
            
            try:
                guess = int(input("guess: "))
                bet = int(input("bet: "))
            except ValueError:
                print("Invalid Input")
            else: 
                random(guess, bet)
        elif action=="e":
            break
        else:
            print("Invalid Input")
            
def random(guess, bet):
    import random
    list = ["pula","puti"]
    random.shuffle(list)
    result = list[0]
    
    if guess == 1:
        if result == "pula":
            print("-----------------------------------------------")
            print("You Win")
            print("Guess: pula")
            print("Result: "+result)
            print("bet: "+str(bet))
            print("earn: PHP"+ str(bet*2))
            print("\n-----------------------------------------------")
        else:
            print("-----------------------------------------------")
            print("You Lose")
            print("Guess: pula")
            print("Result: "+result)
            print("bet: "+str(bet))
            print("earn: PHP 0.00")
            print("\n-----------------------------------------------")
    else:
        if result == "puti":
            print("-----------------------------------------------")
            print("You Win")
            print("Guess: puti")
            print("Result: "+result)
            print("bet: "+str(bet))
            print("earn: PHP"+ str(bet*2))
            print("\n-----------------------------------------------")
        else:
            print("-----------------------------------------------")
            print("You Lose")
            print("Guess: puti")
            print("Result: "+result)
            print("bet: "+str(bet))
            print("earn: PHP 0.00")
            print("\n-----------------------------------------------")
        
            
            
main()
        
        
