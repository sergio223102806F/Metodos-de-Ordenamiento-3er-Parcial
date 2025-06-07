import heapq                                   # Importa el módulo heapq para usar una cola de prioridad (min-heap).
import matplotlib.pyplot as plt                # Importa matplotlib para crear gráficos y visualizaciones.
import networkx as nx                          # Importa networkx para crear y manipular grafos.

class DijkstraSimulator:                       # Define la clase DijkstraSimulator para simular el algoritmo de Dijkstra.
                                               
    def __init__(self):                        # Constructor de la clase.
        self.graph = {}                        # Diccionario para almacenar el grafo: {nodo: {vecino: peso}}.
        self.positions = {}                    # Diccionario para almacenar posiciones de los nodos en el gráfico (para visualización).
        self.visualization = True              # Booleano para activar o desactivar la visualización gráfica paso a paso.
                                               
    def add_edge(self, u, v, weight):          # Método para añadir una arista al grafo.
        if u not in self.graph:                # Si el nodo 'u' no está en el grafo, lo inicializa.
            self.graph[u] = {}                 # Crea un diccionario vacío para los vecinos de 'u'.
        if v not in self.graph:                # Si el nodo 'v' no está en el grafo, lo inicializa.
            self.graph[v] = {}                 # Crea un diccionario vacío para los vecinos de 'v'.
        self.graph[u][v] = weight              # Establece el peso de la arista de 'u' a 'v'.
        self.graph[v][u] = weight              # Establece el peso de la arista de 'v' a 'u' (grafo no dirigido).
                                               
    def dijkstra(self, start):                 # Implementa el algoritmo de Dijkstra para encontrar el camino más corto.
        # Inicialización                           # Sección de inicialización de variables.
        distances = {node: float('infinity') for node in self.graph} # Diccionario para guardar la distancia más corta desde 'start' a cada nodo. Inicializa todas las distancias a infinito.
        distances[start] = 0                   # La distancia desde el nodo de inicio a sí mismo es 0.
        previous_nodes = {node: None for node in self.graph} # Diccionario para rastrear el nodo predecesor en el camino más corto.
        priority_queue = [(0, start)]          # Cola de prioridad (min-heap) para explorar nodos, guarda tuplas (distancia, nodo).
                                               
        print("\nInicialización:")             # Imprime el estado inicial.
        print(f"Distancias: {distances}")      # Muestra las distancias iniciales.
        print(f"Cola de prioridad: {priority_queue}\n") # Muestra la cola de prioridad inicial.
                                               
        while priority_queue:                  # Bucle principal: continúa mientras haya nodos en la cola de prioridad.
            current_distance, current_node = heapq.heappop(priority_queue) # Extrae el nodo con la menor distancia de la cola.
                                               
            print(f"\nProcesando nodo: {current_node}") # Indica qué nodo se está procesando.
            print(f"Distancia actual: {current_distance}") # Muestra la distancia del nodo actual.
                                               
            # Si encontramos una distancia mayor, la ignoramos # Optimización: si ya encontramos un camino más corto a este nodo, ignoramos esta entrada de la cola.
            if current_distance > distances[current_node]: # Comprueba si la distancia extraída es mayor que la ya conocida (obsoleta).
                print(f"Distancia ya mejor ({distances[current_node]}), ignorando...") # Mensaje de ignorado.
                continue                       # Salta a la siguiente iteración del bucle.
                                               
            for neighbor, weight in self.graph[current_node].items(): # Itera sobre cada vecino del nodo actual y el peso de la arista.
                distance = current_distance + weight # Calcula la distancia total al vecino a través del nodo actual.
                print(f"\n  Explorando vecino: {neighbor} (peso: {weight})") # Muestra el vecino que se está explorando.
                print(f"  Distancia calculada: {distance} vs distancia almacenada: {distances[neighbor]}") # Compara la distancia calculada con la almacenada.
                                               
                # Encontramos un camino más corto        # Comprueba si este nuevo camino es más corto que el anterior.
                if distance < distances[neighbor]:     # Si la distancia calculada es menor que la distancia almacenada al vecino.
                    distances[neighbor] = distance     # Actualiza la distancia más corta al vecino.
                    previous_nodes[neighbor] = current_node # Actualiza el nodo predecesor del vecino.
                    heapq.heappush(priority_queue, (distance, neighbor)) # Añade (o actualiza) el vecino en la cola de prioridad con la nueva distancia.
                    print(f"  ¡Mejor camino encontrado! Actualizando distancia a {distance}") # Mensaje de camino encontrado.
                    print(f"  Nodo anterior de {neighbor}: {current_node}") # Muestra el nuevo predecesor.
                    print(f"  Cola actualizada: {priority_queue}") # Muestra el estado actual de la cola de prioridad.
                                               
                    if self.visualization:         # Si la visualización está activada.
                        self.visualize_step(current_node, neighbor, distances, previous_nodes) # Llama al método para visualizar el paso actual.
                                               
        return distances, previous_nodes       # Retorna las distancias más cortas y los nodos predecesores.
                                               
    def visualize_step(self, current_node, updated_node, distances, previous_nodes): # Método para visualizar el grafo y el progreso de Dijkstra.
        G = nx.Graph()                         # Crea un nuevo objeto de grafo de NetworkX.
                                               
        # Añadir nodos y aristas                 # Agrega todos los nodos y aristas del grafo a la visualización.
        for node in self.graph:                # Itera sobre cada nodo en el grafo.
            G.add_node(node)                   # Añade el nodo al grafo de visualización.
            for neighbor, weight in self.graph[node].items(): # Itera sobre los vecinos y pesos de cada nodo.
                if neighbor > node:            # Para evitar duplicados en un grafo no dirigido (solo añade una arista por par).
                    G.add_edge(node, neighbor, weight=weight) # Añade la arista con su peso.
                                               
        # Posiciones para todos los nodos (usando disposición circular si no hay posiciones definidas) # Define las posiciones de los nodos para el dibujo.
        if not self.positions:                 # Si las posiciones no han sido definidas (primera vez).
            self.positions = nx.spring_layout(G) # Usa un algoritmo de diseño de resorte para organizar los nodos.
                                               
        plt.figure(figsize=(10, 6))            # Crea una nueva figura para el gráfico con un tamaño específico.
                                               
        # Dibujar el grafo completo              # Dibuja los componentes del grafo.
        nx.draw_networkx_nodes(G, self.positions, node_size=700, node_color='lightblue') # Dibuja los nodos con un tamaño y color.
        nx.draw_networkx_edges(G, self.positions, width=1, alpha=0.5) # Dibuja las aristas.
        nx.draw_networkx_labels(G, self.positions, font_size=12, font_family='sans-serif') # Dibuja las etiquetas de los nodos.
                                               
        # Etiquetas de peso en las aristas       # Muestra los pesos de las aristas en el grafo.
        edge_labels = nx.get_edge_attributes(G, 'weight') # Obtiene los pesos de las aristas.
        nx.draw_networkx_edge_labels(G, self.positions, edge_labels=edge_labels) # Dibuja las etiquetas de los pesos.
                                               
        # Resaltar nodo actual                   # Resalta el nodo que se está procesando actualmente.
        if current_node:                       # Si hay un nodo actual para resaltar.
            nx.draw_networkx_nodes(G, self.positions, nodelist=[current_node], node_size=800, node_color='red') # Dibuja el nodo actual en rojo.
                                               
        # Resaltar nodo actualizado (si es diferente) # Resalta el nodo cuya distancia fue actualizada.
        if updated_node and updated_node != current_node: # Si hay un nodo actualizado y es diferente del actual.
            nx.draw_networkx_nodes(G, self.positions, nodelist=[updated_node], node_size=800, node_color='green') # Dibuja el nodo actualizado en verde.
                                               
        # Mostrar distancias                     # Muestra las distancias calculadas junto a cada nodo.
        labels = {node: f"{node}\nDist: {distances[node]}" for node in G.nodes()} # Crea etiquetas con el nodo y su distancia.
        nx.draw_networkx_labels(G, self.positions, labels, font_size=10) # Dibuja las etiquetas de distancia.
                                               
        # Mostrar caminos                        # Dibuja el camino más corto encontrado hasta el momento.
        path_edges = []                        # Lista para almacenar las aristas que forman los caminos.
        for node in previous_nodes:            # Itera sobre los nodos para reconstruir los caminos.
            if previous_nodes[node] is not None: # Si el nodo tiene un predecesor (es parte de un camino).
                path_edges.append((previous_nodes[node], node)) # Añade la arista del predecesor al nodo actual.
                                               
        nx.draw_networkx_edges(G, self.positions, edgelist=path_edges, width=2, alpha=0.5, edge_color='r') # Dibuja las aristas del camino en rojo.
                                               
        plt.title(f"Paso: Explorando desde {current_node if current_node else 'Inicio'}. Actualizado {updated_node if updated_node else 'N/A'}") # Establece el título del gráfico.
        plt.axis('off')                        # Desactiva los ejes.
        plt.show()                             # Muestra el gráfico.
                                               
    def print_paths(self, start, previous_nodes, distances): # Método para imprimir los caminos más cortos finales.
        print("\nResultados finales:")         # Encabezado para los resultados finales.
        for node in self.graph:                # Itera sobre todos los nodos del grafo.
            if node != start:                  # Para cada nodo que no sea el de inicio.
                path = []                      # Lista para construir el camino.
                current = node                 # Empieza desde el nodo actual.
                while current is not None:     # Recorre hacia atrás usando los nodos predecesores.
                    path.append(current)       # Añade el nodo al camino.
                    current = previous_nodes[current] # Va al nodo predecesor.
                path.reverse()                 # Invierte el camino para que vaya de inicio a fin.
                print(f"Camino más corto desde {start} a {node}: {' -> '.join(path)} (distancia: {distances[node]})") # Imprime el camino y su distancia.

# Ejemplo de uso                             # Sección para demostrar cómo usar la clase DijkstraSimulator.
def main():                                    # Función principal para ejecutar la simulación.
    simulator = DijkstraSimulator()            # Crea una instancia del simulador.
                                               
    # Construir un grafo de ejemplo            # Define el grafo con nodos y pesos de aristas.
    simulator.add_edge('A', 'B', 4)            # Añade una arista entre A y B con peso 4.
    simulator.add_edge('A', 'C', 2)            # Añade una arista entre A y C con peso 2.
    simulator.add_edge('B', 'C', 1)            # Añade una arista entre B y C con peso 1.
    simulator.add_edge('B', 'D', 5)            # Añade una arista entre B y D con peso 5.
    simulator.add_edge('C', 'D', 8)            # Añade una arista entre C y D con peso 8.
    simulator.add_edge('C', 'E', 10)           # Añade una arista entre C y E con peso 10.
    simulator.add_edge('D', 'E', 2)            # Añade una arista entre D y E con peso 2.
    simulator.add_edge('D', 'F', 6)            # Añade una arista entre D y F con peso 6.
    simulator.add_edge('E', 'F', 2)            # Añade una arista entre E y F con peso 2.
                                               
    # Ejecutar Dijkstra desde el nodo 'A'      # Define el nodo de inicio y ejecuta Dijkstra.
    start_node = 'A'                           # Nodo desde donde se calcularán las distancias.
    distances, previous_nodes = simulator.dijkstra(start_node) # Llama al método dijkstra.
                                               
    # Mostrar resultados finales               # Imprime los resultados del algoritmo.
    simulator.print_paths(start_node, previous_nodes, distances) # Muestra los caminos más cortos y distancias.
                                               
    # Visualización final                      # Realiza una visualización final del grafo con los caminos.
    if simulator.visualization:                # Si la visualización está activada.
        simulator.visualize_step(None, None, distances, previous_nodes) # Llama a visualizar el paso final (sin resaltar nodos específicos).

if __name__ == "__main__":                     # Bloque que asegura que 'main()' se ejecute solo cuando el script es el programa principal.
    main()                                     # Llama a la función principal.
