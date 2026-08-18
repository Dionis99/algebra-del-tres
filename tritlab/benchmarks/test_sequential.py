"""
Probar las 3 arquitecturas en datasets secuenciales complejos.
"""
import sys, os
import random
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from networks.collapsing_network import RedColapsanteV2
from networks.fragmented_network import RedFragmentada
from networks.hybrid_network import RedFragmentadaColapsante
from datasets.sequential_complex import get_dataset_secuencial, list_datasets_secuenciales

def evaluar_secuencial(red, dataset):
    """Evalúa una red en un dataset secuencial."""
    aciertos = 0
    for secuencia, esperado in dataset:
        red.reset()
        salida = 0
        for entradas in secuencia:
            salida = red.forward(*entradas)
        if salida == esperado:
            aciertos += 1
    return aciertos / len(dataset)

def evolucionar_secuencial(factory, dataset, poblacion_size=300, generaciones=400, 
                            tasa_mutacion=0.14, elitismo=10):
    poblacion = [factory() for _ in range(poblacion_size)]
    mejor_fitness = 0.0
    mejor_red = None
    
    for gen in range(generaciones):
        evaluados = [(evaluar_secuencial(red, dataset), red) for red in poblacion]
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
    print("BENCHMARK SECUENCIAL: ¿Cuándo usar cada arquitectura?")
    print("=" * 70)
    
    resultados = {}
    
    for dataset_name in list_datasets_secuenciales():
        dataset = get_dataset_secuencial(dataset_name)
        print(f"\n--- Dataset: {dataset_name.upper()} ({len(dataset)} ejemplos) ---")
        
        for red_name, factory in [
            ("RedColapsanteV2", lambda: RedColapsanteV2(3)),
            ("RedFragmentada", lambda: RedFragmentada(3, 3, 3)),
            ("RedHibrida", lambda: RedFragmentadaColapsante(3, 3, 3)),
        ]:
            print(f"  Entrenando {red_name}...", end=" ", flush=True)
            mejor, fitness = evolucionar_secuencial(factory, dataset)
            print(f"precisión = {fitness:.4f} ({fitness*len(dataset):.1f}/{len(dataset)})")
            
            if dataset_name not in resultados:
                resultados[dataset_name] = {}
            resultados[dataset_name][red_name] = fitness
    
    # Resumen
    print("\n" + "=" * 70)
    print("RESUMEN: ¿Cuándo usar cada arquitectura?")
    print("=" * 70)
    
    for dataset_name, reds in resultados.items():
        print(f"\n{dataset_name.upper()}:")
        for red_name, fitness in reds.items():
            print(f"  {red_name:<25} {fitness:.4f}")
    
    # Guardar
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("experiments", exist_ok=True)
    with open(f"experiments/sequential_{timestamp}.json", "w") as f:
        json.dump(resultados, f, indent=2)
    print(f"\nResultados guardados en experiments/sequential_{timestamp}.json")
    
    return resultados

if __name__ == "__main__":
    random.seed(42)
    run_benchmark()
