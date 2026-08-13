import random

# =============================================================================
# MOTOR ALGEBRAICO DEL TRES
# =============================================================================

P = [-1, 0, 1]

def interaction(a, b):
    """Operación ⊗ (interacción / producto) del Tres."""
    if a == 0 or b == 0:
        return 0
    return a * b

def copresence(a, b):
    """Operación ⊕ (co-presencia / síntesis dialéctica) del Tres."""
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    return 0

def up(x):
    """Operación ↑ (actualización forzada): 0→1, resto sin cambio."""
    return 1 if x == 0 else x

def down(x):
    """Operación ↓ (exclusión forzada): 0→-1, resto sin cambio."""
    return -1 if x == 0 else x

def apply_op(x, op):
    """Aplica operación unaria opcional a un valor ternario."""
    if op == 'up':
        return up(x)
    if op == 'down':
        return down(x)
    return x

# =============================================================================
# DATASETS
# =============================================================================

DATASET_SENTIMIENTO = [
    (-1, -1, 1),   # doble negación → positivo
    (-1, 0, -1),   # negativo + neutro → negativo
    (-1, 1, 0),    # negativo + positivo → conflicto
    (0, -1, -1),   # neutro + negativo → negativo
    (0, 0, 0),     # neutro + neutro → neutro
    (0, 1, 1),     # neutro + positivo → positivo
    (1, -1, 0),    # positivo + negativo → conflicto
    (1, 0, 1),     # positivo + neutro → positivo
    (1, 1, 1),     # positivo + positivo → positivo
]

DATASET_XOR = [
    (-1, -1, -1), (-1, 0, 1), (-1, 1, 1),
    (0, -1, 1), (0, 0, 0), (0, 1, -1),
    (1, -1, 1), (1, 0, -1), (1, 1, -1),
]

DATASET_MAYORIA = [
    (-1, -1, -1), (-1, 0, -1), (-1, 1, 0),
    (0, -1, -1), (0, 0, 0), (0, 1, 0),
    (1, -1, 0), (1, 0, 0), (1, 1, 1),
]

# =============================================================================
# NEURONA DEL TRES
# =============================================================================

class NeuronaDelTres:
    """Neurona funcional pura del Tres, sin memoria interna."""
    def __init__(self, num_inputs):
        self.num_inputs = num_inputs
        self.pesos = [random.choice(P) for _ in range(num_inputs)]
        self.orden = list(range(num_inputs))
        random.shuffle(self.orden)
        self.op = random.choice([None, 'up', 'down'])

    def forward(self, entradas):
        idx0 = self.orden[0]
        resultado = interaction(self.pesos[idx0], entradas[idx0])
        for k in range(1, self.num_inputs):
            idx = self.orden[k]
            term = interaction(self.pesos[idx], entradas[idx])
            resultado = copresence(resultado, term)
        return apply_op(resultado, self.op)

    def clone(self):
        n = NeuronaDelTres(self.num_inputs)
        n.pesos = self.pesos.copy()
        n.orden = self.orden.copy()
        n.op = self.op
        return n

    def mutate(self, tasa=0.15):
        for i in range(self.num_inputs):
            if random.random() < tasa:
                self.pesos[i] = random.choice(P)
        if random.random() < tasa and self.num_inputs >= 2:
            i, j = random.sample(range(self.num_inputs), 2)
            self.orden[i], self.orden[j] = self.orden[j], self.orden[i]
        if random.random() < tasa:
            self.op = random.choice([None, 'up', 'down'])

# =============================================================================
# RED FEEDFORWARD DEL TRES
# =============================================================================

class RedFeedforwardDelTres:
    """Red feedforward simple: 2 entradas → N ocultas → 1 salida."""
    def __init__(self, hidden_size=2):
        self.hidden_size = hidden_size
        self.hidden = [NeuronaDelTres(2) for _ in range(hidden_size)]
        self.output = NeuronaDelTres(hidden_size)

    def forward(self, x1, x2):
        hidden_outs = [n.forward([x1, x2]) for n in self.hidden]
        return self.output.forward(hidden_outs)

    def evaluate(self, dataset):
        aciertos = sum(1 for x1, x2, esp in dataset if self.forward(x1, x2) == esp)
        return aciertos / len(dataset)

    def clone(self):
        r = RedFeedforwardDelTres(self.hidden_size)
        r.hidden = [n.clone() for n in self.hidden]
        r.output = self.output.clone()
        return r

    def mutate(self, tasa=0.15):
        for n in self.hidden:
            n.mutate(tasa)
        self.output.mutate(tasa)

# =============================================================================
# FASE A: DESCENSO POR VECINDARIO TERNARIO
# =============================================================================

def error_en(red, lote):
    """Número de ejemplos mal clasificados en un lote."""
    errores = 0
    for x1, x2, esperado in lote:
        if red.forward(x1, x2) != esperado:
            errores += 1
    return errores

def entrenar_vecindario(
    red,
    dataset,
    epocas=200,
    batch_size=None,
    max_intentos=100,
    verbose=True,
    semilla=None
):
    """
    Entrena una RedFeedforwardDelTres usando descenso por vecindario.

    Parámetros:
      - red: RedFeedforwardDelTres ya instanciada
      - dataset: lista de (x1, x2, esperado)
      - epocas: número de pasadas sobre el dataset
      - batch_size: tamaño del lote (None = dataset completo)
      - max_intentos: mutaciones aleatorias por lote
      - verbose: mostrar progreso
      - semilla: semilla aleatoria opcional
    """
    if semilla is not None:
        random.seed(semilla)

    if batch_size is None:
        batch_size = len(dataset)

    dataset = list(dataset)

    for epoca in range(epocas):
        random.shuffle(dataset)

        for inicio in range(0, len(dataset), batch_size):
            lote = dataset[inicio:inicio + batch_size]
            error_actual = error_en(red, lote)

            if error_actual == 0:
                continue

            for _ in range(max_intentos):
                todas = red.hidden + [red.output]
                neurona = random.choice(todas)

                tipo = random.choice(['peso', 'orden', 'op'])

                if tipo == 'peso':
                    if len(neurona.pesos) == 0:
                        continue
                    idx = random.randrange(len(neurona.pesos))
                    viejo = neurona.pesos[idx]
                    opciones = [v for v in P if v != viejo]
                    nuevo = random.choice(opciones)
                    neurona.pesos[idx] = nuevo

                elif tipo == 'orden':
                    if len(neurona.orden) < 2:
                        continue
                    i, j = random.sample(range(len(neurona.orden)), 2)
                    neurona.orden[i], neurona.orden[j] = neurona.orden[j], neurona.orden[i]

                else:  # 'op'
                    viejo_op = neurona.op
                    opciones = [op for op in [None, 'up', 'down'] if op != viejo_op]
                    neurona.op = random.choice(opciones)

                error_nuevo = error_en(red, lote)

                if error_nuevo < error_actual:
                    error_actual = error_nuevo
                    if error_nuevo == 0:
                        break
                else:
                    if tipo == 'peso':
                        neurona.pesos[idx] = viejo
                    elif tipo == 'orden':
                        neurona.orden[i], neurona.orden[j] = neurona.orden[j], neurona.orden[i]
                    else:
                        neurona.op = viejo_op

        if verbose:
            acc = red.evaluate(dataset)
            print(f"Época {epoca:3d} | Error: {error_en(red, dataset):d}/{len(dataset)} | "
                  f"Accuracy: {acc:.4f}")

    return red

# =============================================================================
# EJECUCIÓN PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("FASE A: DESCENSO POR VECINDARIO TERNARIO")
    print("=" * 70)

    # XOR
    print("\n[1] Entrenando feedforward 2→2→1 en XOR")
    random.seed(42)
    red_xor = RedFeedforwardDelTres(hidden_size=2)
    entrenar_vecindario(
        red_xor,
        DATASET_XOR,
        epocas=200,
        batch_size=9,
        max_intentos=300,
        verbose=True
    )
    acc_xor = red_xor.evaluate(DATASET_XOR)
    print(f"Resultado final XOR: {acc_xor:.4f} ({acc_xor*9:.0f}/9)")

    # Mayoría
    print("\n[2] Entrenando feedforward 2→2→1 en Mayoría")
    random.seed(123)
    red_may = RedFeedforwardDelTres(hidden_size=2)
    entrenar_vecindario(
        red_may,
        DATASET_MAYORIA,
        epocas=200,
        batch_size=9,
        max_intentos=300,
        verbose=True
    )
    acc_may = red_may.evaluate(DATASET_MAYORIA)
    print(f"Resultado final Mayoría: {acc_may:.4f} ({acc_may*9:.0f}/9)")

    # Sentimiento
    print("\n[3] Entrenando feedforward 2→2→1 en Sentimiento")
    random.seed(456)
    red_sen = RedFeedforwardDelTres(hidden_size=2)
    entrenar_vecindario(
        red_sen,
        DATASET_SENTIMIENTO,
        epocas=300,
        batch_size=9,
        max_intentos=400,
        verbose=True
    )
    acc_sen = red_sen.evaluate(DATASET_SENTIMIENTO)
    print(f"Resultado final Sentimiento: {acc_sen:.4f} ({acc_sen*9:.0f}/9)")

    print("\n" + "=" * 70)
    print("RESUMEN FASE A")
    print("=" * 70)
    print(f"XOR          : {acc_xor*100:5.1f}%  (límite feedforward: 77.78%)")
    print(f"Mayoría      : {acc_may*100:5.1f}%  (límite feedforward: 88.89%)")
    print(f"Sentimiento  : {acc_sen*100:5.1f}%  (límite feedforward: 88.89%)")
    print("=" * 70)
