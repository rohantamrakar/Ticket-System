import mysql.connector
from extra import preprocessRate
import datetime

mydb = mysql.connector.connect(
    host="localhost", user="rohan", password="rohan", database="parkingdb"
)

mycursor = mydb.cursor()


def createEntry(vehicleno, parkingslot, vehicletype, entrytime):

    sql1 = "INSERT INTO customers (vehicleno,vehicletype,entrytime) VALUES (%s, %s, %s)"

    val1 = (vehicleno, vehicletype, entrytime)

    mycursor.execute(sql1, val1)

    mydb.commit()
    token = mycursor.lastrowid

    sql2 = "INSERT INTO parkinglot (parkingslot,customerid) VALUES (%s, %s)"
    val2 = (parkingslot, token)
    mycursor.execute(sql2, val2)

    mydb.commit()
    return token


def checkAvailability(parkingslot):

    sql = "SELECT parkingslot FROM  parkinglot WHERE parkingslot = %s"
    mycursor.execute(sql, (parkingslot,))
    row = mycursor.fetchone()

    if not row:
        return True
    else:
        return False


def updateRate():

    rate = preprocessRate()

    for row in rate:
        sql = "UPDATE ratescheme SET " + \
            row[0] + "=" + "'" + row[1] + "'" + \
            "WHERE typeofvehicle = " + "'" + row[2] + "'"

        mycursor.execute(sql)

        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")


def removeParkingSlot(token):
    sql = "DELETE FROM  parkinglot WHERE customerid = %s"
    val = (token,)
    mycursor.execute(sql, val)
    mydb.commit()


def generateBill(exit_time, token):

    sql = "UPDATE customers SET exittime = (%s)  WHERE customerid = %s"
    val = (exit_time, token)
    mycursor.execute(sql, val)
    mydb.commit()

    amount = mycursor.callproc("calculate_amount", args=(token, 0))
    # print("retruned from sql procedure " + str(amount))
    sql = "SELECT * FROM customers WHERE customerid = %s"
    val = (token,)
    mycursor.execute(sql, val)
    bill = mycursor.fetchone()
    removeParkingSlot(token)

    return bill


def tokencheck(customerid):
    sql = "SELECT * FROM parkinglot WHERE customerid = %s"
    mycursor.execute(sql, (customerid,))

    row = mycursor.fetchone()

    if row:
        return True
    else:
        return False


def checkFull():

    sql = "SELECT count(*) FROM  parkinglot"
    mycursor.execute(sql)
    total_row = mycursor.fetchone()[0]
    print("The occupied slots are " + str(total_row) + "/5")
    if total_row == 5:
        return True
    else:
        return False


def checkExitValid(token, exit_time):

    sql = "SELECT entrytime FROM  customers WHERE customerid = %s"
    val = (token,)
    mycursor.execute(sql, val)
    entry_time = mycursor.fetchone()[0]
    entry_time = entry_time.total_seconds()
    exit_time = datetime.timedelta(
        hours=exit_time.hour, minutes=exit_time.minute).total_seconds()

    if entry_time < exit_time:
        return [True, entry_time]
    else:
        return [False, entry_time]


def getOccupied():
    sql = "SELECT parkingslot FROM  parkinglot"
    mycursor.execute(sql)
    parkingslot = mycursor.fetchall()
    occupied = ""
    for slot in parkingslot:
        occupied = occupied + " " + str(slot[0])
    return occupied
