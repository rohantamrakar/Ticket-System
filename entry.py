from extra import clear
import datetime
from time import sleep
from extra import saveAsText
from database import *


def entry():
    vehicletypes = {'2wheeler', '4wheeler', 'heavy'}
    total_slot = 5

    while True:

        parkingslot = int(input("Enter parkingslot number-"))

        if (parkingslot <= total_slot):
            if checkAvailability(parkingslot):
                break
            else:
                print("The parkinglot is occupied.\n Occupied parkinglot are:")
                print(getOccupied())
        else:
            print("Sorry invalid parking number.")

    while True:
        try:
            vehicleno = int(input("Enter vehicle number-"))
            break
        except:
            print("invalid input enter number")

    while True:

        vehicletype = input("Enter type of vehicle-")
        if str(vehicletype) in vehicletypes:
            break
        else:
            print("Sorry invalid  vehicle type.")

    while True:
        try:

            entry_time = input("Enter times in HH:MM\n").split(":")

            entry_time = datetime.time(
                hour=int(entry_time[0]), minute=int(entry_time[1]))

            break

        except:
            print("Enter valid 24format time")

    token = createEntry(vehicleno, parkingslot, vehicletype, entry_time)
    print("You token number is " + str(token))

    saveAsText(token, "token")

    input("Press enter  to go to main menu")
