def straight_merging(arr): # Define la función principal para el Ordenamiento por Fusión Directa.
    """
    Ordena una lista de elementos utilizando el algoritmo de Fusión Directa (Straight Merging).

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

    # 'current_size' es el tamaño de las sublistas a mezclar en la pasada actual.
    # Comienza con sublistas de tamaño 1 (elementos individuales).
    current_size = 1 # Inicializa el tamaño actual de las sublistas ordenadas.

    # El bucle principal controla las pasadas de mezcla.
    # Continúa mientras el tamaño de las sublistas sea menor que el tamaño total de la lista.
    while current_size < n: # Este bucle externo se ejecuta log(n) veces.

        # 'left_start' es el índice de inicio de la primera sublista en cada par a mezclar.
        # Itera a través de la lista para encontrar pares de sublistas a fusionar.
        left_start = 0 # Inicializa el inicio de la sublista izquierda.
        while left_start < n - 1: # Itera mientras haya al menos dos sublistas para mezclar.

            # Define los límites de las dos sublistas a mezclar.
            # La sublista izquierda va de left_start a min(left_start + current_size - 1, n - 1).
            mid = min(left_start + current_size - 1, n - 1) # Calcula el índice final de la sublista izquierda.
            # La sublista derecha va de mid + 1 a min(left_start + 2 * current_size - 1, n - 1).
            right_end = min(left_start + 2 * current_size - 1, n - 1) # Calcula el índice final de la sublista derecha.

            # Realiza la fusión de las dos sublistas.
            _merge(arr, temp_arr, left_start, mid, right_end) # Llama a la función auxiliar _merge para fusionar.

            # Mueve al inicio del siguiente par de sublistas.
            left_start += 2 * current_size # Avanza al inicio del siguiente par de sublistas.

        # Duplica el tamaño de las sublistas para la próxima pasada.
        current_size *= 2 # Incrementa el tamaño de las sublistas que se van a mezclar en la siguiente iteración.

    return arr # Retorna la lista ya ordenada.

def _merge(arr, temp_arr, left, mid, right): # Función auxiliar para mezclar dos sub-arreglos.
    """
    Combina dos sub-arreglos de 'arr' en 'temp_arr' y luego los copia de vuelta a 'arr'.
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
    lista_desordenada = [38, 27, 43, 3, 9, 82, 10] # Crea una lista de ejemplo desordenada.
    print(f"Lista desordenada: {lista_desordenada}") # Imprime la lista original.

    straight_merging(lista_desordenada) # Llama a la función straight_merging para ordenar la lista.
    print(f"Lista ordenada (Straight Merging): {lista_desordenada}") # Imprime la lista ya ordenada.

    print("\n--- Otro ejemplo ---") # Imprime un separador para otro ejemplo.
    lista_grande = [64, 25, 12, 22, 11, 90, 78, 34, 45, 56, 1, 89] # Crea una lista más grande.
    print(f"Lista desordenada: {lista_grande}") # Imprime la lista grande desordenada.
    straight_merging(lista_grande) # Ordena la lista grande.
    print(f"Lista ordenada (Straight Merging): {lista_grande}") # Imprime la lista grande ordenada.

    print("\n--- Ejemplo con lista de tamaño impar ---") # Imprime un separador.
    lista_impar = [5, 2, 8, 1, 9, 4, 7] # Crea una lista de tamaño impar.
    print(f"Lista desordenada: {lista_impar}") # Imprime la lista impar.
    straight_merging(lista_impar) # Ordena la lista impar.
    print(f"Lista ordenada (Straight Merging): {lista_impar}") # Imprime la lista impar ordenada.

    print("\n--- Ejemplo con lista vacía ---") # Imprime un separador.
    lista_vacia = [] # Crea una lista vacía.
    print(f"Lista vacía: {lista_vacia}") # Imprime la lista vacía.
    straight_merging(lista_vacia) # Intenta ordenar una lista vacía.
    print(f"Lista ordenada (Straight Merging): {lista_vacia}") # Imprime la lista vacía.

    print("\n--- Ejemplo con lista de un solo elemento ---") # Imprime un separador.
    lista_un_elemento = [7] # Crea una lista con un solo elemento.
    print(f"Lista de un solo elemento: {lista_un_elemento}") # Imprime la lista de un solo elemento.
    straight_merging(lista_un_elemento) # Intenta ordenar una lista de un solo elemento.
    print(f"Lista ordenada (Straight Merging): {lista_un_elemento}") # Imprime la lista de un solo elemento.
