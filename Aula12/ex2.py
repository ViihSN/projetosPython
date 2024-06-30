"""Exercicio facul - Estrutura de repetição aninhadas:"""

#2x for

for tabuada in range(1, 11, 1):
    print(f'tabuada do {tabuada}:')
    for i in range(1, 11, 1):
        print(f'{tabuada} x {i} = {tabuada * i}')