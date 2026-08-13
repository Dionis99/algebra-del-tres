import random
import math
import time

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
# NEURONA FRAGMENTADA Y RED
# =============================================================================

class NeuronaFragmentada:
    def __init__(self, num_inputs, num_slots=3):
        self.num_inputs = num_inputs
        self.num_slots = num_slots
        self.slots = [0] * num_slots
        self.pesos_out = [random.choice(P) for _ in range(num_inputs + 1)]
        self.orden_out = list(range(num_inputs + 1)); random.shuffle(self.orden_out)
        self.op_out = random.choice([None, 'up', 'down'])
        self.pesos_read = [random.choice(P) for _ in range(num_inputs)]
        self.orden_read = list(range(num_inputs)); random.shuffle(self.orden_read)
        self.op_read = random.choice([None, 'up', 'down'])
        self.pesos_write = [random.choice(P) for _ in range(num_inputs)]
        self.orden_write = list(range(num_inputs)); random.shuffle(self.orden_write)
        self.op_write = random.choice([None, 'up', 'down'])
        self.pesos_val = [random.choice(P) for _ in range(num_inputs)]
        self.orden_val = list(range(num_inputs)); random.shuffle(self.orden_val)
        self.op_val = random.choice([None, 'up', 'down'])

    def _compute(self, entradas, pesos, orden, op):
        idx0 = orden[0]
        r = interaction(pesos[idx0], entradas[idx0])
        for k in range(1, len(entradas)):
            idx = orden[k]
            r = copresence(r, interaction(pesos[idx], entradas[idx]))
        return apply_op(r, op)

    def forward(self, entradas):
        read_idx = (self._compute(entradas, self.pesos_read, self.orden_read, self.op_read) + 1) % self.num_slots
        valor_leido = self.slots[read_idx]
        salida = self._compute(entradas + [valor_leido], self.pesos_out, self.orden_out, self.op_out)
        write_idx = (self._compute(entradas, self.pesos_write, self.orden_write, self.op_write) + 1) % self.num_slots
        valor_escribir = self._compute(entradas, self.pesos_val, self.orden_val, self.op_val)
        self.slots[write_idx] = copresence(self.slots[write_idx], valor_escribir)
        return salida

    def reset(self):
        self.slots = [0] * self.num_slots

    def clone(self):
        n = NeuronaFragmentada(self.num_inputs, self.num_slots)
        n.slots = self.slots.copy()
        for attr in ['pesos_out','orden_out','op_out','pesos_read','orden_read','op_read',
                     'pesos_write','orden_write','op_write','pesos_val','orden_val','op_val']:
            setattr(n, attr, getattr(self, attr).copy() if isinstance(getattr(self, attr), list) else getattr(self, attr))
        return n

class RedFragmentada:
    def __init__(self, hidden_size=3, num_slots=3, num_steps=3):
        self.hidden_size = hidden_size
        self.num_slots = num_slots
        self.num_steps = num_steps
        self.hidden = [NeuronaFragmentada(2, num_slots) for _ in range(hidden_size)]
        self.output = NeuronaFragmentada(hidden_size, num_slots)

    def reset(self):
        for n in self.hidden: n.reset()
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
# MUTACIÓN Y ERROR
# =============================================================================

def mutar_un_parametro_fragmentada(red):
    todas = red.hidden + [red.output]
    neurona = random.choice(todas)
    grupos = [
        ('peso', 'pesos_out'), ('peso', 'pesos_read'), ('peso', 'pesos_write'), ('peso', 'pesos_val'),
        ('orden', 'orden_out'), ('orden', 'orden_read'), ('orden', 'orden_write'), ('orden', 'orden_val'),
        ('op', 'op_out'), ('op', 'op_read'), ('op', 'op_write'), ('op', 'op_val'),
    ]
    tipo, attr = random.choice(grupos)
    if tipo == 'peso':
        lista = getattr(neurona, attr)
        if len(lista) == 0: return False
        idx = random.randrange(len(lista))
        viejo = lista[idx]
        opciones = [v for v in P if v != viejo]
        if not opciones: return False
        lista[idx] = random.choice(opciones)
    elif tipo == 'orden':
        lista = getattr(neurona, attr)
        if len(lista) < 2: return False
        i, j = random.sample(range(len(lista)), 2)
        lista[i], lista[j] = lista[j], lista[i]
    else:
        viejo_op = getattr(neurona, attr)
        opciones = [op for op in [None, 'up', 'down'] if op != viejo_op]
        if not opciones: return False
        setattr(neurona, attr, random.choice(opciones))
    return True

def error_fragmentada(red, dataset):
    errores = 0
    for x1, x2, esperado in dataset:
        red.reset()
        pred = red.forward(x1, x2)
        if pred != esperado: errores += 1
    return errores

# =============================================================================
# UNA CORRIDA INDEPENDIENTE DE RECOCIDO
# =============================================================================

def corrida_recocido(dataset, semilla, epocas=200, intentos_por_epoca=200,
                     T0=0.8, decay=0.99, T_min=0.001):
    random.seed(semilla)
    red = RedFragmentada(hidden_size=3, num_slots=3, num_steps=3)
    current = red.clone()
    current_error = error_fragmentada(current, dataset)
    best = current.clone()
    best_error = current_error
    T = T0
    epoca_solucion = None

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
                        epoca_solucion = epoca
                        return best, best_error, epoca_solucion
        T = max(T_min, T * decay)
        if epoca_solucion is None and best_error == 0:
            epoca_solucion = epoca
            break
    return best, best_error, epoca_solucion

# =============================================================================
# ESTADÍSTICAS PARA UN DATASET
# =============================================================================

def evaluar_robustez(dataset, nombre, n_runs=20):
    exitos = 0
    errores = []
    epocas_exito = []
    t0 = time.time()

    for i in range(n_runs):
        semilla = 1000 + i
        _, error, epoca = corrida_recocido(dataset, semilla)
        errores.append(error)
        if error == 0:
            exitos += 1
            epocas_exito.append(epoca if epoca is not None else 200)
        print(f"  Run {i+1:2d}/{n_runs} | Error: {error}/9 | Época: {epoca}")

    t1 = time.time()
    print(f"\n[RESUMEN {nombre}]")
    print(f"  Éxitos: {exitos}/{n_runs} = {100*exitos/n_runs:.1f}%")
    if epocas_exito:
        print(f"  Época promedio para éxito: {sum(epocas_exito)/len(epocas_exito):.1f}")
    print(f"  Error promedio final: {sum(errores)/len(errores):.2f}")
    print(f"  Tiempo total: {t1-t0:.1f}s\n")

# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("FASE B2: ROBUSTEZ ESTADÍSTICA DE FRAGMENTADAS + RECOCIDO")
    print("=" * 70)

    print("\n--- Sentimiento ---")
    evaluar_robustez(DATASET_SENTIMIENTO, "Sentimiento", n_runs=20)

    print("\n--- XOR ---")
    evaluar_robustez(DATASET_XOR, "XOR", n_runs=20)

    print("\n--- Mayoría ---")
    evaluar_robustez(DATASET_MAYORIA, "Mayoría", n_runs=20)
