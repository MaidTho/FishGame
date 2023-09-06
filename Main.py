import random
import csv
import hashlib
import Dict_Array as Da
from Die import Die

data_arr = []


def SignUp():
    print("Signing you up! ")
    User = input("Enter User: ")
    Pass = input("Enter Pass: ")
    ConfirmPass = input("Confirm Pass: ")

    if ConfirmPass == Pass:
        enc = ConfirmPass.encode()
        hash1 = hashlib.sha256(enc).hexdigest()

        data = [[User, hash1]]

        with open('UserDetails.csv', 'a', newline='') as a:
            write = csv.writer(a)
            write.writerows(data)
            a.close()
            print("Successful Register!")
    else:
        print("Password isn't the same as above!")


def Login():
    User = input("Enter User: ")
    Pass1 = input("Enter Pass: ")

    auth = Pass1.encode()
    auth_hash = hashlib.sha256(auth).hexdigest()

    with open("UserDetails.csv", "r") as f:
        csv_reader = csv.reader(f)
        for index, row in enumerate(csv_reader):
            if index == 0:
                print("Log In Attempt ... ")
    f.close()

    if User == row[0] and auth_hash == row[1]:
        print("Logged in Successfully!")
        GameLoop()
    else:
        print("Login failed! \n")


def GameLoop():
    Fishing = True
    Catch = 0
    Score = 0

    print("||| WELCOME TO FISH-RASSIC PARK |||")
    EndGame = input("Go Home (0) or Go Fish (1)?")
    # --- THROW OUT LINE LOOP --- #
    if EndGame == "0":
        print("You decide to pack up and go home without catching anything.")
        exit()
    if EndGame == "1":
        while Fishing:
            CastLine = input("Cast line? (1) or Go Home (0)?")
            if CastLine == "0":  # --- RESULTS SCREEN --- #
                print("You decide to pack up and go home.")
                print("Total Score: ", Score)
                print("Total Caught: ", Catch)
                print("Exiting program")

                data = [[Score, Catch]]

                with open('UserResults.csv', 'a', newline='') as file:
                    write = csv.writer(file)
                    write.writerows(data)
                file.close()
                exit()

            if CastLine == "1":
                Fishing = True
                print("You CAST out your line ...")

                create_die = Die(6)
                DiceRoll = create_die.roll_die()                
                Da.GetFish(DiceRoll)  # <-- Performs the dice roll "Luje==be " "Line 86"

                KeepOrToss = input("KEEP (1) or TOSS (2)")

                if KeepOrToss == "1":
                    print("You keep it ")
                    flist = list(Da.data_arr[DiceRoll - 1].values())
                    Score += int(flist[3])
                    Catch += 0
                    Catch = Catch + 1  # < - Adds fish to "Catch Counter", works as intended, need to replicate for points
                    print("Total Score: ", Score)
                    print("Total Caught: ", Catch)
                if KeepOrToss == "2":
                    print("You toss it")
                    flist = list(Da.data_arr[DiceRoll - 1].values())
                    Score += int(flist[4])
                    Catch -= 0
                    Catch = Catch - 1  # < - Adds fish to "Catch Counter", works as intended, need to replicate for points
                    print("Total Score: ", Score)
                    print("Total Caught: ", Catch)
            try:
                print(KeepOrToss != input)
            except:
                print("An exception occurred")

def AddFish():
    EditFish = input("You have selected to Add A Fish to the Database, continue, \n 1. Add New Fish. ")

    if EditFish == "1":  # Input New Fish
        print("You selected to Add new Fish to the database!")

        Name = input("New Fish Name: ")
        IsKeeper = input("Is New Fish a Keeper Y/N: ")
        IsFish = input("Is New Fish a Fish Y/N: ")
        PIK = input("Points if New Fish is Kept: ")
        PIR = input("Points if New Fish is Released: ")

        data = [[Name, IsKeeper, IsFish, PIK, PIR, ]]

        with open('Fishing.csv', 'a', newline='') as file:
            write = csv.writer(file)
            write.writerows(data)
        file.close()
    else:
        print("Returning to Main Menu!")


def CheckResults():
    with open("UserResults.csv") as CheckFile:
        reader = csv.reader(CheckFile, delimiter=",")
        for row in reader:
            myFish = (row[0], row[1])
            data_arr.append(myFish)
            print(" ".join(row))
    return data_arr


while 1:
    print("--- Login / Sign Up Directory ---")
    print("1. Sign-Up. ")
    print("2. Log-In. ")
    print("3. Add New Fish to Database")
    print("4. Check Results")
    print("0. Exit")

    selection = int(input("Enter your choice: "))

    if selection == 1:
        SignUp()
    elif selection == 2:
        Login()
    elif selection == 3:
        AddFish()
    elif selection == 4:
        CheckResults()
    elif selection == 0:
        break
    else:
        print("Wrong Choice!")
