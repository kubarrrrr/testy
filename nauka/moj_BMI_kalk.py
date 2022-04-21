# kalkulator BMI

waga = float(input("podaj swoja wage: "))
wzrost = float(input("podaj swoj wzrost w metrach: "))


bmi = float(waga / (wzrost ** 2))
print(bmi)


if bmi < 18.5:
    print("niedowaga")
elif bmi > 18.5 and bmi < 25:
    print("normalna")
else:
    print("nadwaga")