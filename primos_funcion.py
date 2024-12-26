#Start code here
def es_primo(div):
  for n in range(2, div):
    if div % n == 0:
      #print(div, "no es número primo porque", n, "es divisor") # your own code
      return False
  print(div, "es número primo") # your own code
  return True
num = 2
cont = 0
while cont < 20:
  if es_primo(num):
    cont = cont + 1
  num = num + 1

