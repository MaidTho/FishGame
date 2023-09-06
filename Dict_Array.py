import csv

data_arr = []


def GetFish(DiceRoll):
    with open("Fishing.csv", 'r') as file:  # --- OPEN FILE --- #
        csv_file = csv.DictReader(file)
        for row in csv_file:
            data_arr.append(dict(row))

    def testfunc(DR):

        flist = list(data_arr[DR - 1].values())  # < -- data_arr[0] "[0]" pulls the name from file
        Fish_Result = flist[0], flist[1], flist[2], flist[3], flist[4]

        print("You caught a " + flist[0])
        print(flist[0] + " is a " + flist[0])
        print(flist[0] + " is a Keeper " + flist[1])
        print(flist[0] + " is a Fish " + flist[2])
        print(flist[0] + " is worth " + flist[3] + " if you keep")
        print(flist[0] + " is worth " + flist[4] + " if you release")

        return Fish_Result  # < -- return values to calling file

    if DiceRoll == 1:  # < -- King George Whiting
        testfunc(DiceRoll)
    elif DiceRoll == 2:  # < -- Large Mullet
        testfunc(DiceRoll)
    elif DiceRoll == 3:  # < -- Small Mulloway
        testfunc(DiceRoll)
    elif DiceRoll == 4:  # < -- Snapper
        testfunc(DiceRoll)
    elif DiceRoll == 5:  # < -- Seaweed Monster
        testfunc(DiceRoll)
    elif DiceRoll >= 6:  # < -- Lost Bait
        testfunc(DiceRoll)
