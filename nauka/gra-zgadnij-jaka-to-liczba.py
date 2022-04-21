import random

wykonaneProby = 0

print("czesc! jak masz na imie?")
mojeimie = input()

liczba = random.randint(1, 20)
print("sluchaj, " + mojeimie + " mysle o liczbie z przedzialu od 1 do 20.")

for wykonaneProby in range(6):
    print("sprobuj odgadnac.")
    probaOdgadniecia = input()
    probaOdgadniecia = int(probaOdgadniecia)

    if probaOdgadniecia < liczba:
        print("twoja liczba jest za mala")

    if probaOdgadniecia > liczba:
        print("twoja liczba jest za duza")

    if probaOdgadniecia == liczba:
        break

if probaOdgadniecia == liczba:
    wykonaneProby = str(wykonaneProby + 1)
    print("swietna robota " + mojeimie + " udalo ci sie odgadnac " + wykonaneProby + " probach")

if probaOdgadniecia != liczba:
    liczba = str(liczba)
    print("niestety nie. Liczba, którą miałem na mysli to" + liczba + ".")