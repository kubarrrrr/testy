# zmiana małej litery na dużą
#
string1 = input("podaj wyraz:")
list1 = list(string1)
new_list = []
for i in list1:
    if i.isupper():
        i = i.lower()
    elif i.islower():
        i = i.upper()
    new_list.append(i)
    
print (''.join(new_list))