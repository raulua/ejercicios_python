def es_primo(div):
    for n in range(2, div):
        if div % n == 0:
#            print("No es número primo", n, "es divisor")
            return False
    print(div, "es número primo")
    return True

num = 2
suma = 0
cont = 0

while cont < 20:
    if es_primo(num):
        suma += num
        cont += 1
    num +=1

print ("La suma de los veinte primeros números primos es", suma)
