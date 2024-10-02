parkplatz = [0, 1, 2, 2, 1, 0, 0, 0, 1, 1]

def switchPrint(parklpatz, i):
    if parklpatz == 0:
        print("Parkplatz", (i + 1), "ist frei")
    elif parklpatz == 1:
        print("Parkplatz", (i + 1), "ist belegt")
    elif parklpatz == 2:
        print("Parkplatz", (i + 1), "ist reserviert")

def switchWrite(istatus, ParkplatzNr):
    if istatus == 0:
        print("Parkplatz", ParkplatzNr, "wurde freigegeben\n\n")
        parkplatz[ParkplatzNr-1]=0
    elif istatus == 1:
        print("Parkplatz", ParkplatzNr, "wurde belegt\n\n")
        parkplatz[ParkplatzNr-1]=1
    elif istatus == 2:
        print("Parkplatz", ParkplatzNr, "wurde reserviert\n\n")
        parkplatz[ParkplatzNr-1]=2
    else:
        print("Ungültige Eingabe")

while True:
    for i in range(10):
        switchPrint(parkplatz[i], i)
    print("\nGeben Sie den Status an: (0:löschen 1:belegen 2:reservieren)")
    istatus = int(input())
    print("Geben Sie die Parkplatz-Nummer an: ")
    ParkplatzNr = int(input())
    switchWrite(istatus, ParkplatzNr)

