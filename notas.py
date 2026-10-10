notas = []

tot = int(input("Quantas notas deseja colocar? "))

for i in range(1, tot + 1):
    num = float(input(f"Nota {i}: "))
    notas.append(num)

maior = notas[0]
menor = notas[0]

contmax = 0
contmin = 0
media = 0

for j in notas:

    if j > maior:
        maior = j

    if j < menor:
        menor = j

    if j >= 6:
        contmax += 1
    else:
        contmin += 1

    media += j

media = media / tot

print(f"A média foi {media}")
print(f"A maior nota foi {maior}")
print(f"A menor nota foi {menor}")
print(f"O total de notas maiores ou iguais a 6 foi {contmax}")
print(f"O total de notas menores que 6 foi {contmin}")

if media >= 7:
    print(f"\033[32m{media} - Bom desempenho!\033[m")

elif media >= 5:
    print(f"\033[34m{media} - Desempenho regular\033[m")

else:
    print(f"\033[31m{media} - Desempenho baixo\033[m")