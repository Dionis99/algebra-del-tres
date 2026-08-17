"""
Red de Colapsantes V2 (2→3→1).
Capa oculta: 3 neuronas Colapsantes V2.
Capa de salida: 1 neurona Colapsante V2.
"""
import sys, os
import random
from typing import List, Dict, Any

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from neurons.collapsing import NeuronaColapsanteV2

class RedColapsanteV2:
    """
    Red feedforward de Colapsantes V2.
    Arquitectura: 2 entradas → 3 ocultas → 1 salida.
    """
    
    def __init__(self, hidden_size: int = 3):
        self.hidden_size = hidden_size
        self.hidden = [NeuronaColapsanteV2(2) for _ in range(hidden_size)]
        self.output = NeuronaColapsanteV2(hidden_size)
    
    def forward(self, x1: int, x2: int) -> int:
        hidden_outs = [n.forward([x1, x2]) for n in self.hidden]
        return self.output.forward(hidden_outs)
    
    def evaluate(self, dataset) -> float:
        aciertos = sum(1 for entradas, esperado in dataset 
                      if self.forward(*entradas) == esperado)
        return aciertos / len(dataset)
    
    def clone(self) -> 'RedColapsanteV2':
        r = RedColapsanteV2(self.hidden_size)
        r.hidden = [n.clone() for n in self.hidden]
        r.output = self.output.clone()
        return r
    
    def mutate(self, tasa: float = 0.15):
        for n in self.hidden:
            n.mutate(tasa)
        self.output.mutate(tasa)
    
    def reset(self):
        for n in self.hidden:
            n.reset()
        self.output.reset()
    
    def get_params(self) -> Dict[str, Any]:
        return {
            "hidden_size": self.hidden_size,
            "hidden": [n.get_params() for n in self.hidden],
            "output": self.output.get_params(),
        }
    
    def set_params(self, params: Dict[str, Any]):
        self.hidden_size = params["hidden_size"]
        for i, p in enumerate(params["hidden"]):
            self.hidden[i].set_params(p)
        self.output.set_params(params["output"])

# Test básico
if __name__ == "__main__":
    print("=== Test RedColapsanteV2 ===")
    red = RedColapsanteV2(3)
    print(f"Arquitectura: 2 → {red.hidden_size} → 1")
    
    print("\nEvaluación en algunas entradas:")
    for x1 in [-1, 0, 1]:
        for x2 in [-1, 0, 1]:
            salida = red.forward(x1, x2)
            print(f"  [{x1:+d}, {x2:+d}] → {salida:+d}")
