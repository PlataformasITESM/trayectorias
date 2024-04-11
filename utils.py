import numpy as np
import pandas as pd

def contienen_a(matriz, vector):
    """
    Función que obtiene todos las filas de la matriz que contienen al vector.
    """
    return np.all((matriz *vector) == vector, axis = 1)

def subconjuntos_de(matriz, vector):
    """
    Función que obtiene todos las filas de la matriz que son subconjuntos del vector.
    """
    return np.all((matriz *vector) == matriz, axis = 1)

def obtener_conjuntos_base(matriz_ori):
    """
    Función que obtiene los conjuntos base de una matriz binaria. Los conjuntos base
    son aquellos que no contienen a ninguno de los otros conjuntos.

    Parámetros
    ----------
    matriz_ori: np.array
        matriz de forma n_conjuntos, n_elementos

    Retorna
    -------
    conjuntos_base: list
        Lista de índices de conjuntos base de la matriz
    """
    matriz = matriz_ori.copy()
    # Índices de conjuntos que quedan por analizar
    index_remaining = np.arange(matriz.shape[0])
    # Inicialización de lista vacía de conjuntos base a retornar
    conjuntos_base = []
    # Se itera eliminando conjuntos de la matriz hasta que esté vacía
    while matriz.shape[0] > 0:
        # Se agregan los conjuntos más pequeños a los conjuntos base (por definición son base).
        n_elementos = matriz.sum(1).min()
        # Máscara de conjuntos más pequeños
        son_base = matriz.sum(axis = 1) == n_elementos
        conjuntos_base += index_remaining[son_base].tolist()
        # Se almacenan aquellos conjuntos recién agregados a los base
        matriz_filt = matriz[son_base]
        # Se eliminan de la matriz los conjuntos recién agregados a los base.
        index_remaining = index_remaining[~son_base]
        matriz      = matriz[~son_base]
        # Se itera sobre los conjuntos recién agregados a los base.
        for vector in matriz_filt:
            # Por cada conjunto base, se eliminan de la matriz todos los que lo contienen, ya que
            # no pueden ser conjuntos base
            son_subconjuntos = contienen_a(matriz, vector)
            index_remaining = index_remaining[~son_subconjuntos]
            matriz = matriz[~son_subconjuntos]
    return conjuntos_base

