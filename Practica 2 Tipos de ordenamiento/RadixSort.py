def counting_sort_for_radix(arr, exp): # Función auxiliar para Counting Sort, adaptada para Radix Sort.
    """
    Realiza un Counting Sort en 'arr' basado en el dígito representado por 'exp'.
    'exp' es un exponente de 10 (ej: 1 para unidades, 10 para decenas, 100 para centenas).
    """
    n = len(arr) # Obtiene la longitud de la lista.
    output = [0] * n # Crea una lista 'output' del mismo tamaño para almacenar los elementos ordenados por el dígito actual.
    count = [0] * 10 # Crea una lista 'count' de tamaño 10 (para dígitos del 0 al 9), inicializada a ceros.

    # Paso 1: Cuenta las ocurrencias de cada dígito en la posición actual.
    for i in range(n): # Itera sobre cada número en la lista de entrada.
        index = (arr[i] // exp) % 10 # Calcula el dígito actual del número (ej: (345 // 10) % 10 = 4).
        count[index] += 1 # Incrementa el contador para ese dígito.

    # Paso 2: Cambia 'count[i]' para que contenga la posición real de este dígito en 'output'.
    # Esto asegura la estabilidad del ordenamiento.
    for i in range(1, 10): # Itera desde 1 hasta 9.
        count[i] += count[i - 1] # Suma acumulativa para obtener las posiciones finales.

    # Paso 3: Construye la lista de salida.
    # Itera desde el final para asegurar la estabilidad (importante para Radix Sort).
    i = n - 1 # Inicializa el índice para recorrer 'arr' desde el final.
    while i >= 0: # Mientras no se haya procesado toda la lista.
        index = (arr[i] // exp) % 10 # Calcula el dígito actual del número.
        output[count[index] - 1] = arr[i] # Coloca el número en su posición correcta en 'output'.
        count[index] -= 1 # Decrementa el contador para ese dígito (para el siguiente número con el mismo dígito).
        i -= 1 # Mueve al siguiente número en 'arr'.

    # Paso 4: Copia los elementos ordenados del 'output' de vuelta a 'arr'.
    for i in range(n): # Itera sobre la lista.
        arr[i] = output[i] # Actualiza la lista original con los elementos ordenados por el dígito actual.

def radix_sort(arr): # Define la función principal para el Ordenamiento Radix.
    """
    Ordena una lista de números enteros no negativos utilizando el algoritmo de Radix Sort.
    """
    if not arr: # Si la lista está vacía, no hay nada que ordenar.
        return [] # Retorna una lista vacía.

    # Encuentra el número máximo para saber cuántos dígitos procesar.
    max_val = max(arr) # Encuentra el valor más grande en la lista.

    # Itera desde el dígito menos significativo (unidades) hasta el más significativo.
    # 'exp' representa 10^0, 10^1, 10^2, ... para acceder a los dígitos de unidades, decenas, centenas, etc.
    exp = 1 # Inicializa el exponente (para las unidades).
    while max_val // exp > 0: # Mientras haya dígitos para procesar (es decir, el número máximo dividido por exp es mayor que 0).
        counting_sort_for_radix(arr, exp) # Llama a Counting Sort para ordenar por el dígito actual.
        exp *= 10 # Pasa al siguiente dígito (decenas, centenas, etc.).

    return arr # Retorna la lista con los números ya ordenados.

---
### Ejemplo de Uso

```python
if __name__ == "__main__": # Esto asegura que el código dentro solo se ejecute cuando el script se corre directamente.
    lista_desordenada = [170, 45, 75, 90, 802, 24, 2, 66] # Crea una lista de ejemplo desordenada.
    print(f"Lista desordenada: {lista_desordenada}") # Imprime la lista original.

    radix_sort(lista_desordenada) # Llama a la función radix_sort para ordenar la lista.
    print(f"Lista ordenada (Radix Sort): {lista_desordenada}") # Imprime la lista ya ordenada.

    print("\n--- Otro ejemplo ---") # Imprime un separador para otro ejemplo.
    lista_grande = [88, 1, 999, 10, 5, 202, 345, 12, 777] # Crea una lista más grande.
    print(f"Lista desordenada: {lista_grande}") # Imprime la lista grande desordenada.
    radix_sort(lista_grande) # Ordena la lista grande.
    print(f"Lista ordenada (Radix Sort): {lista_grande}") # Imprime la lista grande ordenada.

    print("\n--- Ejemplo con lista vacía ---") # Imprime un separador.
    lista_vacia = [] # Crea una lista vacía.
    print(f"Lista vacía: {lista_vacia}") # Imprime la lista vacía.
    radix_sort(lista_vacia) # Intenta ordenar una lista vacía.
    print(f"Lista ordenada (Radix Sort): {lista_vacia}") # Imprime la lista vacía (permanece vacía).

    print("\n--- Ejemplo con lista de un solo elemento ---") # Imprime un separador.
    lista_un_elemento = [42] # Crea una lista con un solo elemento.
    print(f"Lista de un solo elemento: {lista_un_elemento}") # Imprime la lista de un solo elemento.
    radix_sort(lista_un_elemento) # Intenta ordenar una lista de un solo elemento.
    print(f"Lista ordenada (Radix Sort): {lista_un_elemento}") # Imprime la lista de un solo elemento (permanece igual).

    print("\n--- Ejemplo con números de diferentes longitudes ---") # Imprime un separador.
    lista_mixta = [100, 4, 10, 5000, 2, 70] # Crea una lista con números de diferentes longitudes de dígitos.
    print(f"Lista desordenada: {lista_mixta}") # Imprime la lista mixta.
    radix_sort(lista_mixta) # Ordena la lista mixta.
    print(f"Lista ordenada (Radix Sort): {lista_mixta}") # Imprime la lista mixta ordenada.
