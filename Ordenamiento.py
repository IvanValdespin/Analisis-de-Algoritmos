"""Ivan Giobanni Valdespin Garcia
   06.09.2021"""




def insercion(elements: list)->list:

    """Algoritmo de ordenamiento por insercion
    Este algoritmo inicia desde la segunda posicion del segundo elemento del arreglo
    En el mejor de los caso el arreglo esta ordenado y solo hace una corrida, por lo cual la complejidad es O(n)
    El peor tiempo de ejecución es cuando todo el arreglo esta invertido por lo cual la complejidad es O(n²)
   args:
      elements: Lista de elementos a ordenar
   returns:
      elements: Lista ordenada
"""

    #Si el arreglo de elementos es menor a 2 elementos, entonces el arreglo esta ordenado
    if len(elements) <= 1:
        return elements
    
    for position in range(1,len(elements)):
        key = elements[position]
        previous = position - 1
        #Inserta elements[position] en la secuencia ordenada elements[1...j-1]
        while previous >= 0 and elements[previous] > key:
            elements[previous + 1] = elements[previous]
            previous -= 1
        elements[previous + 1] = key
    return elements

def seleccion(elements:int) -> list:
    """Algoritmo de ordenamiento por selección"""

    for index in range(len(elements)):
        smallest = elements[index]
        position = index
        for index2 in range(index, len(elements)):
            if elements[index2] < smallest:
                smallest = elements[index2]
                position = index2
        elements[position] = elements[index]
        elements[index] = smallest
    
    return elements


