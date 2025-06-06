def merge_sort(arr): # Define la función principal para el ordenamiento por mezcla.
    """
    Ordena una lista de elementos utilizando el algoritmo de Merge Sort (Ordenamiento por Mezcla). # Docstring: Describe la función.

    Args: # Docstring: Describe los argumentos.
        arr: La lista de elementos a ordenar. # Docstring: Especifica el argumento 'arr'.

    Returns: # Docstring: Describe lo que la función retorna.
        La lista ordenada. # Docstring: Especifica que retorna la lista ordenada.
    """
    if len(arr) <= 1: # Caso base de la recursión: si la lista tiene 0 o 1 elemento, ya está ordenada.
        return arr # Retorna la lista tal cual.

    # Divide la lista en dos mitades (aproximadamente iguales).
    mid = len(arr) // 2 # Calcula el punto medio de la lista.
    left_half = arr[:mid] # Crea la mitad izquierda de la lista.
    right_half = arr[mid:] # Crea la mitad derecha de la lista.

    # Llama recursivamente a merge_sort en ambas mitades.
    left_half = merge_sort(left_half) # Ordena recursivamente la mitad izquierda.
    right_half = merge_sort(right_half) # Ordena recursivamente la mitad derecha.

    # Combina las dos mitades ordenadas.
    return merge(left_half, right_half) # Llama a la función 'merge' para combinar las mitades y retorna el resultado.

def merge(left, right): # Define la función auxiliar para mezclar dos listas ordenadas.
    """
    Combina dos listas ordenadas en una sola lista ordenada. # Docstring: Describe la función.

    Args: # Docstring: Describe los argumentos.
        left: La primera lista ordenada. # Docstring: Especifica el argumento 'left'.
        right: La segunda lista ordenada. # Docstring: Especifica el argumento 'right'.

    Returns: # Docstring: Describe lo que la función retorna.
        Una nueva lista que es la combinación ordenada de 'left' y 'right'. # Docstring: Especifica lo que retorna.
    """
    result = [] # Inicializa una lista vacía para almacenar la lista combinada.
    i = 0 # Inicializa el índice para recorrer la lista 'left'.
    j = 0 # Inicializa el índice para recorrer la lista 'right'.

    # Compara elementos de ambas listas y los añade a 'result' en orden.
    while i < len(left) and j < len(right): # Mientras haya elementos en ambas listas para comparar.
        if left[i] < right[j]: # Si el elemento de la izquierda es menor.
            result.append(left[i]) # Añade el elemento de la izquierda a 'result'.
            i += 1 # Avanza al siguiente elemento en la lista 'left'.
        else: # Si el elemento de la derecha es menor o igual.
            result.append(right[j]) # Añade el elemento de la derecha a 'result'.
            j += 1 # Avanza al siguiente elemento en la lista 'right'.

    # Añade los elementos restantes de la lista 'left' (si los hay).
    while i < len(left): # Si quedan elementos en 'left'.
        result.append(left[i]) # Añádelos directamente a 'result' (ya están ordenados).
        i += 1 # Avanza al siguiente elemento en la lista 'left'.

    # Añade los elementos restantes de la lista 'right' (si los hay).
    while j < len(right): # Si quedan elementos en 'right'.
        result.append(right[j]) # Añádelos directamente a 'result' (ya están ordenados).
        j += 1 # Avanza al siguiente elemento en la lista 'right'.

    return result # Retorna la lista combinada y ordenada.

---
### Ejemplo de Uso

```python
if __name__ == "__main__": # Esto asegura que el código dentro solo se ejecute cuando el script se corre directamente.
    lista_desordenada = [38, 27, 43, 3, 9, 82, 10] # Crea una lista de ejemplo desordenada.
    print(f"Lista desordenada: {lista_desordenada}") # Imprime la lista original.

    lista_ordenada = merge_sort(lista_desordenada) # Llama a la función merge_sort para ordenar la lista.
    print(f"Lista ordenada (Merge Sort): {lista_ordenada}") # Imprime la lista ya ordenada.

    print("\n--- Otro ejemplo ---") # Imprime un separador para otro ejemplo.
    lista_grande = [64, 25, 12, 22, 11, 90, 78, 34, 45, 56, 1, 89] # Crea una lista más grande.
    print(f"Lista desordenada: {lista_grande}") # Imprime la lista grande desordenada.
    lista_ordenada_grande = merge_sort(lista_grande) # Ordena la lista grande.
    print(f"Lista ordenada (Merge Sort): {lista_ordenada_grande}") # Imprime la lista grande ordenada.

    print("\n--- Ejemplo con lista casi ordenada ---") # Imprime un separador.
    lista_casi_ordenada = [1, 2, 4, 3, 5, 6] # Crea una lista casi ordenada.
    print(f"Lista casi ordenada: {lista_casi_ordenada}") # Imprime la lista casi ordenada.
    lista_ordenada_casi = merge_sort(lista_casi_ordenada) # Ordena la lista casi ordenada.
    print(f"Lista ordenada (Merge Sort): {lista_ordenada_casi}") # Imprime la lista casi ordenada después de ordenarla.

    print("\n--- Ejemplo con lista ya ordenada ---") # Imprime un separador.
    lista_ya_ordenada = [1, 2, 3, 4, 5] # Crea una lista ya ordenada.
    print(f"Lista ya ordenada: {lista_ya_ordenada}") # Imprime la lista ya ordenada.
    lista_ordenada_ya = merge_sort(lista_ya_ordenada) # Ordena una lista ya ordenada.
    print(f"Lista ordenada (Merge Sort): {lista_ordenada_ya}") # Imprime la lista ya ordenada.

    print("\n--- Ejemplo con lista vacía ---") # Imprime un separador.
    lista_vacia = [] # Crea una lista vacía.
    print(f"Lista vacía: {lista_vacia}") # Imprime la lista vacía.
    lista_ordenada_vacia = merge_sort(lista_vacia) # Ordena una lista vacía.
    print(f"Lista ordenada (Merge Sort): {lista_ordenada_vacia}") # Imprime la lista vacía.

    print("\n--- Ejemplo con lista de un solo elemento ---") # Imprime un separador.
    lista_un_elemento = [7] # Crea una lista con un solo elemento.
    print(f"Lista de un solo elemento: {lista_un_elemento}") # Imprime la lista de un solo elemento.
    lista_ordenada_un_elemento = merge_sort(lista_un_elemento) # Ordena una lista de un solo elemento.
    print(f"Lista ordenada (Merge Sort): {lista_ordenada_un_elemento}") # Imprime la lista de un solo elemento.

