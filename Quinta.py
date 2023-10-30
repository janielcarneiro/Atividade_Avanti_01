#encontrar o maior e menor numero


def encontrar_maior_e_menor(lista):

    maior = lista[0]
    menor = lista[0]

    for valor in lista:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor

    return maior, menor

lista = [1, 5, 2, 3, 90, 0]

maior, menor = encontrar_maior_e_menor(lista)

print(f"Menor Valor encontrado: {menor}  Maior:{maior}")



