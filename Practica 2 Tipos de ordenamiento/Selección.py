def selection_sort(arr): # Define una función llamada selection_sort que toma una lista 'arr' como argumento.
    """
    Ordena una lista de elementos utilizando el algoritmo de Selection Sort. # Docstring: Describe la función.

    Args: # Docstring: Describe los argumentos.
        arr: La lista de elementos a ordenar. # Docstring: Especifica el argumento 'arr'.

    Returns: # Docstring: Describe lo que la función retorna.
        La lista ordenada. # Docstring: Especifica que retorna la lista ordenada.
    """
    n = len(arr) # Obtiene la longitud de la lista 'arr' y la guarda en 'n'.

    # Recorre toda la lista. El bucle externo es para la posición actual del elemento a ordenar.
    for i in range(n): # Itera desde el primer elemento (índice 0) hasta el último.

        # Encuentra el índice del elemento mínimo en la parte no ordenada de la lista.
        min_idx = i # Inicializa 'min_idx' con el índice de la posición actual.

        # Itera a través de la parte no ordenada de la lista para encontrar el mínimo.
        for j in range(i + 1, n): # El bucle interno busca el elemento más pequeño desde 'i+1' hasta el final.
            if arr[j] < arr[min_idx]: # Compara el elemento actual 'arr[j]' con el mínimo encontrado hasta ahora.
                min_idx = j # Si 'arr[j]' es menor, actualiza 'min_idx' al índice de 'arr[j]'.

        # Intercambia el elemento mínimo encontrado con el primer elemento de la parte no ordenada.
        # Esto coloca el elemento mínimo en su posición correcta en la parte ordenada.
        arr[i], arr[min_idx] = arr[min_idx], arr[i] # Realiza el intercambio de los valores.

    return arr # Retorna la lista 'arr' una vez que ha sido completamente ordenada.

# --- Ejemplo de uso --- # Sección para demostrar cómo usar la función.
if __name__ == "__main__": # Esto asegura que el código dentro solo se ejecute cuando el script se corre directamente.
    lista_desordenada = [64, 25, 12, 22, 11] # Crea una lista de ejemplo desordenada.
    print(f"Lista desordenada: {lista_desordenada}") # Imprime la lista original.

    selection_sort(lista_desordenada) # Llama a la función selection_sort para ordenar la lista.
    print(f"Lista ordenada (Selection Sort): {lista_desordenada}") # Imprime la lista ya ordenada.

    print("\n--- Otro ejemplo ---") # Imprime un separador para otro ejemplo.
    lista_grande = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 33] # Crea una lista más grande.
    print(f"Lista desordenada: {lista_grande}") # Imprime la lista grande desordenada.
    selection_sort(lista_grande) # Ordena la lista grande (la modifica directamente ya que es mutable).
    print(f"Lista ordenada (Selection Sort): {lista_grande}") # Imprime la lista grande ordenada.

    print("\n--- Ejemplo con lista casi ordenada ---") # Imprime un separador.
    lista_casi_ordenada = [1, 2, 4, 3, 5, 6] # Crea una lista casi ordenada.
    print(f"Lista casi ordenada: {lista_casi_ordenada}") # Imprime la lista casi ordenada.
    selection_sort(lista_casi_ordenada) # Ordena la lista casi ordenada.
    print(f"Lista ordenada (Selection Sort): {lista_casi_ordenada}") # Imprime la lista casi ordenada después de ordenarla.

    print("\n--- Ejemplo con lista ya ordenada ---") # Imprime un separador.
    lista_ya_ordenada = [1, 2, 3, 4, 5] # Crea una lista ya ordenada.
    print(f"Lista ya ordenada: {lista_ya_ordenada}") # Imprime la lista ya ordenada.
    selection_sort(lista_ya_ordenada) # Intenta ordenar una lista ya ordenada.
    print(f"Lista ordenada (Selection Sort): {lista_ya_ordenada}") # Imprime la lista ya ordenada.

    print("\n--- Ejemplo con lista vacía ---") # Imprime un separador.
    lista_vacia = [] # Crea una lista vacía.
    print(f"Lista vacía: {lista_vacia}") # Imprime la lista vacía.
    selection_sort(lista_vacia) # Intenta ordenar una lista vacía.
    print(f"Lista ordenada (Selection Sort): {lista_vacia}") # Imprime la lista vacía (permanece vacía).

    print("\n--- Ejemplo con lista de un solo elemento ---") # Imprime un separador.
    lista_un_elemento = [7] # Crea una lista con un solo elemento.
    print(f"Lista de un solo elemento: {lista_un_elemento}") # Imprime la lista de un solo elemento.
    selection_sort(lista_un_elemento) # Intenta ordenar una lista de un solo elemento.
    print(f"Lista ordenada (Selection Sort): {lista_un_elemento}") # Imprime la lista de un solo elemento (permanece igual).