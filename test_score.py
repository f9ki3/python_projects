import time
from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('TestScore App'))
print("By: F9ki3\n")
time.sleep(1)
print("This program calculates your test scores\n")


#Get input from users
full_name = input("Enter your name: ")
total_items = int(input("Enter total items of the test: "))
score = int(input("Enter your score: "))
percentage = (score / total_items ) * 100
grade = int(percentage)


if percentage >= 90 and percentage <=100:
    print ("---------------------------------------------------------------")
    print ("Congrats", full_name, "You pass the test your score is: ", score)
    print ("SCORE: ", score)
    print ("REMARK: A")
elif percentage >= 80 and percentage <=89:
    print ("---------------------------------------------------------------")
    print ("Congrats", full_name, "You pass the test your score is: ", score)
    print ("SCORE: ", score)
    print ("REMARK: B")
elif percentage >= 70 and percentage <=79:
    print ("---------------------------------------------------------------")
    print ("Congrats", full_name, "You pass the test your score is: ", score)
    print ("SCORE: ", score)
    print ("REMARK: C")
elif percentage >= 60 and percentage <=69:
    print ("---------------------------------------------------------------")
    print ("Congrats", full_name, "You pass the test your score is: ", score)
    print ("SCORE: ", score)
    print ("REMARK: D")
elif percentage >= 50 and percentage <=59:
    print ("---------------------------------------------------------------")
    print ("Congrats", full_name, "You pass the test your score is: ", score)
    print ("SCORE: ", score)
    print ("REMARK: A")
elif percentage <= 49:
    print ("---------------------------------------------------------------")
    print ("Sorry", full_name, "You failed the test your score is: ", score)
    print ("SCORE: ", score)
    print ("REMARK: F")
else:
    print ("---------------------------------------------------------------") 
    print("Invalid Input")