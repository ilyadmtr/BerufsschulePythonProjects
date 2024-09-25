import os

# MacOS und Linux 'clear', Windows 'cls'
os.system('clear' if os.name == 'posix' else 'cls')

# Aufgabe 1
print("\nAufgabe 1:")
print("Analysieren Sie das folgende Verhalten:")
print("Welche Schlussfolgerung ziehen Sie aus dem Verhalten?")
text1 = "Text"
print("Text1 ist vom Datentyp:", type(text1), "und hat den Inhalt", text1)
text1 = 2
print("Text1 ist vom Datentyp:", type(text1), "und hat den Inhalt", text1)
text1 = True
print("Text1 ist vom Datentyp:", type(text1), "und hat den Inhalt", text1)

# Aufgabe 2
einkaufen = ["Brot", 5, "Äpfel", "Eier"]

# Aufgabe 2a
print("\nAufgabe 2a:")
print("Ausgabe des Arrayinhalts:")
print(einkaufen)  # ['Brot', 5, 'Äpfel', 'Eier']

# Aufgabe 2b
print("\nAufgabe 2b: ")
print("Ausgabe der Listeneinträge untereinander:")
for item in einkaufen:
    print(item)  # Brot, 5, Äpfel, Eier

# Aufgabe 2c
print("\nAufgabe 2c: ")
einkaufen.insert(3, "Salat")  # Einfügen des Wertes 'Salat' nach 'Äpfel'
print(einkaufen)  # ['Brot', 5, 'Äpfel', 'Salat', 'Eier']

# Aufgabe 2d
print("\nAufgabe 2d: ")
einkaufen.remove(5)  # Löschen des Eintrags '5'
print(einkaufen)  # ['Brot', 'Äpfel', 'Salat', 'Eier']

# Aufgabe 3a
print("\nAufgabe 3a: ")
print("Durchlaufen der Liste einkaufen mit Foreach Schleife")
for item in einkaufen:
    print(item)

# Aufgabe 3b
print("\nAufgabe 3b: ")
print("Durchlaufen der Liste einkaufen mit einer zählergesteuerten Schleife")
for i in range(len(einkaufen)):
    print(einkaufen[i])

# Aufgabe 3c
print("\nAufgabe 3c: ")
print("Durchlaufen der Liste einkaufen mit While Schleife")
i = 0
while i < len(einkaufen):
    print(einkaufen[i])
    i += 1

# Aufgabe 4a
print("\nAufgabe 4a: ")
text = "Welt"
print("Hallo " + text)  # 'Hallo Welt'

# Aufgabe 4b
print("\nAufgabe 4b: ")
zahl = 2
print(f"{zahl} Personen")  # '2 Personen'

# Aufgabe 5
print("\nAufgabe 5: ")
person1 = "Kai"
person2 = "Tom"
print(person1, person2)
print("Austausch Person1 mit Person2 und das Ergebnis auf der Konsole ausgeben")
person1, person2 = person2, person1
print(person1, person2)  # Tom Kai

# Aufgabe 6
print("\nAufgabe 6: ")
ergebnis = int(input("Ergebnis: "))
if ergebnis == 1:
    print("super")
elif ergebnis == 2:
    print("gut")
else:
    print("Fehler")

# Aufgabe 7
print("\nAufgabe 7: ")
def formatierteAusgabe(bezeichnung, wert):
    print(f"+++ {bezeichnung} +++")
    print(wert)

level = 40
nickname = "Mat"
formatierteAusgabe("Nickname", nickname)
formatierteAusgabe("Level", level)
