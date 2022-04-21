names_set = set()

names_set.add("kuba")
names_set.add("jacek")

names_set2 = {"wacek", "placek"}

names_set.update(names_set2)

for name in names_set:
    print(name) 
