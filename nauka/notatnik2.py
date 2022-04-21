# def solution(word: str) -> bool:
# 	if word[-1] == "s":
# 		print(True)
# 	else:
# 		print(False)

# solution("kot")




word = []
def zmiana(word: str):
    for x in word:
        if x.isupper():
            x = x.lower()
        word.append(x)
    print ''.join(word)
            
zmiana("KoteK")

            
