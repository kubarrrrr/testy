transakcje = []

WYBOR = None

while WYBOR != "0":
    print("0 koniec operacji\n1 wplac kase")
    WYBOR = input("wybierz opcje : ")
    if WYBOR == "1":
        kwota = input("podaj kwote do wplaty:")
        transakcje.append(int(kwota))

    print(transakcje)