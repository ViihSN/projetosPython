"""Exercicio facul - Parametros opcionais - Escreva uma rotina que crie uma borda ao redor de uma palavra,
 para destaca-la como sendo um titulo."""

def borda(s1):
    tam = len(s1)
    if tam:
        print('+', '-' * tam, '+')
        print('|', s1, '|')
        print('+', '-' * tam, '+')

borda('Ola, mundo!')
borda('logica de programação e algoritmos')
    