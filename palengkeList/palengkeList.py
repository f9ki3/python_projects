#Lets make a shoping list with python and sqlite for database also apply OOP encapsulation 
#This section import all libraries
import sqlite3, json, sys
from datetime import datetime
from pyfiglet import Figlet

#This are the classes
class Database():
    def __init__(self):
        #this is the connection for our database using sqlite
        self.conn = sqlite3.connect("shopping_list.db")
    
    #lets create the method to create the db
    def CreateTableShoppingList(self):
        self.conn.cursor().execute('''
        CREATE TABLE IF NOT EXISTS shopping_list(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     date_added TEXT NOT NULL,
                     description TEXT NOT NULL,
                     quantity INTEGER NOT NULL,
                     unit TEXT NOT NULL
                     )
        ''')
        self.conn.close()
    
    #Lets make method that insert data to the table
    def InsertTableShoppingList(self, description, qty, unit):
        date = datetime.today().strftime('%Y-%m-%d')
        data = [date,description, qty, unit]
        self.conn.cursor().execute(f'''
        INSERT INTO shopping_list(date_added, description, quantity, unit) 
        VALUES (?, ?, ?, ?)
        ''', data)
        self.conn.commit()
        self.conn.close()
        #Lets put some notifier if success
        print("Added record successfully")
    
    #lets make the retived method
    def RetievedTableShoppingList(self):
        response = self.conn.cursor().execute('SELECT * FROM shopping_list').fetchall()
        return response
    
    #lets create a delete record
    def DeleteTableShoppingList(self, id):
        self.conn.cursor().execute(f'DELETE FROM shopping_list WHERE id = {id}')
        self.conn.commit()
        self.conn.close()
        print("Delete record successfully")

#lets run the main program here
def main():
    #now lets run the methods here by the time program runs
    Database().CreateTableShoppingList()
    mainScreen()
    listOfChoices = [1,2,3,4]
    while True:
        menuScreen()
        while True:
            try:
                userInput = int(input("Choose Selection: "))
                choice = userInput in listOfChoices
                if choice == True:
                    break
                print('Invalid Input!')
                continue
            except ValueError:
                print('Invalid Input!')
                continue
        menu(userInput)
    
#functions sections
def mainScreen():
    title = Figlet(font='slant').renderText('ShopList App')
    print(title)
    return

def menuScreen():
    print('''
---------------------------------
. Welcome to the ShopList App   .
.                               .
. press (1) to add new items    .
. press (2) to view list        .
. press (3) to delete items     .
. press (4) to exit the program .
.                               .
---------------------------------
''')
    return

def menu(userInput):
    if userInput == 1:
        questions = [
            'Item Decription: ',
            'Quantity: ',
            'Unit: '
        ]
        answers =[]
        for question in questions:
            answer = input(question)
            answers.append(answer)
        a,b,c = answers
        Database().InsertTableShoppingList(a,b,c)
        return

    elif userInput == 2:
        data = Database().RetievedTableShoppingList()
        for x in data:
            print(x)
    elif userInput == 3:
        while True:
            try:
                userInput = int(input("input id to delete: "))
                break
            except ValueError:
                print('Invalid Input!')
                continue
        Database().DeleteTableShoppingList(userInput)
        return
    elif userInput == 4:
        print("You've been exited!")
        sys.exit()
    else:
        print('Invalid Input!')
        return

if __name__ == "__main__":
    main()