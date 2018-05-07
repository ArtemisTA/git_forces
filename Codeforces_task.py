nm = input()
if len(nm) == 3:
    amountofdominoesplaced = int(nm[0])*int(nm[2])/2
    if int(nm[0])*int(nm[2])%2 > 0:
        amountofdominoesplaced = amountofdominoesplaced - 0.5
    print(amountofdominoesplaced)
if len(nm) == 4:
    try:
        amountofdominoesplaced = ((int(nm[0])*10 + int(nm[1]))*int(nm[3]))/2
        if ((int(nm[0])*10 + int(nm[1]))*int(nm[3]))%2 > 0:
            amountofdominoesplaced = amountofdominoesplaced - 0.5
        print(amountofdominoesplaced)
    except:
        amountofdominoesplaced = ((int(nm[0])*10 + int(nm[1]))*int(nm[3]))/2
        if (int(nm[0])*(int(nm[2]) * 10 + int(nm[4])))%2 > 0:
            amountofdominoesplaced = amountofdominoesplaced - 0.5
        print(amountofdominoesplaced)
if len(nm) == 5:
    amountofdominoesplaced = (int(nm[0])*10 + int(nm[1])) * (int(nm[3])*10 + int(nm[4]))/2
    if (int(nm[0])*10 + int(nm[1])) * (int(nm[3])*10 + int(nm[4]))%2:
        amountofdominoesplaced = amountofdominoesplaced - 0.5
    print(amountofdominoesplaced)