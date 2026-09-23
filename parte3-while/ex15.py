positivos = 0
numero = float(input("Digite um número (ou 0 para parar): "))
while numero != 0:
    if numero > 0:
        positivos = positivos + 1
    numero = float(input("Digite um número (ou 0 para sair): "))
print(f"Quantidade de números positivos digitados: {positivos}")