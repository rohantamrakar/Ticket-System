
import mysql.connector
import time
from database import checkFull, updateRate
from entry import entry
from exit import bill
from extra import clear


mydb = mysql.connector.connect(
    host="localhost", user="rohan", password="rohan", database="parkingdb")


updateRate()
while 1:
    # clear()
    print("---------Parking Ticket System----------")
    print(":              1)Entry                 :")
    print(":              2)Bill                  :")
    print("----------------------------------------")
    slot_full = checkFull()

    choice = input("Enter the option-")
    if choice == 1 or choice == '1':
        if slot_full:
            print("Slots are full")
            input("Enter to continue")
        else:
            entry()

    elif choice == 2 or choice == '2':
        bill()
    else:
        print("invalid option")
        exit()
