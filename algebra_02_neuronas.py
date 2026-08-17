"""
ALGEBRA DEL TRES - Parte 2: Neuronas colapsantes y fragmentadas
"""

from algebra_01_motor_datasets import *

class NeuronaColapsanteV2:
    """
    Neurona donde los pesos en 0 colapsan deterministamente
    segun la presion del contexto y un umbral aprendido.
    """
    def __init__(self, num_inputs: int):
        self.num_inputs = num_inputs
        self.pesos = [random.choice(P_VALS) for _ in range(num_inputs)]
        self.orden = list(range(num_inputs))
        random.shuffle(self.orden)
        self.op = random.choice([None, 'up', 'down'])
        self.umbral_colapso = random.uniform(-0.9, 0.9)

    def _colapsar(self, peso: int, presion: float) -> int:
        if peso != 0:
            return peso
        return 1 if presion > self.umbral_colapso else -1

    def forward(self, entradas: List[int]) -> int:
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

    def mutate(self, tasa: float = 0.15):
        for i in range(self.num_inputs):
            if random.random() < tasa:
                self.pesos[i] = int(random.choice(P_VALS))
        if random.random() < tasa and self.num_inputs >= 2:
            i, j = random.sample(range(self.num_inputs), 2)
            self.orden[i], self.orden[j] = self.orden[j], self.orden[i]
        if random.random() < tasa:
            self.op = random.choice([None, 'up', 'down'])
        if random.random() < tasa:
            self.umbral_colapso = random.uniform(-0.9, 0.9)


class NeuronaFragmentadaColapsante:
    """
    Neurona con memoria fragmentada donde los 4 sub-cerebros son colapsantes.
    """
    def __init__(self, num_inputs: int, num_slots: int = 3):
        self.num_inputs = num_inputs
        self.num_slots = num_slots
        self.slots = [0] * num_slots
        self.read = NeuronaColapsanteV2(num_inputs)
        self.out = NeuronaColapsanteV2(num_inputs + 1)
        self.write = NeuronaColapsanteV2(num_inputs)
        self.val = NeuronaColapsanteV2(num_inputs)

    def forward(self, entradas: List[int]) -> int:
        read_idx = (self.read.forward(entradas) + 1) % self.num_slots
        valor_leido = self.slots[read_idx]
        salida = self.out.forward(entradas + [valor_leido])
        write_idx = (self.write.forward(entradas) + 1) % self.num_slots
        valor_escribir = self.val.forward(entradas)
        self.slots[write_idx] = copresence(self.slots[write_idx], valor_escribir)
        return salida

    def reset(self):
        self.slots = [0] * self.num_slots

    def clone(self):
        n = NeuronaFragmentadaColapsante(self.num_inputs, self.num_slots)
        n.slots = self.slots.copy()
        n.read = self.read.clone()
        n.out = self.out.clone()
        n.write = self.write.clone()
        n.val = self.val.clone()
        return n

    def mutate(self, tasa: float = 0.15):
        self.read.mutate(tasa)
        self.out.mutate(tasa)
        self.write.mutate(tasa)
        self.val.mutate(tasa)
