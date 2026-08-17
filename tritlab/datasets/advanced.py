"""
Datasets avanzados para probar T3-NA y T3-R.
"""

# Dataset con 3 entradas: paridad ternaria
DATASET_PARIDAD_3 = [
    ([-1, -1, -1], -1), ([-1, -1, 0], 0), ([-1, -1, 1], 1),
    ([-1, 0, -1], 0), ([-1, 0, 0], 0), ([-1, 0, 1], 0),
    ([-1, 1, -1], 1), ([-1, 1, 0], 0), ([-1, 1, 1], -1),
    ([0, -1, -1], 0), ([0, -1, 0], 0), ([0, -1, 1], 0),
    ([0, 0, -1], 0), ([0, 0, 0], 0), ([0, 0, 1], 0),
    ([0, 1, -1], 0), ([0, 1, 0], 0), ([0, 1, 1], 0),
    ([1, -1, -1], 1), ([1, -1, 0], 0), ([1, -1, 1], -1),
    ([1, 0, -1], 0), ([1, 0, 0], 0), ([1, 0, 1], 0),
    ([1, 1, -1], -1), ([1, 1, 0], 0), ([1, 1, 1], 1),
]

# Dataset con 3 entradas: mayoría ternaria
DATASET_MAYORIA_3 = [
    ([-1, -1, -1], -1), ([-1, -1, 0], -1), ([-1, -1, 1], -1),
    ([-1, 0, -1], -1), ([-1, 0, 0], 0), ([-1, 0, 1], 0),
    ([-1, 1, -1], -1), ([-1, 1, 0], 0), ([-1, 1, 1], 1),
    ([0, -1, -1], -1), ([0, -1, 0], 0), ([0, -1, 1], 0),
    ([0, 0, -1], 0), ([0, 0, 0], 0), ([0, 0, 1], 0),
    ([0, 1, -1], 0), ([0, 1, 0], 0), ([0, 1, 1], 1),
    ([1, -1, -1], -1), ([1, -1, 0], 0), ([1, -1, 1], 1),
    ([1, 0, -1], 0), ([1, 0, 0], 0), ([1, 0, 1], 1),
    ([1, 1, -1], 1), ([1, 1, 0], 1), ([1, 1, 1], 1),
]

# Dataset secuencial: memoria de signo
# CORREGIDO: todas las tuplas correctamente formateadas
DATASET_SECUENCIAL_MEMORIA = [
    ([[1, 0], [0, 0]], 1),
    ([[0, 1], [0, 0]], 1),
    ([[-1, 0], [0, 0]], -1),
    ([[0, -1], [0, 0]], -1),
    ([[1, 1], [-1, -1]], -1),
    ([[-1, -1], [1, 1]], 1),
    ([[0, 0], [1, 1]], 1),
    ([[0, 0], [-1, -1]], -1),
    ([[1, 0], [-1, 0]], -1),
    ([[-1, 0], [1, 0]], 1),
]

# Dataset secuencial: paridad de secuencia
DATASET_SECUENCIAL_PARIDAD = [
    ([[1, 1], [1, 1]], 1),
    ([[-1, 1], [1, 1]], -1),
    ([[-1, -1], [1, 1]], 1),
    ([[1, 1], [-1, 1]], -1),
    ([[1, -1], [1, -1]], 1),
    ([[0, 0], [0, 0]], 0),
    ([[1, 0], [0, 1]], 1),
    ([[-1, 0], [0, -1]], 1),
]

def get_dataset_avanzado(nombre: str):
    datasets = {
        "paridad_3": DATASET_PARIDAD_3,
        "mayoria_3": DATASET_MAYORIA_3,
        "sec_memoria": DATASET_SECUENCIAL_MEMORIA,
        "sec_paridad": DATASET_SECUENCIAL_PARIDAD,
    }
    if nombre not in datasets:
        raise ValueError(f"Dataset '{nombre}' no existe")
    return datasets[nombre]

def list_datasets_avanzados():
    return ["paridad_3", "mayoria_3", "sec_memoria", "sec_paridad"]

# Test
if __name__ == "__main__":
    print("=== Datasets Avanzados ===")
    for nombre in list_datasets_avanzados():
        dataset = get_dataset_avanzado(nombre)
        print(f"\n{nombre.upper()}: {len(dataset)} ejemplos")
        for entradas, esperado in dataset[:3]:
            if isinstance(entradas[0], list):
                print(f"  {entradas} → {esperado:+d}")
            else:
                print(f"  {entradas} → {esperado:+d}")
        print("  ...")
