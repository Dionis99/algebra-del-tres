"""
T3: NeuronaDelTres básica.
Implementación de referencia: pesos ternarios, ⊕ secuencial con orden, op final.
"""
import random
from typing import List, Dict, Any

# Imports robustos: funcionan como script, como módulo, o desde cualquier ubicación
try:
    from ..algebra.operators import interaction, copresence, apply_op, P_VALS
    from .base import TritNeuron
except ImportError:
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from algebra.operators import interaction, copresence, apply_op, P_VALS
    from neurons.base import TritNeuron

class NeuronaTres(TritNeuron):
    def __init__(self, num_inputs: int):
        self.num_inputs = num_inputs
        self.pesos = [random.choice(P_VALS) for _ in range(num_inputs)]
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
    
    def clone(self) -> 'NeuronaTres':
        n = NeuronaTres(self.num_inputs)
        n.pesos = self.pesos.copy()
        n.orden = self.orden.copy()
        n.op = self.op
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
        pass
    
    def get_params(self) -> Dict[str, Any]:
        return {"num_inputs": self.num_inputs, "pesos": self.pesos.copy(), 
                "orden": self.orden.copy(), "op": self.op}
    
    def set_params(self, params: Dict[str, Any]):
        self.num_inputs = params["num_inputs"]
        self.pesos = params["pesos"].copy()
        self.orden = params["orden"].copy()
        self.op = params["op"]

if __name__ == "__main__":
    print("=== Test NeuronaTres (T3) ===")
    n = NeuronaTres(2)
    print(f"Pesos: {n.pesos}, Orden: {n.orden}, Op: {n.op}")
    print("\nEvaluación:")
    for x1 in [-1, 0, 1]:
        for x2 in [-1, 0, 1]:
            print(f"  [{x1:+d}, {x2:+d}] → {n.forward([x1, x2]):+d}")
