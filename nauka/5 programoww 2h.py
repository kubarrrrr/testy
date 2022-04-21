no_of_tries = 5
word = "kamil"
used_letters = []

user_word = []


for _ in word:
    user_word.append("_")

    while True:
        letter = input("Podaj literę: ")
        used_letters.append(letter)

        print(word.index(letter))

        print("uzyte litery:" used_letters)