numeros = [1, 10, 100, 1000, 10000]
maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
print(f"O maior número da lista é: {maior}")