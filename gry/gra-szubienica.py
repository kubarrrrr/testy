import random
SZUBIENICA_OBRAZKI = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
o   |
    |
    |
   ===''', '''
 +---+
 o   |
 |   |
     |
    ===''', '''
 +---+
 o   |
/|   |
     |
    ===''', '''
+---+
 o  |
/|\ |
    |
   ===''', '''
+---+
 o  |
/|\ |
/   |
   ===''', '''
+---+
 o  |
/|\ |
/   |
   ===''']
słowa = 'baran bocian borsuk bóbr foka fretka gęś gołąb indyk jastrząb jaszczurka jeleń kaczkakobra kojot kot koza kret królik kruk lama leniwiec lew lis łabędź łasica łosoć łoś małpa małż mrówka muł mysz niedźwieź nietoperz nosorożec orzeł osioł owca pająk panda papuga pawian pies pstrąg puma pyton rekin ropucha skunks sowa szczur traszka tygrys wąż wielbłąd wieloryb wilk wombat wrona wydra zebra żaba żółw'.split()

def wylosujSłowo(listaSłów):
    indeksSłowa = random.randint(0, len(listaSłów) -1)
    return listaSłów[indeksSłowa]

def wyświetlPlanszę(strzałyNiecelne, strzałyCelne, tajneSłowo):
    print(SZUBIENICA_OBRAZKI[len(strzałyNiecelne)])
    print()

    print('Strzały niecelne:', end=' ')
    for litera in strzałyNiecelne:
        print(litera, end=' ')
    print()

    pusteMiejsca = '_' * len(tajneSłowo)

    for i in range(len(tajneSłowo)):
        if tajneSłowo[i] in strzałyCelne:
            pusteMiejsca = pusteMiejsca[:i] + tajneSłowo[i] + pusteMiejsca[i+1:]

    for litera in pusteMiejsca:
        print(litera, end=' ')
    print()

def wczytajStrzał(jużPodawane):
    while True:
        print('podaj literę.')
        strzał = input()
        strzał = strzał.lower()
        if len(strzał) != 1:
            print('Proszę podać literę.')
        elif strzał in jużPodawane:
            print("Ta litera już była - spróbuj innej")
        elif strzał not in 'aąbcćdeęfghijklłmnoóprsśtuvwxyzżź':
            print('Proszę podać literę.')
        else:
            return strzał

def zagrajPonownie():
    print('Chcesz zagrać ponwnie? (tak lub nie')
    return input().lower().startswith('t')

print('S Z U B I E N I C A')
strzałyNiecelne = ''
strzałyCelne = ''
tajneSłowo = wylosujSłowo(słowa)
koniecGry = False

while True:
    wyświetlPlanszę(strzałyNiecelne, strzałyCelne, tajneSłowo)

    strzał = wczytajStrzał(strzałyNiecelne + strzałyCelne)

    if strzał in tajneSłowo:
        strzałyCelne = strzałyCelne + strzał

        wszystkieLiteryOdgadnięte = True

        for i in range(len(tajneSłowo)):
            if tajneSłowo[i] not in strzałyCelne:
                wszystkieLiteryOdgadnięte = False
                break
        if wszystkieLiteryOdgadnięte:
            print('Tak! tajne słowo to "' + tajneSłowo + '"! Zwycięstwo!')
            koniecGry = True

    else:
        strzałyNiecelne = strzałyNiecelne + strzał

        if len(strzałyNiecelne) == len(SZUBIENICA_OBRAZKI) - 1:
            wyświetlPlanszę(strzałyNiecelne, strzałyCelne, tajneSłowo)
            print('Nie masz już więcej strzałów!\nPo ' + str(len(strzałyNiecelne)) + ' strzałach niecelnych i ' + str(len(strzałyCelne)) + 'strzałach celnych, tajne słowo to "' + tajneSłowo + '"')
            koniecGry = True

    if koniecGry:
        if zagrajPonownie():
            strzałyNiecelne = ''
            strzałyCelne = ''
            koniecGry = False
            tajneSłowo = wylosujSłowo(słowa)
        else:
            break