"""Exercicio facul - Lanchonete"""

print('LANCHONETE')
print('1 - Coxinha R$5.00')
print('2 - Pastel R$7.00')
print('3 - Café R$4.00')
print('4 - Suco R$6.00')
print('5 - SAIR')

total = 0
#menu infinito

while True:
    opera = int(input('Qual item gostaria de comprar?'))

    if(opera == 1):
        quantidade = int(input('Quantas unidades quer comprar?'))
        total = total + quantidade * 5.00
    elif(opera == 2):
        quantidade = int(input('Quantas unidades quer comprar?'))
        total = total + quantidade * 7.00
    elif(opera == 3):
        quantidade = int(input('Quantas unidades quer comprar?'))
        total = total + quantidade * 4.00
    elif(opera == 4):
        quantidade = int(input('Quantas unidades quer comprar?'))
        total = total + quantidade * 6.00
    elif(opera == 5):
        break
    else:
      print('Produto invalido. Selecione outro.')
    
print(f'\n O total a ser gasto neste pedido é de R$ {total}.')

"""Resposta 
LANCHONETE
1 - Coxinha R$5.00
2 - Pastel R$7.00
3 - Café R$4.00
4 - Suco R$6.00
5 - SAIR
Qual item gostaria de comprar?2
Quantas unidades quer comprar?2
Qual item gostaria de comprar?4
Quantas unidades quer comprar?1
Qual item gostaria de comprar?5
O total a ser gasto neste pedido é de R$ 20.0."""