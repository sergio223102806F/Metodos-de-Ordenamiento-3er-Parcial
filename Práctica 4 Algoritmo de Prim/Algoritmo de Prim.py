import heapq # Importa el módulo heapq para usar una cola de prioridad (min-heap).
import matplotlib.pyplot as plt # Importa matplotlib para crear gráficos y visualizaciones.
import networkx as nx # Importa networkx para crear y manipular grafos.

class PrimSimulator: # Define la clase PrimSimulator para simular el algoritmo de Prim.
    def __init__(self): # Constructor de la clase.
        self.graph = {} # Diccionario para almacenar el grafo: {nodo: {vecino: peso}}.
        self.positions = {} # Diccionario para almacenar posiciones de los nodos (para visualización).
        self.visualization = True # Booleano para activar o desactivar la visualización gráfica paso a paso.

    def add_edge(self, u, v, weight): # Método para añadir una arista al grafo.
        if u not in self.graph: # Si el nodo 'u' no está en el grafo, lo inicializa.
            self.graph[u] = {} # Crea un diccionario vacío para los vecinos de 'u'.
        if v not in self.graph: # Si el nodo 'v' no está en el grafo, lo inicializa.
            self.graph[v] = {} # Crea un diccionario vacío para los vecinos de 'v'.
        self.graph[u][v] = weight # Establece el peso de la arista de 'u' a 'v'.
        self.graph[v][u] = weight # Establece el peso de la arista de 'v' a 'u' (grafo no dirigido).

    def prim(self, start_node): # Implementa el algoritmo de Prim para encontrar el Árbol de Expansión Mínima (MST).
        # Inicialización
        min_spanning_tree_edges = [] # Lista para almacenar las aristas que forman el MST.
        min_cost = 0 # Costo total del MST.
        
        # Cola de prioridad (min-heap): (peso_arista, nodo_actual, nodo_origen)
        # El nodo_origen es el nodo desde el cual llegamos al nodo_actual con ese peso.
        priority_queue = [(0, start_node, None)] # Inicializa la cola con el nodo de inicio (peso 0, sin origen).
        
        # Conjunto para llevar un registro de los nodos ya incluidos en el MST.
        visited = set() # Conjunto para almacenar los nodos ya visitados/incluidos en el MST.

        print("\nInicialización:") # Imprime el estado inicial.
        print(f"Nodo de inicio: {start_node}") # Muestra el nodo de inicio.
        print(f"Cola de prioridad: {priority_queue}") # Muestra la cola de prioridad inicial.
        print(f"Nodos visitados: {visited}\n") # Muestra los nodos visitados (inicialmente vacío).

        while priority_queue: # Bucle principal: continúa mientras haya aristas en la cola de prioridad.
            weight, current_node, origin_node = heapq.heappop(priority_queue) # Extrae la arista de menor peso.

            print(f"\nProcesando arista: ({origin_node} - {current_node}, peso: {weight})") # Muestra la arista actual.

            if current_node in visited: # Si el nodo ya ha sido visitado (ya está en el MST).
                print(f"  Nodo {current_node} ya visitado, ignorando esta arista.") # Mensaje de ignorado.
                continue # Salta a la siguiente iteración del bucle.

            # Añadir el nodo al conjunto de visitados.
            visited.add(current_node) # Agrega el nodo actual al conjunto de visitados.
            print(f"  Añadiendo nodo {current_node} a visitados. Nodos visitados: {visited}") # Muestra los nodos visitados.

            # Si no es el nodo inicial (o si es una arista real para el MST).
            if origin_node is not None: # Si no es el nodo de inicio (la primera entrada en la cola).
                min_spanning_tree_edges.append((origin_node, current_node, weight)) # Añade la arista al MST.
                min_cost += weight # Suma el peso de la arista al costo total del MST.
                print(f"  Añadiendo arista al MST: {origin_node} - {current_node} (peso: {weight})") # Muestra la arista añadida.
                print(f"  Costo total del MST: {min_cost}") # Muestra el costo actual del MST.
                
                if self.visualization: # Si la visualización está activada.
                    self.visualize_step(current_node, origin_node, visited, min_spanning_tree_edges) # Llama al método de visualización.

            # Explorar los vecinos del nodo actual.
            print(f"  Explorando vecinos de {current_node}:") # Indica la exploración de vecinos.
            for neighbor, neighbor_weight in self.graph[current_node].items(): # Itera sobre cada vecino del nodo actual.
                if neighbor not in visited: # Si el vecino aún no ha sido visitado (no está en el MST).
                    heapq.heappush(priority_queue, (neighbor_weight, neighbor, current_node)) # Añade la arista al vecino a la cola de prioridad.
                    print(f"    Añadida arista ({current_node} - {neighbor}, peso: {neighbor_weight}) a la cola.") # Muestra la arista añadida a la cola.
            print(f"  Cola de prioridad actual: {priority_queue}") # Muestra el estado actual de la cola.

        return min_spanning_tree_edges, min_cost # Retorna las aristas del MST y su costo total.

    def visualize_step(self, current_node_added, origin_node, visited_nodes, mst_edges): # Método para visualizar el grafo y el progreso de Prim.
        G = nx.Graph() # Crea un nuevo objeto de grafo de NetworkX.
        
        # Añadir nodos y aristas del grafo original
        for node in self.graph: # Itera sobre cada nodo en el grafo.
            G.add_node(node) # Añade el nodo al grafo de visualización.
            for neighbor, weight in self.graph[node].items(): # Itera sobre los vecinos y pesos de cada nodo.
                if neighbor > node: # Para evitar duplicados en un grafo no dirigido.
                    G.add_edge(node, neighbor, weight=weight) # Añade la arista con su peso.
        
        # Posiciones para todos los nodos (usando disposición de resorte si no hay posiciones definidas)
        if not self.positions: # Si las posiciones no han sido definidas.
            self.positions = nx.spring_layout(G, k=0.7, iterations=50) # Usa un algoritmo de diseño de resorte.
        
        plt.figure(figsize=(10, 7)) # Crea una nueva figura para el gráfico.
        
        # Dibujar nodos
        node_colors = ['lightblue' if node not in visited_nodes else 'lightgreen' for node in G.nodes()] # Colorea nodos visitados de verde.
        nx.draw_networkx_nodes(G, self.positions, node_size=800, node_color=node_colors) # Dibuja los nodos.
        
        # Resaltar el nodo recién añadido al MST
        if current_node_added: # Si hay un nodo que acaba de ser añadido.
            nx.draw_networkx_nodes(G, self.positions, nodelist=[current_node_added], node_size=900, node_color='red') # Resalta el nodo actual en rojo.
            
        nx.draw_networkx_labels(G, self.positions, font_size=10, font_family='sans-serif') # Dibuja las etiquetas de los nodos.
        
        # Dibujar aristas originales
        nx.draw_networkx_edges(G, self.positions, width=1, alpha=0.6, edge_color='gray') # Dibuja las aristas originales en gris.
        
        # Dibujar aristas del MST
        mst_edge_list = [(u, v) for u, v, w in mst_edges] # Lista de tuplas (u,v) para las aristas del MST.
        nx.draw_networkx_edges(G, self.positions, edgelist=mst_edge_list, width=2.5, edge_color='blue') # Dibuja las aristas del MST en azul.
        
        # Etiquetas de peso en las aristas
        edge_labels = nx.get_edge_attributes(G, 'weight') # Obtiene los pesos de las aristas.
        nx.draw_networkx_edge_labels(G, self.positions, edge_labels=edge_labels, font_size=8, font_color='darkgreen') # Dibuja las etiquetas de los pesos.
        
        plt.title(f"Algoritmo de Prim - Paso: Añadiendo {current_node_added} (desde {origin_node if origin_node else 'Inicio'})") # Establece el título del gráfico.
        plt.axis('off') # Desactiva los ejes.
        plt.show() # Muestra el gráfico.

# Ejemplo de uso
def main(): # Función principal para ejecutar la simulación.
    simulator = PrimSimulator() # Crea una instancia del simulador.

    # Construir un grafo de ejemplo
    simulator.add_edge('A', 'B', 4) # Añade una arista entre A y B con peso 4.
    simulator.add_edge('A', 'H', 8) # Añade una arista entre A y H con peso 8.
    simulator.add_edge('B', 'C', 8) # Añade una arista entre B y C con peso 8.
    simulator.add_edge('B', 'H', 11) # Añade una arista entre B y H con peso 11.
    simulator.add_edge('C', 'D', 7) # Añade una arista entre C y D con peso 7.
    simulator.add_edge('C', 'F', 4) # Añade una arista entre C y F con peso 4.
    simulator.add_edge('C', 'I', 2) # Añade una arista entre C y I con peso 2.
    simulator.add_edge('D', 'E', 9) # Añade una arista entre D y E con peso 9.
    simulator.add_edge('D', 'F', 14) # Añade una arista entre D y F con peso 14.
    simulator.add_edge('E', 'F', 10) # Añade una arista entre E y F con peso 10.
    simulator.add_edge('F', 'G', 2) # Añade una arista entre F y G con peso 2.
    simulator.add_edge('G', 'H', 1) # Añade una arista entre G y H con peso 1.
    simulator.add_edge('G', 'I', 6) # Añade una arista entre G y I con peso 6.
    simulator.add_edge('H', 'I', 7) # Añade una arista entre H y I con peso 7.

    # Ejecutar Prim desde el nodo 'A'
    start_node = 'A' # Define el nodo de inicio para el algoritmo de Prim.
    mst_edges, mst_cost = simulator.prim(start_node) # Ejecuta el algoritmo de Prim.

    # Mostrar resultados finales
    print("\n--- Árbol de Expansión Mínima (MST) Final ---") # Encabezado de los resultados finales.
    print(f"Aristas en el MST: {mst_edges}") # Muestra las aristas que forman el MST.
    print(f"Costo total del MST: {mst_cost}") # Muestra el costo total del MST.
    
    # Visualización final del MST
    if simulator.visualization: # Si la visualización está activada.
        # Dibujar el grafo final con el MST resaltado
        G = nx.Graph() # Crea un nuevo objeto de grafo.
        for node in simulator.graph: # Añade todos los nodos al grafo.
            G.add_node(node)
            for neighbor, weight in simulator.graph[node].items(): # Añade todas las aristas originales.
                if neighbor > node:
                    G.add_edge(node, neighbor, weight=weight)
        
        if not simulator.positions: # Si las posiciones no han sido calculadas, las calcula.
            simulator.positions = nx.spring_layout(G, k=0.7, iterations=50)
            
        plt.figure(figsize=(10, 7)) # Crea una figura para el gráfico.
        
        # Nodos
        nx.draw_networkx_nodes(G, simulator.positions, node_size=800, node_color='lightblue') # Dibuja los nodos.
        nx.draw_networkx_labels(G, simulator.positions, font_size=10, font_family='sans-serif') # Dibuja las etiquetas de los nodos.
        
        # Aristas originales (de fondo)
        nx.draw_networkx_edges(G, simulator.positions, width=1, alpha=0.6, edge_color='gray') # Dibuja las aristas originales en gris.
        
        # Aristas del MST (resaltadas)
        final_mst_edge_list = [(u, v) for u, v, w in mst_edges] # Lista de las aristas del MST.
        nx.draw_networkx_edges(G, simulator.positions, edgelist=final_mst_edge_list, width=3, edge_color='red') # Dibuja las aristas del MST en rojo.
        
        # Etiquetas de peso
        edge_labels = nx.get_edge_attributes(G, 'weight') # Obtiene los pesos de las aristas.
        nx.draw_networkx_edge_labels(G, simulator.positions, edge_labels=edge_labels, font_size=8, font_color='darkgreen') # Dibuja los pesos de las aristas.
        
        plt.title("Árbol de Expansión Mínima (MST) Final") # Título del gráfico final.
        plt.axis('off') # Desactiva los ejes.
        plt.show() # Muestra el gráfico final.

if __name__ == "__main__": # Bloque que asegura que 'main()' se ejecute solo cuando el script es el programa principal.
    main() # Llama a la función principal.


