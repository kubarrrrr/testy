user_choice = -1

tasks =[]

while user_choice != 5:
    if user_choice == 1:
        print(tasks)

        if user_choice

    if user_choice == 2:
        task = input("wpisz tresc zadania: ")
        tasks.append(task)

    # if user_choice == 3:

    print() 
    print("1. pokaż zadania")
    print("2. dodaj zadanie")
    print("3. usuń zadanie")
    print("4. zapisz zmiany do pliku")
    print("5. wyjdź")

    user_choice = int(input("wybierz liczbę: "))