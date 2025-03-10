from math import sqrt

# entrada de dados
x = float(input("Informe o valor de x "))

# verifica se o valor de x é válido
if x > 5 or x < -5:
    y = (x - 8) / sqrt(x ** 2 - 25)
    print(f'y = {y:.4f}')
else:
    print('valor inválido para x')
    
    
    
    
    
    
# verifica se o valor de x é inválido
if x <= 5 and x >= -5:
    print('valor inválido para x')
else:
    y = (x - 8) / sqrt(x ** 2 - 25)
    print(f'y = {y:.4f}')