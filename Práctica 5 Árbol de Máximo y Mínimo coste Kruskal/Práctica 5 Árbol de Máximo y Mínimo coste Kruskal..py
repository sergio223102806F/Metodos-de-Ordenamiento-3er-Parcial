import heapq # Importa el módulo heapq para usar una cola de prioridad (min-heap).
import matplotlib.pyplot as plt # Importa matplotlib para crear gráficos y visualizaciones.
import networkx as nx # Importa networkx para crear y manipular grafos.

class UnionFind: # Clase auxiliar para la estructura de datos Union-Find (también conocida como Disjoint Set Union).
    def __init__(self, nodes): # Constructor: inicializa cada nodo en su propio conjunto.
        self.parent = {node: node for node in nodes} # Cada nodo es inicialmente su propio padre.
        self.rank = {node: 0 for node in nodes} # Para optimización por rango (altura del árbol).

    def find(self, i): # Método para encontrar la raíz del conjunto al que pertenece el elemento 'i'.
        if self.parent[i] == i: # Si 'i' es su propio padre, es la raíz.
            return i
        self.parent[i] = self.find(self.parent[i]) # Compresión de caminos: hace que el padre apunte directamente a la raíz.
        return self.parent[i]

    def union(self, i, j): # Método para unir los conjuntos que contienen a 'i' y 'j'.
        root_i = self.find(i) # Encuentra la raíz del conjunto de 'i'.
        root_j = self.find(j) # Encuentra la raíz del conjunto de 'j'.

        if root_i != root_j: # Si están en conjuntos diferentes (no forman un ciclo).
            # Unión por rango: adjunta el árbol más pequeño al más grande.
            if self.rank[root_i] < self.rank[root_j]: # Si el rango de root_i es menor que el de root_j.
                self.parent[root_i] = root_j # root_i se convierte en hijo de root_j.
            elif self.rank[root_i] > self.rank[root_j]: # Si el rango de root_i es mayor que el de root_j.
                self.parent[root_j] = root_i # root_j se convierte en hijo de root_i.
            else: # Si los rangos son iguales.
                self.parent[root_j] = root_i # root_j se convierte en hijo de root_i.
                self.rank[root_i] += 1 # Incrementa el rango de root_i.
            return True # La unión fue exitosa (se conectaron dos componentes).
        return False # No se realizó la unión (ya estaban en el mismo conjunto, formarían un ciclo).

class KruskalSimulator: # Define la clase KruskalSimulator para simular el algoritmo de Kruskal.
    def __init__(self): # Constructor de la clase.
        self.graph = {} # Diccionario para almacenar el grafo: {nodo: {vecino: peso}}.
        self.edges = [] # Lista para almacenar todas las aristas del grafo: (peso, u, v).
        self.nodes = set() # Conjunto para almacenar todos los nodos del grafo.
        self.positions = {} # Diccionario para almacenar posiciones de los nodos (para visualización).
        self.visualization = True # Booleano para activar o desactivar la visualización gráfica paso a paso.

    def add_edge(self, u, v, weight): # Método para añadir una arista al grafo.
        if u not in self.graph: # Si el nodo 'u' no está en el grafo, lo inicializa.
            self.graph[u] = {}
        if v not in self.graph: # Si el nodo 'v' no está en el grafo, lo inicializa.
            self.graph[v] = {}
        self.graph[u][v] = weight # Añade la arista y su peso.
        self.graph[v][u] = weight # Añade la arista en la dirección opuesta (grafo no dirigido).
        self.edges.append((weight, u, v)) # Añade la arista a la lista de todas las aristas.
        self.nodes.add(u) # Añade los nodos al conjunto de nodos.
        self.nodes.add(v)

    def kruskal(self, type_of_tree="min"): # Implementa el algoritmo de Kruskal para MST (min o max).
        # Inicialización
        mst_edges = [] # Lista para almacenar las aristas que forman el MST/MXST.
        mst_cost = 0 # Costo total del MST/MXST.
        
        # Ordenar las aristas:
        # Para MST (costo mínimo): ordenar de menor a mayor peso.
        # Para MXST (costo máximo): ordenar de mayor a menor peso.
        sorted_edges = sorted(self.edges, key=lambda x: x[0], reverse=(type_of_tree == "max")) # Ordena las aristas por peso.
        
        uf = UnionFind(self.nodes) # Crea una instancia de Union-Find con todos los nodos.

        print(f"\n--- Iniciando Kruskal para {type_of_tree.upper()}imum Spanning Tree ---")
        print(f"Número total de nodos: {len(self.nodes)}")
        print(f"Número total de aristas: {len(self.edges)}")
        print(f"Aristas ordenadas ({type_of_tree}): {sorted_edges}\n")
        
        # Para la visualización inicial
        if self.visualization:
            self.visualize_step(None, None, [], "Inicialización") # Muestra el grafo inicial sin aristas resaltadas.

        # Iterar sobre las aristas ordenadas
        for weight, u, v in sorted_edges: # Recorre las aristas una por una en el orden definido.
            print(f"  Procesando arista: ({u} - {v}, peso: {weight})")

            # Comprobar si añadir esta arista forma un ciclo usando Union-Find.
            if uf.find(u) != uf.find(v): # Si los nodos 'u' y 'v' pertenecen a diferentes componentes (no forman un ciclo).
                uf.union(u, v) # Une los dos componentes, añadiendo la arista al MST/MXST.
                mst_edges.append((u, v, weight)) # Añade la arista al resultado.
                mst_cost += weight # Suma el peso al costo total.
                print(f"    -> Añadida al {type_of_tree.upper()}ST. Componentes de {u} y {v} unidos.")
                print(f"    Costo actual del {type_of_tree.upper()}ST: {mst_cost}")
                print(f"    Aristas en el {type_of_tree.upper()}ST: {mst_edges}")

                if self.visualization: # Si la visualización está activada.
                    self.visualize_step(u, v, mst_edges, f"Añadida {u}-{v} (costo: {weight})") # Muestra el grafo con la nueva arista resaltada.
                
                # Criterio de parada: el MST/MXST tiene (V - 1) aristas.
                if len(mst_edges) == len(self.nodes) - 1: # Si ya se han añadido V-1 aristas (V es el número de nodos).
                    print(f"\nSe han añadido {len(self.nodes) - 1} aristas. {type_of_tree.upper()}ST completado.")
                    break # Termina el bucle, el MST/MXST está completo.
            else: # Si los nodos 'u' y 'v' ya están en el mismo componente.
                print(f"    -> Arista ({u} - {v}) IGNORADA: forma un ciclo.")
                if self.visualization: # Muestra las aristas ignoradas si la visualización está activada.
                    self.visualize_step(u, v, mst_edges, f"Ignorada {u}-{v} (forma ciclo)", ignored=True)

        return mst_edges, mst_cost # Retorna las aristas del MST/MXST y su costo total.

    def visualize_step(self, u_highlight=None, v_highlight=None, current_mst_edges=[], title_suffix="", ignored=False): # Método para visualizar el progreso del algoritmo.
        G = nx.Graph() # Crea un nuevo objeto de grafo de NetworkX.
        
        # Añadir todos los nodos y aristas del grafo original
        for node in self.graph: # Itera sobre cada nodo en el grafo original.
            G.add_node(node) # Añade el nodo al grafo de visualización.
            for neighbor, weight in self.graph[node].items(): # Itera sobre los vecinos y pesos de cada nodo.
                if neighbor > node: # Para evitar duplicados en un grafo no dirigido.
                    G.add_edge(node, neighbor, weight=weight) # Añade la arista con su peso.
        
        # Posiciones para todos los nodos
        if not self.positions: # Si las posiciones no han sido definidas (primera vez).
            self.positions = nx.spring_layout(G, k=0.7, iterations=50) # Usa un algoritmo de diseño de resorte.
        
        plt.figure(figsize=(10, 7)) # Crea una nueva figura para el gráfico.
        
        # Dibujar nodos
        nx.draw_networkx_nodes(G, self.positions, node_size=800, node_color='lightblue') # Dibuja los nodos.
        nx.draw_networkx_labels(G, self.positions, font_size=10, font_family='sans-serif') # Dibuja las etiquetas de los nodos.
        
        # Dibujar todas las aristas originales (en gris claro como fondo)
        all_edges = list(G.edges(data=True)) # Obtiene todas las aristas con sus atributos.
        nx.draw_networkx_edges(G, self.positions, edgelist=[(u,v) for u,v,d in all_edges], width=1, alpha=0.6, edge_color='gray') # Dibuja todas las aristas en gris.
        
        # Dibujar las aristas actualmente en el MST/MXST (en azul)
        mst_edge_list = [(u, v) for u, v, w in current_mst_edges] # Lista de tuplas (u,v) para las aristas del MST/MXST.
        nx.draw_networkx_edges(G, self.positions, edgelist=mst_edge_list, width=2.5, edge_color='blue') # Dibuja las aristas del MST/MXST en azul.
        
        # Resaltar la arista que se está procesando en el paso actual
        if u_highlight is not None and v_highlight is not None: # Si hay una arista para resaltar.
            highlight_color = 'red' if not ignored else 'orange' # Rojo si se añade, naranja si se ignora.
            nx.draw_networkx_edges(G, self.positions, edgelist=[(u_highlight, v_highlight)], width=3, edge_color=highlight_color) # Resalta la arista.
        
        # Etiquetas de peso en las aristas
        edge_labels = nx.get_edge_attributes(G, 'weight') # Obtiene los pesos de las aristas.
        nx.draw_networkx_edge_labels(G, self.positions, edge_labels=edge_labels, font_size=8, font_color='darkgreen') # Dibuja los pesos de las aristas.
        
        plt.title(f"Algoritmo de Kruskal - {title_suffix}") # Establece el título del gráfico.
        plt.axis('off') # Desactiva los ejes.
        plt.show() # Muestra el gráfico.

# Ejemplo de uso
def main(): # Función principal para ejecutar la simulación.
    # --- Grafo de ejemplo ---
    # Este grafo se usará para ambos, MST y MXST.
    graph_edges = [
        ('A', 'B', 4), ('A', 'H', 8),
        ('B', 'C', 8), ('B', 'H', 11),
        ('C', 'D', 7), ('C', 'F', 4), ('C', 'I', 2),
        ('D', 'E', 9), ('D', 'F', 14),
        ('E', 'F', 10),
        ('F', 'G', 2),
        ('G', 'H', 1), ('G', 'I', 6),
        ('H', 'I', 7)
    ]

    # --- Simulación de Árbol de Expansión Mínima (MST) ---
    print("\n\n################################################################################")
    print("### SIMULACIÓN DE ÁRBOL DE EXPANSIÓN MÍNIMA (MST) CON KRUSKAL ###")
    print("################################################################################")
    mst_simulator = KruskalSimulator() # Crea una instancia del simulador para el MST.
    for u, v, w in graph_edges: # Añade las aristas al simulador.
        mst_simulator.add_edge(u, v, w)
    
    # Ejecutar Kruskal para el MST (min)
    mst_edges, mst_cost = mst_simulator.kruskal(type_of_tree="min") # Llama al método kruskal para MST.

    print("\n--- MST Final ---") # Encabezado de los resultados finales del MST.
    print(f"Aristas en el MST: {mst_edges}") # Muestra las aristas del MST.
    print(f"Costo total del MST: {mst_cost}") # Muestra el costo total del MST.
    
    # Visualización final del MST
    if mst_simulator.visualization: # Si la visualización está activada.
        mst_simulator.visualize_step(None, None, mst_edges, "Árbol de Expansión Mínima (MST) Final") # Muestra el gráfico final del MST.

    # --- Simulación de Árbol de Expansión Máxima (MXST) ---
    print("\n\n################################################################################")
    print("### SIMULACIÓN DE ÁRBOL DE EXPANSIÓN MÁXIMA (MXST) CON KRUSKAL ###")
    print("################################################################################")
    mxst_simulator = KruskalSimulator() # Crea otra instancia del simulador para el MXST.
    for u, v, w in graph_edges: # Añade las mismas aristas al simulador.
        mxst_simulator.add_edge(u, v, w)

    # Ejecutar Kruskal para el MXST (max)
    mxst_edges, mxst_cost = mxst_simulator.kruskal(type_of_tree="max") # Llama al método kruskal para MXST.

    print("\n--- MXST Final ---") # Encabezado de los resultados finales del MXST.
    print(f"Aristas en el MXST: {mxst_edges}") # Muestra las aristas del MXST.
    print(f"Costo total del MXST: {mxst_cost}") # Muestra el costo total del MXST.

    # Visualización final del MXST
    if mxst_simulator.visualization: # Si la visualización está activada.
        mxst_simulator.visualize_step(None, None, mxst_edges, "Árbol de Expansión Máxima (MXST) Final") # Muestra el gráfico final del MXST.

if __name__ == "__main__": # Bloque que asegura que 'main()' se ejecute solo cuando el script es el programa principal.
    main() # Llama a la función principal.
