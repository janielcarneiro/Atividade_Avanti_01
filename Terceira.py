#função para encontrar o segundo maior valor na lista

def Procurar(lista):

    maior_valor = max(lista)
    lista.remove(maior_valor)

    segundo_maior_valor = max(lista)

    return segundo_maior_valor


lista = [2, 4, 8, 16, 32, 64, 128]

maior_valor = Procurar(lista)

print(f"Maior Valor encontrado: ", maior_valor)