# by the default 1 feet is 12 inches
# and 4 inch is 10 cm

def main():
    greet()
    while True:
        user_input = input("action:")
        if user_input == 's':
            menu()
            action = input("select unit: ")
            convert(action)
        elif user_input == 'e':
            print("exited!")
            return False
        else:
            print("Invalid Input")
            

def greet():
    print('''
    -----------------------------------
    | Welcome to Tape Measure App     |
    | press (s) to start              |
    | press (e) to exit               |    
    -----------------------------------
    ''')
def menu():
    print('''
    -----------------------------------
    | Select action here:             | 
    | press (i) to convert inch       |  
    | press (c) to convert centimeter |  
    | press (f) to convert foot       | 
    -----------------------------------
          ''')

def convert(action):
    #inch to ft = 1 inch is 0.0833333333
    
    unit = input("select unit to convert: ")
    value = float(input("Enter the value: "))
    
    if action == "i":
        inchToCentimeter = value * 2.54
        inchTofoot = value * 0.0833333333
    
        print(f'''
            {round(inchToCentimeter)}, {round(inchTofoot)}
        ''')
    

main()