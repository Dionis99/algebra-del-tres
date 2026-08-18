"""
T3-F: Neurona Fragmentada con memoria multi-slot.
Cada neurona tiene slots de memoria y decide qué leer/escribir contextualmente.
"""
import sys, os
import random
from typing import List, Dict, Any

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algebra.operators import interaction, copresence, apply_op, P_VALS
from neurons.base import TritNeuron

class NeuronaFragmentada(TritNeuron):
    """
    Neurona Fragmentada (T3-F) con memoria multi-slot.
    
    Cada neurona tiene:
    - slots: memoria persistente [0, 0, 0]
    - pesos_read: decide qué slot leer
    - pesos_out: computa salida con entradas + slot leído
    - pesos_write: decide dónde escribir
    - pesos_val: decide qué valor escribir
    """
    
    def __init__(self, num_inputs: int, num_slots: int = 3):
        self.num_inputs = num_inputs
        self.num_slots = num_slots
        self.slots = [0] * num_slots
        
        # Pesos para computar salida (entradas + slot leído)
        self.pesos_out = [random.choice(P_VALS) for _ in range(num_inputs + 1)]
        self.orden_out = list(range(num_inputs + 1))
        random.shuffle(self.orden_out)
        self.op_out = random.choice([None, 'up', 'down'])
        
        # Pesos para decidir slot de lectura
        self.pesos_read = [random.choice(P_VALS) for _ in range(num_inputs)]
        self.orden_read = list(range(num_inputs))
        random.shuffle(self.orden_read)
        self.op_read = random.choice([None, 'up', 'down'])
        
        # Pesos para decidir slot de escritura
        self.pesos_write = [random.choice(P_VALS) for _ in range(num_inputs)]
        self.orden_write = list(range(num_inputs))
        random.shuffle(self.orden_write)
        self.op_write = random.choice([None, 'up', 'down'])
        
        # Pesos para decidir valor a escribir
        self.pesos_val = [random.choice(P_VALS) for _ in range(num_inputs)]
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
    
    def forward(self, entradas: List[int]) -> int:
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
    
    def clone(self) -> 'NeuronaFragmentada':
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
    
    def mutate(self, tasa: float = 0.15):
        for lst in [self.pesos_out, self.pesos_read, self.pesos_write, self.pesos_val]:
            for i in range(len(lst)):
                if random.random() < tasa:
                    lst[i] = random.choice(P_VALS)
        for orden in [self.orden_out, self.orden_read, self.orden_write, self.orden_val]:
            if random.random() < tasa and len(orden) >= 2:
                i, j = random.sample(range(len(orden)), 2)
                orden[i], orden[j] = orden[j], orden[i]
        for op_attr in ['op_out', 'op_read', 'op_write', 'op_val']:
            if random.random() < tasa:
                setattr(self, op_attr, random.choice([None, 'up', 'down']))
    
    def reset(self):
        self.slots = [0] * self.num_slots
    
    def get_params(self) -> Dict[str, Any]:
        return {
            "num_inputs": self.num_inputs,
            "num_slots": self.num_slots,
            "slots": self.slots.copy(),
            "pesos_out": self.pesos_out.copy(),
            "orden_out": self.orden_out.copy(),
            "op_out": self.op_out,
            "pesos_read": self.pesos_read.copy(),
            "orden_read": self.orden_read.copy(),
            "op_read": self.op_read,
            "pesos_write": self.pesos_write.copy(),
            "orden_write": self.orden_write.copy(),
            "op_write": self.op_write,
            "pesos_val": self.pesos_val.copy(),
            "orden_val": self.orden_val.copy(),
            "op_val": self.op_val,
        }
    
    def set_params(self, params: Dict[str, Any]):
        self.num_inputs = params["num_inputs"]
        self.num_slots = params["num_slots"]
        self.slots = params["slots"].copy()
        self.pesos_out = params["pesos_out"].copy()
        self.orden_out = params["orden_out"].copy()
        self.op_out = params["op_out"]
        self.pesos_read = params["pesos_read"].copy()
        self.orden_read = params["orden_read"].copy()
        self.op_read = params["op_read"]
        self.pesos_write = params["pesos_write"].copy()
        self.orden_write = params["orden_write"].copy()
        self.op_write = params["op_write"]
        self.pesos_val = params["pesos_val"].copy()
        self.orden_val = params["orden_val"].copy()
        self.op_val = params["op_val"]

if __name__ == "__main__":
    print("=== Test NeuronaFragmentada (T3-F) ===")
    n = NeuronaFragmentada(2, 3)
    print(f"Slots: {n.slots}")
    print(f"Pesos_out: {n.pesos_out}")
    
    print("\nEvaluación secuencial (memoria persiste):")
    for entradas in [[1, 1], [-1, -1], [1, -1]]:
        salida = n.forward(entradas)
        print(f"  {entradas} → {salida:+d} (slots={n.slots})")
