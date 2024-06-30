#trabalhando com métodos em strings
s1 = 'logica de programação e algoritmos'
print(s1.startswith('logica')) #pega a primeira palavra

s1='logica de programação e algoritmos'
print(s1.endswith('algoritmos')) #pega a ultima palavra

s1 = 'logica de programação e algoritmos'
print(s1.upper()) #tras a frase em maiuscula
print(s1.lower()) #tras a frase em minuscula

#################################################

#contar caracteres
s1='logica de programação e algoritmos'
print(s1.count('a'))

###################################################

#quebrando strings
s1='um mafagafinho, dois mafagafinho, tres mafagafinhos...'
print(s1.split(' '))