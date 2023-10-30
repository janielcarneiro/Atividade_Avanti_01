#vai receber duas listas e retornar os elementos
#que não se repete em nenhuma das duas

def Lista_Limpa(lista1, lista2):
    #Juntar as duas listas
    lista_completa = lista1 + lista2

    #set = serve para remover elementos duplicados
    conjunto = set(lista_completa)

    #transformar em uma lista
    lista_limpa = list(conjunto)

    return lista_limpa

lista_1 = [2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
lista_2 = [7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12]

lista_sem_repeticao = Lista_Limpa(lista_1, lista_2)

print(f"Lista_1 e Lista_2: {lista_sem_repeticao}");