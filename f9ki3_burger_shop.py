import time
from pyfiglet import Figlet

f = Figlet(font="slant")

print(f.renderText('BurgerShop'))
print("By: f9ki3\n")
print("INSTRUCTION: This program is a burger shop where you can \norder burgers and pay for amount\n")

name = str(input("Enter customer name: "))
time.sleep(2)

#orders
print("select number according to its order:")
print ('''
------------------------------------------
|   * MENU          * PRICE     * ORDER   |
|   * CHEESE BURGER * PHP 50.00 *   1     |
|   * HAM BURGER    * PHP 55.00 *   2     |
|   * EGG SANDWHICH * PHP 25.00 *   3     |
|   * BACON BURGER  * PHP 65.00 *   4     |
|   * VEGGIE BURGER * PHP 60.00 *   5     |
|                                         |       
------------------------------------------
''')

order = int(input("Enter order: "))
qty = int(input("Enter quantiy: "))

print("select number according to its type:")
print ('''
------------------------------------------
|   * DISCOUNT          * TYPE           |
|   * SENIOR            *   1            |
|   * PWD               *   2            |
|   * NONE              *   0            |       
------------------------------------------
''')

discount = int(input("Enter discount type here:"))
payment = float(input("Enter payment here: "))

def compute (name,order,qty,discount,payment):
    if order == 1:
        subtotal = qty * 50.00
        if discount == 1:
            print("------------------------------------------")
            rate = (20/subtotal)* subtotal
            total = subtotal-rate
            change = payment-total
            
            if total>payment:
                print ("TOTAL:", total)
                print ("PAYMENT: ", payment)
                print ("CHANGE: ", change)

        elif discount == 2:
            print("------------------------------------------")
            rate = (15/subtotal)* subtotal
            total = subtotal-rate
            change = payment-total
            print ("TOTAL:", total)
            print ("PAYMENT: ", payment)
            print ("CHANGE: ", change)
        elif discount == 0:
            print("------------------------------------------")
            change = payment-subtotal
            print ("TOTAL:", subtotal)
            print ("PAYMENT: ", payment)
            print ("CHANGE: ", change)
        else:
            print("Invalid Input")

compute (name,order,qty,discount,payment)