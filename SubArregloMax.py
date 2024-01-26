"""Problema: Se tiene una "bolsa de valores" precios de articulos en el que se esta permitido
   comprar solo uno. Los precios varian a diario. Se pueden vender en otro día de la compra
   La meta es obtener la máxima ganancia. Se tiene la ventaja de saber los precios anticipadamente"""

import math as mt

def find_max_cruz_subarray(elements: list) -> int:
    """Encuentra el arreglo cruzado máximo.
    
    Args:
        elements: arreglo de elementos a analizar
    Returns:
        max_left: Día ideal para comprar
        max_right: Día ideal para vender
        total_sum: Ganancia total máxima en la serie de tiempo.

    """
    #Definiendo variables a utilizar
    left_sum = -mt.inf
    right_sum = -mt.inf
    max_left = 0
    max_right = 0
    suma = 0
    down = 0
    high = len(elements)
    medium = mt.floor(high/2)

    #Obtención de la suma máxima del lado izquierdo
    for index in range(medium-1,down,-1):
        suma += elements[index]
        if suma > left_sum:
            left_sum = suma
            max_left = index
    suma = 0

    #Obtención de la suma máxima del lado derecho
    for index in range(medium, high):
        suma += elements[index]
        if suma > right_sum:
            right_sum = suma
            max_right = index
    
    total_sum = left_sum + right_sum
    
    return(max_left, max_right, total_sum)








#Prueba de resultados obtenidos
a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(find_max_cruz_subarray(a))

    

