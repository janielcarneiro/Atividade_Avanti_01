##Algoritmo para receber tupla, retornar ordenada pelo nome


def Ordenar_Tuplas(tuplas):
    lista_ordenada = {}
    t = dict(sorted(tuplas.items()))
    lista_ordenada.update(t)
    return lista_ordenada
    
d = {'Janiel':22, 'Alessandro':31, 'layane':14, 'Chico': 7}

retorno = Ordenar_Tuplas(d)
print(f"Retorno: {retorno}")