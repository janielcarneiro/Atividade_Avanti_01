# Atividade_Avanti_01
Atividades do conteúdo do modulo 01 e 02 de Machine Learning 2023.2

1. Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.
2. Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas
3. Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.
4. Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.
5. Dada uma lista contendo números inteiros, como você encontraria o maior número e o menor número dessa lista em uma única passagem?
6. Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?
7. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?
8. Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?
9. Complete o código:



import __________.pyplot as plt

import numpy as ___


fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5),layout="constrained")


for ___ in range(2):

    for ___ in range(2):

        axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),

                               transform=axs[row, col].transAxes,

                               ha='center', va='center', ________=18,

                               color='darkgrey')

fig.suptitle('__.subplots()')



10. Complete o código:


import numpy as np

import __________ as mpl

import __________.______ as plt


x = np.________(-2 * np.pi, 2 * np.pi, 100)

y = np.____(x)


__, __ = plt.subplots()

ax.____(_, _)
