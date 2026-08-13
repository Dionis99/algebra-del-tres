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
# NEURONA FRAGMENTADA (MEMORIA MULTI-SLOT)
# =============================================================================

class NeuronaFragmentada:
    def __init__(self, num_inputs, num_slots=3):
        self.num_inputs = num_inputs
        self.num_slots = num_slots
        self.slots = [0] * num_slots

        # Pesos para computar salida (entradas + slot leído)
        self.pesos_out = [random.choice(P) for _ in range(num_inputs + 1)]
        self.orden_out = list(range(num_inputs + 1))
        random.shuffle(self.orden_out)
        self.op_out = random.choice([None, 'up', 'down'])

        # Pesos para decidir slot de lectura
        self.pesos_read = [random.choice(P) for _ in range(num_inputs)]
        self.orden_read = list(range(num_inputs))
        random.shuffle(self.orden_read)
        self.op_read = random.choice([None, 'up', 'down'])

        # Pesos para decidir slot de escritura
        self.pesos_write = [random.choice(P) for _ in range(num_inputs)]
        self.orden_write = list(range(num_inputs))
        random.shuffle(self.orden_write)
        self.op_write = random.choice([None, 'up', 'down'])

        # Pesos para decidir valor a escribir
        self.pesos_val = [random.choice(P) for _ in range(num_inputs)]
        self.orden_val = list(range(num_inputs))
        random.shuffle(self.orden_val)
        self.op_val = random.choice([None, 'up', 'down'])

    def _compute(self, entradas, pesos, orden, op):
        idx0 = orden[0]
        r = interaction(pesos[idx0], entradas[idx0])
        for k in range(1, len(entradas)):
            idx = orden[k]
            r = copresence(r, interaction(pesos[idx], entradas[idx]))
        return apply_op(r, op)

    def forward(self, entradas):
        # Leer de un slot
        read_idx = (self._compute(entradas, self.pesos_read, self.orden_read, self.op_read) + 1) % self.num_slots
        valor_leido = self.slots[read_idx]

        # Computar salida
        salida = self._compute(entradas + [valor_leido], self.pesos_out, self.orden_out, self.op_out)

        # Escribir en un slot
        write_idx = (self._compute(entradas, self.pesos_write, self.orden_write, self.op_write) + 1) % self.num_slots
        valor_escribir = self._compute(entradas, self.pesos_val, self.orden_val, self.op_val)
        self.slots[write_idx] = copresence(self.slots[write_idx], valor_escribir)

        return salida

    def reset(self):
        self.slots = [0] * self.num_slots

    def clone(self):
        n = NeuronaFragmentada(self.num_inputs, self.num_slots)
        n.slots = self.slots.copy()
        n.pesos_out = self.pesos_out.copy()
        n.orden_out = self.orden_out.copy()
        n.op_out = self.op_out
        n.pesos_read = self.pesos_read.copy()
        n.orden_read = self.orden_read.copy()
        n.op_read = self.op_read
        n.pesos_write = self.pesos_write.copy()
        n.orden_write = self.orden_write.copy()
        n.op_write = self.op_write
        n.pesos_val = self.pesos_val.copy()
        n.orden_val = self.orden_val.copy()
        n.op_val = self.op_val
        return n

class RedFragmentada:
    def __init__(self, hidden_size=3, num_slots=3, num_steps=3):
        self.hidden_size = hidden_size
        self.num_slots = num_slots
        self.num_steps = num_steps
        self.hidden = [NeuronaFragmentada(2, num_slots) for _ in range(hidden_size)]
        self.output = NeuronaFragmentada(hidden_size, num_slots)

    def reset(self):
        for n in self.hidden:
            n.reset()
        self.output.reset()

    def forward(self, x1, x2):
        for _ in range(self.num_steps):
            hidden_outs = [n.forward([x1, x2]) for n in self.hidden]
            salida = self.output.forward(hidden_outs)
        return salida

    def clone(self):
        r = RedFragmentada(self.hidden_size, self.num_slots, self.num_steps)
        r.hidden = [n.clone() for n in self.hidden]
        r.output = self.output.clone()
        return r

# =============================================================================
# FUNCIONES DE MUTACIÓN Y ERROR PARA FRAGMENTADAS
# =============================================================================

def mutar_un_parametro_fragmentada(red):
    """Modifica un solo parámetro aleatorio de una RedFragmentada."""
    todas = red.hidden + [red.output]
    neurona = random.choice(todas)

    # Grupos de parámetros mutables en cada neurona
    grupos = [
        ('peso', 'pesos_out'),
        ('peso', 'pesos_read'),
        ('peso', 'pesos_write'),
        ('peso', 'pesos_val'),
        ('orden', 'orden_out'),
        ('orden', 'orden_read'),
        ('orden', 'orden_write'),
        ('orden', 'orden_val'),
        ('op', 'op_out'),
        ('op', 'op_read'),
        ('op', 'op_write'),
        ('op', 'op_val'),
    ]

    tipo, attr = random.choice(grupos)

    if tipo == 'peso':
        lista = getattr(neurona, attr)
        if len(lista) == 0:
            return False
        idx = random.randrange(len(lista))
        viejo = lista[idx]
        opciones = [v for v in P if v != viejo]
        if not opciones:
            return False
        lista[idx] = random.choice(opciones)
    elif tipo == 'orden':
        lista = getattr(neurona, attr)
        if len(lista) < 2:
            return False
        i, j = random.sample(range(len(lista)), 2)
        lista[i], lista[j] = lista[j], lista[i]
    else:  # 'op'
        viejo_op = getattr(neurona, attr)
        opciones = [op for op in [None, 'up', 'down'] if op != viejo_op]
        if not opciones:
            return False
        setattr(neurona, attr, random.choice(opciones))

    return True

def error_fragmentada(red, dataset):
    errores = 0
    for x1, x2, esperado in dataset:
        red.reset()
        pred = red.forward(x1, x2)
        if pred != esperado:
            errores += 1
    return errores

# =============================================================================
# RECOCIDO SIMULADO PARA FRAGMENTADAS
# =============================================================================

def entrenar_fragmentada_recocido(red, dataset, epocas=200, intentos_por_epoca=200,
                                  T0=0.7, T_min=0.001, decay=0.995, seed=None):
    if seed is not None:
        random.seed(seed)

    current = red.clone()
    current_error = error_fragmentada(current, dataset)

    best = current.clone()
    best_error = current_error

    T = T0

    for epoca in range(epocas):
        for _ in range(intentos_por_epoca):
            candidato = current.clone()
            if not mutar_un_parametro_fragmentada(candidato):
                continue

            error_candidato = error_fragmentada(candidato, dataset)

            if (error_candidato < current_error or
                random.random() < math.exp((current_error - error_candidato) / T)):
                current = candidato
                current_error = error_candidato

                if current_error < best_error:
                    best_error = current_error
                    best = current.clone()
                    if best_error == 0:
                        return best, best_error

        T = max(T_min, T * decay)

    return best, best_error

# =============================================================================
# ENTRENAMIENTO CON REINICIOS MÚLTIPLES
# =============================================================================

def entrenar_fragmentada_con_reinicios(dataset, hidden_size=3, num_slots=3, num_steps=3,
                                       num_reinicios=15, epocas_por_reinicio=250,
                                       intentos_por_epoca=250, T0=0.7, decay=0.99,
                                       semilla_base=42):
    mejor_red = None
    mejor_error = float('inf')

    for r in range(num_reinicios):
        red = RedFragmentada(hidden_size, num_slots, num_steps)
        red_best, red_error = entrenar_fragmentada_recocido(
            red, dataset,
            epocas=epocas_por_reinicio,
            intentos_por_epoca=intentos_por_epoca,
            T0=T0, decay=decay,
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
    print("FASE B: FRAGMENTADAS CON RECOCIDO SIMULADO")
    print("=" * 70)

    # Sentimiento
    print("\n[1] Sentimiento")
    red_sen, err_sen = entrenar_fragmentada_con_reinicios(
        DATASET_SENTIMIENTO,
        num_reinicios=20,
        epocas_por_reinicio=300,
        intentos_por_epoca=300,
        T0=0.8, decay=0.99
    )
    acc_sen = 1 - err_sen/len(DATASET_SENTIMIENTO)
    print(f"  Resultado Sentimiento: {acc_sen:.4f} ({acc_sen*9:.0f}/9)")

    # XOR
    print("\n[2] XOR")
    red_xor, err_xor = entrenar_fragmentada_con_reinicios(
        DATASET_XOR,
        num_reinicios=20,
        epocas_por_reinicio=300,
        intentos_por_epoca=300,
        T0=0.8, decay=0.99
    )
    acc_xor = 1 - err_xor/len(DATASET_XOR)
    print(f"  Resultado XOR: {acc_xor:.4f} ({acc_xor*9:.0f}/9)")

    # Mayoría
    print("\n[3] Mayoría")
    red_may, err_may = entrenar_fragmentada_con_reinicios(
        DATASET_MAYORIA,
        num_reinicios=15,
        epocas_por_reinicio=250,
        intentos_por_epoca=250,
        T0=0.7, decay=0.99
    )
    acc_may = 1 - err_may/len(DATASET_MAYORIA)
    print(f"  Resultado Mayoría: {acc_may:.4f} ({acc_may*9:.0f}/9)")

    print("\n" + "=" * 70)
    print("RESUMEN FASE B")
    print("=" * 70)
    print(f"Sentimiento  : {acc_sen*100:5.1f}%  (límite feedforward: 88.89%)")
    print(f"XOR          : {acc_xor*100:5.1f}%  (límite feedforward: 77.78%)")
    print(f"Mayoría      : {acc_may*100:5.1f}%  (límite feedforward: 88.89%)")
    print("=" * 70)
