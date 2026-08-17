"""
Motor algebraico del Tres: operaciones ⊗, ⊕, ↑, ↓ con tablas de verdad.
Versión optimizada con numpy para velocidad.
"""
import numpy as np

P_VALS = [-1, 0, 1]

# Tablas de verdad como matrices 3x3
# Índices: -1→0, 0→1, 1→2
IDX = {-1: 0, 0: 1, 1: 2}

# Tabla de interacción ⊗
INTERACTION_TABLE = np.zeros((3, 3), dtype=np.int8)
for i, a in enumerate(P_VALS):
    for j, b in enumerate(P_VALS):
        INTERACTION_TABLE[i, j] = 0 if (a == 0 or b == 0) else a * b

# Tabla de co-presencia ⊕
COPRESENCE_TABLE = np.zeros((3, 3), dtype=np.int8)
for i, a in enumerate(P_VALS):
    for j, b in enumerate(P_VALS):
        if a == b:
            COPRESENCE_TABLE[i, j] = a
        elif a == 0:
            COPRESENCE_TABLE[i, j] = b
        elif b == 0:
            COPRESENCE_TABLE[i, j] = a
        else:
            COPRESENCE_TABLE[i, j] = 0

def interaction(a: int, b: int) -> int:
    """⊗: interacción. 0 anula; si no, producto clásico."""
    return int(INTERACTION_TABLE[IDX[a], IDX[b]])

def copresence(a: int, b: int) -> int:
    """⊕: co-presencia. Igual refuerza; 0 deja pasar; opuestos → 0."""
    return int(COPRESENCE_TABLE[IDX[a], IDX[b]])

def up(x: int) -> int:
    """↑: actualización forzada. 0→1, resto sin cambio."""
    return 1 if x == 0 else x

def down(x: int) -> int:
    """↓: exclusión forzada. 0→-1, resto sin cambio."""
    return -1 if x == 0 else x

def apply_op(x: int, op: str = None) -> int:
    """Aplica operación unaria opcional."""
    if op == 'up': return up(x)
    if op == 'down': return down(x)
    return x

# Vectorizadas para eficiencia
def interaction_vec(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """⊗ vectorizado."""
    return np.where((a == 0) | (b == 0), 0, a * b).astype(np.int8)

def copresence_vec(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """⊕ vectorizado."""
    return np.where(
        a == b, a,
        np.where(a == 0, b, np.where(b == 0, a, 0))
    ).astype(np.int8)

# Tests básicos
if __name__ == "__main__":
    print("=== Motor Algebraico del Tres ===")
    print("⊗ (interacción):")
    for a in P_VALS:
        row = [interaction(a, b) for b in P_VALS]
        print(f"  {a:+d} ⊗ {P_VALS} = {row}")
    
    print("\n⊕ (co-presencia):")
    for a in P_VALS:
        row = [copresence(a, b) for b in P_VALS]
        print(f"  {a:+d} ⊕ {P_VALS} = {row}")
    
    print("\n↑ (actualización):")
    print(f"  ↑({P_VALS}) = {[up(x) for x in P_VALS]}")
    
    print("\n↓ (exclusión):")
    print(f"  ↓({P_VALS}) = {[down(x) for x in P_VALS]}")
    
    # Test no-asociatividad
    print("\n=== Test No-Asociatividad ===")
    a, b, c = 1, 1, -1
    left = copresence(copresence(a, b), c)
    right = copresence(a, copresence(b, c))
    print(f"({a}⊕{b})⊕{c} = {left}")
    print(f"{a}⊕({b}⊕{c}) = {right}")
    print(f"¿Asociativa? {left == right}")
