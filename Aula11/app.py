"""Exercicio  facul - Condicional de múltipla escolha (elif)"""

print('Escolha o que deseja comprar: ')
print('1 - Maça ')
print('2 - Laranja ')
print('3 - Banana ')

produto = int(input('Qual sua escolha? '))
quantidade = int(input('Quantas unidades?'))

if(produto == 1):
    pagar = quantidade * 2.3
    print(f'Voce comprou {quantidade} maças. Total á pagar: {pagar}')
elif(produto == 2):
    pagar = quantidade *3.60
    print(f'Voce comprou {quantidade} laranjas. Total á pagar: {pagar}')
elif(produto == 3):
    pagar = quantidade * 1.85
    print(f'Voce comprou {quantidade} bananas. Total á pagar: {pagar}')
else: 
    print('Produto inexistente!')

"""resposta: 
Escolha o que deseja comprar: 
1 - Maça 
2 - Laranja
3 - Banana
Qual sua escolha? 3
Quantas unidades?10
Voce comprou 10 bananas. Total á pagar: 18.5"""