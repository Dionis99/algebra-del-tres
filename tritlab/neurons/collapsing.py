"""
T3-G: Neurona Colapsante V2.
Pesos en 0 colapsan contextualmente según presión del entorno.
El umbral de colapso es el "saber" aprendido de la neurona.
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

class NeuronaColapsanteV2(TritNeuron):
    """
    Neurona Colapsante V2 (T3-G).
    
    Innovación clave: los pesos en 0 no son estáticos, sino que colapsan
    contextualmente según la presión del entorno.
    
    Fórmula:
    - presion = promedio(entradas)
    - Si peso != 0: usar peso normalmente
    - Si peso == 0: colapsar a 1 si presion > umbral, sino -1
    
    El umbral de colapso es el "saber" aprendido: determina cuándo la
    potencialidad (0) se actualiza como afirmación (1) o negación (-1).
    """
    
    def __init__(self, num_inputs: int):
        self.num_inputs = num_inputs
        self.pesos = [random.choice(P_VALS) for _ in range(num_inputs)]
        self.orden = list(range(num_inputs))
        random.shuffle(self.orden)
        self.op = random.choice([None, 'up', 'down'])
        self.umbral_colapso = random.uniform(-0.9, 0.9)
    
    def _colapsar(self, peso: int, presion: float) -> int:
        """Colapsa un peso según la presión del contexto."""
        if peso != 0:
            return peso
        return 1 if presion > self.umbral_colapso else -1
    
    def forward(self, entradas: List[int]) -> int:
        assert len(entradas) == self.num_inputs
        
        # Calcular presión del contexto (promedio de entradas)
        presion = sum(entradas) / max(len(entradas), 1)
        
        # Colapsar pesos en 0 según presión
        pesos_colapsados = [self._colapsar(w, presion) for w in self.pesos]
        
        # Aplicar ⊗ y ⊕ con orden aprendido
        idx0 = self.orden[0]
        resultado = interaction(pesos_colapsados[idx0], entradas[idx0])
        
        for k in range(1, self.num_inputs):
            idx = self.orden[k]
            term = interaction(pesos_colapsados[idx], entradas[idx])
            resultado = copresence(resultado, term)
        
        return apply_op(resultado, self.op)
    
    def clone(self) -> 'NeuronaColapsanteV2':
        n = NeuronaColapsanteV2(self.num_inputs)
        n.pesos = self.pesos.copy()
        n.orden = self.orden.copy()
        n.op = self.op
        n.umbral_colapso = self.umbral_colapso
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
        
        # Mutar umbral de colapso (el "saber")
        if random.random() < tasa:
            self.umbral_colapso += random.uniform(-0.3, 0.3)
            self.umbral_colapso = max(-1.0, min(1.0, self.umbral_colapso))
    
    def reset(self):
        pass  # Colapsante V2 no tiene estado interno
    
    def get_params(self) -> Dict[str, Any]:
        return {
            "num_inputs": self.num_inputs,
            "pesos": self.pesos.copy(),
            "orden": self.orden.copy(),
            "op": self.op,
            "umbral_colapso": self.umbral_colapso,
        }
    
    def set_params(self, params: Dict[str, Any]):
        self.num_inputs = params["num_inputs"]
        self.pesos = params["pesos"].copy()
        self.orden = params["orden"].copy()
        self.op = params["op"]
        self.umbral_colapso = params["umbral_colapso"]

# Test básico
if __name__ == "__main__":
    print("=== Test NeuronaColapsanteV2 (T3-G) ===")
    n = NeuronaColapsanteV2(2)
    print(f"Pesos: {n.pesos}")
    print(f"Orden: {n.orden}")
    print(f"Op: {n.op}")
    print(f"Umbral de colapso: {n.umbral_colapso:.3f}")
    
    print("\nEvaluación en todas las entradas:")
    for x1 in [-1, 0, 1]:
        for x2 in [-1, 0, 1]:
            salida = n.forward([x1, x2])
            print(f"  [{x1:+d}, {x2:+d}] → {salida:+d}")
    
    # Test de determinismo
    print("\nTest de determinismo (misma entrada, 5 evaluaciones):")
    for _ in range(5):
        salida = n.forward([1, -1])
        print(f"  [1, -1] → {salida:+d}", end="  ")
    print()
