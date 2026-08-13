import random
import math

# =============================================================================
# MOTOR ALGEBRAICO DEL TRES
# =============================================================================

P = [-1, 0, 1]

def interaction(a, b):
    if a == 0 or b == 0:
        return 0
    return a * b

def copresence(a, b):
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    return 0

def up(x):
    return 1 if x == 0 else x

def down(x):
    return -1 if x == 0 else x

def apply_op(x, op):
    if op == 'up':
        return up(x)
    if op == 'down':
        return down(x)
    return x

# =============================================================================
# DATASETS
# =============================================================================

DATASET_SENTIMIENTO = [
    (-1, -1, 1), (-1, 0, -1), (-1, 1, 0),
    (0, -1, -1), (0, 0, 0), (0, 1, 1),
    (1, -1, 0), (1, 0, 1), (1, 1, 1),
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
# NEURONA Y RED FEEDFORWARD
# =============================================================================

class NeuronaDelTres:
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

class RedFeedforwardDelTres:
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

# =============================================================================
# FUNCIONES AUXILIARES PARA MUTACIÓN
# =============================================================================

def mutar_un_parametro(red):
    """Modifica UN solo parámetro aleatorio de la red."""
    todas = red.hidden + [red.output]
    neurona = random.choice(todas)

    tipo = random.choice(['peso', 'orden', 'op'])

    if tipo == 'peso':
        if len(neurona.pesos) == 0:
            return False
        idx = random.randrange(len(neurona.pesos))
        viejo = neurona.pesos[idx]
        opciones = [v for v in P if v != viejo]
        if not opciones:
            return False
        neurona.pesos[idx] = random.choice(opciones)
    elif tipo == 'orden':
        if len(neurona.orden) < 2:
            return False
        i, j = random.sample(range(len(neurona.orden)), 2)
        neurona.orden[i], neurona.orden[j] = neurona.orden[j], neurona.orden[i]
    else:  # 'op'
        viejo_op = neurona.op
        opciones = [op for op in [None, 'up', 'down'] if op != viejo_op]
        if not opciones:
            return False
        neurona.op = random.choice(opciones)

    return True

def error_en(red, lote):
    errores = 0
    for x1, x2, esperado in lote:
        if red.forward(x1, x2) != esperado:
            errores += 1
    return errores

# =============================================================================
# ENTRENAMIENTO POR RECOCIDO SIMULADO
# =============================================================================

def entrenar_recocido(
    red,
    dataset,
    epocas=300,
    intentos_por_epoca=100,
    T0=0.5,
    T_min=0.001,
    decay=0.995,
    seed=None
):
    if seed is not None:
        random.seed(seed)

    current = red.clone()
    current_error = error_en(current, dataset)

    best = current.clone()
    best_error = current_error

    T = T0

    for epoca in range(epocas):
        for _ in range(intentos_por_epoca):
            candidato = current.clone()
            if not mutar_un_parametro(candidato):
                continue

            error_candidato = error_en(candidato, dataset)

            # Aceptación por Boltzmann
            if (error_candidato < current_error or
                random.random() < math.exp((current_error - error_candidato) / T)):
                current = candidato
                current_error = error_candidato

                if current_error < best_error:
                    best_error = current_error
                    best = current.clone()
                    if best_error == 0:
                        return best, best_error

        # Enfriar la temperatura
        T = max(T_min, T * decay)

        # Si hay mejora, registramos
        # (opcional) mostrar progreso
        # print(f"Época {epoca:3d} | Error actual: {current_error}/{len(dataset)} | "
        #       f"Mejor error: {best_error}/{len(dataset)} | T: {T:.4f}")

    return best, best_error

# =============================================================================
# ENTRENAMIENTO CON REINICIOS MÚLTIPLES
# =============================================================================

def entrenar_con_reinicios(
    dataset,
    hidden_size=2,
    num_reinicios=20,
    epocas_por_reinicio=150,
    intentos_por_epoca=100,
    T0=0.5,
    decay=0.99,
    semilla_base=42
):
    mejor_red = None
    mejor_error = float('inf')

    for r in range(num_reinicios):
        red = RedFeedforwardDelTres(hidden_size)
        red_best, red_error = entrenar_recocido(
            red,
            dataset,
            epocas=epocas_por_reinicio,
            intentos_por_epoca=intentos_por_epoca,
            T0=T0,
            decay=decay,
            seed=semilla_base + r
        )

        print(f"  Reinicio {r+1:2d}/{num_reinicios} | Mejor error: {red_error}/{len(dataset)} "
              f"| Accuracy: {1 - red_error/len(dataset):.4f}")

        if red_error < mejor_error:
            mejor_error = red_error
            mejor_red = red_best.clone()
            if mejor_error == 0:
                break

    return mejor_red, mejor_error

# =============================================================================
# EJECUCIÓN PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("FASE A MEJORADA: RECOCIDO SIMULADO + REINICIOS")
    print("=" * 70)

    # XOR
    print("\n[1] XOR ternario")
    mejor_red_xor, err_xor = entrenar_con_reinicios(
        DATASET_XOR,
        num_reinicios=20,
        epocas_por_reinicio=200,
        intentos_por_epoca=150,
        T0=0.6,
        decay=0.99
    )
    acc_xor = 1 - err_xor/len(DATASET_XOR)
    print(f"  Resultado XOR: {acc_xor:.4f} ({acc_xor*9:.0f}/9)")

    # Mayoría
    print("\n[2] Mayoría")
    mejor_red_may, err_may = entrenar_con_reinicios(
        DATASET_MAYORIA,
        num_reinicios=20,
        epocas_por_reinicio=200,
        intentos_por_epoca=150,
        T0=0.6,
        decay=0.99
    )
    acc_may = 1 - err_may/len(DATASET_MAYORIA)
    print(f"  Resultado Mayoría: {acc_may:.4f} ({acc_may*9:.0f}/9)")

    # Sentimiento
    print("\n[3] Sentimiento")
    mejor_red_sen, err_sen = entrenar_con_reinicios(
        DATASET_SENTIMIENTO,
        num_reinicios=30,
        epocas_por_reinicio=250,
        intentos_por_epoca=150,
        T0=0.7,
        decay=0.99
    )
    acc_sen = 1 - err_sen/len(DATASET_SENTIMIENTO)
    print(f"  Resultado Sentimiento: {acc_sen:.4f} ({acc_sen*9:.0f}/9)")

    print("\n" + "=" * 70)
    print("RESUMEN FASE A MEJORADA")
    print("=" * 70)
    print(f"XOR          : {acc_xor*100:5.1f}%  (límite feedforward: 77.78%)")
    print(f"Mayoría      : {acc_may*100:5.1f}%  (límite feedforward: 88.89%)")
    print(f"Sentimiento  : {acc_sen*100:5.1f}%  (límite feedforward: 88.89%)")
    print("=" * 70)
