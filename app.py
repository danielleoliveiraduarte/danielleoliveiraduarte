# Programa de calculo de media de notas
# Autor: Danielle de Oliveira Duarte

# Entrada
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Processamento
media = (nota1 + nota2) / 2

# Saida
print(f"\nAluno: {nome}")
print(f"Média: {media:.2f}")

if media >=6:
    print("Situacao: Aprovado")
else:
    print("Situacao: Reprovado")


