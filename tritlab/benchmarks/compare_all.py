"""
Benchmark comparativo: todas las arquitecturas en los 3 datasets.
Mide precisión final y generación de convergencia.
"""
import sys, os
import random
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from networks.collapsing_network import RedColapsanteV2
from networks.fragmented_network import RedFragmentada
from networks.hybrid_network import RedFragmentadaColapsante
from datasets.basic import get_dataset, list_datasets

def evolucionar_con_tracking(factory, dataset, poblacion_size=300, generaciones=400, 
                              tasa_mutacion=0.14, elitismo=10):
    poblacion = [factory() for _ in range(poblacion_size)]
    mejor_fitness = 0.0
    mejor_red = None
    gen_convergencia = None
    
    for gen in range(generaciones):
        evaluados = [(red.evaluate(dataset), red) for red in poblacion]
        evaluados.sort(key=lambda x: x[0], reverse=True)
        
        if evaluados[0][0] > mejor_fitness:
            mejor_fitness = evaluados[0][0]
            mejor_red = evaluados[0][1].clone()
            if mejor_fitness >= 1.0 and gen_convergencia is None:
                gen_convergencia = gen
        
        if mejor_fitness >= 1.0 and gen >= gen_convergencia + 10:
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
    
    return mejor_red, mejor_fitness, gen_convergencia

def run_benchmark():
    print("=" * 70)
    print("BENCHMARK COMPARATIVO: Todas las arquitecturas")
    print("Población: 300, Generaciones: 400")
    print("=" * 70)
    
    resultados = {}
    
    for dataset_name in list_datasets():
        dataset = get_dataset(dataset_name)
        print(f"\n--- Dataset: {dataset_name.upper()} ---")
        
        for red_name, factory in [
            ("RedColapsanteV2", lambda: RedColapsanteV2(3)),
            ("RedFragmentada", lambda: RedFragmentada(3, 3, 3)),
            ("RedHibrida", lambda: RedFragmentadaColapsante(3, 3, 3)),
        ]:
            print(f"  Entrenando {red_name}...", end=" ", flush=True)
            mejor, fitness, gen_conv = evolucionar_con_tracking(factory, dataset)
            gen_str = f"gen {gen_conv}" if gen_conv is not None else "no convergió"
            print(f"precisión = {fitness:.4f} ({gen_str})")
            
            if dataset_name not in resultados:
                resultados[dataset_name] = {}
            resultados[dataset_name][red_name] = {
                "precision": fitness,
                "gen_convergencia": gen_conv
            }
    
    # Resumen
    print("\n" + "=" * 70)
    print("RESUMEN COMPARATIVO")
    print("=" * 70)
    
    for dataset_name, reds in resultados.items():
        print(f"\n{dataset_name.upper()}:")
        print(f"  {'Arquitectura':<25} {'Precisión':<12} {'Gen. Converge'}")
        print("  " + "-" * 55)
        for red_name, data in reds.items():
            gen_str = f"gen {data['gen_convergencia']}" if data['gen_convergencia'] is not None else "no convergió"
            print(f"  {red_name:<25} {data['precision']:<12.4f} {gen_str}")
    
    # Guardar
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("experiments", exist_ok=True)
    with open(f"experiments/compare_all_{timestamp}.json", "w") as f:
        json.dump(resultados, f, indent=2)
    print(f"\nResultados guardados en experiments/compare_all_{timestamp}.json")
    
    return resultados

if __name__ == "__main__":
    random.seed(42)
    run_benchmark()
