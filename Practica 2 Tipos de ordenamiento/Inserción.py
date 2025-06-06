def insertion_sort(arr): # Define una función llamada insertion_sort que toma una lista 'arr' como argumento.
    """
    Ordena una lista de elementos utilizando el algoritmo de Insertion Sort. # Docstring: Describe la función.

    Args: # Docstring: Describe los argumentos.
        arr: La lista de elementos a ordenar. # Docstring: Especifica el argumento 'arr'.

    Returns: # Docstring: Describe lo que la función retorna.
        La lista ordenada. # Docstring: Especifica que retorna la lista ordenada.
    """
    n = len(arr) # Obtiene la longitud de la lista 'arr' y la guarda en 'n'.

    # Recorre todos los elementos de la lista, empezando por el segundo (índice 1)
    # ya que consideramos que el primer elemento (índice 0) ya está "ordenado"
    # dentro de su propio sub-arreglo de un solo elemento.
    for i in range(1, n): # Inicia un bucle que va desde el segundo elemento (índice 1) hasta el final de la lista.
        key = arr[i]  # Guarda el elemento actual en 'key' para insertarlo en su posición correcta.
        j = i - 1     # Inicializa 'j' para apuntar al último elemento de la parte ya ordenada (a la izquierda de 'key').

        # Mueve los elementos de arr[0..i-1] que son mayores que 'key'
        # una posición adelante de su posición actual
        while j >= 0 and key < arr[j]: # Bucle para comparar 'key' con los elementos a su izquierda y moverlos.
            arr[j + 1] = arr[j]  # Desplaza el elemento actual 'arr[j]' una posición a la derecha.
            j -= 1               # Decrementa 'j' para comparar con el siguiente elemento a la izquierda.

        arr[j + 1] = key  # Inserta 'key' en la posición correcta una vez que el bucle 'while' termina.

    return arr # Retorna la lista 'arr' una vez que ha sido completamente ordenada.

# --- Ejemplo de uso --- # Sección para demostrar cómo usar la función.
if __name__ == "__main__": # Esto asegura que el código dentro solo se ejecute cuando el script se corre directamente.
    lista_desordenada = [12, 11, 13, 5, 6] # Crea una lista de ejemplo desordenada.
    print(f"Lista desordenada: {lista_desordenada}") # Imprime la lista original.

    lista_ordenada = insertion_sort(lista_desordenada) # Llama a la función insertion_sort para ordenar la lista.
    print(f"Lista ordenada (Insertion Sort): {lista_ordenada}") # Imprime la lista ya ordenada.

    print("\n--- Otro ejemplo ---") # Imprime un separador para otro ejemplo.
    lista_grande = [64, 25, 12, 22, 11, 90, 78, 34, 45, 56, 1, 89] # Crea una lista más grande.
    print(f"Lista desordenada: {lista_grande}") # Imprime la lista grande desordenada.
    insertion_sort(lista_grande) # Ordena la lista grande (la modifica directamente ya que es mutable).
    print(f"Lista ordenada (Insertion Sort): {lista_grande}") # Imprime la lista grande ordenada.

    print("\n--- Ejemplo con lista casi ordenada ---") # Imprime un separador.
    lista_casi_ordenada = [1, 2, 4, 3, 5, 6] # Crea una lista casi ordenada.
    print(f"Lista casi ordenada: {lista_casi_ordenada}") # Imprime la lista casi ordenada.
    insertion_sort(lista_casi_ordenada) # Ordena la lista casi ordenada.
    print(f"Lista ordenada (Insertion Sort): {lista_casi_ordenada}") # Imprime la lista casi ordenada después de ordenarla.

    print("\n--- Ejemplo con lista ya ordenada ---") # Imprime un separador.
    lista_ya_ordenada = [1, 2, 3, 4, 5] # Crea una lista ya ordenada.
    print(f"Lista ya ordenada: {lista_ya_ordenada}") # Imprime la lista ya ordenada.
    insertion_sort(lista_ya_ordenada) # Intenta ordenar una lista ya ordenada (demuestra el mejor caso).
    print(f"Lista ordenada (Insertion Sort): {lista_ya_ordenada}") # Imprime la lista ya ordenada.

    print("\n--- Ejemplo con lista vacía ---") # Imprime un separador.
    lista_vacia = [] # Crea una lista vacía.
    print(f"Lista vacía: {lista_vacia}") # Imprime la lista vacía.
    insertion_sort(lista_vacia) # Intenta ordenar una lista vacía.
    print(f"Lista ordenada (Insertion Sort): {lista_vacia}") # Imprime la lista vacía (permanece vacía).

    print("\n--- Ejemplo con lista de un solo elemento ---") # Imprime un separador.
    lista_un_elemento = [7] # Crea una lista con un solo elemento.
    print(f"Lista de un solo elemento: {lista_un_elemento}") # Imprime la lista de un solo elemento.
    insertion_sort(lista_un_elemento) # Intenta ordenar una lista de un solo elemento.
    print(f"Lista ordenada (Insertion Sort): {lista_un_elemento}") # Imprime la lista de un solo elemento (permanece igual).