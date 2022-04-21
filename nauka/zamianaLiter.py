def front_back(str):
  mid = str[1:-1]
  fir = str[0]
  las = str[-1]
  str =  las + mid + fir
  x = str
  return x

print(front_back(input("podaj wyraz do zamiany liter ")))