import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from neurons.recurrent import NeuronaTresRecurrente

print("=== Test Mejorado NeuronaTresRecurrente (T3-R) ===")
n = NeuronaTresRecurrente(2)
n.pesos = [1, 1]
n.op = None
print(f"Pesos: {n.pesos}, Op: {n.op}, Memoria inicial: {n.memoria}")

print("\nEvaluación secuencial (memoria persiste):")
for i, entradas in enumerate([[1,1], [-1,-1], [1,-1], [0,0]]):
    salida = n.forward(entradas)
    print(f"  Paso {i}: {entradas} → {salida:+d} (memoria={n.memoria})")

print("\n=== Test de persistencia ===")
n2 = NeuronaTresRecurrente(1)
n2.pesos = [1]
for x in [[1], [1], [-1], [-1]]:
    print(f"  {x} → {n2.forward(x):+d} (memoria={n2.memoria})")
