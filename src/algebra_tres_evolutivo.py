"""
=============================================================================
EL ALGEBRA DEL TRES - REDES NEURONALES EVOLUTIVAS
Version completa y autonoma. Copia, pega, ejecuta.
=============================================================================
"""

import random
from typing import List, Tuple, Optional

# =============================================================================
# PARTE 1: MOTOR ALGEBRAICO DEL TRES
# =============================================================================

P = [-1, 0, 1]  # Conjunto base: negacion, neutralidad, afirmacion

def interaction(a: int, b: int) -> int:
    """Operacion ⊗ (interaccion / producto) del Tres."""
    if a == 0 or b == 0:
        return 0
    return a * b

def copresence(a: int, b: int) -> int:
    """Operacion ⊕ (co-presencia / sintesis dialectica) del Tres."""
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a
    return 0

def up(x: int) -> int:
    """Operacion ↑ (actualizacion forzada): 0→1, resto sin cambio."""
    return 1 if x == 0 else x

def down(x: int) -> int:
    """Operacion ↓ (exclusion forzada): 0→-1, resto sin cambio."""
    return -1 if x == 0 else x

def apply_op(x: int, op: Optional[str]) -> int:
    """Aplica operacion opcional a un valor ternario."""
    if op == 'up':
        return up(x)
    if op == 'down':
        return down(x)
    return x

# =============================================================================
# PARTE 2: DATASETS
# =============================================================================

DATASET_SENTIMIENTO = [
    (-1, -1, 1),   # doble negacion → positivo
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
# PARTE 3: NEURONA DEL TRES (BASE)
# =============================================================================

class NeuronaDelTres:
    """
    Neurona funcional pura del Tres. Sin memoria interna.
    Formula: op( ⊕_{i en orden} (w_i ⊗ x_i) )
    """
    def __init__(self, num_inputs: int):
        self.num_inputs = num_inputs
        self.pesos = [random.choice(P) for _ in range(num_inputs)]
        self.orden = list(range(num_inputs))
        random.shuffle(self.orden)
        self.op = random.choice([None, 'up', 'down'])
    
    def forward(self, entradas: List[int]) -> int:
        assert len(entradas) == self.num_inputs
        idx0 = self.orden[0]
        resultado = interaction(self.pesos[idx0], entradas[idx0])
        for k in range(1, self.num_inputs):
            idx = self.orden[k]
            term = interaction(self.pesos[idx], entradas[idx])
            resultado = copresence(resultado, term)
        return apply_op(resultado, self.op)
    
    def clone(self) -> 'NeuronaDelTres':
        n = NeuronaDelTres(self.num_inputs)
        n.pesos = self.pesos.copy()
        n.orden = self.orden.copy()
        n.op = self.op
        return n
    
    def mutate(self, tasa: float = 0.15):
        for i in range(self.num_inputs):
            if random.random() < tasa:
                self.pesos[i] = random.choice(P)
        if random.random() < tasa and self.num_inputs >= 2:
            i, j = random.sample(range(self.num_inputs), 2)
            self.orden[i], self.orden[j] = self.orden[j], self.orden[i]
        if random.random() < tasa:
            self.op = random.choice([None, 'up', 'down'])

# =============================================================================
# PARTE 4: RED FEEDFORWARD DEL TRES
# =============================================================================

class RedFeedforwardDelTres:
    """Red feedforward simple: 2 entradas → N ocultas → 1 salida."""
    def __init__(self, hidden_size: int = 2):
        self.hidden_size = hidden_size
        self.hidden = [NeuronaDelTres(2) for _ in range(hidden_size)]
        self.output = NeuronaDelTres(hidden_size)
    
    def forward(self, x1: int, x2: int) -> int:
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
# PARTE 5: NEURONA FRAGMENTADA (CON MEMORIA MULTI-SLOT)
# =============================================================================

class NeuronaFragmentada:
    """
    Neurona del Tres con memoria fragmentada en multiples slots.
    Cada neurona decide: de que slot leer, en que slot escribir, que escribir.
    """
    def __init__(self, num_inputs: int, num_slots: int = 3):
        self.num_inputs = num_inputs
        self.num_slots = num_slots
        self.slots = [0] * num_slots
        
        # Pesos para computar salida (entradas + slot leido)
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
    
    def mutate(self, tasa=0.15):
        for lst in [self.pesos_out, self.pesos_read, self.pesos_write, self.pesos_val]:
            for i in range(len(lst)):
                if random.random() < tasa:
                    lst[i] = random.choice(P)
        for orden in [self.orden_out, self.orden_read, self.orden_write, self.orden_val]:
            if random.random() < tasa and len(orden) >= 2:
                i, j = random.sample(range(len(orden)), 2)
                orden[i], orden[j] = orden[j], orden[i]
        for op_attr in ['op_out', 'op_read', 'op_write', 'op_val']:
            if random.random() < tasa:
                setattr(self, op_attr, random.choice([None, 'up', 'down']))

# =============================================================================
# PARTE 6: RED CON NEURONAS FRAGMENTADAS
# =============================================================================

class RedFragmentada:
    """Red donde cada neurona tiene memoria fragmentada en multiples slots."""
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
    
    def evaluate(self, dataset):
        aciertos = 0
        for x1, x2, esp in dataset:
            self.reset()
            if self.forward(x1, x2) == esp:
                aciertos += 1
        return aciertos / len(dataset)
    
    def clone(self):
        r = RedFragmentada(self.hidden_size, self.num_slots, self.num_steps)
        r.hidden = [n.clone() for n in self.hidden]
        r.output = self.output.clone()
        return r
    
    def mutate(self, tasa=0.15):
        for n in self.hidden:
            n.mutate(tasa)
        self.output.mutate(tasa)

# =============================================================================
# PARTE 7: ALGORITMO EVOLUTIVO GENERICO
# =============================================================================

class EvolucionGenerica:
    """Algoritmo evolutivo que funciona con cualquier arquitectura que tenga:
    evaluate(), clone(), mutate()"""
    
    def __init__(self, factory, dataset, poblacion_size=300, generaciones=400,
                 tasa_mutacion=0.14, elitismo=5, nombre="Red"):
        self.factory = factory
        self.dataset = dataset
        self.poblacion_size = poblacion_size
        self.generaciones = generaciones
        self.tasa_mutacion = tasa_mutacion
        self.elitismo = elitismo
        self.nombre = nombre
        self.poblacion = []
        self.mejor_historico = None
        self.mejor_fitness = 0.0
        self.historia_mejor = []
        self.historia_avg = []
        self.generacion_mejor = 0
    
    def inicializar(self):
        self.poblacion = [self.factory() for _ in range(self.poblacion_size)]
    
    def evaluar_poblacion(self):
        return [(red.evaluate(self.dataset), red) for red in self.poblacion]
    
    def seleccionar_torneo(self, evaluados, k=3):
        torneo = random.sample(evaluados, k)
        torneo.sort(key=lambda x: x[0], reverse=True)
        return torneo[0][1]
    
    def cruzar(self, p1, p2):
        hijo = self.factory()
        if hasattr(p1, 'hidden') and hasattr(p2, 'hidden'):
            for i in range(len(p1.hidden)):
                hijo.hidden[i] = p1.hidden[i].clone() if random.random() < 0.5 else p2.hidden[i].clone()
        if hasattr(p1, 'output') and hasattr(p2, 'output'):
            hijo.output = p1.output.clone() if random.random() < 0.5 else p2.output.clone()
        return hijo
    
    def evolucionar(self):
        self.inicializar()
        for gen in range(self.generaciones):
            evaluados = self.evaluar_poblacion()
            evaluados.sort(key=lambda x: x[0], reverse=True)
            
            mejor_f = evaluados[0][0]
            mejor_red = evaluados[0][1]
            avg_f = sum(f for f, _ in evaluados) / len(evaluados)
            
            if mejor_f > self.mejor_fitness:
                self.mejor_fitness = mejor_f
                self.mejor_historico = evaluados[0][1].clone()
                self.generacion_mejor = gen
            
            self.historia_mejor.append(mejor_f)
            self.historia_avg.append(avg_f)
            
            if gen % 25 == 0 or gen == self.generaciones - 1 or mejor_f >= 1.0:
                print(f"[{self.nombre}] Gen {gen:3d} | Mejor: {mejor_f:.4f} ({mejor_f*9:.0f}/9) | "
                      f"Prom: {avg_f:.4f} | Hist: {self.mejor_fitness:.4f}")
            
            if mejor_f >= 1.0:
                print(f"\n🎯 [{self.nombre}] ¡SOLUCION PERFECTA en gen {gen}!")
                break
            
            nueva = [evaluados[i][1].clone() for i in range(self.elitismo)]
            while len(nueva) < self.poblacion_size:
                p1 = self.seleccionar_torneo(evaluados, k=3)
                p2 = self.seleccionar_torneo(evaluados, k=3)
                hijo = self.cruzar(p1, p2)
                hijo.mutate(self.tasa_mutacion)
                nueva.append(hijo)
            
            self.poblacion = nueva
        
        return self.mejor_historico

# =============================================================================
# PARTE 8: EJECUCION PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("EL ALGEBRA DEL TRES - REDES NEURONALES EVOLUTIVAS")
    print("=" * 70)
    
    # --- Experimento 1: Feedforward en Sentimiento ---
    print("\n[1] Feedforward 2->2->1 en Sentimiento")
    random.seed(42)
    ff_factory = lambda: RedFeedforwardDelTres(hidden_size=2)
    ev_ff = EvolucionGenerica(ff_factory, DATASET_SENTIMIENTO, 300, 400, 0.14, 5, "FF")
    mejor_ff = ev_ff.evolucionar()
    print(f"Resultado: {ev_ff.mejor_fitness:.4f} ({ev_ff.mejor_fitness*9:.0f}/9)")
    
    # --- Experimento 2: Neuronas Fragmentadas en Sentimiento ---
    print("\n[2] Neuronas Fragmentadas en Sentimiento")
    random.seed(42)
    frag_factory = lambda: RedFragmentada(hidden_size=3, num_slots=3, num_steps=3)
    ev_frag = EvolucionGenerica(frag_factory, DATASET_SENTIMIENTO, 300, 400, 0.14, 5, "Frag")
    mejor_frag = ev_frag.evolucionar()
    print(f"Resultado: {ev_frag.mejor_fitness:.4f} ({ev_frag.mejor_fitness*9:.0f}/9)")
    
    # --- Verificacion detallada ---
    print("\n[3] Verificacion detallada Neuronas Fragmentadas:")
    for x1, x2, esp in DATASET_SENTIMIENTO:
        mejor_frag.reset()
        pred = mejor_frag.forward(x1, x2)
        ok = "OK" if pred == esp else "FAIL"
        print(f"  ({x1:2d}, {x2:2d}) -> pred={pred:2d}, esp={esp:2d} [{ok}]")
    
    # --- Experimento 3: Neuronas Fragmentadas en XOR ---
    print("\n[4] Neuronas Fragmentadas en XOR")
    random.seed(123)
    frag_factory2 = lambda: RedFragmentada(hidden_size=3, num_slots=3, num_steps=3)
    ev_frag2 = EvolucionGenerica(frag_factory2, DATASET_XOR, 300, 400, 0.14, 5, "Frag-XOR")
    mejor_frag2 = ev_frag2.evolucionar()
    print(f"Resultado: {ev_frag2.mejor_fitness:.4f} ({ev_frag2.mejor_fitness*9:.0f}/9)")
    
    # --- Experimento 4: Neuronas Fragmentadas en Mayoria ---
    print("\n[5] Neuronas Fragmentadas en Mayoria")
    random.seed(456)
    frag_factory3 = lambda: RedFragmentada(hidden_size=3, num_slots=3, num_steps=3)
    ev_frag3 = EvolucionGenerica(frag_factory3, DATASET_MAYORIA, 300, 400, 0.14, 5, "Frag-May")
    mejor_frag3 = ev_frag3.evolucionar()
    print(f"Resultado: {ev_frag3.mejor_fitness:.4f} ({ev_frag3.mejor_fitness*9:.0f}/9)")
    
    print("\n" + "=" * 70)
    print("RESUMEN FINAL")
    print("=" * 70)
    print(f"Feedforward Sentimiento:  {ev_ff.mejor_fitness*100:5.1f}%")
    print(f"Fragmentada Sentimiento:  {ev_frag.mejor_fitness*100:5.1f}%")
    print(f"Fragmentada XOR:          {ev_frag2.mejor_fitness*100:5.1f}%")
    print(f"Fragmentada Mayoria:      {ev_frag3.mejor_fitness*100:5.1f}%")
    print("=" * 70)
