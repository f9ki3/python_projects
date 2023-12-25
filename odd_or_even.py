from pyfiglet import Figlet

f = Figlet(font="slant")
print(f.renderText("Odd or Even"))
print("By: F9ki3")
print ("\n*This program determine the value if it is ODD or EVEN\n")
print ("---------------------------------------------------------")
x = 0

while x == 0:
    
 #lets make function for odd/even
 def odd_even (value):
     word = Figlet(font="slant")
     action = value % 2

     if action == 1:
          return print (word.renderText("ODD NUMBER"))
     elif action==0:
          return print (word.renderText("EVEN NUMBER"))
     else: 
          return print ("Invalid Input")
     
 inputs = input("Enter a test value here: ")
 if inputs == "exit":
     x = 1
 else:
     odd_even(int(inputs))
     
else:
    print("You Exit")

 