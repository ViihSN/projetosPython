"""exercico facul - Condicionais aninhados: """

print('Escolha o que deseja comprar: ')
print('1 - Maça ')
print('2 - Laranja ')
print('3 - Banana ')

produto = int(input('Qual sua escolha? '))
quantidade = int(input('Quantas unidades?'))

if(produto == 1):
    pagar = quantidade * 2.3
    print(f'Voce comprou {quantidade} maças. Total á pagar: {pagar}')
else: 
    if(produto == 2):
        pagar = quantidade * 3.6
        print(f'Voce comprou {quantidade} maças. Total á pagar: {pagar}')
    else: 
        if(produto == 3):
            pagar = quantidade * 1.85
            print(f'Voce comprou {quantidade} maças. Total á pagar: {pagar}')
        else:
            print('Produto inexistente!')

"""RESPOSTA:

Escolha o que deseja comprar: 
1 - Maça 
2 - Laranja
3 - Banana
Qual sua escolha? 2
Quantas unidades?200
Voce comprou 200 laranjas. Total á pagar: 720.0
ou 
Escolha o que deseja comprar: 
1 - Maça 
2 - Laranja
3 - Banana
Qual sua escolha? 5
Quantas unidades?5
Produto inexistente!"""