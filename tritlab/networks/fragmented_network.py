"""
Red de Fragmentadas (2→3→1).
"""
import sys, os
import random
from typing import List, Dict, Any

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from neurons.fragmented import NeuronaFragmentada

class RedFragmentada:
    def __init__(self, hidden_size: int = 3, num_slots: int = 3, num_steps: int = 3):
        self.hidden_size = hidden_size
        self.num_slots = num_slots
        self.num_steps = num_steps
        self.hidden = [NeuronaFragmentada(2, num_slots) for _ in range(hidden_size)]
        self.output = NeuronaFragmentada(hidden_size, num_slots)
    
    def forward(self, x1: int, x2: int) -> int:
        for _ in range(self.num_steps):
            hidden_outs = [n.forward([x1, x2]) for n in self.hidden]
            salida = self.output.forward(hidden_outs)
        return salida
    
    def evaluate(self, dataset) -> float:
        aciertos = 0
        for entradas, esperado in dataset:
            self.reset()
            if self.forward(*entradas) == esperado:
                aciertos += 1
        return aciertos / len(dataset)
    
    def clone(self) -> 'RedFragmentada':
        r = RedFragmentada(self.hidden_size, self.num_slots, self.num_steps)
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
