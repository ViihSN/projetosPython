"""Exercicio facul- Escreva um programa que pergunte a 
 quantidade de km percorridos por um carro alugado pelo
 usuario, assim como a quantidade de dias pelos quais o 
 carro foi alugado. Calcule o preço a pagar, sabendo 
 que o carro custa R$60 por dia e R$0,15 por km rodado: """

km = int(input('Quantos km foram percorridos? '))
dias = int(input('Quantos dias foram percorridos? '))

valor = 60 * dias + 0.15 * km 
print(f'Km = {km}. Dias: {dias}.')
print(f'valor a ser pago: {valor}')

"""resultado no console:

Quantos km foram percorridos? 100
Quantos dias foram percorridos? 10
Km = 100. Dias: 10.
valor a ser pago: 615.0"""