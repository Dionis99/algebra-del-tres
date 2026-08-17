"""
Datasets básicos para benchmark de neuronas ternarias.
Cada dataset es una lista de tuplas (entradas, salida_esperada).
"""

# Dataset 1: Sentimiento ternario
DATASET_SENTIMIENTO = [
    ([-1, -1], 1),   # doble negación → positivo
    ([-1, 0], -1),   # negativo + neutro → negativo
    ([-1, 1], 0),    # negativo + positivo → conflicto
    ([0, -1], -1),   # neutro + negativo → negativo
    ([0, 0], 0),     # neutro + neutro → neutro
    ([0, 1], 1),     # neutro + positivo → positivo
    ([1, -1], 0),    # positivo + negativo → conflicto
    ([1, 0], 1),     # positivo + neutro → positivo
    ([1, 1], 1),     # positivo + positivo → positivo
]

# Dataset 2: XOR ternario
DATASET_XOR = [
    ([-1, -1], -1), ([-1, 0], 1), ([-1, 1], 1),
    ([0, -1], 1), ([0, 0], 0), ([0, 1], -1),
    ([1, -1], 1), ([1, 0], -1), ([1, 1], -1),
]

# Dataset 3: Mayoría
DATASET_MAYORIA = [
    ([-1, -1], -1), ([-1, 0], -1), ([-1, 1], 0),
    ([0, -1], -1), ([0, 0], 0), ([0, 1], 0),
    ([1, -1], 0), ([1, 0], 0), ([1, 1], 1),
]

def get_dataset(nombre: str):
    """Devuelve dataset por nombre."""
    datasets = {
        "sentimiento": DATASET_SENTIMIENTO,
        "xor": DATASET_XOR,
        "mayoria": DATASET_MAYORIA,
    }
    if nombre not in datasets:
        raise ValueError(f"Dataset '{nombre}' no existe. Opciones: {list(datasets.keys())}")
    return datasets[nombre]

def list_datasets():
    """Lista nombres de datasets disponibles."""
    return ["sentimiento", "xor", "mayoria"]

# Test
if __name__ == "__main__":
    print("=== Datasets Básicos ===")
    for nombre in list_datasets():
        dataset = get_dataset(nombre)
        print(f"\n{nombre.upper()}: {len(dataset)} ejemplos")
        for entradas, esperado in dataset:
            print(f"  {entradas} → {esperado:+d}")
