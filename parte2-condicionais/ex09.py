media = float(input("Digite a média do aluno: "))
if media >= 6:
    print(f"O aluno foi aprovado com a média de {media}")
if media < 4:
    print(f"O aluno foi reprovado com a média de {media}")
if media >= 4 and media < 6:
    print(f"O aluno está de recuperação com a média de {media}")