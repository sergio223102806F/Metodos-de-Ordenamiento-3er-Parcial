import heapq # Importa el módulo heapq para usar una cola de prioridad (min-heap).

def balanced_multiway_merging(arr, k): # Define la función principal para la Fusión Múltiple Balanceada.
    """
    Ordena una lista de elementos utilizando el algoritmo de Fusión Múltiple Balanceada.
    Asume que la lista se puede dividir en 'k' tramos iniciales.

    Args:
        arr: La lista de elementos a ordenar.
        k: El número de sublistas (tramos) a mezclar simultáneamente.

    Returns:
        La lista ordenada.
    """
    n = len(arr) # Obtiene la longitud de la lista.
    if n <= 1: # Si la lista tiene 0 o 1 elemento, ya está ordenada.
        return arr # Retorna la lista tal cual.

    if k <= 1: # Si k es 1 o menos, se degrada a un no-ordenamiento o un caso base.
        # En un sistema real, esto podría lanzar un error o simplemente retornar.
        print(f"Advertencia: k={k} no es válido para multiway merging. Usando k=2.") # Mensaje de advertencia.
        k = 2 # Establece k a 2 para que funcione como una fusión binaria.

    # Paso 1: Dividir la lista en k "tramos" iniciales y ordenarlos individualmente.
    # En un escenario real de ordenamiento externo, estos tramos se generarían y ordenarían
    # en disco, a menudo mediante una combinación de lectura, ordenamiento en memoria y escritura.
    chunk_size = (n + k - 1) // k # Calcula el tamaño aproximado de cada tramo (redondeando hacia arriba).
    runs = [] # Lista para almacenar los tramos (sublistas ordenadas).
    for i in range(0, n, chunk_size): # Itera para crear los tramos.
        # Ordena cada tramo usando el algoritmo de ordenamiento incorporado de Python (Timsort, muy eficiente).
        # En un escenario externo, esto sería una lectura-ordenación-escritura a disco.
        current_run = sorted(arr[i:min(i + chunk_size, n)]) # Crea y ordena un tramo.
        runs.append(current_run) # Añade el tramo ordenado a la lista de tramos.

    # Paso 2: Realizar la fusión múltiple de los tramos.
    # Se usa una cola de prioridad (min-heap) para eficientemente encontrar el siguiente elemento más pequeño
    # entre todos los tramos.

    # El heap almacenará tuplas de (valor, índice_del_run, índice_dentro_del_run).
    min_heap = [] # Inicializa una cola de prioridad vacía.

    # Inicializa el heap con el primer elemento de cada tramo.
    for i, run in enumerate(runs): # Itera sobre cada tramo y su índice.
        if run: # Si el tramo no está vacío.
            # Inserta el primer elemento del tramo en el heap.
            heapq.heappush(min_heap, (run[0], i, 0)) # Añade (valor, índice_del_run, índice_dentro_del_run) al heap.

    sorted_result = [] # Lista para almacenar el resultado final ordenado.

    # Extrae elementos del heap y los añade al resultado final.
    while min_heap: # Mientras el heap no esté vacío.
        val, run_idx, element_idx = heapq.heappop(min_heap) # Extrae el elemento más pequeño del heap.
        sorted_result.append(val) # Añade el elemento más pequeño al resultado ordenado.

        # Si el tramo de donde se extrajo el elemento tiene más elementos, añade el siguiente al heap.
        if element_idx + 1 < len(runs[run_idx]): # Si hay más elementos en este tramo.
            next_val = runs[run_idx][element_idx + 1] # Obtiene el siguiente elemento del mismo tramo.
            heapq.heappush(min_heap, (next_val, run_idx, element_idx + 1)) # Añade el siguiente elemento al heap.

    return sorted_result # Retorna la lista completamente ordenada.

---
### Ejemplo de Uso

```python
if __name__ == "__main__": # Esto asegura que el código dentro solo se ejecute cuando el script se corre directamente.
    lista_desordenada = [9, 1, 7, 3, 5, 2, 8, 4, 6, 0, 10, 11, 12, 13, 14, 15] # Lista de ejemplo.
    k_val = 3 # Número de tramos a mezclar.

    print(f"Lista desordenada: {lista_desordenada}") # Imprime la lista original.
    print(f"Número de vías de fusión (k): {k_val}") # Imprime el valor de k.

    lista_ordenada = balanced_multiway_merging(lista_desordenada, k_val) # Llama a la función de fusión múltiple.
    print(f"Lista ordenada (Balanced Multiway Merging): {lista_ordenada}") # Imprime la lista ya ordenada.

    print("\n--- Otro ejemplo con k=4 ---") # Imprime un separador.
    lista_grande = [100, 4, 200, 1, 50, 7, 300, 2, 80, 5, 400, 3]
    k_val_2 = 4
    print(f"Lista desordenada: {lista_grande}")
    print(f"Número de vías de fusión (k): {k_val_2}")
    lista_ordenada_grande = balanced_multiway_merging(lista_grande, k_val_2)
    print(f"Lista ordenada (Balanced Multiway Merging): {lista_ordenada_grande}")

    print("\n--- Ejemplo con lista vacía ---") # Imprime un separador.
    lista_vacia = []
    print(f"Lista vacía: {lista_vacia}")
    lista_ordenada_vacia = balanced_multiway_merging(lista_vacia, 3)
    print(f"Lista ordenada (Balanced Multiway Merging): {lista_ordenada_vacia}")

    print("\n--- Ejemplo con k muy grande (más que elementos) ---") # Imprime un separador.
    lista_pequena = [5, 2, 8, 1]
    k_val_grande = 10
    print(f"Lista desordenada: {lista_pequena}")
    print(f"Número de vías de fusión (k): {k_val_grande}")
    lista_ordenada_pequena = balanced_multiway_merging(lista_pequena, k_val_grande)
    print(f"Lista ordenada (Balanced Multiway Merging): {lista_ordenada_pequena}")