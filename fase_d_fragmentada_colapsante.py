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
# NEURONA COLAPSANTE V2 (usada como sub-módulo)
# =============================================================================

class NeuronaColapsanteV2:
    def __init__(self, num_inputs):
        self.num_inputs = num_inputs
        self.pesos = [random.choice(P) for _ in range(num_inputs)]
        self.orden = list(range(num_inputs))
        random.shuffle(self.orden)
        self.op = random.choice([None, 'up', 'down'])
        self.umbral_colapso = random.uniform(-0.9, 0.9)

    def _colapsar(self, peso, presion):
        if peso != 0:
            return peso
        return 1 if presion > self.umbral_colapso else -1

    def forward(self, entradas):
        presion = sum(entradas) / max(len(entradas), 1)
        idx0 = self.orden[0]
        w0 = self._colapsar(self.pesos[idx0], presion)
        resultado = interaction(w0, entradas[idx0])
        for k in range(1, self.num_inputs):
            idx = self.orden[k]
            wk = self._colapsar(self.pesos[idx], presion)
            term = interaction(wk, entradas[idx])
            resultado = copresence(resultado, term)
        return apply_op(resultado, self.op)

    def clone(self):
        n = NeuronaColapsanteV2(self.num_inputs)
        n.pesos = self.pesos.copy()
        n.orden = self.orden.copy()
        n.op = self.op
        n.umbral_colapso = self.umbral_colapso
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
        if random.random() < tasa:
            self.umbral_colapso = random.uniform(-0.9, 0.9)

# =============================================================================
# NEURONA FRAGMENTADA COLAPSANTE
# =============================================================================

class NeuronaFragmentadaColapsante:
    def __init__(self, num_inputs, num_slots=3):
        self.num_inputs = num_inputs
        self.num_slots = num_slots
        self.slots = [0] * num_slots

        # Cuatro sub-redes colapsantes
        self.read = NeuronaColapsanteV2(num_inputs)      # decide slot de lectura
        self.out = NeuronaColapsanteV2(num_inputs + 1)   # decide salida
        self.write = NeuronaColapsanteV2(num_inputs)     # decide slot de escritura
        self.val = NeuronaColapsanteV2(num_inputs)       # decide valor a escribir

    def reset(self):
        self.slots = [0] * self.num_slots

    def forward(self, entradas):
        # Leer slot: read devuelve -1,0,1 → mapear a índice 0..num_slots-1
        read_raw = self.read.forward(entradas)
        read_idx = (read_raw + 1) % self.num_slots
        valor_leido = self.slots[read_idx]

        # Computar salida
        salida = self.out.forward(entradas + [valor_leido])

        # Escribir: write da índice, val da valor
        write_raw = self.write.forward(entradas)
        write_idx = (write_raw + 1) % self.num_slots
        valor_escribir = self.val.forward(entradas)
        self.slots[write_idx] = copresence(self.slots[write_idx], valor_escribir)

        return salida

    def clone(self):
        n = NeuronaFragmentadaColapsante(self.num_inputs, self.num_slots)
        n.slots = self.slots.copy()
        n.read = self.read.clone()
        n.out = self.out.clone()
        n.write = self.write.clone()
        n.val = self.val.clone()
        return n

    def mutate(self, tasa=0.15):
        self.read.mutate(tasa)
        self.out.mutate(tasa)
        self.write.mutate(tasa)
        self.val.mutate(tasa)

# =============================================================================
# RED FRAGMENTADA COLAPSANTE
# =============================================================================

class RedFragmentadaColapsante:
    def __init__(self, hidden_size=3, num_slots=3, num_steps=3):
        self.hidden_size = hidden_size
        self.num_slots = num_slots
        self.num_steps = num_steps
        self.hidden = [NeuronaFragmentadaColapsante(2, num_slots) for _ in range(hidden_size)]
        self.output = NeuronaFragmentadaColapsante(hidden_size, num_slots)

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
        r = RedFragmentadaColapsante(self.hidden_size, self.num_slots, self.num_steps)
        r.hidden = [n.clone() for n in self.hidden]
        r.output = self.output.clone()
        return r

    def mutate(self, tasa=0.15):
        for n in self.hidden:
            n.mutate(tasa)
        self.output.mutate(tasa)

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
# FUNCIONES DE ENTRENAMIENTO (RECOCIDO SIMULADO)
# =============================================================================

def error_fragmentada_colapsante(red, dataset):
    errores = 0
    for x1, x2, esperado in dataset:
        red.reset()
        pred = red.forward(x1, x2)
        if pred != esperado:
            errores += 1
    return errores

def mutar_un_parametro(red):
    """Muta un parámetro aleatorio en cualquiera de las sub-redes."""
    todas = red.hidden + [red.output]
    neurona = random.choice(todas)
    # Elegir una sub-red al azar
    subred = random.choice(['read', 'out', 'write', 'val'])
    componente = getattr(neurona, subred)
    componente.mutate(tasa=1.0)  # muta un solo parámetro interno (peso/orden/op/umbral)
    return True

def corrida_recocido(dataset, semilla, epocas=200, intentos_por_epoca=200,
                     T0=0.8, decay=0.99, T_min=0.001):
    random.seed(semilla)
    red = RedFragmentadaColapsante(hidden_size=3, num_slots=3, num_steps=3)
    current = red.clone()
    current_error = error_fragmentada_colapsante(current, dataset)
    best = current.clone()
    best_error = current_error
    T = T0
    epoca_solucion = None

    for epoca in range(epocas):
        for _ in range(intentos_por_epoca):
            candidato = current.clone()
            mutar_un_parametro(candidato)
            error_candidato = error_fragmentada_colapsante(candidato, dataset)
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
        if best_error == 0:
            break
    return best, best_error, epoca_solucion

def corrida_con_reinicios(dataset, semilla_base=5000, n_restarts=3,
                          epocas_por_restart=150, intentos_por_epoca=200):
    mejor_red = None
    mejor_error = 9
    for r in range(n_restarts):
        semilla = semilla_base * 10 + r
        red_best, error, _ = corrida_recocido(dataset, semilla,
                                              epocas=epocas_por_restart,
                                              intentos_por_epoca=intentos_por_epoca)
        if error < mejor_error:
            mejor_error = error
            mejor_red = red_best.clone()
        if mejor_error == 0:
            break
    return mejor_red, mejor_error

# =============================================================================
# EVALUACIÓN EN LOS 3 DATASETS
# =============================================================================

def main():
    print("=" * 70)
    print("FASE D: FRAGMENTADA COLAPSANTE (MEZCLA)")
    print("=" * 70)

    for nombre, dataset in [("Sentimiento", DATASET_SENTIMIENTO),
                            ("XOR", DATASET_XOR),
                            ("Mayoría", DATASET_MAYORIA)]:
        print(f"\n--- {nombre} ---")
        t0 = time.time()
        red, error = corrida_con_reinicios(dataset, semilla_base=7000, n_restarts=3,
                                           epocas_por_restart=150, intentos_por_epoca=200)
        t1 = time.time()
        acc = 1 - error/9
        print(f"  Error final: {error}/9")
        print(f"  Accuracy: {acc:.4f} ({acc*9:.0f}/9)")
        print(f"  Tiempo: {t1-t0:.1f}s")

        # Verificación detallada
        if acc == 1.0:
            print("  Verificación (10x):")
            estable = True
            for x1, x2, esp in dataset:
                preds = [red.forward(x1, x2) for _ in range(10)]
                if len(set(preds)) != 1:
                    estable = False
                    break
            print(f"    {'ESTABLE' if estable else 'INESTABLE'}")

if __name__ == "__main__":
    main()
