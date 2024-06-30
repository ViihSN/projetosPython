"""Exercicio facul - Estrutura de repetição aninhadas:"""

#while + for

tabuada = 1
while tabuada <= 10:
    print(f'tabuada do {tabuada}:')
    for i in range(1, 11, 1):
        print(f'{tabuada} x {i} = {tabuada * 1}')
    tabuada += 1