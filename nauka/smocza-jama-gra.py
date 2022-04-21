import random
import time

def wyswietlIntro():
    print('''znajdujesz się w krainie smoków.
    Przed sobą widzisz dwie jaskinie
    W jednej mieszka przyjazny smok, 
    któy podzieli się z tobąswoim skarbem.
    Drugi smok jest chciwy i glodny,
    więc pożre cię bez zmróżenia oka.''' )

def wybierzJaskinie():
    jaskinia = " "
    while jaskinia != "1" and jaskinia != "2":
        print("Do której jaskini chcesz wejść? (1 lub 2)")
        jaskinia = input()

    return jaskinia

def zbadajJaskinie(wybranaJaskinia):
    print("zblizasz sie do mrocznej jaskini...")
    time.sleep(2)
    print("wtem! Nagle! Raptem!")
    time.sleep(2)
    print("pojawia się straszliwy smok... Otwiera swoją paszczę i...")
    print()
    time.sleep(2)

    przyjaznaJaskinia = random.randint(1, 2)

    if wybranaJaskinia == str(przyjaznaJaskinia):
        print('oddaje ci swój skarb')
    else:
        print("mniam mniam Pożera cię w całości")

zagraj = "tak"
while zagraj == "tak":
    wyswietlIntro()
    numerJaskini = wybierzJaskinie()
    zbadajJaskinie(numerJaskini)

    print("CHcesz zagrać ponownie? (tak lub nie)")
    zagraj = input()
