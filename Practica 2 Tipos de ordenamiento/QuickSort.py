def quick_sort(arr): # Define la función principal para el Ordenamiento Rápido.
    """
    Ordena una lista de elementos utilizando el algoritmo de QuickSort.

    Args:
        arr: La lista de elementos a ordenar.

    Returns:
        La lista ordenada.
    """
    # Función auxiliar recursiva para QuickSort
    def _quick_sort_recursive(arr, low, high): # Define una función interna recursiva que toma la lista, un índice bajo y un índice alto.
        if low < high: # Caso base: si el sub-arreglo tiene 0 o 1 elemento, ya está ordenado (low >= high).
            # pi es el índice de partición, arr[pi] está ahora en su lugar correcto
            pi = partition(arr, low, high) # Llama a la función de particionamiento para encontrar la posición del pivote.

            # Ordena recursivamente los elementos antes y después de la partición
            _quick_sort_recursive(arr, low, pi - 1) # Llama a QuickSort para el sub-arreglo izquierdo del pivote.
            _quick_sort_recursive(arr, pi + 1, high) # Llama a QuickSort para el sub-arreglo derecho del pivote.

    # Llama a la función recursiva inicial con toda la lista.
    _quick_sort_recursive(arr, 0, len(arr) - 1) # Inicia el proceso de ordenamiento recursivo.
    return arr # Retorna la lista modificada (ordenada in-place).

def partition(arr, low, high): # Define la función de particionamiento.
    """
    Toma el último elemento como pivote, coloca el pivote en su posición correcta
    en el arreglo ordenado, y coloca todos los elementos más pequeños antes
    del pivote y todos los elementos más grandes después del pivote.
    """
    pivot = arr[high] # Elige el último elemento como pivote (una estrategia común).
    i = (low - 1) # Inicializa 'i' como el índice del elemento más pequeño.

    for j in range(low, high): # Recorre la lista desde 'low' hasta 'high-1' (sin incluir el pivote).
        # Si el elemento actual es menor o igual que el pivote
        if arr[j] <= pivot: # Compara el elemento actual con el pivote.
            i += 1 # Incrementa el índice del elemento más pequeño.
            arr[i], arr[j] = arr[j], arr[i] # Intercambia arr[i] y arr[j].

    # Coloca el pivote en su posición correcta.
    arr[i + 1], arr[high] = arr[high], arr[i + 1] # Intercambia el pivote con el elemento en (i+1).
    return (i + 1) # Retorna el índice donde el pivote ha sido colocado.

---
### Ejemplo de Uso

```python
if __name__ == "__main__": # Esto asegura que el código dentro solo se ejecute cuando el script se corre directamente.
    lista_desordenada = [10, 7, 8, 9, 1, 5] # Crea una lista de ejemplo desordenada.
    print(f"Lista desordenada: {lista_desordenada}") # Imprime la lista original.

    quick_sort(lista_desordenada) # Llama a la función quick_sort para ordenar la lista (modifica in-place).
    print(f"Lista ordenada (QuickSort): {lista_desordenada}") # Imprime la lista ya ordenada.

    print("\n--- Otro ejemplo ---") # Imprime un separador para otro ejemplo.
    lista_grande = [64, 25, 12, 22, 11, 90, 78, 34, 45, 56, 1, 89] # Crea una lista más grande.
    print(f"Lista desordenada: {lista_grande}") # Imprime la lista grande desordenada.
    quick_sort(lista_grande) # Ordena la lista grande.
    print(f"Lista ordenada (QuickSort): {lista_grande}") # Imprime la lista grande ordenada.

    print("\n--- Ejemplo con lista casi ordenada ---") # Imprime un separador.
    lista_casi_ordenada = [1, 2, 4, 3, 5, 6] # Crea una lista casi ordenada.
    print(f"Lista casi ordenada: {lista_casi_ordenada}") # Imprime la lista casi ordenada.
    quick_sort(lista_casi_ordenada) # Ordena la lista casi ordenada.
    print(f"Lista ordenada (QuickSort): {lista_casi_ordenada}") # Imprime la lista casi ordenada después de ordenarla.

    print("\n--- Ejemplo con lista ya ordenada (peor caso para este pivote) ---") # Imprime un separador.
    lista_ya_ordenada = [1, 2, 3, 4, 5] # Crea una lista ya ordenada.
    print(f"Lista ya ordenada: {lista_ya_ordenada}") # Imprime la lista ya ordenada.
    quick_sort(lista_ya_ordenada) # Ordena una lista ya ordenada.
    print(f"Lista ordenada (QuickSort): {lista_ya_ordenada}") # Imprime la lista ya ordenada.

    print("\n--- Ejemplo con lista vacía ---") # Imprime un separador.
    lista_vacia = [] # Crea una lista vacía.
    print(f"Lista vacía: {lista_vacia}") # Imprime la lista vacía.
    quick_sort(lista_vacia) # Intenta ordenar una lista vacía.
    print(f"Lista ordenada (QuickSort): {lista_vacia}") # Imprime la lista vacía (permanece vacía).

    print("\n--- Ejemplo con lista de un solo elemento ---") # Imprime un separador.
    lista_un_elemento = [7] # Crea una lista con un solo elemento.
    print(f"Lista de un solo elemento: {lista_un_elemento}") # Imprime la lista de un solo elemento.
    quick_sort(lista_un_elemento) # Intenta ordenar una lista de un solo elemento.
    print(f"Lista ordenada (QuickSort): {lista_un_elemento}") # Imprime la lista de un solo elemento.