import random
# Lav en program hvor du spiller terning imod maskinen
# Den der først vinder 10 gange skal stoppe spillet
# Der skal trykkes på en tast mellem terningkast
# Udskriv antal øjne og stillingen mellem dig og maskinen
# ved hvert kast

def menu():
    print("Du spiller mod maskinen")
    x=input("Tryk på en tast + enter for starte")

Dig=0
Maskine=0

while True:
    x=random.randrange(1,7)
    #skriv det restende program her
