#exercicio facul - retorno de valores em função

def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while ((tam < min) or (tam > max)):
        s1 = input(pergunta)
        tam = len(s1)
    return s1
x = valida_string('Digite uma string: ', 10, 30)
print('Voce digitou a string: {}. \n Dado valido. Encerrando o programa...'.format(x))