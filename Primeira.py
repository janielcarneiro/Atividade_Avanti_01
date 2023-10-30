#Algoritmo para Verficar se o Numero e Primo
# Retornar uma Lista de numeros primos

def Retornar_Primos(lista):
    lista_primos = [];
    for numero in lista:
        if numero <= 1:
            continue
        primo = True

        for i in range(2, numero):
            if(numero % i == 0):
                primo = False
                break
        if primo == True:
            lista_primos.append(numero)
    return lista_primos
        
lista = [1, 4, 5, 7, 13, 
         9, 2, 15, 17, 19, 
         21, 23, 29, 31, 33
        ];

verificar_primo = Retornar_Primos(lista)

print(f"Numeros Primos: {verificar_primo}")

