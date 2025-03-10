# programa para ler as duas notas de um aluno.
# calcular e imprimir a média

nota1 = float(input("Informe a primeira nota --> "))
nota2 = float(input("Informe a segunda nota --> "))

media = (nota1 + nota2) / 2

print(f'média = {media:.2f}')
if media >= 7:
    print('APROVADO')
else: 
    print('REPROVADO')
    
if media < 7:
    print('REPROVADO')
else:
    print('APROVADO')
    
    