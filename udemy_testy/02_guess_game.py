import random

def guess(x):
    random_number = random.randint(1, x)
    
    while True:
        guess = int(input(f'podaj liczbę pomiędzy 1, a {x} '))
        if guess > random_number:
            print('too high')
        elif guess < random_number:
            print('too low')
        else:
            break
   
    print(f'hurray! you have guessed correct number!{random_number}')

guess(int(input('podaj ostatanią cyfrę z przedziału')))

# print(f'We are starting a guessing game. Please write a range of the end number {guess(10)}')