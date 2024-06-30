#copias de listas

lista_original = [5, 6, 7, 8]
lista_referenciada = lista_original[:]
print(lista_original)
print(lista_referenciada)

lista_referenciada[0] = 21 #alteração
print(lista_original)
print(lista_referenciada)