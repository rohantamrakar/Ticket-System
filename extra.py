import os


def clear(): return os. system('cls')


def saveAsText(data, type):

    if type == "token":
        f = open("./token/" + str(data) + ".txt", "w+")
        f.write("your token number is " + str(data))

        f.close()

    if type == "bill":
        f = open("./bill/" + str(data[0]) + ".txt", "w+")
        f.write("Token id = " + str(data[0]) + "\n")
        f.write("Vehilce number = " + str(data[1]) + "\n")
        f.write("Vehicle type= " + str(data[2]) + "\n")
        f.write("Entry time = " + str(data[3]) + "\n")
        f.write("Exit time= " + str(data[4]) + "\n")
        f.write("Amount = " + str(data[5]) + "\n")
        f.close()


def preprocessRate():
    with open("./rate_scheme/rate_scheme.txt", "r") as myfile:
        data = myfile.read().lower().replace("free", "0").replace(" ", "").splitlines()
    data.pop(0)
    rate = [r.split(",")for r in data]
    print(rate)
    return rate


def printBill(bill):
    print("Token id = " + str(bill[0]))
    print("Vehilce number = " + str(bill[1]))
    print("Vehicle type= " + str(bill[2]))
    print("Entry time = " + str(bill[3]))
    print("Exit time= " + str(bill[4]))
    print("Amount = " + str(bill[5]))
    input("press enter to continue")
