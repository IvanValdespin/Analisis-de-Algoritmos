"""Problema: Se tiene una "bolsa de valores" precios de articulos en el que se esta permitido
   comprar solo uno. Los precios varian a diario. Se pueden vender en otro día de la compra
   La meta es obtener la máxima ganancia. Se tiene la ventaja de saber los precios anticipadamente"""

import math as mt

def find_max_cruz_subarray(elements: list, low:int, middle:int, hight:int) -> int:
    """Encuentra el arreglo cruzado máximo.
    
    Args:
        elements: arreglo de la diferencia de precios por día
        low: Cantidad mínima de elementos
        high
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

    #Obtención de la suma máxima del lado izquierdo
    for index in range(middle-1,low,-1):
        suma += elements[index]
        if suma > left_sum:
            left_sum = suma
            max_left = index
    suma = 0

    #Obtención de la suma máxima del lado derecho
    for index in range(middle, high):
        suma += elements[index]
        if suma > right_sum:
            right_sum = suma
            max_right = index
    
    total_sum = left_sum + right_sum
    
    return(max_left, max_right, total_sum)


def find_max_subarray(elements: list, low:int, high:int) -> int:
    print(low, high)
    if low == high:
        return( low, high, elements[low])
    else:
        print("Entro")
        middle = mt.floor((low + high)/2)
        low_left, high_left, suma_left = find_max_subarray(elements, low, middle)
        low_right, high_right, suma_right = find_max_subarray(elements, middle-1, high)
        low_cross, high_cross, suma_cross = find_max_cruz_subarray(elements, low, middle, high)

    if suma_left >= suma_right and suma_left >= suma_cross:
        print("Entro 1")
        return (low_left, high_left, suma_left)
    if suma_right >= suma_left and suma_right >= suma_cross:
        print("Entro 2")
        return (low_right, high_right, suma_right)
    else:
        print("Entro 3")
        return (low_cross, high_cross, suma_cross)





#Prueba de resultados obtenidos
elements = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7,-12]
low = 0
high = len(elements)
middle = mt.floor(high/2)

print(find_max_cruz_subarray(elements, low, middle, high))
print(find_max_subarray(elements, low, high))

    

