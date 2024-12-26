#Start code here
num = 2
bucle = 0
while bucle < 20:
  primo = True
  div = 2
  while div < num:
    if num % div == 0:
      primo = False
      break
    div = div + 1
  if primo == True:
    bucle = bucle + 1
    print(str(bucle)+") ", num, " es número primo") # your own code
  num = num + 1
