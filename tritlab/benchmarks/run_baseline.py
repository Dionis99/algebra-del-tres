"""
Benchmark completo: T3, T3-NA, T3-R, T3-G en datasets básicos y avanzados.
"""
import sys, os
import random
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from neurons.ternary import NeuronaTres
from neurons.non_associative import NeuronaTresNoAsociativa
from neurons.recurrent import NeuronaTresRecurrente
from neurons.collapsing import NeuronaColapsanteV2
from datasets.basic import get_dataset, list_datasets
from datasets.advanced import get_dataset_avanzado, list_datasets_avanzados

def evaluar_neurona(neurona, dataset, secuencial=False):
    aciertos = 0
    if secuencial:
        for secuencia, esperado in dataset:
            neurona.reset()
            salida = 0
            for entradas in secuencia:
                salida = neurona.forward(entradas)
            if salida == esperado:
                aciertos += 1
    else:
        for entradas, esperado in dataset:
            neurona.reset()
            if neurona.forward(entradas) == esperado:
                aciertos += 1
    return aciertos / len(dataset)

def evolucionar_simple(factory, dataset, secuencial=False, poblacion_size=300, 
                       generaciones=400, tasa_mutacion=0.14, elitismo=10):
    poblacion = [factory() for _ in range(poblacion_size)]
    mejor_fitness = 0.0
    mejor_neurona = None
    
    for gen in range(generaciones):
        evaluados = [(evaluar_neurona(n, dataset, secuencial), n) for n in poblacion]
        evaluados.sort(key=lambda x: x[0], reverse=True)
        
        if evaluados[0][0] > mejor_fitness:
            mejor_fitness = evaluados[0][0]
            mejor_neurona = evaluados[0][1].clone()
        
        if mejor_fitness >= 1.0:
            break
        
        nueva = [evaluados[i][1].clone() for i in range(elitismo)]
        while len(nueva) < poblacion_size:
            torneo = random.sample(evaluados[:100], min(3, len(evaluados)))
            torneo.sort(key=lambda x: x[0], reverse=True)
            padre = torneo[0][1]
            hijo = padre.clone()
            hijo.mutate(tasa_mutacion)
            nueva.append(hijo)
        poblacion = nueva
    
    return mejor_neurona, mejor_fitness

def run_benchmark():
    print("=" * 70)
    print("BENCHMARK COMPLETO: T3 vs T3-NA vs T3-R vs T3-G")
    print("Población: 300, Generaciones: 400, Elitismo: 10")
    print("=" * 70)
    
    resultados = {}
    
    # Datasets básicos (2 entradas)
    print("\n" + "=" * 70)
    print("DATASETS BÁSICOS (2 entradas)")
    print("=" * 70)
    
    for dataset_name in list_datasets():
        dataset = get_dataset(dataset_name)
        print(f"\n--- Dataset: {dataset_name.upper()} ---")
        
        for neurona_name, factory in [
            ("T3", lambda: NeuronaTres(2)),
            ("T3-NA", lambda: NeuronaTresNoAsociativa(2)),
            ("T3-R", lambda: NeuronaTresRecurrente(2)),
            ("T3-G", lambda: NeuronaColapsanteV2(2)),
        ]:
            print(f"  Entrenando {neurona_name}...", end=" ", flush=True)
            mejor, fitness = evolucionar_simple(factory, dataset)
            print(f"precisión = {fitness:.4f} ({fitness*len(dataset):.1f}/{len(dataset)})")
            if dataset_name not in resultados:
                resultados[dataset_name] = {}
            resultados[dataset_name][neurona_name] = fitness
    
    # Datasets avanzados (3 entradas)
    print("\n" + "=" * 70)
    print("DATASETS AVANZADOS (3 entradas)")
    print("=" * 70)
    
    for dataset_name in ["paridad_3", "mayoria_3"]:
        dataset = get_dataset_avanzado(dataset_name)
        print(f"\n--- Dataset: {dataset_name.upper()} ---")
        
        for neurona_name, factory in [
            ("T3", lambda: NeuronaTres(3)),
            ("T3-NA", lambda: NeuronaTresNoAsociativa(3)),
            ("T3-R", lambda: NeuronaTresRecurrente(3)),
            ("T3-G", lambda: NeuronaColapsanteV2(3)),
        ]:
            print(f"  Entrenando {neurona_name}...", end=" ", flush=True)
            mejor, fitness = evolucionar_simple(factory, dataset)
            print(f"precisión = {fitness:.4f} ({fitness*len(dataset):.1f}/{len(dataset)})")
            if dataset_name not in resultados:
                resultados[dataset_name] = {}
            resultados[dataset_name][neurona_name] = fitness
    
    # Datasets secuenciales
    print("\n" + "=" * 70)
    print("DATASETS SECUENCIALES (memoria temporal)")
    print("=" * 70)
    
    for dataset_name in ["sec_memoria", "sec_paridad"]:
        dataset = get_dataset_avanzado(dataset_name)
        print(f"\n--- Dataset: {dataset_name.upper()} ---")
        
        for neurona_name, factory in [
            ("T3-R", lambda: NeuronaTresRecurrente(2)),
        ]:
            print(f"  Entrenando {neurona_name}...", end=" ", flush=True)
            mejor, fitness = evolucionar_simple(factory, dataset, secuencial=True)
            print(f"precisión = {fitness:.4f} ({fitness*len(dataset):.1f}/{len(dataset)})")
            if dataset_name not in resultados:
                resultados[dataset_name] = {}
            resultados[dataset_name][neurona_name] = fitness
    
    # Resumen final
    print("\n" + "=" * 70)
    print("RESUMEN FINAL")
    print("=" * 70)
    
    for dataset_name, neurona_results in resultados.items():
        print(f"\n{dataset_name.upper()}:")
        for neurona_name, fitness in neurona_results.items():
            print(f"  {neurona_name:<10} {fitness:.4f}")
    
    # Guardar resultados
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("experiments", exist_ok=True)
    with open(f"experiments/benchmark_{timestamp}.json", "w") as f:
        json.dump(resultados, f, indent=2)
    print(f"\nResultados guardados en experiments/benchmark_{timestamp}.json")
    
    return resultados

if __name__ == "__main__":
    random.seed(42)
    run_benchmark()
