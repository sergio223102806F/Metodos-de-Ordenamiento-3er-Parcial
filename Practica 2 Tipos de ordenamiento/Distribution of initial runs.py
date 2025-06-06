import collections

def create_and_distribute_initial_runs(input_data, buffer_size, num_output_devices, strategy="balanced"):
    """
    Simula la creación y distribución de tramos iniciales para algoritmos de ordenamiento externo.

    Parameters:
    input_data (list): La lista completa de datos a ordenar (simulando datos en disco).
    buffer_size (int): El tamaño del buffer de memoria disponible para ordenar los tramos.
                       (Cuántos elementos pueden caber en memoria a la vez).
    num_output_devices (int): El número de dispositivos de salida (ej. cintas, archivos)
                              donde se distribuirán los tramos.
    strategy (str): La estrategia de distribución. "balanced" (equilibrada) o "polyphase_simple" (para Polyphase).

    Returns:
    list of list: Una lista donde cada elemento es una lista de tramos
                  (una lista de listas), representando los tramos en cada dispositivo de salida.
                  Ejemplo: [[tramo1_d1, tramo2_d1], [tramo1_d2], ...]
    """
    n = len(input_data)
    if n == 0:
        return [[] for _ in range(num_output_devices)]

    if buffer_size <= 0:
        raise ValueError("El tamaño del buffer debe ser mayor que 0.")
    if num_output_devices <= 0:
        raise ValueError("Debe haber al menos un dispositivo de salida.")

    # 1. Crear los "dispositivos de salida" como listas de tramos.
    output_devices = [[] for _ in range(num_output_devices)]

    # 2. Iterar sobre los datos de entrada para crear tramos.
    #    'input_data_idx' rastrea la posición actual en los datos de entrada.
    input_data_idx = 0
    current_output_device_idx = 0 # Para distribución cíclica (balanceada)

    print(f"\n--- Creación y Distribución de Tramos Iniciales (Estrategia: {strategy}) ---")
    print(f"Tamaño de datos: {n}, Tamaño de buffer: {buffer_size}, Dispositivos de salida: {num_output_devices}")

    run_counter = 0 # Contador para el número de tramos creados.

    while input_data_idx < n:
        # Extraer un bloque de datos que quepa en el buffer de memoria.
        end_idx = min(input_data_idx + buffer_size, n)
        current_block = input_data[input_data_idx:end_idx]

        # Ordenar el bloque en memoria para crear un tramo.
        sorted_run = sorted(current_block) # Usamos el sorted() de Python como nuestro "ordenador interno"

        print(f"  Tramo {run_counter}: {sorted_run}")

        # Distribuir el tramo al dispositivo de salida.
        if strategy == "balanced":
            # Distribución Round-Robin (cíclica) para equilibrar la carga.
            output_devices[current_output_device_idx].append(sorted_run)
            print(f"    -> Distribuido a Dispositivo {current_output_device_idx}")
            current_output_device_idx = (current_output_device_idx + 1) % num_output_devices
        
        elif strategy == "polyphase_simple":
            # Para Polyphase, la distribución es más compleja (Fibonacci).
            # Aquí, una simulación muy simplificada:
            # Distribuye a k-1 dispositivos de "entrada", dejando uno "vacío" o con menos para ser el de salida.
            # Esto NO es la distribución Fibonacci real, pero intenta simular el concepto de desequilibrio inicial.
            
            # La distribución real de Polyphase se basa en la secuencia Fibonacci generalizada
            # para el número de tramos, para que las cintas se vacíen de forma sincrónica.
            # Por ejemplo, para k=3, las proporciones podrían ser 8:5:0 (o 5:3:0 si miramos una generación anterior).
            
            # Para esta simulación simple, simplemente distribuyamos en k-1 dispositivos.
            # Y la última cinta tendrá 0 o muy pocos tramos al inicio.
            
            if num_output_devices == 1: # Si solo hay 1 dispositivo, todos van ahí.
                output_devices[0].append(sorted_run)
                print(f"    -> Distribuido a Dispositivo 0 (solo 1 dispositivo)")
            else:
                # Distribución simple a los primeros num_output_devices - 1
                # En un Polyphase real, se requieren contadores de tramos y "relleno"
                # para que las proporciones coincidan con Fibonacci.
                
                # Simulación de la distribución desequilibrada (no Fibonacci exacta)
                # que favorece las primeras cintas para Polyphase.
                # Es una simplificación.
                
                # Para k=3, por ejemplo, queremos que Cinta0 y Cinta1 tengan tramos, Cinta2 vacía.
                # Luego, cuando fusionamos A+B->C, C se llena.
                # Luego A+C->B, B se llena.
                
                # Aquí una distribución a k-1 dispositivos de forma rotativa.
                target_device_idx = current_output_device_idx % (num_output_devices - 1)
                output_devices[target_device_idx].append(sorted_run)
                print(f"    -> Distribuido a Dispositivo {target_device_idx} (simulación Polyphase)")
                current_output_device_idx += 1 # Mueve al siguiente dispositivo para la próxima distribución
            
        else:
            raise ValueError("Estrategia de distribución no válida. Use 'balanced' o 'polyphase_simple'.")

        input_data_idx = end_idx
        run_counter += 1

    print("\n--- Tramos distribuidos en Dispositivos de Salida ---")
    for i, device_runs in enumerate(output_devices):
        print(f"Dispositivo {i} ({len(device_runs)} tramos): {device_runs}")

    return output_devices

---
### **Ejemplo de Uso de la Simulación**

```python
if __name__ == "__main__":
    # Datos de entrada que simulan estar en un disco o un archivo grande.
    big_data = [
        38, 27, 43, 3, 9, 82, 10, 1, 56, 74,
        15, 34, 61, 8, 99, 21, 5, 49, 7, 20
    ]

    # --- Escenario 1: Distribución Balanceada (para Fusión Múltiple Balanceada) ---
    print("----- Escenario 1: Distribución Balanceada (Round-Robin) -----")
    # Buffer de 4 elementos, 3 dispositivos de salida.
    distributed_runs_balanced = create_and_distribute_initial_runs(big_data, 4, 3, strategy="balanced")
    
    print("\nEstado final de la distribución balanceada:")
    for i, device_runs in enumerate(distributed_runs_balanced):
        print(f"  Dispositivo {i}: {device_runs}")

    # --- Escenario 2: Distribución Simplificada para Polyphase ---
    print("\n----- Escenario 2: Distribución Simplificada para Polyphase -----")
    # Buffer de 4 elementos, 3 dispositivos de salida (k=3), simulando un Polyphase.
    # Nota: Esta simulación NO recrea la distribución Fibonacci exacta del Polyphase real.
    distributed_runs_polyphase = create_and_distribute_initial_runs(big_data, 4, 3, strategy="polyphase_simple")

    print("\nEstado final de la distribución simplificada Polyphase:")
    for i, device_runs in enumerate(distributed_runs_polyphase):
        print(f"  Dispositivo {i}: {device_runs}")

    # --- Ejemplo con un buffer más grande ---
    print("\n----- Escenario 3: Buffer más grande, menos tramos -----")
    distributed_runs_large_buffer = create_and_distribute_initial_runs(big_data, 10, 2, strategy="balanced")
    print("\nEstado final de la distribución con buffer grande:")
    for i, device_runs in enumerate(distributed_runs_large_buffer):
        print(f"  Dispositivo {i}: {device_runs}")