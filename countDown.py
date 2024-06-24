import time,os, platform
from pyfiglet import Figlet
def main():
    timeInput = int(input("Enter number of seconds: "))
    countDown(timeInput)

def countDown(timeInput):
    for second in range(timeInput,0,-1):
        os.system('clear')
        textStyle = Figlet(font='slant').renderText(str(second))
        print(textStyle)
        time.sleep(1)
        timeInput -= 1
    os.system('clear')
    print(Figlet(font='slant').renderText(str('Times Up!')))

if __name__ == "__main__":
    main()