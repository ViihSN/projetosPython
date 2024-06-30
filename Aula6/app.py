"""Exercicio facul - Crie uma variavel de string que receba 
uma frase qualquer. 
Crie uma segunda variavel, agora contendo a metade da string 
digitada. Imprima na tela somente 
os dois ultimos caracters da segunda variavel do tipo string:"""

frase1 = input('Digite uma frase: ')
tamanho = len(frase1)

frase2 = frase1 [ : int (tamanho / 2)]

print(frase2 [-2])



"""resultado no console: 
Digite uma frase: eu sei que voce vai ser a minha melhor amigas"""