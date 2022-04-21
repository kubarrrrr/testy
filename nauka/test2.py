biggest = None
print("Before:", biggest)
for i in [9, 41, 12, 3, 74, 15]:
    if biggest is None or i > biggest:
        biggest = i
    print("Loop:", i, biggest)
print("Biggest:", biggest)