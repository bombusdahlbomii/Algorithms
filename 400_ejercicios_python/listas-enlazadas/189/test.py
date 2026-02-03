import pytest
from linked_list import ListaEnlazada 

# --- FIXTURES (Datos de prueba reutilizables) ---
@pytest.fixture
def empty_list():
    return ListaEnlazada()

@pytest.fixture
def single_node_list():
    ll = ListaEnlazada()
    ll.add(10)
    return ll

@pytest.fixture
def normal_list():
    ll = ListaEnlazada()
    datos = [1, 2, 3, 4, 5]
    for d in datos:
        ll.add(d)
    return ll

# --- CASOS DE PRUEBA ---

def test_reverse_structure(normal_list):
    """Prueba que el orden se invierta correctamente [1,2,3,4,5] -> [5,4,3,2,1]"""
    print(f"\nAntes: {normal_list.to_list()}")
    
    normal_list.reverse()
    
    print(f"Después: {normal_list.to_list()}")
    
    expected = [5, 4, 3, 2, 1]
    assert normal_list.to_list() == expected

def test_reverse_pointers_integrity(normal_list):
    """Prueba técnica: Verifica que self.head y self.tail sean correctos tras invertir."""
    normal_list.reverse()
    
    # El nuevo head debe ser 5
    assert normal_list.head.data == 5
    # El nuevo tail debe ser 1
    assert normal_list.tail.data == 1
    # El tail debe apuntar a None (fin de lista)
    assert normal_list.tail.next is None

def test_reverse_empty_list(empty_list):
    """Prueba de robustez: Invertir lista vacía no debe fallar."""
    empty_list.reverse()
    assert empty_list.head is None
    assert empty_list.tail is None

def test_reverse_single_node(single_node_list):
    """Prueba de borde: Una lista de 1 elemento queda igual, pero head==tail."""
    single_node_list.reverse()
    
    assert single_node_list.to_list() == [10]
    # En una lista de 1 elemento, head y tail son el mismo objeto
    assert single_node_list.head is single_node_list.tail

def test_reverse_double_inversion(normal_list):
    """Prueba lógica: Invertir dos veces devuelve al estado original."""
    original = normal_list.to_list()
    
    normal_list.reverse() # Invertir
    normal_list.reverse() # Re-invertir
    
    assert normal_list.to_list() == original