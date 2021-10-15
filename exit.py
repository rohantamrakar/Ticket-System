from datetime import time, timedelta
from database import tokencheck, generateBill, checkExitValid
from extra import printBill, saveAsText


def bill():
    while True:
        try:
            token = int(input("Enter token number-"))
        except ValueError:
            print("Please enter integer")
            continue

        tokenExist = tokencheck(token)
        if (tokenExist):

            while True:

                exit_time = input("Enter times in HH:MM\n").split(":")
                try:
                    exit_time = time(
                        hour=int(exit_time[0]), minute=int(exit_time[1]))
                except:
                    print("Please enter valid time")
                    continue
                valid, entry_time = checkExitValid(token, exit_time)
                if valid:
                    break
                else:
                    print("Enter valid time , the entry time is " +
                          str(timedelta(seconds=entry_time)))

            bill = generateBill(exit_time, token)
            printBill(bill)
            saveAsText(bill, "bill")
            break

        else:
            print("Sorry invalid token number.")
