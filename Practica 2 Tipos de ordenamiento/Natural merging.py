def natural_merging(arr): # Define la función principal para el Ordenamiento por Fusión Natural.
    """
    Ordena una lista de elementos utilizando el algoritmo de Fusión Natural (Natural Merging).

    Args:
        arr: La lista de elementos a ordenar.

    Returns:
        La lista ordenada.
    """
    n = len(arr) # Obtiene la longitud de la lista.
    if n <= 1: # Si la lista tiene 0 o 1 elemento, ya está ordenada.
        return arr # Retorna la lista tal cual.

    # Lista temporal para almacenar los resultados de la mezcla.
    temp_arr = [0] * n # Crea una lista temporal del mismo tamaño que la original.

    # Variable para controlar si la lista está completamente ordenada.
    # Será True si en una pasada no se realiza ninguna fusión (ya solo hay un tramo).
    is_sorted = False # Inicializa la bandera de ordenamiento.

    # Bucle principal: Continúa hasta que la lista esté completamente ordenada (is_sorted = True).
    while not is_sorted: # Este bucle se ejecuta al menos una vez y hasta que la lista esté ordenada.
        is_sorted = True # Asume que la lista está ordenada al inicio de cada pasada.

        # Encuentra el inicio del primer tramo.
        left_start = 0 # Inicializa el índice de inicio del tramo izquierdo.

        # Itera para encontrar y mezclar pares de tramos.
        while left_start < n - 1: # Mientras haya al menos dos elementos para formar un tramo.
            # 1. Encontrar el final del primer tramo (left_run_end).
            # Un tramo termina cuando el siguiente elemento es menor (rompe el orden ascendente).
            left_run_end = left_start # El final del tramo izquierdo comienza en su inicio.
            while left_run_end < n - 1 and arr[left_run_end] <= arr[left_run_end + 1]: # Mientras el orden se mantenga.
                left_run_end += 1 # Avanza el final del tr tramo izquierdo.

            # Si left_run_end es el último elemento, solo queda un tramo en este par,
            # o es el último tramo de la lista, ya no hay más para mezclar en esta pasada.
            if left_run_end == n - 1: # Si el primer tramo llega hasta el final de la lista.
                break # Sale del bucle interno, no hay un segundo tramo para mezclar.

            # 2. Encontrar el final del segundo tramo (right_run_end).
            # El segundo tramo comienza justo después del primero.
            right_start = left_run_end + 1 # El inicio del tramo derecho es el siguiente elemento.
            right_run_end = right_start # El final del tramo derecho comienza en su inicio.
            while right_run_end < n - 1 and arr[right_run_end] <= arr[right_run_end + 1]: # Mientras el orden se mantenga.
                right_run_end += 1 # Avanza el final del tramo derecho.

            # Realiza la fusión de los dos tramos encontrados.
            _merge(arr, temp_arr, left_start, left_run_end, right_run_end) # Llama a la función auxiliar _merge para fusionar.

            # Si se realizó una fusión, la lista aún no está completamente ordenada.
            is_sorted = False # Indica que se realizó una fusión, por lo que se necesita otra pasada.

            # Mueve el inicio para buscar el siguiente par de tramos.
            left_start = right_run_end + 1 # El nuevo inicio para buscar tramos es después del tramo derecho fusionado.

    return arr # Retorna la lista ya ordenada.

def _merge(arr, temp_arr, left, mid, right): # Función auxiliar para mezclar dos sub-arreglos (idéntica a Straight Merging).
    """
    Combina dos sub-arreglos ordenados de 'arr' en 'temp_arr' y luego los copia de vuelta a 'arr'.
    El primer sub-arreglo es arr[left..mid].
    El segundo sub-arreglo es arr[mid+1..right].
    """
    i = left # Índice para el sub-arreglo izquierdo.
    j = mid + 1 # Índice para el sub-arreglo derecho.
    k = left # Índice para la lista temporal 'temp_arr'.

    # Compara elementos de ambas sublistas y los añade a 'temp_arr' en orden.
    while i <= mid and j <= right: # Mientras haya elementos en ambas sublistas para comparar.
        if arr[i] <= arr[j]: # Si el elemento del sub-arreglo izquierdo es menor o igual.
            temp_arr[k] = arr[i] # Añade el elemento a 'temp_arr'.
            i += 1 # Avanza al siguiente elemento en el sub-arreglo izquierdo.
        else: # Si el elemento del sub-arreglo derecho es menor.
            temp_arr[k] = arr[j] # Añade el elemento a 'temp_arr'.
            j += 1 # Avanza al siguiente elemento en el sub-arreglo derecho.
        k += 1 # Avanza al siguiente espacio en 'temp_arr'.

    # Copia los elementos restantes del sub-arreglo izquierdo (si los hay).
    while i <= mid: # Si quedan elementos en el sub-arreglo izquierdo.
        temp_arr[k] = arr[i] # Añádelos directamente a 'temp_arr'.
        i += 1 # Avanza el índice del sub-arreglo izquierdo.
        k += 1 # Avanza el índice de 'temp_arr'.

    # Copia los elementos restantes del sub-arreglo derecho (si los hay).
    while j <= right: # Si quedan elementos en el sub-arreglo derecho.
        temp_arr[k] = arr[j] # Añádelos directamente a 'temp_arr'.
        j += 1 # Avanza el índice del sub-arreglo derecho.
        k += 1 # Avanza el índice de 'temp_arr'.

    # Copia los elementos de 'temp_arr' de vuelta a 'arr' en las posiciones correctas.
    for idx in range(left, right + 1): # Itera sobre el rango que acaba de ser mezclado.
        arr[idx] = temp_arr[idx] # Copia los elementos ordenados de vuelta a la lista original.

---
### Ejemplo de Uso

```python
if __name__ == "__main__": # Esto asegura que el código dentro solo se ejecute cuando el script se corre directamente.
    lista_desordenada = [1, 5, 2, 6, 9, 3, 4, 7] # Lista con tramos naturales: [1,5], [2,6,9], [3,4,7]
    print(f"Lista desordenada: {lista_desordenada}") # Imprime la lista original.

    natural_merging(lista_desordenada) # Llama a la función natural_merging para ordenar la lista.
    print(f"Lista ordenada (Natural Merging): {lista_desordenada}") # Imprime la lista ya ordenada.

    print("\n--- Otro ejemplo con más tramos ---") # Imprime un separador.
    lista_con_tramos = [8, 1, 3, 2, 4, 0, 5, 6, 7] # Tramos: [8], [1,3], [2,4], [0,5,6,7]
    print(f"Lista desordenada: {lista_con_tramos}") # Imprime la lista con tramos.
    natural_merging(lista_con_tramos) # Ordena la lista.
    print(f"Lista ordenada (Natural Merging): {lista_con_tramos}") # Imprime la lista ordenada.

    print("\n--- Ejemplo con lista casi ordenada ---") # Imprime un separador.
    lista_casi_ordenada = [1, 2, 3, 5, 4, 6, 7, 8] # Un solo "desorden" al final.
    print(f"Lista casi ordenada: {lista_casi_ordenada}") # Imprime la lista casi ordenada.
    natural_merging(lista_casi_ordenada) # Ordena.
    print(f"Lista ordenada (Natural Merging): {lista_casi_ordenada}") # Imprime la lista ordenada.

    print("\n--- Ejemplo con lista ya ordenada ---") # Imprime un separador.
    lista_ya_ordenada = [1, 2, 3, 4, 5] # Lista ya ordenada.
    print(f"Lista ya ordenada: {lista_ya_ordenada}") # Imprime la lista ya ordenada.
    natural_merging(lista_ya_ordenada) # Ordena (debería ser muy rápido).
    print(f"Lista ordenada (Natural Merging): {lista_ya_ordenada}") # Imprime la lista ya ordenada.

    print("\n--- Ejemplo con lista vacía ---") # Imprime un separador.
    lista_vacia = [] # Lista vacía.
    print(f"Lista vacía: {lista_vacia}") # Imprime la lista vacía.
    natural_merging(lista_vacia) # Ordena.
    print(f"Lista ordenada (Natural Merging): {lista_vacia}") # Imprime la lista vacía.
