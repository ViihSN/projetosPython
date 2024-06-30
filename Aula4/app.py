"""Exercicio facul
 Desenvolva um algoritmo que solicite ao
 usuario o preço de um produto e um percentual de 
 desconto a ser aplicado a ele. Calcule e exiba o valor 
 do desconto e o preço final do produto.
"""
valorProduto = float(input('Digite o preço do produto:'))
percentual = float(input('Digite o percentual de desconto (0-100%): '))

desconto = valorProduto * (percentual / 100)
valorFinal = valorProduto - desconto

print(f'O preço do produto é {valorProduto}. O desconto é de {percentual}%')
print(f'O valor calculado de desconto: {desconto}. O valor final do produto é: {valorFinal}')


"""resultado no console:

Digite o preço do produto:100
Digite o percentual de desconto (0-100%): 30
O preço do produto é 100.0. O desconto é de 30.0%
O valor calculado de desconto: 30.0. O valor final do produto é: 70.0"""