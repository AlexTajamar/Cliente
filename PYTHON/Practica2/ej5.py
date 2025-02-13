import random

num = random.randint(0, 100)
adv = ""
intentos = int(input("Dame un número de intentos: "))  
cnt = 0 

while num != adv:
    adv = int(input("Introduce un número: ")) 
    cnt += 1  

    if num < adv:
        print("Es menor")
    else:
        print("Es mayor")

    if cnt == intentos:  
        print("Has alcanzado el número máximo de intentos.")
        break

print("El número era " + str(num))
