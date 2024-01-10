def main():
    while True:
        greet()
        user_input = input("action:")
        if user_input == 's':
            menu()
            action = input("select unit: ")
            if action == 'i' or action == 'f' or action == 'c':
                convert(action)
            else:
                print("-----------------------------------\nInvalid Input")
        elif user_input == 'e':
            print("-----------------------------------\nyou exited!")
            return False
        else:
            print("-----------------------------------\nInvalid Input")
            

def greet():
    print('''
-----------------------------------
| Welcome to Tape Measure App     |
| by f9ki3\n                      |
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
    if action == "i":
        while True:
            unitToConvert = unit()
            if unitToConvert[0] == "c":
                print("Result: ", str(round(unitToConvert[2], 2)) + "cm")
                break
            elif unitToConvert[0] == "f":
                print("Result: ", str(round(unitToConvert[3], 2))+ "ft")
                break
            elif unitToConvert[0] == "i":
                print("Result: ",str(round(unitToConvert[1]))+ "inch")
                break
            else: 
                print("Invalid Input")
                break
    elif action == "c":
        while True:
            unitToConvert = unit()
            if unitToConvert[0] == "i":
                print("Result: ", str(round(unitToConvert[5], 2)) + "inch")
                break
            elif unitToConvert[0] == "f":
                print("Result: ", str(round(unitToConvert[4], 2)) + "ft")
                break
            elif unitToConvert[0] == "c":
                print("Result: ", str(round(unitToConvert[1])) + "cm")
                break
            else: 
                print("Invalid Input")
                break
    elif action == "f":
        while True:
            unitToConvert = unit()
            if unitToConvert[0] == "i":
                print("Result: ", str(round(unitToConvert[6], 2)) + "inch")
                break
            elif unitToConvert[0] == "c":
                print("Result: ", str(round(unitToConvert[7], 2)) + "cm")
                break
            elif unitToConvert[0] == "f":
                print("Result: ", str(round(unitToConvert[1])) + "ft")
                break
            else: 
                print("Invalid Input")
                break
            
def unit():
    unit = input("select unit to convert: ")
    value = float(input("Enter the value: "))
    
    inchToCentimeter = value * 2.54
    inchTofoot = value * 0.0833333333
    centimeterToFoot = value * 0.0328
    centimeterToInch = value * 0.393700787
    feetToInch = value * 12
    feetToCentimeter = value * 30.48   
    
    return unit, value, inchToCentimeter, inchTofoot, centimeterToFoot, centimeterToInch, feetToInch, feetToCentimeter

main()