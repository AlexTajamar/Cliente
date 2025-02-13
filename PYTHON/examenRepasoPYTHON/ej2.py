def estaEnLista(letra, lista):
    i = 0
    while i < len(lista):
        if lista[i][0] == letra:
            return i
        i += 1
    return -1

print(estaEnLista('A',[['E',3],['A',2]]))