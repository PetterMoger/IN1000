from verden import Verden
from sys import exit

def hovedprogram():
    # ber om input fra bruker på dimensjoner og tegner verden.
    rader = int(input("Rader: "))
    kolonner = int(input("Kolonner: "))
    verden = Verden(rader, kolonner)
    verden.tegn()
    
    x = input("Input: ")
    while x == "":
        verden.oppdatering()
        verden.tegn()
        x = input("Input: ")
        if x == "q":
            break

# starte hovedprogrammet
hovedprogram()