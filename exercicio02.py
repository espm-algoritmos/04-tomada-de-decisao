# entrada das notas
prova1 = float(input("Informe a nota da primeira prova: "))
prova2 = float(input("Informe a nota da segunda prova: "))
trabalho1 = float(input("Informe a nota do primeiro trabalho: "))
trabalho2 = float(input("Informe a nota do segundo trabalho: "))

# cálculo das médias
media_prova = (prova1 + prova2) / 2 * 0.7
media_trabalho = (trabalho1 + trabalho2) / 2 * 0.3
media_final = media_prova + media_trabalho
print(f'média final = {media_final:.2f}')

# verificação da situação do aluno
if media_final < 7:
    print("REPROVADO")
else:
    print("APROVADO")