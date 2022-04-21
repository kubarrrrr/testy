# def not_string(str):
    # x=str[]
    # if str [0 ='n', 1='o', 2='t']:
    #     return "unchanged"
    # else:
    #     x.append[0=n, 1=o, 2=t]

def not_string(str):
  x = str
  if x.startswith('not'):
    return 'unchanged'
  else:  
    return ("not " + x)

print(not_string('not dog'))
print(not_string('dog'))