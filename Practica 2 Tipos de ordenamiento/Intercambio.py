def bubble_sort(arr): # Define una función llamada bubble_sort que toma una lista 'arr' como argumento.
    """
    Ordena una lista de elementos utilizando el algoritmo de Bubble Sort (Ordenamiento de Burbuja). # Docstring: Describe la función.

    Args: # Docstring: Describe los argumentos.
        arr: La lista de elementos a ordenar. # Docstring: Especifica el argumento 'arr'.

    Returns: # Docstring: Describe lo que la función retorna.
        La lista ordenada. # Docstring: Especifica que retorna la lista ordenada.
    """
    n = len(arr) # Obtiene la longitud de la lista 'arr' y la guarda en 'n'.

    # Bucle exterior para controlar el número de pasadas necesarias.
    # Una lista de 'n' elementos requiere como máximo 'n-1' pasadas.
    for i in range(n - 1): # Itera 'n-1' veces, ya que en cada pasada un elemento se "burbujea" a su posición final.
        # Bandera para optimización: si no se hacen intercambios en una pasada, la lista ya está ordenada.
        swapped = False # Inicializa una bandera para detectar si se realizó algún intercambio en la pasada actual.

        # Bucle interior para comparar y intercambiar elementos adyacentes.
        # En cada pasada, el elemento más grande restante se mueve a su posición correcta al final.
        # La parte derecha de la lista (arr[n-1-i:]) ya estará ordenada después de 'i' pasadas.
        for j in range(n - 1 - i): # Itera hasta el final de la parte desordenada de la lista.
            # Compara el elemento actual con el siguiente.
            if arr[j] > arr[j + 1]: # Si el elemento actual es mayor que el siguiente...
                # Intercambia los elementos si están en el orden incorrecto.
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Realiza el intercambio de los valores.
                swapped = True # Establece la bandera 'swapped' a True, indicando que hubo un intercambio.

        # Si no hubo intercambios en esta pasada, la lista ya está ordenada y podemos salir.
        if not swapped: # Si la bandera 'swapped' sigue siendo False después del bucle interno...
            break # ...significa que la lista ya está ordenada, así que se rompe el bucle externo.

    return arr # Retorna la lista 'arr' una vez que ha sido completamente ordenada.



### Ejemplo de uso:


if __name__ == "__main__": # Esto asegura que el código dentro solo se ejecute cuando el script se corre directamente.
    lista_desordenada = [5, 1, 4, 2, 8] # Crea una lista de ejemplo desordenada.
    print(f"Lista desordenada: {lista_desordenada}") # Imprime la lista original.

    bubble_sort(lista_desordenada) # Llama a la función bubble_sort para ordenar la lista.
    print(f"Lista ordenada (Bubble Sort): {lista_desordenada}") # Imprime la lista ya ordenada.

    print("\n--- Otro ejemplo ---") # Imprime un separador para otro ejemplo.
    lista_grande = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 33] # Crea una lista más grande.
    print(f"Lista desordenada: {lista_grande}") # Imprime la lista grande desordenada.
    bubble_sort(lista_grande) # Ordena la lista grande (la modifica directamente ya que es mutable).
    print(f"Lista ordenada (Bubble Sort): {lista_grande}") # Imprime la lista grande ordenada.

    print("\n--- Ejemplo con lista casi ordenada ---") # Imprime un separador.
    lista_casi_ordenada = [1, 2, 4, 3, 5, 6] # Crea una lista casi ordenada.
    print(f"Lista casi ordenada: {lista_casi_ordenada}") # Imprime la lista casi ordenada.
    bubble_sort(lista_casi_ordenada) # Ordena la lista casi ordenada.
    print(f"Lista ordenada (Bubble Sort): {lista_casi_ordenada}") # Imprime la lista casi ordenada después de ordenarla.

    print("\n--- Ejemplo con lista ya ordenada ---") # Imprime un separador.
    lista_ya_ordenada = [1, 2, 3, 4, 5] # Crea una lista ya ordenada.
    print(f"Lista ya ordenada: {lista_ya_ordenada}") # Imprime la lista ya ordenada.
    bubble_sort(lista_ya_ordenada) # Intenta ordenar una lista ya ordenada (demuestra la optimización).
    print(f"Lista ordenada (Bubble Sort): {lista_ya_ordenada}") # Imprime la lista ya ordenada.

    print("\n--- Ejemplo con lista vacía ---") # Imprime un separador.
    lista_vacia = [] # Crea una lista vacía.
    print(f"Lista vacía: {lista_vacia}") # Imprime la lista vacía.
    bubble_sort(lista_vacia) # Intenta ordenar una lista vacía.
    print(f"Lista ordenada (Bubble Sort): {lista_vacia}") # Imprime la lista vacía (permanece vacía).

    print("\n--- Ejemplo con lista de un solo elemento ---") # Imprime un separador.
    lista_un_elemento = [7] # Crea una lista con un solo elemento.
    print(f"Lista de un solo elemento: {lista_un_elemento}") # Imprime la lista de un solo elemento.
    bubble_sort(lista_un_elemento) # Intenta ordenar una lista de un solo elemento.
    print(f"Lista ordenada (Bubble Sort): {lista_un_elemento}") # Imprime la lista de un solo elemento (permanece igual).
