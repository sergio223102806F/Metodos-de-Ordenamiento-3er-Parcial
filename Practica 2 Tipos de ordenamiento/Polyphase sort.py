import heapq

def polyphase_merge_simulation(data_lists):
    """
    Simula la etapa de fusión de múltiples vías de un algoritmo como Polyphase Sort.
    Toma una lista de listas ya ordenadas (representando "tramos" o "cintas" con datos).

    Parameters:
    data_lists (list of list): Una lista donde cada elemento es una lista de números ya ordenada
                                (simulando los tramos iniciales de las cintas de entrada).

    Returns:
    list: Una nueva lista que contiene todos los elementos ordenados de las listas de entrada.
    """
    # Usamos una cola de prioridad (min-heap) para eficientemente encontrar el
    # siguiente elemento más pequeño de todas las listas de entrada.
    min_heap = []

    # 'results' almacenará la lista final ordenada.
    sorted_result = []

    # 1. Inicializar el heap con el primer elemento de cada lista (tramo).
    # Cada elemento en el heap será una tupla: (valor, índice_de_lista, índice_dentro_de_lista)
    for list_idx, current_list in enumerate(data_lists):
        if current_list: # Asegúrate de que la lista no esté vacía.
            # Añade el primer elemento de esta lista al heap.
            heapq.heappush(min_heap, (current_list[0], list_idx, 0))

    # 2. Extraer el elemento más pequeño del heap, añadirlo al resultado y
    #    añadir el siguiente elemento de su lista de origen (si existe).
    while min_heap: # Continúa mientras haya elementos en el heap.
        # Saca el elemento más pequeño del heap.
        value, list_idx, element_idx = heapq.heappop(min_heap)

        # Añade el valor al resultado ordenado.
        sorted_result.append(value)

        # Mueve al siguiente elemento en la lista de origen.
        next_element_idx = element_idx + 1

        # Si hay más elementos en la lista de origen, añádelos al heap.
        if next_element_idx < len(data_lists[list_idx]):
            next_value = data_lists[list_idx][next_element_idx]
            heapq.heappush(min_heap, (next_value, list_idx, next_element_idx))

    return sorted_result

---
### **Cómo usar la simulación (Ejemplo Funcional)**

```python
if __name__ == "__main__":
    # --- Ejemplo 1: Simulando tramos pre-ordenados de 3 "cintas" ---
    # En un Polyphase Sort real, estas listas serían los "tramos" leídos de las cintas.
    # Asumimos que ya están ordenados internamente.
    cinta_1_tramos = [
        [1, 5, 9, 13],  # Tramo 1 de cinta 1
        [17, 21]        # Tramo 2 de cinta 1
    ]
    cinta_2_tramos = [
        [2, 6, 10],     # Tramo 1 de cinta 2
        [14, 18, 22]    # Tramo 2 de cinta 2
    ]
    cinta_3_tramos = [
        [3, 7, 11],     # Tramo 1 de cinta 3
        [15, 19, 23]    # Tramo 2 de cinta 3
    ]

    # En una fase de Polyphase, fusionaríamos un tramo de cada cinta de entrada.
    # Para simular una única "pasada" de fusión de Polyphase,
    # tomaremos el primer tramo de cada "cinta" de entrada.
    print("--- Simulación de una única fase de fusión de Polyphase ---")
    
    # Supongamos que estamos en una fase donde fusionamos los primeros tramos de cada cinta.
    tramos_para_fusionar_fase_1 = [
        cinta_1_tramos[0],
        cinta_2_tramos[0],
        cinta_3_tramos[0]
    ]

    print(f"Tramos a fusionar en esta fase (desde 3 'cintas'): {tramos_para_fusionar_fase_1}")
    resultado_fase_1 = polyphase_merge_simulation(tramos_para_fusionar_fase_1)
    print(f"Resultado de la fusión de esta fase: {resultado_fase_1}")

    # En un Polyphase real, 'resultado_fase_1' se escribiría en una cinta de salida,
    # y las cintas originales perderían sus tramos fusionados. El proceso se repetiría.

    print("\n--- Ejemplo 2: Fusionando los segundos tramos (simulación de otra fase) ---")
    tramos_para_fusionar_fase_2 = [
        cinta_1_tramos[1],
        cinta_2_tramos[1],
        cinta_3_tramos[1]
    ]
    print(f"Tramos a fusionar en la siguiente fase: {tramos_para_fusionar_fase_2}")
    resultado_fase_2 = polyphase_merge_simulation(tramos_para_fusionar_fase_2)
    print(f"Resultado de la fusión de la siguiente fase: {resultado_fase_2}")

    # Para obtener el resultado final, en un Polyphase real,
    # fusionaríamos 'resultado_fase_1' y 'resultado_fase_2' en una fase posterior.
    print("\n--- Resultado final conceptual (fusionando los resultados de las fases) ---")
    resultado_final_conceptual = polyphase_merge_simulation([resultado_fase_1, resultado_fase_2])
    print(f"Resultado final (conceptual): {resultado_final_conceptual}")

    # --- Ejemplo 3: Manejo de listas vacías o con un solo tramo ---
    print("\n--- Ejemplo 3: Listas con diferentes números de tramos ---")
    lista_con_vacia = [
        [1, 2, 3],
        [],          # Una "cinta" vacía
        [4, 5, 6, 7]
    ]
    print(f"Listas a fusionar: {lista_con_vacia}")
    resultado_ej3 = polyphase_merge_simulation(lista_con_vacia)
    print(f"Resultado: {resultado_ej3}")

    lista_un_elemento = [[5]]
    print(f"\nLista con un solo elemento: {lista_un_elemento}")
    resultado_un_elemento = polyphase_merge_simulation(lista_un_elemento)
    print(f"Resultado: {resultado_un_elemento}")