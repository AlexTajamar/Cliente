import random
print("numero aleatorio : ")
num=random.randint(0,100)
adv=""

while num!=adv:
    adv=int(input("introduce un numero"))
    if num<adv :
      print("es menor")
    else:
      print("es mayor")
print("el numero es "+str(num))
