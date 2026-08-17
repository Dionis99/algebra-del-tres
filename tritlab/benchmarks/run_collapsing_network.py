"""
Benchmark de RedColapsanteV2 en los 3 datasets básicos.
"""
import sys, os
import random
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from networks.collapsing_network import RedColapsanteV2
from datasets.basic import get_dataset, list_datasets

def evolucionar_red(dataset, poblacion_size=300, generaciones=400, 
                    tasa_mutacion=0.14, elitismo=10):
    poblacion = [RedColapsanteV2(3) for _ in range(poblacion_size)]
    mejor_fitness = 0.0
    mejor_red = None
    
    for gen in range(generaciones):
        evaluados = [(red.evaluate(dataset), red) for red in poblacion]
        evaluados.sort(key=lambda x: x[0], reverse=True)
        
        if evaluados[0][0] > mejor_fitness:
            mejor_fitness = evaluados[0][0]
            mejor_red = evaluados[0][1].clone()
        
        if mejor_fitness >= 1.0:
            break
        
        nueva = [evaluados[i][1].clone() for i in range(elitismo)]
        while len(nueva) < poblacion_size:
            torneo = random.sample(evaluados[:100], 3)
            torneo.sort(key=lambda x: x[0], reverse=True)
            padre = torneo[0][1]
            hijo = padre.clone()
            hijo.mutate(tasa_mutacion)
            nueva.append(hijo)
        poblacion = nueva
    
    return mejor_red, mejor_fitness

def run_benchmark():
    print("=" * 70)
    print("BENCHMARK: RedColapsanteV2 (2→3→1)")
    print("Población: 300, Generaciones: 400")
    print("=" * 70)
    
    resultados = {}
    
    for dataset_name in list_datasets():
        dataset = get_dataset(dataset_name)
        print(f"\n--- Dataset: {dataset_name.upper()} ---")
        print(f"  Entrenando RedColapsanteV2...", end=" ", flush=True)
        mejor, fitness = evolucionar_red(dataset)
        print(f"precisión = {fitness:.4f} ({fitness*len(dataset):.1f}/{len(dataset)})")
        resultados[dataset_name] = fitness
        
        # Verificación detallada si alcanzó 100%
        if fitness >= 1.0:
            print(f"  Verificación detallada:")
            for entradas, esperado in dataset:
                pred = mejor.forward(*entradas)
                ok = "✓" if pred == esperado else "✗"
                print(f"    {entradas} → {pred:+d} (esperado {esperado:+d}) {ok}")
    
    # Resumen
    print("\n" + "=" * 70)
    print("RESUMEN")
    print("=" * 70)
    for dataset_name, fitness in resultados.items():
        print(f"  {dataset_name.upper():<15} {fitness:.4f}")
    
    # Guardar
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("experiments", exist_ok=True)
    with open(f"experiments/collapsing_network_{timestamp}.json", "w") as f:
        json.dump(resultados, f, indent=2)
    print(f"\nResultados guardados en experiments/collapsing_network_{timestamp}.json")
    
    return resultados

if __name__ == "__main__":
    random.seed(42)
    run_benchmark()
