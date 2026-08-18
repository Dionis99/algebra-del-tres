"""
T3-FC: Neurona FragmentadaColapsante (hibridación memoria + colapso).
Combina slots de memoria con colapso contextual de pesos en 0.
"""
import sys, os
import random
from typing import List, Dict, Any

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algebra.operators import interaction, copresence, apply_op, P_VALS
from neurons.base import TritNeuron
from neurons.collapsing import NeuronaColapsanteV2

class NeuronaFragmentadaColapsante(TritNeuron):
    """
    Neurona FragmentadaColapsante (T3-FC).
    
    Cada neurona tiene:
    - slots: memoria persistente
    - read: neurona Colapsante que decide qué slot leer
    - out: neurona Colapsante que computa salida
    - write: neurona Colapsante que decide dónde escribir
    - val: neurona Colapsante que decide qué valor escribir
    
    Los 4 sub-cerebros son Colapsantes V2, así que sus pesos en 0
    colapsan contextualmente según la presión del entorno.
    """
    
    def __init__(self, num_inputs: int, num_slots: int = 3):
        self.num_inputs = num_inputs
        self.num_slots = num_slots
        self.slots = [0] * num_slots
        
        # Cada sub-red es una Colapsante V2
        self.read = NeuronaColapsanteV2(num_inputs)
        self.out = NeuronaColapsanteV2(num_inputs + 1)
        self.write = NeuronaColapsanteV2(num_inputs)
        self.val = NeuronaColapsanteV2(num_inputs)
    
    def forward(self, entradas: List[int]) -> int:
        # Leer: el slot emerge de superposición contextual
        read_idx = (self.read.forward(entradas) + 1) % self.num_slots
        valor_leido = self.slots[read_idx]
        
        # Computar: pesos en 0 colapsan según presión de entradas + memoria
        salida = self.out.forward(entradas + [valor_leido])
        
        # Escribir: dónde depositar el recuerdo emerge contextualmente
        write_idx = (self.write.forward(entradas) + 1) % self.num_slots
        valor_escribir = self.val.forward(entradas)
        self.slots[write_idx] = copresence(self.slots[write_idx], valor_escribir)
        
        return salida
    
    def clone(self) -> 'NeuronaFragmentadaColapsante':
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
    
    def reset(self):
        self.slots = [0] * self.num_slots
    
    def get_params(self) -> Dict[str, Any]:
        return {
            "num_inputs": self.num_inputs,
            "num_slots": self.num_slots,
            "slots": self.slots.copy(),
            "read": self.read.get_params(),
            "out": self.out.get_params(),
            "write": self.write.get_params(),
            "val": self.val.get_params(),
        }
    
    def set_params(self, params: Dict[str, Any]):
        self.num_inputs = params["num_inputs"]
        self.num_slots = params["num_slots"]
        self.slots = params["slots"].copy()
        self.read.set_params(params["read"])
        self.out.set_params(params["out"])
        self.write.set_params(params["write"])
        self.val.set_params(params["val"])

if __name__ == "__main__":
    print("=== Test NeuronaFragmentadaColapsante (T3-FC) ===")
    n = NeuronaFragmentadaColapsante(2, 3)
    print(f"Slots: {n.slots}")
    print(f"Read umbral: {n.read.umbral_colapso:.3f}")
    print(f"Out umbral: {n.out.umbral_colapso:.3f}")
    
    print("\nEvaluación secuencial (memoria + colapso):")
    for entradas in [[1, 1], [-1, -1], [1, -1]]:
        salida = n.forward(entradas)
        print(f"  {entradas} → {salida:+d} (slots={n.slots})")
