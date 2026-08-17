"""
T3-R: NeuronaDelTres Recurrente con memoria temporal.
"""
import random
from typing import List, Dict, Any

try:
    from ..algebra.operators import interaction, copresence, apply_op, P_VALS
    from .base import TritNeuron
except ImportError:
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from algebra.operators import interaction, copresence, apply_op, P_VALS
    from neurons.base import TritNeuron

class NeuronaTresRecurrente(TritNeuron):
    def __init__(self, num_inputs: int):
        self.num_inputs = num_inputs
        self.pesos = [random.choice(P_VALS) for _ in range(num_inputs)]
        self.orden = list(range(num_inputs))
        random.shuffle(self.orden)
        self.op = random.choice([None, 'up', 'down'])
        self.memoria = 0
    
    def forward(self, entradas: List[int]) -> int:
        assert len(entradas) == self.num_inputs
        idx0 = self.orden[0]
        resultado = interaction(self.pesos[idx0], entradas[idx0])
        for k in range(1, self.num_inputs):
            idx = self.orden[k]
            term = interaction(self.pesos[idx], entradas[idx])
            resultado = copresence(resultado, term)
        resultado = copresence(resultado, self.memoria)
        resultado = apply_op(resultado, self.op)
        self.memoria = resultado
        return resultado
    
    def clone(self) -> 'NeuronaTresRecurrente':
        n = NeuronaTresRecurrente(self.num_inputs)
        n.pesos = self.pesos.copy()
        n.orden = self.orden.copy()
        n.op = self.op
        n.memoria = self.memoria
        return n
    
    def mutate(self, tasa: float = 0.15):
        for i in range(self.num_inputs):
            if random.random() < tasa:
                self.pesos[i] = random.choice(P_VALS)
        if random.random() < tasa and self.num_inputs >= 2:
            i, j = random.sample(range(self.num_inputs), 2)
            self.orden[i], self.orden[j] = self.orden[j], self.orden[i]
        if random.random() < tasa:
            self.op = random.choice([None, 'up', 'down'])
    
    def reset(self):
        self.memoria = 0
    
    def get_params(self) -> Dict[str, Any]:
        return {"num_inputs": self.num_inputs, "pesos": self.pesos.copy(),
                "orden": self.orden.copy(), "op": self.op}
    
    def set_params(self, params: Dict[str, Any]):
        self.num_inputs = params["num_inputs"]
        self.pesos = params["pesos"].copy()
        self.orden = params["orden"].copy()
        self.op = params["op"]

if __name__ == "__main__":
    print("=== Test NeuronaTresRecurrente (T3-R) ===")
    n = NeuronaTresRecurrente(2)
    n.pesos = [1, 1]  # Forzar pesos no-cero para test más informativo
    print(f"Pesos: {n.pesos}, Op: {n.op}, Memoria: {n.memoria}")
    for entradas in [[1,1], [-1,-1], [1,-1], [0,0]]:
        print(f"  {entradas} → {n.forward(entradas):+d} (memoria={n.memoria})")
