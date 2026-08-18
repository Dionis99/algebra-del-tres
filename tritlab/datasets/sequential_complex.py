"""
Datasets secuenciales complejos para probar memoria temporal.
"""

# Dataset 1: Contador de signos
# La red debe contar cuántos -1 ha visto y emitir el signo del conteo
# Si hay más -1 que 1 → -1, si hay más 1 que -1 → 1, si empate → 0
DATASET_CONTADOR = [
    ([[1, 0]], 1),           # 1 positivo
    ([[-1, 0]], -1),         # 1 negativo
    ([[1, 0], [1, 0]], 1),   # 2 positivos
    ([[-1, 0], [-1, 0]], -1), # 2 negativos
    ([[1, 0], [-1, 0]], 0),  # empate
    ([[-1, 0], [1, 0]], 0),  # empate
    ([[1, 0], [1, 0], [-1, 0]], 1),  # 2 vs 1
    ([[-1, 0], [-1, 0], [1, 0]], -1), # 2 vs 1
    ([[1, 0], [-1, 0], [1, 0]], 1),  # 2 vs 1
    ([[-1, 0], [1, 0], [-1, 0]], -1), # 2 vs 1
    ([[0, 0], [1, 0]], 1),   # cero no cuenta
    ([[0, 0], [-1, 0]], -1), # cero no cuenta
    ([[1, 0], [0, 0], [1, 0]], 1),  # ceros intermedios
    ([[-1, 0], [0, 0], [-1, 0]], -1), # ceros intermedios
]

# Dataset 2: Último signo no-cero
# La red debe recordar el último signo no-cero visto
DATASET_ULTIMO_SIGNO = [
    ([[1, 0]], 1),
    ([[-1, 0]], -1),
    ([[0, 0], [1, 0]], 1),
    ([[0, 0], [-1, 0]], -1),
    ([[1, 0], [0, 0]], 1),      # último no-cero es 1
    ([[-1, 0], [0, 0]], -1),    # último no-cero es -1
    ([[1, 0], [-1, 0]], -1),    # último no-cero es -1
    ([[-1, 0], [1, 0]], 1),     # último no-cero es 1
    ([[1, 0], [0, 0], [-1, 0]], -1),  # último no-cero es -1
    ([[-1, 0], [0, 0], [1, 0]], 1),   # último no-cero es 1
    ([[0, 0], [0, 0], [1, 0]], 1),    # último no-cero es 1
    ([[0, 0], [0, 0], [-1, 0]], -1),  # último no-cero es -1
]

# Dataset 3: Alternancia
# La red debe detectar si la secuencia alterna signos (1,-1,1,-1...)
# Salida: 1 si alterna perfectamente, -1 si no, 0 si hay ceros
DATASET_ALTERNANCIA = [
    ([[1, 0]], 1),                    # un solo elemento, alterna por defecto
    ([[-1, 0]], 1),                   # un solo elemento
    ([[1, 0], [-1, 0]], 1),           # alterna
    ([[-1, 0], [1, 0]], 1),           # alterna
    ([[1, 0], [1, 0]], -1),           # no alterna
    ([[-1, 0], [-1, 0]], -1),         # no alterna
    ([[1, 0], [-1, 0], [1, 0]], 1),   # alterna
    ([[-1, 0], [1, 0], [-1, 0]], 1),  # alterna
    ([[1, 0], [1, 0], [1, 0]], -1),   # no alterna
    ([[1, 0], [-1, 0], [-1, 0]], -1), # no alterna (dos -1 seguidos)
    ([[0, 0], [1, 0]], 0),            # cero al inicio → indeterminado
    ([[1, 0], [0, 0]], 0),            # cero al final → indeterminado
]

# Dataset 4: Paridad de secuencia
# Salida: 1 si número par de -1, -1 si impar, 0 si hay ceros
DATASET_PARIDAD_SEC = [
    ([[1, 0]], 1),                    # 0 negativos → par
    ([[-1, 0]], -1),                  # 1 negativo → impar
    ([[1, 0], [1, 0]], 1),            # 0 negativos → par
    ([[-1, 0], [-1, 0]], 1),          # 2 negativos → par
    ([[1, 0], [-1, 0]], -1),          # 1 negativo → impar
    ([[-1, 0], [1, 0]], -1),          # 1 negativo → impar
    ([[1, 0], [1, 0], [1, 0]], 1),    # 0 negativos → par
    ([[-1, 0], [-1, 0], [-1, 0]], -1), # 3 negativos → impar
    ([[1, 0], [-1, 0], [1, 0]], -1),  # 1 negativo → impar
    ([[0, 0], [1, 0]], 0),            # cero → indeterminado
    ([[1, 0], [0, 0]], 0),            # cero → indeterminado
]

def get_dataset_secuencial(nombre: str):
    datasets = {
        "contador": DATASET_CONTADOR,
        "ultimo_signo": DATASET_ULTIMO_SIGNO,
        "alternancia": DATASET_ALTERNANCIA,
        "paridad_sec": DATASET_PARIDAD_SEC,
    }
    if nombre not in datasets:
        raise ValueError(f"Dataset '{nombre}' no existe")
    return datasets[nombre]

def list_datasets_secuenciales():
    return ["contador", "ultimo_signo", "alternancia", "paridad_sec"]

# Test
if __name__ == "__main__":
    print("=== Datasets Secuenciales Complejos ===")
    for nombre in list_datasets_secuenciales():
        dataset = get_dataset_secuencial(nombre)
        print(f"\n{nombre.upper()}: {len(dataset)} ejemplos")
        for entradas, esperado in dataset[:3]:
            print(f"  {entradas} → {esperado:+d}")
        print("  ...")
