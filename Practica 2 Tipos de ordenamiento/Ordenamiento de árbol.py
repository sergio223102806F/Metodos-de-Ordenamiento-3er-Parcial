class Node: # Define una clase para representar un nodo en el árbol binario de búsqueda.
    def __init__(self, key): # Constructor de la clase Node.
        self.key = key # Almacena el valor (clave) del nodo.
        self.left = None # Inicializa el puntero al hijo izquierdo como None.
        self.right = None # Inicializa el puntero al hijo derecho como None

def insert(root, key): # Define una función para insertar una nueva clave en el BST.
    if root is None: # Si el árbol (o subárbol) está vacío, el nuevo nodo es la raíz.
        return Node(key) # Crea y retorna un nuevo nodo con la clave.
    else: # Si el árbol no está vacío, decide dónde insertar.
        if key < root.key: # Si la nueva clave es menor que la clave del nodo actual.
            root.left = insert(root.left, key) # Llama recursivamente a insert en el subárbol izquierdo.
        else: # Si la nueva clave es mayor o igual que la clave del nodo actual.
            root.right = insert(root.right, key) # Llama recursivamente a insert en el subárbol derecho.
    return root # Retorna la raíz (modificada) del subárbol.

def inorder_traversal(root, sorted_list): # Define una función para realizar un recorrido inorden del BST.
    if root: # Si el nodo actual no es None (es decir, existe).
        inorder_traversal(root.left, sorted_list) # Recorre recursivamente el subárbol izquierdo.
        sorted_list.append(root.key) # Agrega la clave del nodo actual a la lista ordenada.
        inorder_traversal(root.right, sorted_list) # Recorre recursivamente el subárbol derecho.

def tree_sort(arr): # Define la función principal para el ordenamiento de árbol.
    if not arr: # Si la lista de entrada está vacía, no hay nada que ordenar.
        return [] # Retorna una lista vacía.

    root = None # Inicializa la raíz del árbol binario de búsqueda como None.
    for element in arr: # Itera sobre cada elemento de la lista de entrada.
        root = insert(root, element) # Inserta cada elemento en el árbol. La 'root' se actualiza en cada inserción.

    sorted_list = [] # Inicializa una lista vacía para almacenar los elementos ordenados.
    inorder_traversal(root, sorted_list) # Realiza el recorrido inorden para llenar la lista ordenada.
    return sorted_list # Retorna la lista con los elementos ya ordenados.

---
### Ejemplo de Uso

```python
if __name__ == "__main__": # Esto asegura que el código dentro solo se ejecute cuando el script se corre directamente.
    lista_desordenada = [7, 3, 9, 1, 5, 8, 2] # Crea una lista de ejemplo desordenada.
    print(f"Lista desordenada: {lista_desordenada}") # Imprime la lista original.

    lista_ordenada = tree_sort(lista_desordenada) # Llama a la función tree_sort para ordenar la lista.
    print(f"Lista ordenada (Tree Sort): {lista_ordenada}") # Imprime la lista ya ordenada.

    print("\n--- Otro ejemplo ---") # Imprime un separador para otro ejemplo.
    lista_grande = [64, 25, 12, 22, 11, 90, 78, 34, 45, 56, 1, 89] # Crea una lista más grande.
    print(f"Lista desordenada: {lista_grande}") # Imprime la lista grande desordenada.
    lista_ordenada_grande = tree_sort(lista_grande) # Ordena la lista grande.
    print(f"Lista ordenada (Tree Sort): {lista_ordenada_grande}") # Imprime la lista grande ordenada.

    print("\n--- Ejemplo con lista casi ordenada ---") # Imprime un separador.
    lista_casi_ordenada = [1, 2, 4, 3, 5, 6] # Crea una lista casi ordenada.
    print(f"Lista casi ordenada: {lista_casi_ordenada}") # Imprime la lista casi ordenada.
    lista_ordenada_casi = tree_sort(lista_casi_ordenada) # Ordena la lista casi ordenada.
    print(f"Lista ordenada (Tree Sort): {lista_ordenada_casi}") # Imprime la lista casi ordenada después de ordenarla.

    print("\n--- Ejemplo con lista ya ordenada ---") # Imprime un separador.
    lista_ya_ordenada = [1, 2, 3, 4, 5] # Crea una lista ya ordenada.
    print(f"Lista ya ordenada: {lista_ya_ordenada}") # Imprime la lista ya ordenada.
    lista_ordenada_ya = tree_sort(lista_ya_ordenada) # Ordena una lista ya ordenada.
    print(f"Lista ordenada (Tree Sort): {lista_ordenada_ya}") # Imprime la lista ya ordenada.

    print("\n--- Ejemplo con lista vacía ---") # Imprime un separador.
    lista_vacia = [] # Crea una lista vacía.
    print(f"Lista vacía: {lista_vacia}") # Imprime la lista vacía.
    lista_ordenada_vacia = tree_sort(lista_vacia) # Ordena una lista vacía.
    print(f"Lista ordenada (Tree Sort): {lista_ordenada_vacia}") # Imprime la lista vacía.

    print("\n--- Ejemplo con lista de un solo elemento ---") # Imprime un separador.
    lista_un_elemento = [7] # Crea una lista con un solo elemento.
    print(f"Lista de un solo elemento: {lista_un_elemento}") # Imprime la lista de un solo elemento.
    lista_ordenada_un_elemento = tree_sort(lista_un_elemento) # Ordena una lista de un solo elemento.
    print(f"Lista ordenada (Tree Sort): {lista_ordenada_un_elemento}") # Imprime la lista de un solo elemento.