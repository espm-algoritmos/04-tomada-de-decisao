# entrada de dados
lado1 = int(input("valor do lado 1 --> "))
lado2 = int(input("valor do lado 2 --> "))
lado3 = int(input("valor do lado 3 --> "))

# é um triângulo?
if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
    print('É um triângulo')
else:
    print('Não é um triângulo')