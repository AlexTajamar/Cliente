from ej1 import vocalORnot
from ej2 import estaEnLista
from ej3 import transformar
from ej4 import orden

palabra = input('dame una palabra: ')
resultado = []

for x in palabra:
    if vocalORnot(x):
        pos = estaEnLista(x.upper(), resultado)  
        
        if pos == -1:  
            resultado.append([x.upper(), 1])
        else:  
            resultado[pos][1] += 1

print(resultado)
print(transformar(resultado))
print(orden(resultado))