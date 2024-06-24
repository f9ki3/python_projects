import time

def main():
    timeInput = int(input("Enter number of seconds: "))
    countDown(timeInput)

def countDown(timeInput):
    for second in range(0,timeInput,1):
        time.sleep(1)
        print(timeInput)
        timeInput -= 1

if __name__ == "__main__":
    main()