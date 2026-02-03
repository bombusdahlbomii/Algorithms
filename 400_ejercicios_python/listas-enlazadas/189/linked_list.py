"""
Algoritmo con complejidad O(1) porque en el metodo `add(self, data)` para 
con puntero `tail` O(1)
- salto directo a la direccion de memoria
- siempre tarda lo mismo
- usa poquito mas de RAM porque guarda la variable `tail`
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class ListaEnlazada: 
    def __init__(self):
        self.head = None # EL inicio de la lista (Head)
        self.tail = None # puntero que indica el ultimo nodo

    def add(self, data):
        """Agrega un nodo al final en O(1) usando tail."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def reverse(self):
        """
        Objetivo: Invertir la lista en un solo recorrido O(n)
        """
        prev = None
        current = self.head
        self.tail = self.head # El head actual se convertira en el tail

        while current:
            # 1. Guardar el siguiente nodo temporalmente                (guardar el futuro)
            next_node = current.next
            # 2. Invertir el puintero 'next' del acutual hacia 'prev'   (Invertir la flecha)
            current.next = prev
            # 3. Mover 'prev' al lugar 'current'                        (Avanzar el previo)
            prev = current
            # 4. Mover 'current' al que guardaste en el paso 1          (Anvazar el actual)
            current = next_node
        
        self.head = prev # Al final, 'prev' queda apuntando al nuevo frente

    def to_list(self):
        """Convierte la lista enlazada a una lista de Python para facilitar la lectura."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements