"""
Interfaz común para todas las neuronas del TritNeuronZoo.
Todas las neuronas deben implementar estos métodos para ser intercambiables.
"""
from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class TritNeuron(ABC):
    """
    Interfaz base para neuronas ternarias.
    
    Métodos obligatorios:
    - forward(entradas): computa salida dado vector de entradas
    - clone(): crea copia independiente
    - mutate(tasa): aplica mutación aleatoria
    - reset(): reinicia estado interno (memoria, slots)
    - get_params(): devuelve parámetros como dict
    - set_params(params): carga parámetros desde dict
    """
    
    @abstractmethod
    def forward(self, entradas: List[int]) -> int:
        """Computa salida dado vector de entradas ternarias."""
        pass
    
    @abstractmethod
    def clone(self) -> 'TritNeuron':
        """Crea copia independiente de la neurona."""
        pass
    
    @abstractmethod
    def mutate(self, tasa: float = 0.15):
        """Aplica mutación aleatoria con probabilidad tasa."""
        pass
    
    @abstractmethod
    def reset(self):
        """Reinicia estado interno (memoria, slots, etc.)."""
        pass
    
    @abstractmethod
    def get_params(self) -> Dict[str, Any]:
        """Devuelve parámetros como diccionario."""
        pass
    
    @abstractmethod
    def set_params(self, params: Dict[str, Any]):
        """Carga parámetros desde diccionario."""
        pass
    
    def diagnostics(self) -> Dict[str, Any]:
        """Devuelve métricas de diagnóstico (opcional)."""
        return {
            "tipo": self.__class__.__name__,
            "num_inputs": getattr(self, "num_inputs", 0),
        }
