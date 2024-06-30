"""Exercicio facul - Estrutura de repetição aninhadas:"""

#2x while

tabuada = 1
while tabuada <=10:
    print(f'tabuada do {tabuada}:')
    i=1
    while i <= 10:
        print(f'{tabuada} x {i} = {tabuada * i}')
        i+= 1
    tabuada += 1
