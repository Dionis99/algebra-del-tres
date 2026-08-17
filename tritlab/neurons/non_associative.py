"""
T3-NA: NeuronaDelTres No Asociativa con árbol de parentización.
"""
import random
from typing import List, Dict, Any, Tuple

try:
    from ..algebra.operators import interaction, copresence, apply_op, P_VALS
    from .base import TritNeuron
except ImportError:
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from algebra.operators import interaction, copresence, apply_op, P_VALS
    from neurons.base import TritNeuron

def build_random_tree(n: int) -> List[Tuple[int, int]]:
    if n == 1:
        return []
    active = list(range(n))
    tree = []
    next_node = n
    while len(active) > 1:
        i, j = random.sample(range(len(active)), 2)
        left, right = active[i], active[j]
        tree.append((left, right))
        active = [x for k, x in enumerate(active) if k not in [i, j]]
        active.append(next_node)
        next_node += 1
    return tree

class NeuronaTresNoAsociativa(TritNeuron):
    def __init__(self, num_inputs: int):
        self.num_inputs = num_inputs
        self.pesos = [random.choice(P_VALS) for _ in range(num_inputs)]
        self.tree = build_random_tree(num_inputs)
        self.op = random.choice([None, 'up', 'down'])
    
    def forward(self, entradas: List[int]) -> int:
        assert len(entradas) == self.num_inputs
        valores = [interaction(self.pesos[i], entradas[i]) for i in range(self.num_inputs)]
        if not self.tree:
            resultado = valores[0]
        else:
            for left_idx, right_idx in self.tree:
                valores.append(copresence(valores[left_idx], valores[right_idx]))
            resultado = valores[-1]
        return apply_op(resultado, self.op)
    
    def clone(self) -> 'NeuronaTresNoAsociativa':
        n = NeuronaTresNoAsociativa(self.num_inputs)
        n.pesos = self.pesos.copy()
        n.tree = self.tree.copy()
        n.op = self.op
        return n
    
    def mutate(self, tasa: float = 0.15):
        for i in range(self.num_inputs):
            if random.random() < tasa:
                self.pesos[i] = random.choice(P_VALS)
        if random.random() < tasa:
            self.tree = build_random_tree(self.num_inputs)
        if random.random() < tasa:
            self.op = random.choice([None, 'up', 'down'])
    
    def reset(self):
        pass
    
    def get_params(self) -> Dict[str, Any]:
        return {"num_inputs": self.num_inputs, "pesos": self.pesos.copy(),
                "tree": self.tree.copy(), "op": self.op}
    
    def set_params(self, params: Dict[str, Any]):
        self.num_inputs = params["num_inputs"]
        self.pesos = params["pesos"].copy()
        self.tree = params["tree"].copy()
        self.op = params["op"]

if __name__ == "__main__":
    print("=== Test NeuronaTresNoAsociativa (T3-NA) ===")
    n = NeuronaTresNoAsociativa(3)
    print(f"Pesos: {n.pesos}, Árbol: {n.tree}, Op: {n.op}")
    for entradas in [[-1,-1,-1], [-1,0,1], [1,1,1], [0,0,0]]:
        print(f"  {entradas} → {n.forward(entradas):+d}")
